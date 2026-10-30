# An experiment that attains the memory frontier

The optimal probe stores correlations with the detector input in a retained quantum system. Once the detector announces its Pauli label, the retained system can be measured in the corresponding basis. The construction below turns each call into either an explicitly flagged erasure or one informative noisy sign. Its usable fraction is exactly

```math
c_r=\frac{dr-1}{d^2-1}.
```

This page proves attainment of [T1](fisher_information.md#t1-exact-fisher-information-for-one-detector-use) for every integer $`1\leq r\leq d`$. It also gives the repeated experiment attaining [T2](fisher_information.md#t2-exact-adaptive-fisher-information-at-zero-visibility). The [model](model.md) fixes the order in which the label is revealed and the quantum-memory accounting.

## Construction for arbitrary r

Choose any set $`C=\{x_1,\ldots,x_r\}`$ of distinct computational basis strings from $`\{0,1\}^n`$. Prepare

```math
|\psi_C\rangle=
\frac1{\sqrt r}\sum_{j=1}^r|x_j\rangle_S|j\rangle_R.
```

The retained system has dimension $`r`$ and marginal $`\sigma_R=I_r/r`$. Let $`V_C|j\rangle=|x_j\rangle`$ and define the retained observable

```math
Q_P=(V_C^\dagger P V_C)^{\mathsf T}.
```

The transpose is taken in the displayed index basis of the retained system. Conditional blocks of the complete output are

```math
\frac{I_r+s\theta Q_P}{2Mr},
\qquad M=d^2-1.
```

After observing $`P`$, measure $`Q_P`$. Its eigenvalues belong to $`\{-1,0,+1\}`$, as proved next. If the measured value $`t`$ is zero, record an erasure. Otherwise record the sign $`y=st`$.

### Why every compressed Pauli has only three eigenvalues

A tensor-product Pauli is a Hermitian monomial involution. On computational basis strings, its permutation is $`x\mapsto x\oplus a`$ for a fixed bit string $`a`$, with phases in $`\{\pm1,\pm i\}`$.

If $`a=0`$, the compression is diagonal with entries $`\pm1`$. If $`a\ne0`$, the full basis splits into disjoint pairs. When both vertices of a pair lie in $`C`$, its compressed block has the form

```math
\begin{pmatrix}
0&\alpha^*\\
\alpha&0
\end{pmatrix},
\qquad |\alpha|=1,
```

and eigenvalues $`\pm1`$. A retained vertex whose partner lies outside $`C`$ gives a zero block. Transposition preserves this spectrum. Therefore

```math
\operatorname{spec}(Q_P)\subseteq\{-1,0,+1\},
\qquad Q_P^3=Q_P.
```

This argument is why the construction works for an arbitrary integer $`r`$: a power-of-two code space is not needed.

## The exact erasure-coin experiment

In any fixed eigenbasis of $`Q_P`$, a record $`(P,s,t,\alpha)`$ has probability

```math
\Pr(P,s,t,\alpha)=\frac{1+s\theta t}{2Mr},
```

where $`\alpha`$ indexes the eigenspace multiplicity. The [Pauli compression identity](fisher_information.md#pauli-identities) gives

```math
L:=\sum_{P\ne I}\operatorname{rank}Q_P
=\sum_{P\ne I}\operatorname{Tr}Q_P^2
=r(dr-1).
```

Each nonzero eigenvector contributes one record to each sign $`y=\pm1`$. Summing the probabilities yields

```math
\boxed{
\Pr(\mathrm{erasure})=1-c_r,
\qquad
\Pr(y=+1)=c_r\frac{1+\theta}{2},
\qquad
\Pr(y=-1)=c_r\frac{1-\theta}{2}.
}
```

The erasure probability is independent of the visibility. Given a usable call, the retained sign is one ordinary biased coin with mean $`\theta`$.

The discarded labels carry no additional information for this construction: their conditional distribution, given the erasure flag and the retained sign, is parameter-independent. Moreover, the quantum outputs commute in the fixed blockwise eigenbasis just used. Consequently the constructed quantum output and this three-outcome classical experiment are statistically equivalent, with parameter-independent channels in both directions.

Its Fisher information is

```math
\sum_{y=\pm1}
\frac{[\partial_\theta\Pr(y)]^2}{\Pr(y)}
=\frac{c_r}{1-\theta^2},
```

which attains T1. Independent repetition gives additive Fisher information, attaining T2 at zero. The same exact coin representation supplies the upper bounds in [adaptive calibration](adaptive_calibration.md).

Statistical equivalence here concerns this specified construction. It does not mean that all permissible detector experiments are postprocessings of the erasure coin, and it does not claim exact optimality for every finite-sample testing loss.

## The transpose and Y sign

For a maximally entangled pair, the retained conditional operator is the transpose of the input operator. The transpose cannot be omitted from the readout rule. In the computational basis,

```math
X^{\mathsf T}=X,
\qquad Z^{\mathsf T}=Z,
\qquad Y^{\mathsf T}=-Y.
```

Thus a physical measurement of the untransposed Pauli can be used if its outcome is multiplied by the known sign $`(-1)^{\nu_Y}`$, where $`\nu_Y`$ counts its $`Y`$ factors. This is a classical outcome correction, requiring no extra quantum memory.

## Implementation with k Bell pairs

Let $`r=2^k`$, with $`0\leq k\leq n`$. Choose the computational subset whose last $`n-k`$ bits are zero. The probe is

```math
|\psi_k\rangle
=|\Phi^+\rangle_{S_A R}^{\otimes k}
\otimes|0\rangle_{S_B}^{\otimes(n-k)}.
```

There are $`n`$ detector-input qubits and $`k`$ retained qubits. Write the announced Pauli as $`P=P_A\otimes P_B`$, where the two factors act on the Bell-paired and fixed parts of the input.

If any factor of $`P_B`$ is $`X`$ or $`Y`$, then $`\langle0|P_B|0\rangle=0`$, so the compression is zero. Declare an erasure directly from the reported label. No memory measurement is needed on that branch.

If all factors of $`P_B`$ belong to $`\{I,Z\}`$, then $`\langle0|P_B|0\rangle=1`$ and

```math
Q_P=P_A^{\mathsf T}.
```

Measure the corresponding local Paulis on the retained qubits, multiply their outcomes, and apply the known $`Y`$ transpose sign. This gives $`t`$; retain $`y=st`$. If $`P_A=I`$, set $`t=1`$ without measuring the memory.

The informative-label count is

```math
4^k2^{n-k}-1
=2^{n+k}-1
=dr-1.
```

Division by the $`d^2-1`$ possible labels recovers $`c_r`$. The detector label alone determines the erasure flag for this power-of-two construction. In the general subset construction, the flag can also depend on the memory outcome.

### Preparation and readout costs

Starting from initialized qubits, preparing the probe uses $`k`$ Hadamard gates and $`k`$ controlled-NOT gates, one for each Bell pair. The remaining $`n-k`$ input qubits stay in $`|0\rangle`$. The same $`k`$ retained qubits may be measured, reset, and reused for the next call while all outcomes are stored classically.

For a direct local Pauli measurement, use no basis rotation for $`Z`$, one Hadamard for $`X`$, and $`S^\dagger`$ followed by a Hadamard for $`Y`$, then measure in the computational basis. The retained readout therefore uses at most $`k`$ single-qubit measurements and $`2k`$ single-qubit basis gates. It needs no entangling gates. Products of measured signs and the transpose correction are classical operations.

| Resource per detector call | Explicit count or bound |
|---|---|
| Detector input | $`n`$ freshly initialized qubits, consumed by the call |
| Retained quantum memory | $`k`$ qubits, dimension $`r=2^k`$ |
| Probe entangling gates | $`k`$ controlled-NOT gates |
| Additional probe gates | $`k`$ Hadamard gates |
| Retained readout | At most $`k`$ single-qubit measurements and $`2k`$ basis gates |
| Memory recycling | At most $`k`$ single-qubit resets after recording the outcomes |
| Detector output record | $`2n`$ bits encoding the Pauli label and one reported sign bit |
| Sufficient calibration record | One erasure flag and, when usable, one sign |

These are circuit and record counts for the explicit power-of-two construction. They do not assign an energetic cost to initialization, reset, random-bit generation, or physical measurement. No efficient encoding is asserted for an arbitrary, unstructured subset $`C`$ of non-power-of-two size.

## A local implementation of the detector

The set of $`d^2-1`$ possible Pauli labels does not require storing an exponential table of observables. One exact implementation samples $`n`$ single-qubit labels from $`\{I,X,Y,Z\}`$, rejects the all-identity choice, and keeps the accepted string private until the probe has been consumed. Two fair bits per tentative single-qubit label give the exact expected randomness cost

```math
\frac{2n}{1-4^{-n}}
```

fair bits per accepted Pauli string. Its output representation uses $`2n`$ bits. Rejection is internal label generation, not a discarded experimental probe: it takes place before acting on the input.

For an accepted $`P`$, measure its nonidentity factors locally and form their parity $`u`$. This uses at most $`n`$ single-qubit measurements and $`2n`$ single-qubit basis gates, with no detector-side entangling gate. Draw one private noisy sign $`e`$ with $`\Pr(e=\pm1)=(1\pm\theta)/2`$ and return $`s=eu`$ together with $`P`$. The resulting effects are

```math
\frac1M\sum_{u=\pm1}
\Pr(e=su)\,\frac{I+uP}{2}
=\frac{I+s\theta P}{2M}.
```

The local readouts can be finer than the reported parity, but those raw results and the private noisy sign are discarded internally. Only $`(P,s)`$ is available to the calibration protocol. Providing the raw parity $`u`$ would reveal $`e`$ directly and define a stronger detector interface.

The same access distinction applies to the timing of $`P`$: if it were announced before preparation, the experimenter could send a known eigenstate and obtain one informative noisy sign on every call without retained memory. The advantage studied here is the response to information disclosed after a destructive measurement.

## Further reading

The [Fisher page](fisher_information.md) proves that no input with the same retained dimension has greater one-use Fisher information and that adaptive reuse cannot exceed the additive zero-visibility limit. The [relative-entropy page](relative_entropy.md) establishes the global comparison with the zero-visibility detector, and [adaptive calibration](adaptive_calibration.md) turns it into minimax estimation and testing bounds. The [related-work discussion](../references/RELATED_WORK.md#frey2011) distinguishes the memory frontier from earlier demonstrations that entanglement can assist measurement estimation.
