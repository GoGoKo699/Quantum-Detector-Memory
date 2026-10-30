# Physical meaning and scope

A destructive detector can return a purely classical record yet benefit strongly from a quantum reference that never enters it. The reason is **delayed measurement context**: the device chooses one of exponentially many Pauli axes after the probe has already been committed. A retained entangled reference converts the reported axis into a matching readout; with insufficient memory most axes produce erasures.

For (d=2), the optimal unassisted Fisher information is (1/[3(1-	heta^2)]); a Bell pair yields (1/(1-	heta^2)). The factor three is a detector-calibration example, not the first known ancilla advantage in channel or measurement metrology. For (n) qubits and (k) reference qubits, the useful-event probability is ((2^{n+k}-1)/(2^{2n}-1)). Each additional reference qubit approximately doubles the information rate until full reference dimension is reached.

The matching adaptive converse is significant because it rules out recovering the lost information merely by retaining coherent processing across calls, adaptive feedback, or an arbitrarily large classical history. It does not forbid changes of the experimental interface, especially advance knowledge of the measurement label. It does not establish robustness to unknown reference noise, gate overhead, detector drift, or laboratory implementation advantage.

The one-use Fisher and null-relative-entropy optima do **not** imply universal statistical-experiment dominance or exact finite-(N) optimality for every loss. At a single call a different probe can sometimes yield greater total variation for a specified binary test. The global minimax scaling, rather than universal finite-sample dominance, is the established consequence.

For attribution and model distinctions see [related work](../references/RELATED_WORK.md).