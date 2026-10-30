#!/usr/bin/env python3
"""Finite numerical checks of the Pauli detector memory frontiers.

The detector outputs and their tangents are built from POVM effects and partial
traces. SLD information and Umegaki relative entropy are evaluated by matrix
diagonalization. These checks corroborate the analytical proofs; they do not
establish an untested dimension, asymptotic limit, or universal theorem.
"""

from __future__ import annotations

import argparse
import itertools
import json
import platform
from pathlib import Path

import numpy as np


SEED = 20261030
THETAS = (0.0, 0.2, -0.6, 0.9)
ATOL = 3e-9
RTOL = 3e-9
MATRIX_TOL = 2e-11
EIGENVALUE_TOL = 1e-12
FD_STEP = 1e-5
FD_TOL = 3e-8

SINGLE_PAULIS = (
    np.eye(2, dtype=complex),
    np.array([[0, 1], [1, 0]], dtype=complex),
    np.array([[0, -1j], [1j, 0]], dtype=complex),
    np.diag([1, -1]).astype(complex),
)


class Checks:
    def __init__(self) -> None:
        self.maxima: dict[str, float] = {}
        self.counts: dict[str, int] = {}

    def count(self, name: str, increment: int = 1) -> None:
        self.counts[name] = self.counts.get(name, 0) + increment

    def maximum(self, name: str, value: float) -> None:
        self.maxima[name] = max(self.maxima.get(name, -float("inf")), float(value))

    def close(self, name: str, actual, expected, *, tolerance: float | None = None) -> None:
        a, b = np.asarray(actual), np.asarray(expected)
        error = float(np.max(np.abs(a - b)))
        scale = max(float(np.max(np.abs(a))), float(np.max(np.abs(b))))
        limit = ATOL + RTOL * scale if tolerance is None else tolerance
        self.maximum(name, error)
        if not np.isfinite(error) or error > limit:
            raise AssertionError(f"{name}: error {error:.6g} exceeds {limit:.6g}")

    def bounded(self, name: str, actual: float, upper: float) -> None:
        excess = float(actual - upper)
        self.maximum(name, excess)
        if not np.isfinite(actual) or excess > ATOL + RTOL * abs(upper):
            raise AssertionError(f"{name}: {actual:.12g} exceeds {upper:.12g}")


def hermitian(a: np.ndarray) -> np.ndarray:
    if np.max(np.abs(a - a.conj().T)) > MATRIX_TOL:
        raise AssertionError("Non-Hermitian matrix in a state or tangent")
    return (a + a.conj().T) / 2


def positive_eigh(a: np.ndarray):
    values, vectors = np.linalg.eigh(hermitian(a))
    if values.min(initial=0.0) < -MATRIX_TOL:
        raise AssertionError("A purported positive operator has a negative eigenvalue")
    return np.maximum(values, 0.0), vectors


def sld(a: np.ndarray, tangent: np.ndarray) -> float:
    """Unnormalized SLD form, including support--kernel cross terms."""
    values, vectors = positive_eigh(a)
    t = vectors.conj().T @ hermitian(tangent) @ vectors
    denominators = values[:, None] + values[None, :]
    keep = denominators > EIGENVALUE_TOL
    if np.max(np.abs(t[~keep]), initial=0.0) > MATRIX_TOL:
        raise AssertionError("Tangent has an incompatible kernel--kernel component")
    return float(np.sum(2 * np.abs(t[keep]) ** 2 / denominators[keep]).real)


def relative_entropy(a: np.ndarray, b: np.ndarray) -> float:
    """Tr A(log A-log B), with a checked support condition."""
    av, _ = positive_eigh(a)
    bv, bu = positive_eigh(b)
    support = bv > EIGENVALUE_TOL
    projection = bu[:, support] @ bu[:, support].conj().T
    if np.max(np.abs(a - projection @ a @ projection)) > MATRIX_TOL:
        raise AssertionError("Relative-entropy numerator leaves the reference support")
    logb = (bu[:, support] * np.log(bv[support])) @ bu[:, support].conj().T
    nonzero = av > EIGENVALUE_TOL
    first = np.sum(av[nonzero] * np.log(av[nonzero]))
    return float((first - np.trace(a @ logb)).real)


