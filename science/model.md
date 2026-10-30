# Question, model and exact results

How much retained quantum memory is needed to calibrate a detector that destroys every probe and returns only a classical record? The answer depends on when the detector reveals its measurement setting. A reference system can preserve a correlation with a setting that was unknown when the probe entered the device.

This project studies one unknown contrast shared by a known family of randomly selected Pauli measurements. It gives exact information frontiers and a matching global estimation rate. The unknown is a single scalar; no unknown Pauli direction or list of channel eigenvalues must be learned.

## Detector and order of access

Let $`n\geq1`$, $`d=2^n`$, and $`M=d^2-1`$. Write $`\mathcal P_n^\circ`$ for the $`M`$ nonidentity Hermitian tensor-product Pauli operators. One detector use consumes a system $`S`$ of dimension $`d`$ and returns the classical pair $`X=(P,s)`$ with effects

```math
E_{P,s}(\theta)=\frac{I+s\theta P}{2M},
\qquad P\in\mathcal P_n^\circ,\quad s\in\{-1,+1\},
\quad -1\lt\theta\lt1.
```

These effects are positive and sum to the identity. The corresponding channel is

```math
\Lambda_\theta(A)
=\sum_{P,s}\operatorname{Tr}[E_{P,s}(\theta)A]\,
   \lvert P,s\rangle\langle P,s\rvert .
```

Operationally the detector selects a fresh uniform $`P`$, performs its noisy sign measurement, consumes the probe, and then discloses both $`P`$ and $`s`$. The label is independent of the input because

```math
\sum_s E_{P,s}(\theta)=I/M.
```

The user cannot choose or learn $`P`$ before preparing the current probe. Across uses, the private labels and detector noise are independent, with the same unknown $`\theta`$. This is a memoryless-device assumption.

A direct implementation measures the local Pauli factors, computes their parity, flips the parity with probability $`(1-\theta)/2`$, and discards all quantum outputs and finer measurement records. The detector is a classical-output interface even when its probe was entangled with an external reference.

## The charged resource

Fix an integer $`1\leq r\leq d`$. At every detector call, **all retained coherent systems accessible to the protocol outside the current input** have joint Hilbert-space dimension at most $`r`$, conditional on the complete classical history. Retained references, coherent controllers, unmeasured future probes, deferred quantum records and purifications all count. The current $`d`$-dimensional input is the sole exception. Irreversibly discarded environments unavailable to the protocol are not retained memory; an accessible purification is.

Between calls, the experimenter may use arbitrary parameter-independent channels and instruments, history-dependent preparation, fresh ancillas, measurements and resets. Any quantum information surviving the next call must fit within the same retained dimension. Classical memory and independent randomness are unrestricted. Preparation and reference readout are trusted and ideal. Initial resources contain no information about $`\theta`$.

The budget $`N`$ counts every use, including failed preparations or postselection branches that use the device. Results concern the normalized complete experiment, with success and failure flags retained. At most $`N`$ means a worst-case budget, not an expected stopping-time budget. Unused calls may be padded and discarded.

For $`r=2^k`$, this is a cap of $`k`$ retained qubits during each invocation, in addition to the $`n`$-qubit probe. The local construction uses $`k`$ Bell pairs and $`n-k`$ fixed input qubits. No external quantum store is left uncharged.

## Output with a retained reference

For an input state $`\rho_{SR}`$, define

```math
\sigma_R=\operatorname{Tr}_S\rho_{SR},
\qquad
B_P=\operatorname{Tr}_S[(P\otimes I_R)\rho_{SR}],
\qquad
\tau_\theta(\rho)=(\Lambda_\theta\otimes\operatorname{id}_R)(\rho).
```

Then

```math
\tau_\theta(\rho)
=\bigoplus_{P,s}\frac{\sigma_R+s\theta B_P}{2M},
\qquad
-\sigma_R\preceq B_P\preceq\sigma_R.
```

The reference marginal stays equal to $`\sigma_R`$ after the detector outcome is ignored. At zero contrast,

```math
\tau_0(\rho)=u_X\otimes\sigma_R,
\qquad u_X=\frac{I_X}{2M}.
```

Every interior output block has the same support as $`\sigma_R`$. Inverse operators in the proofs are restricted to their stated supports; the Fisher proof uses the full Moore–Penrose Jordan inverse where a general incoming tangent requires it.

## Quantities and exact claims

All logarithms are natural. Define

```math
c_r=\frac{dr-1}{d^2-1},
\qquad
h(\theta)=\frac{(1+\theta)\log(1+\theta)
                  +(1-\theta)\log(1-\theta)}{2}.
```

