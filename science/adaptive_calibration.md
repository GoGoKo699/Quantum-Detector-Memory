# Adaptive calibration and global statistical guarantees

The [one-use entropy frontier](relative_entropy.md) controls arbitrary sequential protocols, including protocols that keep quantum information between detector calls and use unrestricted classical feedback. With

```math
c_r=\frac{dr-1}{d^2-1},
\qquad
h(\theta)=
\frac{(1+\theta)\log(1+\theta)+(1-\theta)\log(1-\theta)}2,
```

the maximum final relative entropy between parameter $`\theta`$ and parameter zero is exactly $`Nc_rh(\theta)`$ after $`N`$ calls.

The [model](model.md) counts every coherent system outside the detector in the memory bound $`r`$ at each query, conditional on the complete classical history. Initial states and controls are parameter-independent. The current input is consumed by the detector, and the Pauli label is disclosed afterward. Query budgets are worst-case bounds. All output records, including abort and postselection-failure flags, belong to the statistical experiment.

## Exact amortization against zero

Write

```math
\tau_\theta(\rho)
=(\Lambda_\theta\otimes\operatorname{id}_R)(\rho).
```

For any incoming state $`\eta_{SR}`$,

```math
\tau_0(\eta)=u_X\otimes\eta_R,
```

where $`u_X`$ is the uniform detector-output state. The memory marginal of $`\tau_\theta(\rho)`$ is $`\rho_R`$ for every $`\theta`$.

Take two possibly different incoming states $`\rho,\eta`$ with $`D(\rho\Vert\eta)\lt\infty`$. Expanding the logarithm of the product reference and using the unchanged memory marginal gives the exact identity

```math
\begin{aligned}
D(\tau_\theta(\rho)\Vert\tau_0(\eta))
&=D(\tau_\theta(\rho)\Vert u_X\otimes\eta_R)\\
&=D(\tau_\theta(\rho)\Vert u_X\otimes\rho_R)
 +D(\rho_R\Vert\eta_R).
\end{aligned}
```

The support inclusion needed here follows from finite input divergence. The first term is bounded by $`c_rh(\theta)`$ using the one-use theorem; the second is at most $`D(\rho\Vert\eta)`$ by partial-trace data processing. Therefore

```math
\boxed{\displaystyle
D(\tau_\theta(\rho)\Vert\tau_0(\eta))
-D(\rho\Vert\eta)
\leq c_rh(\theta).}
```

The supremum of this difference over finite-divergence pairs is exactly $`c_rh(\theta)`$: take the same attaining input under both hypotheses. Restricting the difference to finite-divergence pairs avoids undefined subtraction of infinities.

