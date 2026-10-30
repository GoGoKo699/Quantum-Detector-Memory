# From Watrous to the detector-memory law

[Learning route](README.md) · [Milestones](MILESTONES.md) · [Worked experiment](WORKED_EXAMPLE.md) · [Scientific model](../science/model.md)

## One source, with a specific bridge

The sole educational anchor is **John Watrous, *The Theory of Quantum Information* (Cambridge University Press, 2018)**. The [author's page](https://cs.uwaterloo.ca/~watrous/TQI/) provides the personal-use manuscript and errata. The section numbering below follows its January 2018 pre-publication version, as checked against the [front matter](https://cs.uwaterloo.ca/~watrous/TQI/TQI.frontmatter.pdf). Link to that source rather than redistributing it.

The necessary foundations are finite-dimensional operators, states, channels, measurements, discrimination and relative entropy. The book supplies that language. This repository supplies the SLD calculation, the rank-constrained Pauli evaluation, the exact erasure experiment and the resource-constrained adaptive/statistical deductions. None of those project theorems is attributed to Watrous merely because it is our educational anchor.

| Preparation in Watrous | Purpose here | Project destination |
|---|---|---|
| Sections 1.1.2–1.1.3 | Positive operators, adjoints, spectral decompositions, norms and Schmidt structure | [Fisher quadratic form](../science/fisher_information.md) |
| Sections 1.2.1–1.2.2 | Convex mixtures, expectations and probabilities | [Estimator and concentration argument](../science/adaptive_calibration.md) |
| Sections 2.1.1–2.1.3 | Classical registers, quantum states, reductions and purifications | [Memory and classical history](../science/model.md) |
| Sections 2.2.1–2.2.3 | Completely positive trace-preserving maps and their representations | [Destructive detector as a channel](../science/model.md) |
| Sections 2.3.1–2.3.2 | POVMs, probabilities and classical-output measurements | [Detector and reference readout](../science/attaining_protocol.md) |
| Section 3.1.1 | Binary discrimination and trace-distance interpretation | [Estimation-to-testing reduction](../science/adaptive_calibration.md) |
| Section 3.3.1 | What ancillary access changes in a channel experiment | [Resource assumptions](../science/interpretation.md) |
| Sections 5.1–5.2, especially 5.2.3 | Classical/quantum relative entropy, convexity and data processing | [Reverse test and adaptive divergence](../science/relative_entropy.md) |

This is a selective route, not an assignment to read the entire book. The manuscript's section headings are navigation aids; the local derivations below identify what must be added.

## Notation and conventions

A column vector $`u`$ in the anchor becomes $`|u\rangle`$ here, and $`uv^*`$ becomes $`|u\rangle\langle v|`$. The adjoint $`A^*`$ is written $`A^\dagger`$. A state is a positive operator of trace one. The trace over the probe is $`\operatorname{Tr}_S`$, leaving the retained reference $`R`$.

The input space has dimension $`d=2^n`$. The integer $`r`$ is a Hilbert-space dimension, not a qubit count: $`r=2^k`$ corresponds to $`k`$ retained qubits. A Schmidt rank $`q`$ of a pure input satisfies $`q\leq r`$. An accessible purification is part of the memory budget, not an extra free register used to justify a proof.

We use the natural-log relative entropy

```math
D(\rho\Vert\sigma)
=\operatorname{Tr}[\rho(\ln\rho-\ln\sigma)].
```

When an entropic quantity in the anchor is expressed using base-two logarithms, multiply it by $`\ln2`$ to obtain this convention. It is finite only when the numerator's support is contained in the denominator's support. The classical convention is $`D(p\Vert q)=\sum_xp_x\ln(p_x/q_x)`$. Total variation is half the classical one-norm; quantum trace distance is half the trace norm. These factors matter in the testing proof.

## Bridge 1: a POVM is the complete accessible interface

For a known Pauli observable $`P`$, the two noisy effects would be $`(I\pm\theta P)/2`$. Here the apparatus also selects $`P`$ uniformly from all $`M=d^2-1`$ nonidentity Pauli strings. Its complete outcomes are pairs $`(P,s)`$, with

```math
E_{P,s}(\theta)=\frac{I+s\theta P}{2M}.
```

Positivity follows from the eigenvalues $`\pm1`$ of $`P`$. Summing the two signs gives $`I/M`$, so the label is uniform independently of the input. Summing every outcome gives $`I`$. The input is consumed, and the label is disclosed only afterward.

With a reference, the appropriate output is not just the probability of each label. It is a classical-quantum state whose blocks are unnormalized conditional reference states:

```math
\tau_\theta(\rho_{SR})
=\bigoplus_{P,s}\frac{\sigma_R+s\theta B_P}{2M},
```

```math
\sigma_R=\operatorname{Tr}_S\rho_{SR},
\qquad
B_P=\operatorname{Tr}_S[(P\otimes I_R)\rho_{SR}].
```

A block's trace is its outcome probability. The complete block-diagonal operator has trace one. Discarding the detector outcome leaves $`\sigma_R`$, independent of the detector action. At zero contrast the output is a uniform classical record tensored with that same marginal. These facts connect the measurement definitions in Chapter 2 to the eventual adaptive proof.

## Bridge 2: add the local Fisher-information language

For differentiable classical probabilities, Fisher information is

```math
F(\theta)=\sum_{x:p_x(\theta)>0}
\frac{[\partial_\theta p_x(\theta)]^2}{p_x(\theta)}.
```

It measures local sensitivity, not the error of an arbitrary finite-data estimator. A sign of mean $`\theta`$ has probabilities $`(1\pm\theta)/2`$ and Fisher information $`1/(1-\theta^2)`$.

For a differentiable state family, the symmetric logarithmic derivative $`L`$ solves $`(\rho L+L\rho)/2=\dot\rho`$. Its information is $`F_Q=\operatorname{Tr}(\rho L^2)`$. The canonical [Fisher page](../science/fisher_information.md) develops the equivalent quadratic form

```math
g_A(T,T)=
\sum_{a,b:\lambda_a+\lambda_b>0}
\frac{2|T_{ab}|^2}{\lambda_a+\lambda_b}.
```

Here the entries of the tangent $`T`$ are in an eigenbasis of $`A`$. This expression works for unnormalized blocks and includes support–kernel terms. For a fixed probe the detector tangent stays within the reference support; a parameter-dependent incoming state in an adaptive experiment can have additional off-diagonal tangent terms. The proof must retain them.

Convexity allows a pure-state calculation to bound mixed inputs without adding a physical purification. Pauli completeness then gives

```math
F(0)\leq\frac{dr-1}{d^2-1}=:c_r.
```

The finite-contrast extension uses an operator resolvent bound, not an assumption that the output blocks commute for arbitrary probes. It yields $`F(\theta)\leq c_r/(1-\theta^2)`$. A concrete construction, rather than the upper bound alone, establishes exact attainability.

## Bridge 3: compress a Pauli and obtain an erased sign

Choose $`r`$ computational strings and entangle their equally weighted superposition with an $`r`$-dimensional reference. After the detector announces $`P`$, measure the transposed compression $`Q_P`$ on the reference. In this construction its eigenvalues are only $`-1,0,+1`$: a Pauli pairs basis strings, and restricting the pairs either keeps an involution or leaves a zero block.

A zero outcome is an observed erasure. A nonzero outcome $`t`$ gives the corrected sign $`y=st`$. Summing the full output probabilities gives

```math
\Pr(Z=0)=1-c_r,
\qquad
\Pr(Z=\pm1)=\frac{c_r}{2}(1\pm\theta).
```

The probability of an informative call is $`c_r`$, independent of $`\theta`$. Every erased call is still charged. The compression transpose is operational: $`Y^{\mathsf T}=-Y`$, so an odd number of measured $`Y`$ factors needs a classical sign correction. The [worked example](WORKED_EXAMPLE.md) follows the experiment with two input qubits and one reference qubit.

For $`r=2^k`$, the preparation is just $`k`$ Bell pairs and $`n-k`$ fixed input qubits. The general integer-$`r`$ construction proves existence but does not supply an efficient arbitrary-subset encoder.

## Bridge 4: move from an entropy inequality to an adaptive converse

Define the natural-log divergence of a biased sign from a fair sign:

```math
h(\theta)=
\frac{(1+\theta)\ln(1+\theta)+(1-\theta)\ln(1-\theta)}2.
```

The erased-sign experiment has divergence $`c_rh(\theta)`$ against zero. To prove that no allowed probe does better, the [entropy page](../science/relative_entropy.md) adds a reverse-test argument to Chapter 5's data processing: a suitable classical preparation channel reproduces both states, so their quantum divergence cannot exceed that of the preparing distributions. Pauli compression and a positive-coefficient scalar expansion evaluate the resulting bound. The reverse-test method is an attributed research ingredient, not a new general entropy principle.

Later query inputs can differ between the two parameter hypotheses. One cannot reapply a same-input bound to those states without accounting for that difference. At zero, the detector has the product output $`u_X\otimes\eta_R`$. Its unchanged reference marginal gives

```math
D(\tau_\theta(\rho)\Vert\tau_0(\eta))
=D(\tau_\theta(\rho)\Vert\tau_0(\rho))
 +D(\rho_R\Vert\eta_R).
```

Partial-trace data processing bounds the second term by the incoming divergence. A query adds at most $`c_rh(\theta)`$. Conditioning on each classical history, averaging and telescoping proves the $`Nc_rh(\theta)`$ bound for arbitrary adaptive strategies. Independent erased-sign trials attain equality. The [adaptive page](../science/adaptive_calibration.md) attributes the inherited replacer-channel method and supplies the full support argument.

## Bridge 5: derive a global statistical statement

With $`N`$ independent trials, $`\mathbb E Z=c_r\theta`$ and $`\mathbb E Z^2=c_r`$. Therefore

```math
\widetilde\theta=\frac1{Nc_r}\sum_{i=1}^N Z_i,
\qquad
\operatorname{Var}(\widetilde\theta)
=\frac1{Nc_r}-\frac{\theta^2}{N}.
```

Clipping to a promised interval cannot increase squared error. The converse uses a different idea: accurate estimation at both zero and a small nonzero contrast would distinguish those hypotheses. Chapter 3 supplies the testing perspective; the local [Pinsker and two-point argument](../science/adaptive_calibration.md) combines it with the adaptive divergence bound. This yields matching minimax rates without assuming unbiasedness.

On $`[-a,a]`$, with $`0<a<1`$, the minimax mean-square error lies between $`1/32`$ and $`1`$ times $`\min\{a^2,1/(Nc_r)\}`$. Uniform high-confidence accuracy adds the factor $`\log(1/\delta)`$ in the stated nontrivial regime. An exact Fisher formula is not, by itself, a proof of either global assertion.

## Integrate the scientific meaning

The memory law combines an interface restriction, a constructive experiment and a converse valid for arbitrary adaptive controls. Announcing the Pauli before preparation removes the memory penalty. Returning the probe, revealing internal detector records, or granting uncounted coherent storage also changes the model.

The [source comparison](../references/RELATED_WORK.md) credits prior depolarizing information formulas, ancillary detector calibration, Pauli-learning resource laws and replacer amortization. The contribution is their evaluated consequence in the stated destructive scalar detector model, including its finite-contrast frontier and charged-memory calibration guarantee. The [one-qubit counterexample](../science/single_parameter_counterexample.md) addresses a specific universal equality, not every claim in the cited detector-estimation work.

The final [milestones](MILESTONES.md) combine these ingredients and their boundaries. Understanding the project means being able to state the experiment, explain why retained memory helps, locate the proof steps and distinguish exact information frontiers from rate-optimal statistical performance.
