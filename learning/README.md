# Learn Quantum Detector Memory

The question is operational: a detector consumes a probe before telling us which Pauli observable it measured. A retained reference can then be measured in response to that late information. How much reference memory is needed to calibrate the detector's one unknown contrast?

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**. Use the [author's book page](https://cs.uwaterloo.ca/~watrous/TQI/) for the personal-use manuscript and errata. The book is not reproduced here. Section pointers refer to the January 2018 pre-publication manuscript; published pagination may differ.

Start with the [two-qubit experiment](WORKED_EXAMPLE.md), then use the [Watrous bridge](WATROUS_BRIDGE.md) alongside the [30-milestone map](MILESTONES.md). M01–M12 build the necessary objects and resource contract. M13–M30 assemble the construction, exact bounds, adaptive argument and global statistical consequence. The map is a common understanding route, not a record of any individual's assessments.

The bridge adds the Fisher-information and detector-specific arguments that are not assumed from Watrous. Primary papers remain necessary for attribution; they are not additional educational anchors. Specialist readers can proceed directly to the [model and exact claims](../science/model.md), [Fisher proof](../science/fisher_information.md), [relative-entropy proof](../science/relative_entropy.md), and [global calibration bounds](../science/adaptive_calibration.md).

Keep three distinctions in view: one-use Fisher information is local; divergence against zero controls a global comparison; matching minimax rates do not specify exact finite-sample optimal risk. Numerical checks corroborate finite cases rather than proving the universal statements.