This marginal-replacement argument is the established replacer-channel amortization method of [Wilde, Berta, Hirche, and Kaur](../references/RELATED_WORK.md#wilde2020). The detector-specific ingredient is the evaluated, attainable coefficient $`c_rh(\theta)`$. Applying the inherited algebra to a fixed reference dimension and then to each classical history gives the bound below.

## Unlimited classical history and sequential control

Before a query, the states under the two hypotheses can be written

```math
\rho_{HSR}=\bigoplus_h p_h\rho_{SR}^h,
\qquad
\eta_{HSR}=\bigoplus_h q_h\eta_{SR}^h.
```

The register $`H`$ records the complete classical history, and each conditional memory has dimension at most $`r`$. Relative entropy obeys the direct-sum identity

```math
D(\rho_{HSR}\Vert\eta_{HSR})
=D(p\Vert q)+\sum_h p_hD(\rho_{SR}^h\Vert\eta_{SR}^h).
```

Apply the amortized bound on each history. A query leaves the pre-existing classical probabilities unchanged and increases the conditional divergence by at most $`c_rh(\theta)`$. Averaging adds at most this same quantity because the weights sum to one. For measurable classical records, the sum is the corresponding integral over conditional density matrices.

A history-dependent instrument is a single parameter-independent channel on the joint classical-quantum state, so data processing covers every intermediate preparation, measurement, reset, and control. Starting from the same initial state under both hypotheses gives

```math
D(\omega_\theta^{\mathsf A,N}\Vert\omega_0^{\mathsf A,N})
\leq Nc_rh(\theta)
```

for the final state of every admissible protocol $`\mathsf A`$. The induction keeps these divergences finite; full-rank intermediate states are unnecessary. A final readout can only decrease the divergence.

Repeating the [attaining protocol](attaining_protocol.md) independently and retaining all classical observations gives a product of erased-sign experiments. Additivity then attains equality:

```math
\boxed{\displaystyle
\sup_{\mathsf A:\,N\text{ calls},\,\dim R\leq r}
D(\omega_\theta^{\mathsf A,N}\Vert\omega_0^{\mathsf A,N})
=Nc_rh(\theta).}
```

Protocols using at most $`N`$ calls are included by padding with unused queries. Each coherent side system, including future probes or a deferred quantum record, must obey the stated memory bound. Classical outcomes can be retained freely because they enter as the direct-sum register above.

## Squared-error minimax risk

Fix $`0\lt a\lt1`$ and define

```math
R_N(a;d,r)=
\inf_{\mathsf A,\widehat\theta}
\sup_{\theta\in[-a,a]}
\mathbb E_\theta[(\widehat\theta-\theta)^2],
```

where the infimum permits all admissible protocols using at most $`N`$ calls and arbitrary estimators. There is no unbiasedness restriction.

**Theorem.** For $`N\geq1`$,

```math
\boxed{\displaystyle
\frac1{32}\min\!\left\{a^2,\frac1{Nc_r}\right\}
\leq R_N(a;d,r)
\leq\min\!\left\{a^2,\frac1{Nc_r}\right\}.}
```

These universal constants are explicit but are not asserted to be sharp.

### Upper bound

In each independent use of the attaining protocol, the observed variable has law

```math
\Pr_\theta(Z=0)=1-c_r,
\qquad
\Pr_\theta(Z=\pm1)=\frac{c_r}{2}(1\pm\theta).
```

Thus $`\mathbb E_\theta Z=c_r\theta`$ and $`\mathbb E_\theta Z^2=c_r`$. The estimator

```math
\widetilde\theta=\frac1{Nc_r}\sum_{i=1}^{N}Z_i
```

is unbiased and satisfies

```math
\mathbb E_\theta[(\widetilde\theta-\theta)^2]
=\frac1{Nc_r}-\frac{\theta^2}{N}
\leq\frac1{Nc_r}.
```

Projecting it onto $`[-a,a]`$ cannot increase its squared error. Alternatively, the constant estimator zero has worst-case error $`a^2`$. Selecting the better strategy using the known values $`N,c_r,a`$ proves the upper bound.

### Lower bound

The positive-coefficient expansion of $`h`$ gives

```math
\frac{\theta^2}{2}
\leq h(\theta)
\leq(\log2)\theta^2
\leq\theta^2,
\qquad |\theta|\leq1.
```

Set

```math
\Delta=\min\!\left\{a,\frac1{\sqrt{2Nc_r}}\right\}.
```

For any protocol, the adaptive entropy bound yields

```math
D(\omega_\Delta\Vert\omega_0)
\leq Nc_rh(\Delta)
\leq Nc_r\Delta^2
\leq\frac12.
```

Let $`P_\Delta,P_0`$ be the classical laws of its final estimator. Data processing and Pinsker's inequality imply $`\operatorname{TV}(P_\Delta,P_0)\leq1/2`$.

Threshold the estimate at $`\Delta/2`$ to test zero against $`\Delta`$. A test error under either hypothesis incurs squared estimation error at least $`\Delta^2/4`$. Hence

```math
\begin{aligned}
\max_{\theta\in\{0,\Delta\}}
\mathbb E_\theta[(\widehat\theta-\theta)^2]
&\geq\frac{\Delta^2}{8}
\left[P_0(\text{choose }\Delta)
      +P_\Delta(\text{choose }0)\right]\\
&\geq\frac{\Delta^2}{8}
\left[1-\operatorname{TV}(P_\Delta,P_0)\right]\\
&\geq\frac{\Delta^2}{16}\\
&\geq\frac1{32}\min\!\left\{a^2,\frac1{Nc_r}\right\}.
\end{aligned}
```

This holds for every protocol and estimator and proves the theorem. With no queries, the minimax risk on the symmetric interval is exactly $`a^2`$.

The same rate extends to the full open interval $`(-1,1)`$, replacing $`a^2`$ by 1: take the supremum over compact subintervals in the lower bound and clip to $`[-1,1]`$ in the upper bound.

## Uniform high-confidence estimation

Let $`N^\star(\epsilon,\delta;a,d,r)`$ be the smallest worst-case query budget for which

```math
\sup_{\theta\in[-a,a]}
\Pr_\theta(|\widehat\theta-\theta|\gt\epsilon)
\leq\delta.
```

Assume $`0\lt\epsilon\leq a/3`$ and $`0\lt\delta\leq1/4`$. Then

```math
\boxed{\displaystyle
\frac{\log(1/\delta)}{36c_r\epsilon^2}
\leq N^\star(\epsilon,\delta;a,d,r)
\leq
\left\lceil
\frac{4\log(2/\delta)}{c_r\epsilon^2}
\right\rceil.}
```

### An estimator with the stated confidence

Use independent erased-sign observations and let $`K`$ be the number of non-erased signs. If $`K\gt0`$, average those signs; if $`K=0`$, return zero. Every erasure consumes a query and remains part of the observed record.

Conditional on $`K=k`$, the informative signs are independent and have mean $`\theta`$. A sign $`Y`$ satisfies

```math
\mathbb E_\theta e^{t(Y-\theta)}\leq e^{t^2/2}.
```

Indeed the second derivative of the log moment-generating function is a tilted variance, bounded by 1, while its value and first derivative vanish at zero. Chernoff's method therefore gives

```math
\Pr_\theta(|\widehat\theta-\theta|\gt\epsilon\mid K=k)
\leq2e^{-k\epsilon^2/2}.
```

The bound remains valid at $`k=0`$, where its right side is 2. Since $`K`$ is binomial with parameters $`N,c_r`$,

```math
\begin{aligned}
\Pr_\theta(|\widehat\theta-\theta|\gt\epsilon)
&\leq2(1-c_r+c_re^{-\epsilon^2/2})^N\\
&\leq2\exp[-Nc_r(1-e^{-\epsilon^2/2})]\\
&\leq2e^{-Nc_r\epsilon^2/4}.
\end{aligned}
```

The last step uses $`\epsilon\leq1`$. Clipping to $`[-a,a]`$ preserves the bound and proves the stated sufficient query budget.

### Matching confidence dependence

An estimator meeting the guarantee at parameters zero and $`3\epsilon`$ produces, by thresholding at $`3\epsilon/2`$, a test with both errors at most $`\delta`$. Binary data processing implies

```math
D(\omega_{3\epsilon}\Vert\omega_0)
\geq
\kappa(\delta)
:=(1-2\delta)\log\frac{1-\delta}{\delta}.
```

The event “choose $`3\epsilon`$” has probability at least $`1-\delta`$ under that hypothesis and at most $`\delta`$ under zero. Binary relative entropy is minimized at these boundary probabilities. The entropy bound consequently gives

```math
N
\geq\frac{\kappa(\delta)}{c_rh(3\epsilon)}
\geq\frac{\kappa(\delta)}{9c_r\epsilon^2}.
```

For $`\delta\leq1/4`$, the inequalities $`1-2\delta\geq1/2`$ and $`1-\delta\geq\sqrt\delta`$ imply $`\kappa(\delta)\geq\frac14\log(1/\delta)`$. This proves the lower bound. The condition $`3\epsilon\leq a`$ places both hypotheses inside the parameter interval.

With $`d=2^n`$ and $`r=2^k`$, these bounds give

```math
N^\star
=\Theta\!\left(
\frac{2^{n-k}}{\epsilon^2}\log\frac1\delta
\right),
\qquad 0\leq k\leq n,
```

within the stated accuracy and confidence regime. At fixed confidence the logarithmic factor is a constant.

## Finite-sample scope

The exact entropy frontier does not imply that the attaining probe minimizes every finite-sample decision loss. A single-qubit example makes this distinction explicit.

For $`d=2,r=1`$ and a pure probe with Bloch vector $`v`$,

```math
p_\theta(a,s)=\frac{1+s\theta v_a}{6},
\qquad
\operatorname{TV}(p_\theta,p_0)
=\frac{|\theta|}{6}
\sum_{a=x,y,z}|v_a|.
```

A Pauli eigenstate, which attains the entropy frontier, gives total variation $`|\theta|/6`$. The valid pure state $`v=(1,1,1)/\sqrt3`$ instead gives

```math
\operatorname{TV}(p_\theta,p_0)=\frac{|\theta|}{2\sqrt3},
```

which is larger. Its one-call equal-prior discrimination error is therefore smaller. The erased-sign experiment does not dominate all other probe experiments in the Blackwell sense.

The conclusions here are exact maximal relative entropy against zero, and matching global minimax and confidence-dependent query rates. They do not determine exact finite-$`N`$ risk or testing error. The comparison against zero also does not supply an exact adaptive Fisher-information frontier at general $`\theta`$ or local minimax constants on intervals excluding zero; the supported Fisher-information statements are given [separately](fisher_information.md).

An expected stopping-time budget or a guarantee conditioned on uncharged postselection would be a different operational problem. The results above count every query and use the entire output experiment, with any abort included in the failure probability.
