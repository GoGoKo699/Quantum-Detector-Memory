# Fisher information and retained quantum memory

The detector reveals which Pauli observable it measured only after consuming the probe. A retained ancilla lets the experimenter respond to that information with a suitable measurement. This page quantifies exactly how much information one use can provide and proves that adaptive reuse cannot exceed the corresponding additive rate at zero visibility.

The [model](model.md) defines the memoryless detector $`\Lambda_\theta`$, the common unknown visibility $`|\theta|\lt1`$, the input dimension $`d=2^n`$, and $`M=d^2-1`$ nonidentity Pauli labels. Throughout this page, $`1\leq r\leq d`$ is the joint dimension of all quantum systems retained outside the detector at a query, and

```math
c_r=\frac{dr-1}{d^2-1}.
```

Classical history is unrestricted. The [attaining experiment](attaining_protocol.md) realizes every integer $`r`$ and gives a simple circuit when $`r=2^k`$.

## T1. Exact Fisher information for one detector use

For every interior visibility $`|\theta|\lt1`$, the largest output symmetric logarithmic derivative quantum Fisher information obtainable from a parameter-independent input is

```math
\boxed{
\sup_{\rho_{SR}:\,\dim R\leq r}
F_Q\!\left[(\Lambda_\theta\otimes\operatorname{id}_R)(\rho_{SR})\right]
=\frac{c_r}{1-\theta^2}.
}
```

The optimization includes mixed and entangled inputs. The same fixed input and the same parameter-independent, label-conditioned ancilla measurement attain the bound for every $`|\theta|\lt1`$. In particular,

```math
F_1(\theta)=\frac{1}{(d+1)(1-\theta^2)},
\qquad
F_d(\theta)=\frac{1}{1-\theta^2}.
```

Full retained memory therefore gives an exact factor $`d+1`$ over the best strategy with no retained quantum system. Intermediate memory has an exact, linear effect through $`dr-1`$. This statement concerns one detector use; it does not assume an unbiased estimator or a particular final measurement.

