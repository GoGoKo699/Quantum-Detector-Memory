# Exact relative entropy in one detector use

The [detector model](model.md) admits a sharp information bound for every retained quantum-memory dimension. Let $`d=2^n`$, $`M=d^2-1`$, and let $`\mathcal P_n^\circ`$ denote the nonidentity Hermitian Paulis. For $`1\leq r\leq d`$, write

```math
c_r=\frac{dr-1}{d^2-1},
\qquad
h(\theta)=
\frac{(1+\theta)\log(1+\theta)+(1-\theta)\log(1-\theta)}2.
```

All logarithms are natural. The function $`h(\theta)`$ is the relative entropy of a sign of mean $`\theta`$ relative to a fair sign.

**Theorem.** For every $`|\theta|\lt1`$,

```math
\sup_{\rho_{SR}:\,\dim R\leq r}
D\!\left(
(\Lambda_\theta\otimes\operatorname{id}_R)(\rho)
\,\middle\Vert\,
(\Lambda_0\otimes\operatorname{id}_R)(\rho)
\right)
=c_rh(\theta).
```

The input is the same under the two parameters. A single parameter-independent input and readout attain the supremum for every $`\theta`$. The proof covers arbitrary mixed inputs and every integer $`r`$.

## Output blocks and their support

For a state $`\rho_{SR}`$, define

```math
\sigma_R=\operatorname{Tr}_S\rho,
\qquad
B_P=\operatorname{Tr}_S[(P\otimes I_R)\rho],
\qquad
\tau_\theta(\rho)=(\Lambda_\theta\otimes\operatorname{id}_R)(\rho).
```

The classical detector output labels orthogonal blocks:

```math
\tau_\theta(\rho)
=\bigoplus_{P\in\mathcal P_n^\circ,\;s=\pm1}
\frac{\sigma_R+s\theta B_P}{2M}.
```

Partial-trace cyclicity makes $`B_P`$ Hermitian, and positivity of $`I\pm P`$ gives

```math
-\sigma_R\leq B_P\leq\sigma_R.
```

Thus $`B_P`$ is supported on $`\operatorname{supp}\sigma_R`$. If $`u_X=I_X/(2M)`$ is the uniform detector-output state, then

```math
\tau_0(\rho)=u_X\otimes\sigma_R,
\qquad
(1-|\theta|)\tau_0(\rho)
\leq\tau_\theta(\rho)
\leq(1+|\theta|)\tau_0(\rho).
```

The two output states therefore have the same support in the interior parameter interval. Their relative entropy is finite, and all inverses below act only on the specified support. The retained marginal is unchanged:

```math
\operatorname{Tr}_X\tau_\theta(\rho)=\sigma_R.
```

## A reverse-test upper bound

