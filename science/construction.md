# Exact flagged-coin construction

Choose any subset (C) of (r) computational basis vectors and prepare

```math
|\psi_C\rangle=r^{-1/2}\sum_{x\in C}|x\rangle_S|x\rangle_R.
```

The reference marginal is (I_r/r). After the detector reports (P,s), measure (Q_P=Pi_C P^TPi_C) on the reference. Each Hermitian Pauli is a signed bit permutation; its compression to (C) decomposes into signed diagonal entries, matched (2	imes2) involutions, and unmatched zero rows. Therefore its spectrum lies in ({-1,0,1}).

Write (t) for the reference measurement result. The event (t
e0) has parameter-independent probability

```math
c_r=\frac{dr-1}{d^2-1},
```

by (sum_{P
e I}Q_P^2=(dr-1)I_r). Conditional on this event, (y=st) obeys (Pr(y=+1)=(1+	heta)/2). Erasures (t=0) carry no information about (	heta). This is an *exact* flagged-erasure Bernoulli experiment, attaining both information frontiers.

With independent trials define (Z_i=0) on erasure and (Z_i=y_i) otherwise. Then (widehat	heta=(Nc_r)^{-1}sum_iZ_i) is unbiased and has variance ((c_r-c_r^2	heta^2)/(Nc_r)^2le1/(Nc_r)). Clip it to the promised interval when useful.

For (r=2^k), choose (C={0,1}^k	imes{0}^{n-k}): prepare (k) Bell pairs and (n-k) fixed input qubits, and use local Clifford/Pauli measurements after reading the (O(n))-bit label. No QRAM is needed. The random Pauli setting can be selected with (O(n)) local basis choices; a general non-power-of-two subset encoding may require more costly known gates. This result charges detector calls and retained coherent width, not a full fault-tolerant or noisy-reference budget.

If the label (P) were available before input preparation, a (P)-eigenstate would yield an informative coin on every call; the memory separation would disappear.