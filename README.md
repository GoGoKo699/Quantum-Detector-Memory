# Quantum Detector Memory

**How much quantum memory is needed to calibrate a detector that destroys the probe and returns only a classical record?**

For a known detector family with one unknown contrast, this project gives an exact retained-memory information frontier and a matching global estimation law. The detector privately selects a fresh random Pauli measurement on each use and reveals the setting only after consuming the probe.

Let $`d=2^n`$ be the probe dimension and $`r\leq d`$ the dimension of all retained quantum systems during a call. The effects are

```math
E_{P,s}(\theta)=\frac{I+s\theta P}{2(d^2-1)},
\qquad P\ne I,\quad s\in\{-1,+1\},\quad |\theta|\lt1,
```

where $`P`$ ranges over Hermitian $`n`$-qubit Paulis. Define $`c_r=(dr-1)/(d^2-1)`$. The exact optimal one-use Fisher information is

```math
F_r^\star(\theta)=\frac{c_r}{1-\theta^2}.
```

For each integer $`r`$, one fixed input and a setting-conditioned reference measurement attain this simultaneously for every interior contrast. The resulting experiment is an observed erasure with probability $`1-c_r`$, followed on success by a Bernoulli sign of mean $`\theta`$.

## Principal results

| Question | Result | Read |
|---|---|---|
| How much one-use information can a reference retain? | Exact Fisher coefficient $`c_r`$ for all $`r`$ and interior contrasts | [Fisher frontier](science/fisher_information.md) |
| Is the frontier physically attainable? | Uniform entanglement over a computational subset; $`k`$ Bell pairs suffice when $`r=2^k`$ | [Construction and resources](science/attaining_protocol.md) |
| Can coherent adaptive reuse improve distinguishability from zero? | Exact maximum relative entropy $`Nc_rh(\theta)`$ after $`N`$ calls | [Entropy](science/relative_entropy.md) and [adaptive calibration](science/adaptive_calibration.md) |
| What is the global estimation cost? | Minimax mean-square error within a factor 32 of $`\min\{a^2,1/(Nc_r)\}`$ on $`[-a,a]`$ | [Finite-sample guarantees](science/adaptive_calibration.md) |
| Can one scalar detector parameter benefit from an ancilla? | A six-outcome qubit detector has an exact factor-three Fisher advantage | [Qubit counterexample](science/single_parameter_counterexample.md) |

Here $`h(\theta)=[(1+\theta)\log(1+\theta)+(1-\theta)\log(1-\theta)]/2`$ and logarithms are natural. The adaptive converses allow arbitrary parameter-independent controls, free classical history, mixed states, intermediate measurements and reference reuse.

With $`k`$ retained qubits, root-mean-square accuracy $`\epsilon`$ on a fixed interval containing zero requires and admits

```math
N_\epsilon
=\Theta\!\left(\frac{2^{2n}-1}{(2^{n+k}-1)\epsilon^2}\right)
=\Theta\!\left(\frac{2^{n-k}}{\epsilon^2}\right)
```

in the nontrivial small-error regime. Uniform high-confidence estimation adds a factor $`\log(1/\delta)`$; [explicit constants and ranges](science/adaptive_calibration.md) are provided.

## Read the science

Start with the [model, assumptions and exact claims](science/model.md), then the [attaining protocol](science/attaining_protocol.md). Specialists can go directly to the [Fisher proof](science/fisher_information.md), [relative-entropy proof](science/relative_entropy.md), or [adaptive minimax argument](science/adaptive_calibration.md).

The [interpretation](science/interpretation.md) explains why disclosure timing matters and compares the result with depolarizing-channel estimation. The [related-work account](references/RELATED_WORK.md) and [structured bibliography](references/references.bib) credit the inherited local Schmidt form, ancillary calibration, Pauli-learning memory tradeoffs and replacer-channel amortization. The [LLM reading guide](llms.txt) maps questions to their authoritative files.

The new claim is the solved destructive-detector calibration model and its consequences. Generic ancillary advantage, the zero-contrast rank numerator and exponential memory tradeoffs have established precedents.

## Learn the project

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**. The [learning entrypoint](learning/README.md) connects its foundations to this detector model without assigning additional textbooks.

| Route | What it provides |
|---|---|
| [Two-qubit worked experiment](learning/WORKED_EXAMPLE.md) | Probe preparation, all fifteen settings, observed erasures, the Y-sign correction and a complete estimator |
| [Watrous-to-project bridge](learning/WATROUS_BRIDGE.md) | Verified source sections, notation and log conventions, and the locally supplied Fisher, entropy and statistical arguments |
| [Thirty-milestone map](learning/MILESTONES.md) | Twelve background milestones and eighteen narrative milestones, with understanding targets, dependencies and canonical proof pointers |

The map is learner independent. It separates local Fisher information, global relative-entropy bounds and minimax rates; the scientific pages above remain the authoritative proofs.

## Reproduce the finite checks

From the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

The [verification guide](verification/README.md) documents the actual matrix checks, deterministic cases, expected tolerances and scope. These corroborate finite-dimensional calculations; the universal adaptive and minimax statements rest on the written proofs.

## Scope that matters

The setting is disclosed after preparation. Every accessible retained coherent register, future entangled probe and purification counts in $`r`$. Preparation and reference readout are trusted; detector calls are independent. Query budgets count failures and are worst-case budgets. The explicit powers-of-two implementation uses local gates and measurements; efficient arbitrary-$`r`$ encoding is not asserted.

The exact adaptive Fisher optimum is established at zero contrast. Exact relative-entropy optimality does not imply exact optimality for every finite-sample testing loss, and the global minimax theorem concerns intervals containing zero. Returning the quantum probe or revealing the setting before preparation changes the resource model.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