We use an established relation between Umegaki and maximal relative entropy, with a short proof that fixes its operator ordering and support convention. This reverse-test method is due to [Matsumoto](../references/RELATED_WORK.md#matsumoto2010).

**Lemma.** Let $`A,B`$ be density operators with $`\operatorname{supp}A\subseteq\operatorname{supp}B`$, and set

```math
X=B^{-1/2}AB^{-1/2}
```

on $`\operatorname{supp}B`$. With $`0\log0=0`$,

```math
D(A\Vert B)\leq
\operatorname{Tr}[B\,X\log X]
=:\widehat D(A\Vert B).
```

The right side is the Belavkin–Staszewski, or maximal $`x\log x`$, relative entropy. Equality holds when $`A`$ and $`B`$ commute.

**Proof.** Diagonalize $`X=\sum_jx_j|j\rangle\langle j|`$ and put

```math
q_j=\langle j|B|j\rangle,
\qquad
p_j=x_jq_j,
\qquad
\omega_j=
\frac{B^{1/2}|j\rangle\langle j|B^{1/2}}{q_j}.
```

Since $`B`$ is faithful on its support, $`q_j\gt0`$. Both $`p`$ and $`q`$ are probability distributions. The classical-to-quantum preparation map $`j\mapsto\omega_j`$ maps $`p`$ to $`A`$ and $`q`$ to $`B`$. Data processing gives

```math
D(A\Vert B)
\leq D(p\Vert q)
=\sum_jq_jx_j\log x_j
=\operatorname{Tr}[B\,X\log X].
```

Zero eigenvalues of $`X`$ contribute zero. Simultaneous diagonalization proves equality in the commuting case. $`\square`$

Only this explicit upper bound is needed here; no properties of maximal relative entropy beyond the displayed construction are assumed.

## Pure inputs and Pauli compression

Let the input have Schmidt rank $`q\leq r`$:

```math
|\psi\rangle
=\sum_{a=1}^{q}\sqrt{\lambda_a}\,|u_a\rangle_S|a\rangle_R,
\qquad
\lambda_a\gt0,
\qquad
\sum_a\lambda_a=1.
```

Let $`U:\mathbb C^q\to\mathbb C^d`$ be the Schmidt isometry, $`U|a\rangle=|u_a\rangle`$, and set $`\Pi=UU^\dagger`$. On the memory support,

```math
\sigma_R=\operatorname{diag}(\lambda_1,\ldots,\lambda_q),
\qquad
Q_P=(U^\dagger P U)^{\mathsf T},
\qquad
B_P=\sqrt{\sigma_R}\,Q_P\sqrt{\sigma_R}.
```

Each $`Q_P`$ is a Hermitian contraction. The transpose is taken in the specified Schmidt basis.

The Pauli twirl gives

```math
\sum_{P\in\mathcal P_n^\circ}P\Pi P=dqI-\Pi.
```

Compressing by $`U`$ and transposing yields the identity

```math
\boxed{\displaystyle
\sum_{P\in\mathcal P_n^\circ}Q_P^2=(dq-1)I_q.}
```

It holds for every Schmidt subspace.

Apply the reverse-test lemma to the complete normalized output states. Their relative likelihood operator has blocks $`I+s\theta Q_P`$, so

```math
\begin{aligned}
D(\tau_\theta(\psi)\Vert\tau_0(\psi))
&\leq
\frac1{2M}\sum_{P,s}
\operatorname{Tr}\!\left[
\sigma_R(I+s\theta Q_P)\log(I+s\theta Q_P)
\right]\\
&=\frac1M\sum_P\operatorname{Tr}[\sigma_Rh(\theta Q_P)].
\end{aligned}
```

Using the complete output avoids applying a normalized-state formula separately to blocks of unequal trace.

The expansion

```math
h(z)=\sum_{m=1}^{\infty}
\frac{z^{2m}}{2m(2m-1)}
```

has nonnegative coefficients. Hence $`h(\theta x)\leq x^2h(\theta)`$ for $`|x|\leq1`$. Functional calculus and the compression identity imply

```math
\begin{aligned}
D(\tau_\theta(\psi)\Vert\tau_0(\psi))
&\leq
\frac{h(\theta)}M
\operatorname{Tr}\!\left[
\sigma_R\sum_PQ_P^2
\right]\\
&=\frac{dq-1}{M}h(\theta)
\leq c_rh(\theta).
\end{aligned}
```

## Mixed inputs and equality

Take a pure-state decomposition $`\rho=\sum_jp_j|\psi_j\rangle\langle\psi_j|`$ within the original $`d\times r`$ space. Add a classical flag $`j`$ to both output mixtures and then discard it. Data processing gives

```math
\begin{aligned}
D(\tau_\theta(\rho)\Vert\tau_0(\rho))
&\leq
\sum_jp_j
D(\tau_\theta(\psi_j)\Vert\tau_0(\psi_j))\\
&\leq c_rh(\theta).
\end{aligned}
```

Every component has Schmidt rank at most $`r`$. This is the usual joint-convexity argument; it does not introduce an uncharged quantum purification.

For equality, use the [attaining protocol](attaining_protocol.md): choose any $`r`$ computational basis strings $`C=\{x_1,\ldots,x_r\}`$ and prepare

```math
|\psi_C\rangle
=\frac1{\sqrt r}\sum_{j=1}^{r}|x_j\rangle_S|j\rangle_R.
```

Its memory marginal is $`I_r/r`$. Each compressed Pauli has spectrum contained in $`\{-1,0,+1\}`$: a Hermitian Pauli is a permutation with phases and two-cycles, and restricting it to $`C`$ either retains a complete cycle or leaves a zero block. The output states commute, making the reverse-test bound tight. The scalar inequality is also tight at every compressed eigenvalue. With $`q=r`$, this proves the theorem.

The protocol produces an observed variable $`Z\in\{0,-1,+1\}`$ with law

```math
\Pr_\theta(Z=0)=1-c_r,
\qquad
\Pr_\theta(Z=\pm1)=\frac{c_r}{2}(1\pm\theta).
```

Its classical relative entropy against $`\theta=0`$ is exactly $`c_rh(\theta)`$. Thus the sharp bound is operationally attainable by measuring the memory after the Pauli label arrives.

The [adaptive calibration theorem](adaptive_calibration.md) uses the unchanged memory marginal to convert this one-use result into an exact bound for arbitrary sequential strategies.
