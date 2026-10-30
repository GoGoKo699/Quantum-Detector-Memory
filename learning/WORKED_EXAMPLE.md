# Two input qubits, one retained qubit

[Learning route](README.md) · [Watrous bridge](WATROUS_BRIDGE.md) · [Exact construction](../science/attaining_protocol.md)

## Prepare the experiment

Let the detector consume two qubits $`S_1,S_2`$. Retain one qubit $`R`$ outside it. Prepare a Bell pair between $`S_1`$ and $`R`$, and prepare $`S_2`$ in $`|0\rangle`$:

```math
|\psi\rangle=|\Phi^+\rangle_{S_1R}\otimes|0\rangle_{S_2},
\qquad |\Phi^+\rangle=(|00\rangle+|11\rangle)/\sqrt2.
```

The probe dimension is $`d=4`$ and retained dimension is $`r=2`$. The apparatus independently selects one of the fifteen nonidentity two-qubit Paulis, consumes the probe, then reports that Pauli $`P`$ and its noisy sign $`s`$. Only these two pieces of detector data are accessible. The unknown contrast is $`\theta`$; preparation and reference readout are trusted.

## Decide which records are informative

Write $`P=A\otimes B`$. If the second factor is $`X`$ or $`Y`$, then $`\langle0|B|0\rangle=0`$. The reference has no useful correlation for this record: mark an erasure. There are eight such labels.

If the second factor is $`I`$ or $`Z`$, its expectation on $`|0\rangle`$ is one. The seven informative labels are

```math
XI,\ YI,\ ZI,\ IZ,\ XZ,\ YZ,\ ZZ.
```

The all-identity label is not in the detector's menu. For these seven labels, measure $`A^{\mathsf T}`$ on the reference, calling its sign $`t`$. When $`A=I`$, set $`t=1`$ without measuring. Retain $`y=st`$.

For example, $`P=XZ`$ calls for an $`X`$ measurement on $`R`$. For $`P=YZ`$, a physical $`Y`$ measurement with outcome $`m`$ must be corrected to $`t=-m`$, because $`Y^{\mathsf T}=-Y`$. Thus the retained sign is $`y=-sm`$. Omitting this correction reverses the inferred contrast for that label.

## Write the entire observed distribution

The informative fraction is

```math
c_2=\frac{4\cdot2-1}{4^2-1}=\frac7{15}.
```

Define $`Z=0`$ for an erasure and $`Z=y`$ otherwise. The complete probability law is

```math
\Pr(Z=0)=\frac8{15},
\qquad
\Pr(Z=+1)=\frac7{30}(1+\theta),
\qquad
\Pr(Z=-1)=\frac7{30}(1-\theta).
```

These three probabilities sum to one. Conditional on being informative, the sign has mean $`\theta`$. Conditioning describes the data; it does not make erased calls free.

At the illustrative value $`\theta=3/5`$, the probabilities are respectively $`40/75`$, $`28/75`$ and $`7/75`$. This value is used to inspect the experiment, not assumed known by the estimator. The mean of $`Z`$ is $`7/25`$, equal to $`c_2\theta`$.

## Estimate and compare resources

From $`N`$ independent calls, use

```math
\widetilde\theta=\frac{15}{7N}\sum_{i=1}^N Z_i.
```

It is unbiased, and its variance is $`15/(7N)-\theta^2/N`$. Clip to the promised interval when reporting an estimate. For a uniform confidence guarantee, the [statistical construction](../science/adaptive_calibration.md) instead averages the non-erased signs and explicitly handles the event that none are observed.

| Retained qubits | Retained dimension | Informative fraction | One-use Fisher information |
|---|---:|---:|---:|
| None | 1 | $`1/5`$ | $`1/[5(1-\theta^2)]`$ |
| One | 2 | $`7/15`$ | $`7/[15(1-\theta^2)]`$ |
| Two | 4 | $`1`$ | $`1/(1-\theta^2)`$ |

The one-reference experiment improves the Fisher coefficient over no reference by $`7/3`$; a full two-qubit reference improves it by five. These are information ratios, not identical factors in standard deviation. The matching global risk rate follows from a separate converse allowing coherent adaptive reuse, not just from this table.

## Change one assumption

Suppose the apparatus announces $`P`$ before preparation. Send a known $`+1`$ eigenstate of $`P`$, formed from local Pauli eigenstates. Its reported sign has mean $`\theta`$ on every call without retaining a reference. The separation therefore depends on delayed disclosure, not simply on the number of detector outcomes.

Alternatively, suppose the apparatus reveals its private ideal parity before its noisy flip. Comparing that parity with $`s`$ exposes the noise sign directly. This is also a stronger interface than the one studied here.

## What this example establishes

It demonstrates preparation, late-label readout, the transpose sign, observed erasures, the estimator and the charged resources. It is not a proof of the general optimum. The all-integer construction and upper bounds are in the [canonical science](../science/model.md). The [finite verification suite](../verification/README.md) checks matrix versions of these identities, including the $`Y`$ convention and non-power-of-two memory dimensions.