def pauli_family(n: int):
    labels, matrices = [], []
    for label in itertools.product(range(4), repeat=n):
        if not any(label):
            continue
        p = np.ones((1, 1), dtype=complex)
        for symbol in label:
            p = np.kron(p, SINGLE_PAULIS[symbol])
        labels.append(label)
        matrices.append(p)
    return labels, np.stack(matrices)


def effects(paulis: np.ndarray, theta: float):
    """Outcome order: P first, then sign -1, +1."""
    m, d, _ = paulis.shape
    signs = np.array([-1.0, 1.0])
    derivatives = (paulis[:, None] * signs[None, :, None, None] / (2 * m)).reshape(
        2 * m, d, d
    )
    operators = np.eye(d)[None] / (2 * m) + theta * derivatives
    return operators, derivatives


def apply_effects(operators: np.ndarray, state: np.ndarray, d: int, r: int):
    """Tr_S[(E_x tensor I) state] from the matrix entries of E_x."""
    tensor = state.reshape(d, r, d, r)
    return np.einsum("xba,arbs->xrs", operators, tensor, optimize=True)


def memory_marginal(state: np.ndarray, d: int, r: int):
    return np.trace(state.reshape(d, r, d, r), axis1=0, axis2=2)


def pure_state(rng: np.random.Generator, dimension: int):
    vector = rng.normal(size=dimension) + 1j * rng.normal(size=dimension)
    vector /= np.linalg.norm(vector)
    return np.outer(vector, vector.conj())


def mixed_state(rng: np.random.Generator, dimension: int):
    a = rng.normal(size=(dimension, dimension)) + 1j * rng.normal(size=(dimension, dimension))
    state = a @ a.conj().T
    return state / np.trace(state)


def subset_state(d: int, subset: np.ndarray):
    r = len(subset)
    v = np.zeros((d, r), dtype=complex)
    v[subset, np.arange(r)] = 1 / np.sqrt(r)
    vector = v.reshape(-1)
    return np.outer(vector, vector.conj())


def random_unitary(rng: np.random.Generator, dimension: int):
    a = rng.normal(size=(dimension, dimension)) + 1j * rng.normal(size=(dimension, dimension))
    q, triangular = np.linalg.qr(a)
    diagonal = np.diag(triangular)
    phases = diagonal / np.abs(diagonal)
    return q * phases.conj()


def h(theta: float) -> float:
    return float(((1 + theta) * np.log1p(theta) + (1 - theta) * np.log1p(-theta)) / 2)


def c_value(d: int, r: int) -> float:
    return (d * r - 1) / (d * d - 1)


def block_diagonal(blocks: np.ndarray):
    number, r, _ = blocks.shape
    result = np.zeros((number * r, number * r), dtype=complex)
    for index, block in enumerate(blocks):
        result[index * r : (index + 1) * r, index * r : (index + 1) * r] = block
    return result


def metrics(state: np.ndarray, d: int, r: int, paulis: np.ndarray, theta: float):
    operators, derivatives = effects(paulis, theta)
    zero_operators, _ = effects(paulis, 0.0)
    outputs = apply_effects(operators, state, d, r)
    tangents = apply_effects(derivatives, state, d, r)
    references = apply_effects(zero_operators, state, d, r)
    fisher = sum(sld(a, t) for a, t in zip(outputs, tangents))
    divergence = sum(relative_entropy(a, b) for a, b in zip(outputs, references))
    return float(fisher), float(divergence), outputs, tangents, references