The coefficient $`c_r`$ will become the probability that one use supplies an informative Bernoulli sign. The function $`h`$ is that sign's relative entropy against a fair sign.

| Result | Statement | Authoritative proof |
|---|---|---|
| One-use Fisher information | $`F_r^\star(\theta)=c_r/(1-\theta^2)`$ for all interior contrasts | [Fisher information](fisher_information.md) |
| One-use relative entropy against zero | $`D_r^\star(\theta\Vert0)=c_rh(\theta)`$ | [Relative entropy](relative_entropy.md) |
| Arbitrary adaptive uses, relative entropy against zero | $`\sup_{\mathsf A}D(\omega_\theta^{\mathsf A,N}\Vert\omega_0^{\mathsf A,N})=Nc_rh(\theta)`$ | [Adaptive calibration](adaptive_calibration.md) |
| Arbitrary adaptive uses, Fisher information at zero | $`\sup_{\mathsf A}F_Q(\omega_\theta^{\mathsf A,N})\vert_{\theta=0}=Nc_r`$ | [Fisher information](fisher_information.md) |
| A common attaining input and readout | Every integer $`r`$ admits an exact flagged-erasure coin with informative probability $`c_r`$ | [Attaining protocol](attaining_protocol.md) |

One-use inputs in the first two rows are parameter independent. Adaptive incoming states may depend on $`\theta`$ through previous queries, and the converse explicitly accounts for that dependence. An arbitrary final readout and unrestricted classical processing are included.

For $`0\lt a\lt1`$, let $`R_N(a;d,r)`$ be the infimum, over all admissible protocols and all estimators, of worst-case mean-square error on $`[-a,a]`$. No local-unbiasedness condition is imposed. For $`N\geq1`$,

```math
\frac1{32}\min\!\left\{a^2,\frac1{Nc_r}\right\}
\leq R_N(a;d,r)
\leq\min\!\left\{a^2,\frac1{Nc_r}\right\}.
```

For uniform additive accuracy $`0\lt\epsilon\leq a/3`$ and failure probability $`0\lt\delta\leq1/4`$, the corresponding worst-case query complexity satisfies

```math
\frac{\log(1/\delta)}{36c_r\epsilon^2}
\leq N^\star(\epsilon,\delta;a,d,r)
\leq
\left\lceil\frac{4\log(2/\delta)}{c_r\epsilon^2}\right\rceil.
```

These are matching rates with explicit, nonoptimal constants. The [statistical proof](adaptive_calibration.md) uses the exact adaptive divergence, binary testing reductions and a concrete estimator. With $`r=2^k`$,

```math
\frac1{c_{2^k}}
=\frac{2^{2n}-1}{2^{n+k}-1}
=\Theta(2^{n-k}).
```

Thus root-mean-square accuracy $`\epsilon`$ costs $`\Theta(2^{n-k}/\epsilon^2)`$ on a fixed interval containing zero, in the nontrivial small-error regime. High confidence adds the displayed logarithmic factor.

## Reading route and dependencies

Read the [attaining protocol](attaining_protocol.md) first for the physical mechanism. The [Fisher proof](fisher_information.md) combines Pauli completeness with an operator resolvent bound. The [entropy proof](relative_entropy.md) combines a reverse-test inequality with compressed-Pauli completeness. The [adaptive account](adaptive_calibration.md) applies the established replacer-channel chain rule and derives global risk and confidence bounds.

The [single-qubit example](single_parameter_counterexample.md) isolates the consequence for a general single-parameter no-ancilla claim and identifies the minimax reasoning that fails. The [interpretation](interpretation.md) compares the detector with its depolarizing-channel ancestor and states the resource boundaries. [Related work](../references/RELATED_WORK.md) attributes the inherited mechanisms and records the limits of the source comparison.

## What exactness does and does not mean

The information frontiers above are exact. The global finite-sample risk is bounded within universal constants. The erasure-coin experiment is a sufficient representation of the attaining construction; it does not dominate every other input for every decision loss. An explicit one-call counterexample appears in the [adaptive account](adaptive_calibration.md).

No exact adaptive Fisher optimum at nonzero contrast, exact finite-sample minimax constant, or minimax law for every interval excluding zero is claimed. The detector effects are valid at the endpoints, but the finite Fisher formulas are stated only on the interior. Increasing memory beyond $`d`$ cannot beat the full-memory coefficient one.

If the label is known before preparation, an eigenstate of that label supplies an informative sign every time and removes the memory separation. Changing the label timing, returning the quantum probe, supplying a free purification, or allowing correlated device calls changes the experiment.
