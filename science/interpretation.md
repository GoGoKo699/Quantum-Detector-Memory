# What the memory law means

The detector destroys each probe before disclosing its measurement setting. Retained quantum memory lets the experimenter choose a reference measurement after that disclosure. The exact coefficient

```math
c_r=\frac{dr-1}{d^2-1}
```

measures how often the [attaining protocol](attaining_protocol.md) recovers an informative sign. It also controls the exact one-use Fisher information, exact adaptive relative entropy against zero, and the global estimation rate.

## Dimension and information

| Retained reference | Informative probability | Reciprocal information coefficient |
|---|---:|---:|
| No retained qubit, $`r=1`$ | $`1/(d+1)`$ | $`d+1`$ |
| $`k`$ retained qubits, $`r=2^k`$ | $`(2^{n+k}-1)/(2^{2n}-1)`$ | $`(2^{2n}-1)/(2^{n+k}-1)`$ |
| Full $`n`$-qubit reference, $`r=d`$ | $`1`$ | $`1`$ |

The full-memory to no-memory one-use Fisher ratio is exactly $`d+1`$ for all $`|\theta|\lt1`$. Intermediate memory levels interpolate linearly in Hilbert-space dimension, with the identity-Pauli subtraction retained exactly. Each additional retained qubit approximately halves the query cost away from the saturation point.

The formula concerns dimension available during a call. It does not price the creation of entanglement, storage time, reset work, control precision or classical computation. The powers-of-two construction does show that the information advantage needs only Bell-pair preparation, local Pauli measurements and classical parity processing.

## What was already present in depolarizing estimation

For physical depolarizing parameters, write

```math
\Gamma_\theta(A)=\theta A+(1-\theta)\operatorname{Tr}(A)\frac{I}{d}.
```

Let $`\mathcal M`$ be ideal uniformly randomized nonidentity-Pauli measurement with its label retained. Then

```math
\Lambda_\theta=\mathcal M\circ\Gamma_\theta.
```

This is a physical channel factorization only for $`-1/(d^2-1)\leq\theta\leq1`$. The detector itself remains valid throughout $`[-1,1]`$, so the factorization should not be used as a physical implementation for more negative contrasts.

[Frey, Collins and Gerlach](../references/RELATED_WORK.md#frey2011) evaluate depolarizing probes uniformly entangled over a rank-$`r`$ subspace. Their Eq. (24) gives

```math
J_r(\theta)
=\frac{dr-1}{(1-\theta)[1+(dr-1)\theta]},
\qquad 0\leq\theta\lt1.
```

At zero, $`J_r(0)=dr-1`$. Their general partial-entanglement expression also contains the same zero-point Schmidt-weight quadratic form used here, up to the detector normalization $`M`$. The rank numerator and the generic $`d+1`$ ancillary ratio at zero are established antecedents.

The compulsory readout changes the finite-contrast law. For the endpoint probe families, direct division gives

```math
\frac{J_d(\theta)}{J_1(\theta)}
=(d+1)\frac{1+(d-1)\theta}{1+(d^2-1)\theta}
\longrightarrow1
\quad(d\longrightarrow\infty,\ \theta\ {\rm fixed},\ 0\lt\theta\lt1).
```

For the destructive detector, the corresponding ratio is exactly $`d+1`$ at every interior contrast. This comparison is an algebraic consequence of the two formulas. It is not a claim that noisy readout increases absolute information: data processing still bounds detector information by that available from the quantum channel output. The readout loses different amounts of accessible information in the two memory regimes.

## What adaptivity can change

A protocol may retain coherent information and prepare later probes using earlier outcomes. The [adaptive proof](adaptive_calibration.md) covers that freedom. Against zero contrast, each call increases relative entropy by at most $`c_rh(\theta)`$, and independent repetitions attain the bound.

The mechanism is the established replacer-channel amortization identity of [Wilde, Berta, Hirche and Kaur](../references/RELATED_WORK.md#wilde2020). At zero, the detector returns a uniform record while leaving the reference marginal intact. Separating its new distinguishability from the incoming reference distinguishability yields the per-call bound.

The sharp coefficient is evaluated here for this detector and memory constraint. The general amortization method is inherited. Likewise, exponential memory–query tradeoffs already occur in Pauli learning, including the current [Kim–Oh](../references/RELATED_WORK.md#kimoh2026) result. Here the unknown is one shared scalar and a fresh measurement label is disclosed at each use; the task and available output differ.

The exact adaptive relative-entropy frontier does not imply that independent repetitions are optimal for every finite-sample loss. Nor does it determine the adaptive Fisher information at every nonzero contrast. The exact adaptive Fisher statement in this account is at zero. The global minimax statement is a rate result on intervals containing zero.

## Assumptions with operational consequences

**Label timing.** If $`P`$ is supplied before preparation, an unassisted $`P`$ eigenstate converts every call into a sign with mean $`\theta`$. Then the coefficient is one even without retained quantum memory. The order of access is a load-bearing assumption.

**Classical history.** An unlimited classical record is allowed. It cannot replace the retained quantum correlation with a setting that is privately selected after preparation. Storing a coherent superposition of histories or an unmeasured future probe counts toward $`r`$.

**Trusted reference.** Noise in Bell preparation, memory storage or reference readout can reduce the achievable information. It is not absorbed into an unmodeled free calibration resource. The present theorem establishes an ideal information limit; it does not certify a laboratory advantage under unspecified noise.

**Independent calls.** Correlated settings, drift, hidden device memory or an additional unknown noise parameter require a different statistical model. The proof does not turn a multivariate or nonstationary calibration problem into the single-scalar experiment.

**Implementation and memory.** A uniform state on an arbitrary $`r`$-element computational subset proves attainability for every integer dimension. Its encoding complexity is not bounded here. The $`r=2^k`$ family has an explicit efficient local implementation and needs no QRAM.

**Costs and postselection.** Query complexity counts failed calls and uses a worst-case budget. Conditional information after discarding unsuccessful branches is not the information of the complete experiment.

## Scientific scope

The combined result is an exactly solved destructive-detector calibration model: a constructive memory frontier, an exact adaptive divergence, a scalar minimax consequence and a transparent single-qubit counterexample to a proposed universal no-advantage principle. The [source account](../references/RELATED_WORK.md) credits the older identities, methods and related resource laws.

The [verification suite](../verification/README.md) checks matrix calculations, all-integer-r constructions, transpose conventions and finite statistical identities. Universal dimension, adaptive and asymptotic statements are established by the written proofs; finite numerical success is not a substitute for them.