def check_primitives(checks: Checks, rng: np.random.Generator):
    d = r = 2
    _, ps = pauli_family(1)
    state = pure_state(rng, d * r)
    operators, _ = effects(ps, 0.37)
    outputs = apply_effects(operators, state, d, r)
    brute = []
    for operator in operators:
        product = np.kron(operator, np.eye(r)) @ state
        brute.append(np.trace(product.reshape(d, r, d, r), axis1=0, axis2=2))
    checks.close("partial_trace_vs_kronecker_error", outputs, np.stack(brute))
    f, divergence, outputs, tangents, references = metrics(state, d, r, ps, 0.37)
    checks.close("block_sld_vs_full_matrix_error", f, sld(block_diagonal(outputs), block_diagonal(tangents)))
    checks.close("block_entropy_vs_full_matrix_error", divergence,
                 relative_entropy(block_diagonal(outputs), block_diagonal(references)))
    # |psi(theta)> proportional to |0>+theta|1>: off-support first derivative.
    checks.close("sld_support_kernel_tangent_error", sld(np.diag([1.0, 0.0]), SINGLE_PAULIS[1]), 4.0)
    checks.count("independent_matrix_diagnostics", 4)


def check_readout(checks: Checks, subset, outputs, paulis, theta, d, r):
    probabilities = np.zeros(3)  # erasure, y=+1, y=-1
    for index, p in enumerate(paulis):
        compression = p[np.ix_(subset, subset)].T
        eigenvalues, eigenvectors = np.linalg.eigh(compression)
        rounded = np.rint(eigenvalues)
        checks.close("compressed_pauli_three_point_spectrum_error", eigenvalues, rounded)
        if np.max(np.abs(rounded)) > 1:
            raise AssertionError("Compressed Pauli left {-1,0,1}")
        for sign_index, sign in enumerate((-1, 1)):
            block = outputs[2 * index + sign_index]
            weights = np.diag(eigenvectors.conj().T @ block @ eigenvectors).real
            for t, weight in zip(rounded.astype(int), weights):
                target = 0 if t == 0 else (1 if sign * t == 1 else 2)
                probabilities[target] += weight
    c = c_value(d, r)
    checks.close("erasure_coin_distribution_error", probabilities,
                 [1 - c, c * (1 + theta) / 2, c * (1 - theta) / 2])
    checks.count("explicit_ancilla_readouts")


def check_fixed_inputs(checks: Checks, rng: np.random.Generator):
    for n in (1, 2, 3):
        d = 2**n
        _, ps = pauli_family(n)
        permutation = (3 * np.arange(d) + 1) % d
        for r in range(1, d + 1):
            c = c_value(d, r)
            for subset in (np.arange(r), permutation[:r]):
                state = subset_state(d, subset)
                checks.count("subset_state_families")
                for theta in THETAS:
                    f, divergence, outputs, _, _ = metrics(state, d, r, ps, theta)
                    checks.close("subset_sld_frontier_error", f, c / (1 - theta * theta))
                    checks.close("subset_entropy_frontier_error", divergence, c * h(theta))
                    checks.close("complete_output_trace_error", np.trace(outputs, axis1=1, axis2=2).sum(), 1)
                    checks.close("retained_marginal_error", outputs.sum(axis=0), memory_marginal(state, d, r))
                    check_readout(checks, subset, outputs, ps, theta, d, r)
                    checks.count("subset_parameter_points")
            for _ in range(3):
                families = [
                    ("random_pure_families", pure_state(rng, d * r)),
                    ("random_mixed_families", mixed_state(rng, d * r)),
                ]
                if r > 1:
                    q = r - 1
                    small = mixed_state(rng, d * q)
                    embedded = np.zeros((d, r, d, r), dtype=complex)
                    embedded[:, :q, :, :q] = small.reshape(d, q, d, q)
                    families.append(("rank_deficient_memory_families", embedded.reshape(d * r, d * r)))
                for category, state in families:
                    checks.count(category)
                    f0 = metrics(state, d, r, ps, 0.0)[0]
                    for theta in THETAS:
                        f, divergence, _, _, _ = metrics(state, d, r, ps, theta)
                        checks.bounded("random_sld_bound_excess", f, c / (1 - theta * theta))
                        checks.bounded("random_entropy_bound_excess", divergence, c * h(theta))
                        checks.bounded("nonzero_parameter_sld_bound_excess", f, f0 / (1 - theta * theta))
                        checks.bounded("relative_entropy_negativity", -divergence, 0.0)
                        checks.count("random_parameter_points")


