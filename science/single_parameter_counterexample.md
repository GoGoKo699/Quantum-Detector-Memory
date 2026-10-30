# A single unknown detector parameter can benefit from an ancilla

The six-outcome qubit member of the [model](model.md) gives a direct operational example: one retained qubit increases the obtainable Fisher information by exactly a factor of three, for every interior contrast. The parameter remains one scalar, the detector output remains classical, and the reference measurement depends only on the reported setting.

## Unassisted qubit

Let $`P`$ range over $`\sigma_x,\sigma_y,\sigma_z`$, and write the input as

```math
\rho_v=\frac{I+v\cdot\sigma}{2},
\qquad \|v\|\leq1.
```

The observed probabilities and their classical Fisher information are

```math
p_\theta(a,s)=\frac{1+s\theta v_a}{6},
\qquad
F_v(\theta)=\frac13\sum_{a=x,y,z}
                    \frac{v_a^2}{1-\theta^2v_a^2}.
```

Because $`v_a^2\leq1`$ and $`\sum_a v_a^2\leq1`$,

```math
F_v(\theta)
\leq\frac{\sum_a v_a^2}{3(1-\theta^2)}
\leq\frac1{3(1-\theta^2)}.
```

A Pauli eigenstate attains the bound. Classical randomization with the preparation label retained averages the component Fisher informations and cannot increase it.

## One retained qubit

Prepare $`\lvert\Phi^+\rangle=(\lvert00\rangle+\lvert11\rangle)/\sqrt2`$ and send the first qubit into the detector. Each outcome $`(a,s)`$ has probability $`1/6`$. Conditional on that outcome, the retained state is

```math
\rho_{R\mid a,s}(\theta)
=\frac{I+s\theta\sigma_a^{\mathsf T}}2.
```

Measure $`\sigma_a^{\mathsf T}`$ on the retained qubit and call the result $`t\in\{-1,+1\}`$. The sign $`y=st`$ obeys

```math
\Pr_\theta(y=\pm1)=\frac{1\pm\theta}{2},
\qquad
F_{\rm Bell}(\theta)=\frac1{1-\theta^2}.
```

The transpose is essential: $`\sigma_y^{\mathsf T}=-\sigma_y`$. One may measure $`\sigma_y`$ and reverse that known sign in classical processing.

The advantage is a factor of three in Fisher information. In the usual regular local estimation regime, the associated standard-deviation ratio is $`\sqrt3`$ at equal sample size, not three. The [global bounds](adaptive_calibration.md) establish a sample-resource advantage without relying on local unbiasedness.

## The reduced-state optimization makes the issue explicit

Take any pure probe-reference state with reduced probe Bloch length $`R`$. Its Schmidt eigenvalues are $`\lambda_\pm=(1\pm R)/2`$. Substituting these in the pure-input expression from the [Fisher proof](fisher_information.md) gives, at zero contrast,

```math
F_{\rm purified}(0)
=\frac{1+8\lambda_+\lambda_-}{3}
=1-\frac23R^2.
```

A pure reduced probe has $`R=1`$ and information $`1/3`$. The unique maximizing reduced state is $`I/2`$, with information one. This mixed reduced state is physically realized by the pure entangled input above.

The distinction is between the joint input being pure and its reduced probe being pure. Requiring a pure reduced probe removes entanglement with the reference.

## Relation to the general no-advantage claim

[Das et al.](../references/RELATED_WORK.md#das2026), *Precision bounds for characterising quantum measurements*, consider detector estimation with outcome-conditioned ancillary measurements. Their arXiv version 2, Supplement II.F, Theorem 4 and Corollary 1, states equality of the extended detector quantity and the maximum unassisted classical Fisher information. The construction above violates that equality under the stated access model.

The relevant proof at Eq. (SM.II.20) exchanges a minimization over admissible logarithmic-derivative operators with a maximization over the reduced probe. For fixed derivative operators, the objective is linear in the reduced state and has a pure maximizer. After minimization, it is a concave lower envelope of linear functions. A concave function can have its maximum in the interior; the pure-state restriction no longer follows.

The displayed function $`1-2R^2/3`$ exhibits that failure directly. The counterexample establishes the failure of the universal equality/no-ancilla statement. It does not invalidate every upper bound, commuting-model result or experimental example in that work.

The published main text and arXiv v2 supplementary proof were checked separately. The proof-level comparison is pinned to arXiv v2; it does not silently equate an inaccessible supplementary version with that source.

## Why classical output does not eliminate the advantage

After the detector call, its record and the retained reference form a classical–quantum state. The detector has destroyed entanglement across its output interface, but the reference states still depend on both the contrast and the reported setting. Measuring the reference after learning the setting extracts that dependence.

An unassisted probe cannot be an eigenstate of all three incompatible Pauli observables. A maximally entangled probe-reference pair supplies the appropriate correlation in each reported basis. The general [construction](attaining_protocol.md) counts exactly how much of this capability remains when the reference dimension is restricted.

This is compatible with the existence of classical-output channels that have no ancilla advantage under additional hypotheses. A no-advantage condition must apply to the actual model; the absence of a quantum output alone is insufficient.

## Decision loss still matters

For one-call testing against zero, the unassisted experiment has

```math
\operatorname{TV}(p_\theta,p_0)
=\frac{|\theta|}{6}\sum_a|v_a|.
```

A Pauli eigenstate gives $`|\theta|/6`$. A pure probe with $`v=(1,1,1)/\sqrt3`$ gives $`|\theta|/(2\sqrt3)`$, which is larger. Thus the unassisted Fisher- and relative-entropy-optimal probe need not minimize one-call Bayesian testing error. This qualification is consistent with every exact information frontier and the minimax rate theorem.