The proof has three ingredients: a zero-visibility calculation using the Pauli basis, a bound that moves from zero to any interior visibility, and the [explicit attaining protocol](attaining_protocol.md#construction-for-arbitrary-r).

## The SLD quadratic form

For a positive operator $`A`$, define the Jordan superoperator

```math
\mathcal J_A(L)=\frac{AL+LA}{2}.
```

For a compatible Hermitian tangent $`T`$, write

```math
g_A(T,T)=\operatorname{Tr}\!\left[T\mathcal J_A^+(T)\right]
=\sum_{a,b:\lambda_a+\lambda_b\gt0}
\frac{2|T_{ab}|^2}{\lambda_a+\lambda_b},
```

where $`A=\sum_a\lambda_a|a\rangle\langle a|`$ and $`+`$ denotes the Moore–Penrose inverse. The SLD Fisher information of a differentiable normalized family is $`F_Q(\rho_\theta)=g_{\rho_\theta}(\dot\rho_\theta,\dot\rho_\theta)`$.

This definition also handles an unnormalized positive block: its tangent need not have zero trace. Orthogonal classical blocks contribute additively, and

```math
g_{aA}(aT,aT)=a\,g_A(T,T)
\qquad(a\gt0).
```

The full inverse convention matters for singular states. A differentiable two-sided positive family has no kernel–kernel component in its first derivative, but it can have support–kernel off-diagonal components. Those components appear in the displayed sum.

The variational formula

```math
g_A(T,T)=\sup_{L=L^\dagger}
\left\{2\operatorname{Tr}(TL)-\operatorname{Tr}(AL^2)\right\}
```

shows that $`g`$ is jointly convex in the state and tangent. It also gives data processing. For a channel $`\Phi`$, put $`K=\Phi^\dagger(L)`$. The Kadison inequality for its unital completely positive adjoint gives

```math
\begin{aligned}
2\operatorname{Tr}[\Phi(T)L]-\operatorname{Tr}[\Phi(A)L^2]
&=2\operatorname{Tr}(TK)-\operatorname{Tr}[A\Phi^\dagger(L^2)]\\
&\leq2\operatorname{Tr}(TK)-\operatorname{Tr}(AK^2)\\
&\leq g_A(T,T).
\end{aligned}
```

Taking the supremum proves that parameter-independent channels, including measurements whose outcomes are retained, cannot increase SLD Fisher information. These facts are used for mixed inputs and adaptive control below.

## Pauli identities

The identity-inclusive Hermitian Pauli basis obeys

```math
\operatorname{Tr}(PQ)=d\,\delta_{P,Q},
\qquad
\sum_P P A P=d\operatorname{Tr}(A)I_d.
```

Parseval's identity therefore gives, for orthonormal vectors $`|u_a\rangle`$ and $`|u_b\rangle`$,

```math
\sum_{P\ne I}|\langle u_a|P|u_b\rangle|^2
=d-\delta_{ab}.
```

There is also a useful compression identity. If $`V:\mathbb C^q\to\mathbb C^d`$ is an isometry and $`Q_P=(V^\dagger P V)^{\mathsf T}`$, then

```math
\sum_{P\ne I}Q_P^2=(dq-1)I_q.
```

Indeed, before transposing, the left side is

```math
V^\dagger\left[\sum_{P\ne I}P(VV^\dagger)P\right]V
=V^\dagger[dqI_d-VV^\dagger]V
=(dq-1)I_q.
```

These identities fix the dimension dependence in both the upper bound and the attaining protocol.

## The upper bound at zero visibility

For a fixed joint input, use the [model's output blocks](model.md), with

```math
\sigma_R=\operatorname{Tr}_S\rho_{SR},
\qquad
B_P=\operatorname{Tr}_S[(P\otimes I_R)\rho_{SR}].
```

The block labelled $`(P,s)`$ is $`(\sigma_R+s\theta B_P)/(2M)`$. Positivity implies $`-\sigma_R\preceq B_P\preceq\sigma_R`$, so $`B_P`$ is supported on $`\operatorname{supp}\sigma_R`$.

First take a pure state of Schmidt rank $`q\leq r`$,

```math
|\psi\rangle=
\sum_{a=1}^q\sqrt{\lambda_a}\,|u_a\rangle_S|a\rangle_R,
\qquad
\lambda_a\gt0,
\quad\sum_a\lambda_a=1.
```

With $`\Lambda=\operatorname{diag}(\lambda_1,\ldots,\lambda_q)`$ and $`V|a\rangle=|u_a\rangle`$, direct partial tracing gives

```math
\sigma_R=\Lambda,
\qquad
B_P=\sqrt\Lambda\,(V^\dagger PV)^{\mathsf T}\sqrt\Lambda.
```

The transpose is in the displayed Schmidt index basis. The SLD formula and the first Pauli identity give

```math
\begin{aligned}
F_\psi(0)
&=\frac1M\sum_{P\ne I}\sum_{a,b}
\frac{2\lambda_a\lambda_b}{\lambda_a+\lambda_b}
|\langle u_a|P|u_b\rangle|^2\\
&=\frac1M\left[
d-1+d\sum_{a\ne b}
\frac{2\lambda_a\lambda_b}{\lambda_a+\lambda_b}
\right].
\end{aligned}
```

The ordered off-diagonal sum satisfies

```math
\sum_{a\ne b}\frac{2\lambda_a\lambda_b}{\lambda_a+\lambda_b}
\leq\sum_{a\ne b}\frac{\lambda_a+\lambda_b}{2}
=q-1.
```

Consequently,

```math
F_\psi(0)\leq\frac{dq-1}{M}\leq c_r.
```

Equality in the first inequality holds precisely when the nonzero Schmidt weights are uniform, including the rank-one case. Reaching $`c_r`$ additionally requires $`q=r`$.

A mixed input has a pure-state convex decomposition with parameter-independent weights. Both its output and its detector tangent depend linearly on that decomposition. Joint convexity therefore gives the same bound. This is a mathematical decomposition within the permitted input and memory spaces; it does not supply an additional physical purification.

## The upper bound at nonzero visibility

Fix an arbitrary input and one Pauli label. In this subsection, restrict to $`\operatorname{supp}\sigma_R`$, where $`\sigma_R`$ is positive definite, and write $`B=B_P`$. Define

```math
K=\mathcal J_{\sigma_R}^{-1/2}
\mathcal J_B
\mathcal J_{\sigma_R}^{-1/2},
\qquad
w=\mathcal J_{\sigma_R}^{-1/2}(B).
```

These square roots and inverses are functions of **superoperators** on the Hilbert–Schmidt space. No commutation of $`\sigma_R`$ with $`B`$ is assumed. Since $`\sigma_R\pm B`$ are positive, their Jordan superoperators are positive, giving $`-I\preceq K\preceq I`$.

Factor the two Jordan superoperators and pair the signs:

```math
\begin{aligned}
\frac12\sum_{s=\pm1}g_{\sigma_R+s\theta B}(B,B)
&=\frac12\sum_{s=\pm1}
\langle w,(I+s\theta K)^{-1}w\rangle\\
&=\langle w,(I-\theta^2K^2)^{-1}w\rangle\\
&\leq\frac{g_{\sigma_R}(B,B)}{1-\theta^2}.
\end{aligned}
```

The inverse factors commute because both are functions of the same self-adjoint $`K`$. The last inequality follows from its spectrum lying in $`[-1,1]`$. Summing over Pauli labels proves

```math
F_\rho(\theta)
\leq\frac{F_\rho(0)}{1-\theta^2}
\leq\frac{c_r}{1-\theta^2}.
```

The [computational-subset experiment](attaining_protocol.md#construction-for-arbitrary-r) attains this upper bound, completing T1.

### Equality and the orientation of the Schmidt subspace

For a pure input, uniform Schmidt weights at rank $`r`$ attain the zero-visibility frontier in every Schmidt subspace. Away from zero, the subspace also matters.

For a uniform rank-$`q`$ state, the Fisher information is

```math
F_\psi(\theta)=\frac1{Mq}\sum_{P\ne I}
\operatorname{Tr}\!\left[
Q_P^2(I-\theta^2Q_P^2)^{-1}\right],
\qquad Q_P=(V^\dagger PV)^{\mathsf T}.
```

At any nonzero interior $`\theta`$, a pure input attains T1 if and only if its nonzero Schmidt weights are uniform, its Schmidt rank is $`r`$, and every compression obeys $`Q_P^3=Q_P`$. Necessity follows because equality in the zero-visibility bound forces uniform weights, after which the scalar inequality

```math
\frac{x^2}{1-\theta^2x^2}
\leq\frac{x^2}{1-\theta^2}
```

is strict unless $`x\in\{-1,0,+1\}`$. The same condition proves sufficiency. The construction on the next page satisfies it at every integer $`r`$. No classification of all mixed-state optimizers is required.

For example, when $`d=2,r=1`$, the pure state with Bloch vector $`(1,1,1)/\sqrt3`$ is optimal at zero but gives

```math
F(\theta)=\frac1{3(1-\theta^2/3)}
\lt\frac1{3(1-\theta^2)}
\qquad(\theta\ne0).
```

Uniform Schmidt weights alone do not establish attainment at nonzero visibility.

## T2. Exact adaptive Fisher information at zero visibility

Consider a normalized protocol with at most $`N`$ detector uses, parameter-independent initial resources, joint retained quantum dimension at most $`r`$ at every query, and arbitrary classical history. Let $`\omega_\theta^{(N)}`$ denote its complete retained output, including any success and failure records. Then

```math
\boxed{
F_Q(\omega_\theta^{(N)})\big|_{\theta=0}
\leq N c_r.
}
```

Equality is attained by repeated uses of the [erasure-coin experiment](attaining_protocol.md#the-exact-erasure-coin-experiment), resetting the same quantum memory between calls and retaining the classical outcomes. T2 allows the incoming state at a later query to contain parameter information from all previous queries. It establishes an exact optimum at $`\theta=0`$, not an exact adaptive optimum at every visibility.

### The single-query increment

Let the incoming family be $`\rho_{SR}(\theta)`$. At zero, put

```math
\sigma_R=\operatorname{Tr}_S\rho_{SR}(0),
\qquad
T=\operatorname{Tr}_S\dot\rho_{SR}(0),
\qquad
B_P=\operatorname{Tr}_S[(P\otimes I)\rho_{SR}(0)].
```

The output block derivative is

```math
\left.\frac{\mathrm d}{\mathrm d\theta}
\frac{\sigma_R(\theta)+s\theta B_P(\theta)}{2M}
\right|_{0}
=\frac{T+sB_P}{2M}.
```

In particular, $`\dot B_P`$ does not contribute at zero. Quadraticity of the SLD form makes the cross term cancel when the two signs are added:

```math
\begin{aligned}
F_{\mathrm{out}}(0)
&=\frac1{2M}\sum_{P,s}
g_{\sigma_R}(T+sB_P,T+sB_P)\\
&=g_{\sigma_R}(T,T)
+\frac1M\sum_Pg_{\sigma_R}(B_P,B_P).
\end{aligned}
```

This identity uses the full Moore–Penrose inverse for $`T`$; it remains valid if $`T`$ has support–kernel off-diagonal entries. The first term is at most the incoming Fisher information by partial-trace data processing. The second is exactly the fixed-input zero-visibility quantity from T1. Hence a query adds at most $`c_r`$:

```math
F_{\mathrm{out}}(0)\leq F_{\mathrm{in}}(0)+c_r.
```

### Conditioning on classical history

For a discrete classical history $`h`$, the hybrid input has Fisher information

```math
F_Q\!\left[\sum_h p_h(\theta)|h\rangle\langle h|
\otimes\rho_h(\theta)\right]
=\sum_{h:p_h\gt0}\frac{\dot p_h^2}{p_h}
+\sum_h p_h F_Q(\rho_h).
```

Apply the increment bound to each conditional input. The existing classical Fisher term is unchanged by the query, and the average new contribution is at most $`\sum_h p_hc_r=c_r`$. Parameter-independent preparation and postprocessing cannot increase the complete-output Fisher information. It starts at zero, so induction gives T2. Continuous classical histories obey the same proof with integrals under a common dominating measure. A strategy using fewer than $`N`$ calls can be padded with discarded calls without changing its original output.

### Interior support and postselection

Finite physical protocols have regular support throughout $`|\theta|\lt1`$. To see this, expand the detector as

```math
\Lambda_\theta=
\frac{1+\theta}{2}\Lambda_{+1}
+\frac{1-\theta}{2}\Lambda_{-1}.
```

The output of any finite adaptive protocol can therefore be written

```math
\omega_\theta^{(N)}
=\sum_{a\in\{-1,+1\}^N}
2^{-N}\prod_{j=1}^N(1+a_j\theta)\;\omega_a,
```

with fixed positive endpoint-protocol outputs $`\omega_a`$. All coefficients are positive in the interior, so the support is the fixed span of their supports. Intermediate outputs and nonzero classical branches have the same property. For continuous histories, the equally weighted endpoint mixture at zero supplies a common dominating measure, and the statement holds for its matrix densities almost everywhere.

This removes the rank-changing ambiguity between pointwise SLD information and its limit from nearby parameters. It does not make postselection free. Conditional information on a rare success can be large; T2 retains the success probability and charges the queries that failed.

## What the bounds establish

T1 gives exact information per use for every interior visibility. T2 shows that adaptive recycling of the same finite quantum memory cannot evade the corresponding additive limit at zero. These are information statements, not claims that the attaining experiment minimizes every finite-sample loss. For example, a different probe can perform better in a particular single-shot test while having smaller Fisher information.

The [relative-entropy frontier](relative_entropy.md) and its [adaptive calibration consequences](adaptive_calibration.md) provide global risk and sample-complexity bounds without an unbiasedness assumption. The [single-parameter qubit example](single_parameter_counterexample.md) isolates the smallest entanglement advantage. The [related-work discussion](../references/RELATED_WORK.md#frey2011) places the result among earlier examples of entanglement-assisted measurement estimation.

**Next:** [Attaining protocol and implementation costs](attaining_protocol.md) · [Relative entropy](relative_entropy.md) · [Model](model.md).