def check_transpose_and_qubit_caveat(checks: Checks):
    for n, target in ((1, (2,)), (2, (2, 3)), (2, (2, 2))):
        d = 2**n
        labels, ps = pauli_family(n)
        state = subset_state(d, np.arange(d))
        theta = 0.43
        outputs = metrics(state, d, d, ps, theta)[2]
        index = labels.index(target)
        p = ps[index]
        correct = sum(sign * np.trace(p.T @ outputs[2 * index + j]).real
                      for j, sign in enumerate((-1, 1))) * len(ps)
        uncorrected = sum(sign * np.trace(p @ outputs[2 * index + j]).real
                          for j, sign in enumerate((-1, 1))) * len(ps)
        transpose_sign = (-1) ** target.count(2)
        checks.close("y_transpose_corrected_correlation_error", correct, theta)
        checks.close("y_transpose_uncorrected_sign_error", uncorrected, transpose_sign * theta)
        checks.count("explicit_y_transpose_cases")
    _, ps = pauli_family(1)
    balanced = (SINGLE_PAULIS[0] + sum(SINGLE_PAULIS[1:]) / np.sqrt(3)) / 2
    stabilizer = np.diag([1.0, 0.0])
    theta = 0.4
    tvs = []
    for state, expected_f, expected_tv in (
        (balanced, 1 / (3 * (1 - theta * theta / 3)), abs(theta) / (2 * np.sqrt(3))),
        (stabilizer, 1 / (3 * (1 - theta * theta)), abs(theta) / 6),
    ):
        f, _, outputs, _, references = metrics(state, 2, 1, ps, theta)
        tv = float(np.sum(np.abs(outputs[:, 0, 0] - references[:, 0, 0])) / 2)
        checks.close("qubit_caveat_sld_error", f, expected_f)
        checks.close("qubit_caveat_total_variation_error", tv, expected_tv)
        tvs.append(tv)
    if not tvs[0] > tvs[1] + 1e-3:
        raise AssertionError("The stated finite-sample decision caveat was not reproduced")
    checks.count("qubit_decision_caveat_inputs", 2)


def check_increment(checks, state, tangent, d, r, ps, category):
    zero_effects, derivatives = effects(ps, 0.0)
    outputs = apply_effects(zero_effects, state, d, r)
    intrinsic_tangents = apply_effects(derivatives, state, d, r)
    output_tangents = intrinsic_tangents + apply_effects(zero_effects, tangent, d, r)
    actual = sum(sld(a, t) for a, t in zip(outputs, output_tangents))
    sigma = memory_marginal(state, d, r)
    sigma_dot = memory_marginal(tangent, d, r)
    intrinsic = sum(sld(a, t) for a, t in zip(outputs, intrinsic_tangents))
    expected = sld(sigma, sigma_dot) + intrinsic
    checks.close("adaptive_zero_point_cancellation_error", actual, expected)
    checks.bounded("adaptive_single_query_increment_excess", actual - sld(state, tangent), c_value(d, r))
    checks.count(category)


def check_physical_incoming_families(checks: Checks, rng: np.random.Generator):
    for n in (1, 2, 3):
        d = 2**n
        _, ps = pauli_family(n)
        zero_effects, derivatives = effects(ps, 0.0)
        # A real preceding detector call on |0>, followed by a fixed
        # measure-and-prepare channel. Its classical outcome is then discarded.
        previous_input = np.zeros((d, d), dtype=complex)
        previous_input[0, 0] = 1
        weights = apply_effects(zero_effects, previous_input, d, 1)[:, 0, 0].real
        weight_dots = apply_effects(derivatives, previous_input, d, 1)[:, 0, 0].real
        for r in range(1, d + 1):
            prepared = [pure_state(rng, d * r) for _ in range(min(5, d * r))]
            state = np.zeros((d * r, d * r), dtype=complex)
            tangent = np.zeros_like(state)
            for j, (weight, weight_dot) in enumerate(zip(weights, weight_dots)):
                state += weight * prepared[j % len(prepared)]
                tangent += weight_dot * prepared[j % len(prepared)]
            check_increment(checks, state, tangent, d, r, ps, "physical_measure_prepare_families")
            # A preceding entangled query, a specified recorded outcome, then
            # append a fresh |0> probe and apply a fixed joint unitary.
            subset = ((3 * np.arange(d) + 1) % d)[:r]
            previous = subset_state(d, subset)
            unitary = random_unitary(rng, d * r)
            outcome = 1  # P=I...IX, s=+1 in the Pauli enumeration.

            def incoming(theta):
                es, _ = effects(ps, theta)
                block = apply_effects(es, previous, d, r)[outcome]
                conditional = block / np.trace(block)
                return unitary @ np.kron(previous_input, conditional) @ unitary.conj().T

            first = apply_effects(zero_effects, previous, d, r)[outcome]
            first_dot = apply_effects(derivatives, previous, d, r)[outcome]
            probability = np.trace(first).real
            probability_dot = np.trace(first_dot).real
            conditional_dot = first_dot / probability - first * probability_dot / probability**2
            state = incoming(0.0)
            tangent = unitary @ np.kron(previous_input, conditional_dot) @ unitary.conj().T
            finite_difference = (incoming(FD_STEP) - incoming(-FD_STEP)) / (2 * FD_STEP)
            checks.close("physical_family_derivative_error", tangent, finite_difference, tolerance=FD_TOL)
            check_increment(checks, state, tangent, d, r, ps, "physical_retained_memory_families")


def check_two_query_protocols(checks: Checks, rng: np.random.Generator):
    for n, r in ((1, 1), (1, 2), (2, 1), (2, 2), (2, 3), (2, 4)):
        d = 2**n
        _, ps = pauli_family(n)
        es, ds = effects(ps, 0.0)
        initial = subset_state(d, ((3 * np.arange(d) + 1) % d)[:r])
        first = apply_effects(es, initial, d, r)
        first_dot = apply_effects(ds, initial, d, r)
        units = [random_unitary(rng, d * r) for _ in range(3)]
        fresh = np.zeros((d, d), dtype=complex)
        fresh[0, 0] = 1
        total_f, total_trace, derivative_trace = 0.0, 0.0, 0.0
        for history, (memory, memory_dot) in enumerate(zip(first, first_dot)):
            unitary = units[history % len(units)]
            state = unitary @ np.kron(fresh, memory) @ unitary.conj().T
            tangent = unitary @ np.kron(fresh, memory_dot) @ unitary.conj().T
            outputs = apply_effects(es, state, d, r)
            tangents = apply_effects(ds, state, d, r) + apply_effects(es, tangent, d, r)
            total_f += sum(sld(a, t) for a, t in zip(outputs, tangents))
            total_trace += np.trace(outputs, axis1=1, axis2=2).sum().real
            derivative_trace += np.trace(tangents, axis1=1, axis2=2).sum().real
        checks.close("two_query_complete_trace_error", total_trace, 1.0)
        checks.close("two_query_derivative_trace_error", derivative_trace, 0.0)
        checks.bounded("two_query_adaptive_fisher_excess", total_f, 2 * c_value(d, r))
        checks.count("complete_two_query_adaptive_protocols")


def run_all():
    rng = np.random.default_rng(SEED)
    checks = Checks()
    check_primitives(checks, rng)
    check_fixed_inputs(checks, rng)
    check_transpose_and_qubit_caveat(checks)
    check_physical_incoming_families(checks, rng)
    check_two_query_protocols(checks, rng)
    return {
        "status": "pass",
        "seed": SEED,
        "python": platform.python_version(),
        "numpy": np.__version__,
        "dimensions": [2, 4, 8],
        "memory_dimensions": "every integer 1 <= r <= d",
        "theta_values": list(THETAS),
        "tolerances": {
            "absolute": ATOL,
            "relative": RTOL,
            "matrix_support": MATRIX_TOL,
            "eigenvalue_cutoff": EIGENVALUE_TOL,
            "finite_difference_step": FD_STEP,
            "finite_difference_absolute": FD_TOL,
        },
        "counts": checks.counts,
        "observed_maxima": checks.maxima,
        "scope": "Finite deterministic numerical corroboration; the analytical proofs establish the general results.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Also write the JSON result to this path.")
    args = parser.parse_args()
    result = run_all()
    rendered = json.dumps(result, indent=2, sort_keys=True, allow_nan=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
