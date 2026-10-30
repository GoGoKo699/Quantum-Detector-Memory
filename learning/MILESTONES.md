# Thirty milestones for Quantum Detector Memory

[Learning route](README.md) · [Watrous bridge](WATROUS_BRIDGE.md) · [Worked experiment](WORKED_EXAMPLE.md) · [Exact science](../science/model.md)

The single educational anchor is John Watrous, *The Theory of Quantum Information* (2018). Section numbers below refer to the author-hosted January 2018 manuscript described in the bridge. Fisher/SLD machinery and the detector-specific statistical steps are supplied locally, not attributed to the anchor without qualification.

**Allocation: 12 background/preliminaries milestones and 18 narrative/innovation milestones.** The first phase builds a complete controlled experiment from probabilities, operators and information measures. The second builds the construction and converse locally before joining them into the global memory law. This allocation follows the dependency structure of this project. It is independent of any reader's assessment history.

Each milestone specifies a question, an understanding target, earlier dependencies, its story role and a conceptual connection, and source pointers. The map is not an exhaustive list of technical lemmas. The canonical scientific pages remain the proof authority.

## Background and preliminaries

### M01 — Probabilities and a noisy sign

**Central question:** What does it mean to calibrate a single contrast?

**Understanding target:** Interpret the two sign probabilities and distinguish a parameter from a random observed outcome.

**Dependencies and story role:** None. Build the experimental and mathematical prerequisites.

**Conceptual connection:** A scalar mean will remain unknown even when the measurement label is reported.

**Source pointers:** Watrous 1.2.2; [canonical scientific account](../science/model.md).

### M02 — States and mixtures

**Central question:** How does a quantum state specify an experiment?

**Understanding target:** Use positivity, unit trace and convex mixtures to distinguish a state from a preparation label.

**Dependencies and story role:** M01. Build the experimental and mathematical prerequisites.

**Conceptual connection:** Mixed inputs are allowed; a pure-state decomposition is a proof device rather than free quantum storage.

**Source pointers:** Watrous 1.1.2–1.1.3; 2.1.2; [canonical scientific account](../science/fisher_information.md).

### M03 — Measurement effects

**Central question:** What information is actually returned by a detector?

**Understanding target:** Explain a POVM and its outcome probabilities, including a measurement that consumes the input.

**Dependencies and story role:** M02. Build the experimental and mathematical prerequisites.

**Conceptual connection:** The accessible outcomes define the interface; internal detector records are not automatically available.

**Source pointers:** Watrous 2.3.1–2.3.2; [canonical scientific account](../science/model.md).

### M04 — Retained conditional states

**Central question:** Why is a classical detector output not the whole joint output?

**Understanding target:** Interpret a block-diagonal classical-quantum state and distinguish block trace from normalized conditional state.

**Dependencies and story role:** M03. Build the experimental and mathematical prerequisites.

**Conceptual connection:** A retained reference may hold correlations conditioned on a reported outcome.

**Source pointers:** Watrous 2.1.1–2.1.3; 2.2.3; [canonical scientific account](../science/model.md).

### M05 — Channels and timing

**Central question:** Which controls can an experimenter apply before and after a call?

**Understanding target:** Represent preparation, measurement and adaptive processing as parameter-independent channels while preserving the order of information access.

**Dependencies and story role:** M04. Build the experimental and mathematical prerequisites.

**Conceptual connection:** Late disclosure is part of the statistical experiment, not merely a presentation choice.

**Source pointers:** Watrous 2.2.1–2.2.3; [canonical scientific account](../science/model.md).

### M06 — Schmidt rank and memory

**Central question:** How does retained dimension constrain an entangled input?

**Understanding target:** Relate Schmidt rank to reference dimension and distinguish dimension r from its logarithmic qubit cost.

**Dependencies and story role:** M02, M04. Build the experimental and mathematical prerequisites.

**Conceptual connection:** All accessible coherent side systems count; a discarded environment and an accessible purification are different resources.

**Source pointers:** Watrous 1.1.3; 2.1.3; [canonical scientific account](../science/model.md).

### M07 — The Pauli operator basis

**Central question:** Why can averaging over Pauli labels give an exact identity?

**Understanding target:** Explain orthogonality, completeness and the exclusion of the identity label; interpret a compressed operator.

**Dependencies and story role:** M02, M03, M06. Build the experimental and mathematical prerequisites.

**Conceptual connection:** Basis completeness will turn a sum over detector settings into the numerator dr minus one.

**Source pointers:** Watrous 1.1.2–1.1.3; 2.2.3; [canonical scientific account](../science/fisher_information.md).

### M08 — Classical local sensitivity

**Central question:** What does Fisher information measure and what does it not prove?

**Understanding target:** Compute the information of a biased sign and separate local sensitivity from a finite-sample estimation guarantee.

**Dependencies and story role:** M01. Build the experimental and mathematical prerequisites.

**Conceptual connection:** The erasure probability will multiply the information of a usable sign.

**Source pointers:** Watrous 1.2.2; project-supplied Fisher bridge; [canonical scientific account](../science/fisher_information.md).

### M09 — Quantum local sensitivity

**Central question:** How is local information defined before the reference is measured?

**Understanding target:** Explain the SLD equation, blockwise quadratic form and the need to retain support–kernel tangent terms.

**Dependencies and story role:** M04, M07, M08. Build the experimental and mathematical prerequisites.

**Conceptual connection:** Convexity and data processing control mixed inputs and later operations; the SLD machinery is supplied by the project.

**Source pointers:** Watrous 1.1.3; 2.2.1; project-supplied SLD bridge; [canonical scientific account](../science/fisher_information.md).

### M10 — Relative entropy

**Central question:** Why use a divergence in addition to Fisher information?

**Understanding target:** State the support condition, natural-log convention, joint convexity and data-processing meaning.

**Dependencies and story role:** M04, M05. Build the experimental and mathematical prerequisites.

**Conceptual connection:** A finite comparison against zero can accumulate across a controlled experiment.

**Source pointers:** Watrous 5.1; 5.2.1–5.2.3; [canonical scientific account](../science/relative_entropy.md).

### M11 — Testing and estimation

**Central question:** How can two hypotheses obstruct accurate estimation?

**Understanding target:** Explain thresholding an estimator into a binary test and the role of trace distance or total variation.

**Dependencies and story role:** M08, M10. Build the experimental and mathematical prerequisites.

**Conceptual connection:** Global lower bounds need an operational testing argument rather than an unbiased local bound alone.

**Source pointers:** Watrous 3.1.1; 5.1–5.2; [canonical scientific account](../science/adaptive_calibration.md).

### M12 — The complete experimental contract

**Central question:** Which resources and guarantees must remain fixed in a comparison?

**Understanding target:** Assemble the detector, disclosure timing, memory cap, independent calls, trusted readout, classical history and worst-case query budget.

**Dependencies and story role:** M03, M05, M06, M09, M11. Integrate the complete background contract.

**Conceptual connection:** This closes the background phase with a complete experiment and prevents uncharged purifications or postselection.

**Source pointers:** Watrous 2.1–2.3; 3.3.1; [canonical scientific account](../science/model.md).

## Narrative and innovation

### M13 — A scalar destructive detector

**Central question:** How do the random-Pauli effects define the promised calibration task?

**Understanding target:** Check positivity, normalization and input-independent label probabilities while keeping theta as the sole unknown.

**Dependencies and story role:** M07, M12. Connect the stated mechanism to the eventual memory law.

**Conceptual connection:** Random known settings do not introduce an unknown direction to be learned.

**Source pointers:** Watrous 2.3.1–2.3.2; [canonical scientific account](../science/model.md).

### M14 — The zero-contrast output

**Central question:** What survives a call when the contrast is zero?

**Understanding target:** Derive the classical-quantum blocks and their unchanged reference marginal, including their common interior support.

**Dependencies and story role:** M04, M10, M13. Connect the stated mechanism to the eventual memory law.

**Conceptual connection:** Uniform output times the reference marginal is the structural reason the adaptive entropy proof works.

**Source pointers:** Watrous 2.1.3; 2.2.3; [canonical scientific account](../science/model.md).

### M15 — The exact zero-point coefficient

**Central question:** Why does the memory factor depend on dr minus one?

**Understanding target:** Connect the Schmidt-weight SLD sum, Pauli completeness and the harmonic-mean bound; explain the pure-to-mixed extension.

**Dependencies and story role:** M06, M07, M09, M14. Connect the stated mechanism to the eventual memory law.

**Conceptual connection:** Uniform Schmidt weights attain the zero-point bound without requiring a particular subspace orientation.

**Source pointers:** Watrous 1.1.3; 1.2.1; [canonical scientific account](../science/fisher_information.md).

### M16 — Moving to finite contrast

**Central question:** How can the zero-point bound control every interior contrast?

**Understanding target:** Explain the Jordan-superoperator contraction and paired-sign resolvent inequality without assuming commuting blocks.

**Dependencies and story role:** M09, M15. Connect the stated mechanism to the eventual memory law.

**Conceptual connection:** The finite-contrast upper bound extends the local coefficient but still needs an attaining input.

**Source pointers:** Watrous 1.1.2–1.1.3; [canonical scientific account](../science/fisher_information.md).

### M17 — When equality holds

**Central question:** Why is maximal Schmidt entanglement alone insufficient away from zero?

**Understanding target:** Separate uniform Schmidt weights from the additional three-eigenvalue condition on compressed Paulis.

**Dependencies and story role:** M15, M16. Connect the stated mechanism to the eventual memory law.

**Conceptual connection:** A balanced Bloch-vector example prevents confusing zero-point optimality with finite-contrast optimality.

**Source pointers:** Watrous 1.1.3; [canonical scientific account](../science/fisher_information.md).

### M18 — Every integer reference dimension

**Central question:** How can a physical probe attain the frontier when r is not a power of two?

**Understanding target:** Explain the computational-subset entangled state and how complete versus broken Pauli pairs give eigenvalues minus one, zero and one.

**Dependencies and story role:** M06, M07, M17. Connect the stated mechanism to the eventual memory law.

**Conceptual connection:** Existence for every integer dimension is distinct from efficient arbitrary-subset preparation.

**Source pointers:** Watrous 1.1.3; 2.1.3; [canonical scientific account](../science/attaining_protocol.md).

### M19 — An observed erasure coin

**Central question:** How does the full output reduce to a usable fraction of biased signs?

**Understanding target:** Derive the three-outcome law, its information and the parameter-independent discarded labels for this specific construction.

**Dependencies and story role:** M08, M10, M18. Connect the stated mechanism to the eventual memory law.

**Conceptual connection:** The exact informative fraction c_r unifies attainability and the statistical protocol; erasures remain charged.

**Source pointers:** Watrous 1.2.2; 2.3.1; [canonical scientific account](../science/attaining_protocol.md).

### M20 — Readout signs and a complete example

**Central question:** What must be measured after a label containing Y arrives?

**Understanding target:** Apply the transpose correction and explain all fifteen labels in the two-qubit, one-reference experiment.

**Dependencies and story role:** M03, M19. Connect the stated mechanism to the eventual memory law.

**Conceptual connection:** A correct abstract formula must agree with an actual reference measurement and recorded sign.

**Source pointers:** Watrous 1.1.2; 2.3.2; [canonical scientific account](../science/attaining_protocol.md).

### M21 — Efficient qubit memories

**Central question:** What is the implementation when r equals 2 to the k?

**Understanding target:** Count Bell preparation, local reference measurements, classical label bits and all detector calls, including failures.

**Dependencies and story role:** M12, M19, M20. Connect the stated mechanism to the eventual memory law.

**Conceptual connection:** The construction uses no QRAM and keeps query complexity separate from hardware, energy and noisy-control costs.

**Source pointers:** Watrous 2.1.3; 2.2.3; 2.3.2; [canonical scientific account](../science/attaining_protocol.md).

### M22 — The reverse-test ingredient

**Central question:** How can a classical preparation experiment upper-bound quantum relative entropy?

**Understanding target:** Follow the two-distribution preparation map and its operator ordering and support conditions.

**Dependencies and story role:** M05, M10, M14. Connect the stated mechanism to the eventual memory law.

**Conceptual connection:** An inherited data-processing construction supplies the entropy upper bound without assuming general output commutation.

**Source pointers:** Watrous 2.2.3; 5.2.3; [canonical scientific account](../science/relative_entropy.md).

### M23 — The sharp one-use divergence

**Central question:** Why is c_r times h(theta) the exact one-use comparison against zero?

**Understanding target:** Combine the reverse test, positive scalar series and compressed-Pauli identity; explain mixed inputs and simultaneous attainment.

**Dependencies and story role:** M07, M18, M19, M22. Connect the stated mechanism to the eventual memory law.

**Conceptual connection:** The parameter-independent construction saturates a bound that is global in the parameter pair.

**Source pointers:** Watrous 1.1.3; 1.2.1; 5.2.3; [canonical scientific account](../science/relative_entropy.md).

### M24 — Arbitrary adaptive entropy

**Central question:** How can the argument allow incoming states that differ between hypotheses?

**Understanding target:** Separate new divergence from incoming marginal divergence, condition on classical histories and telescope over calls.

**Dependencies and story role:** M05, M12, M14, M23. Connect the stated mechanism to the eventual memory law.

**Conceptual connection:** The replacer chain rule, not repeated use of a fixed-input bound, justifies the general adaptive converse.

**Source pointers:** Watrous 2.2.1; 5.2.2–5.2.3; [canonical scientific account](../science/adaptive_calibration.md).

### M25 — Adaptive Fisher information at zero

**Central question:** Why do retained derivatives not evade the zero-point information cap?

**Understanding target:** Explain cancellation of sign-odd cross terms, full tangent support and addition of inherited classical Fisher information.

**Dependencies and story role:** M09, M14, M15, M24. Connect the stated mechanism to the eventual memory law.

**Conceptual connection:** This is an exact zero-contrast adaptive result; it is not asserted at every nonzero contrast.

**Source pointers:** Watrous 1.1.3; 2.2.1; [canonical scientific account](../science/fisher_information.md).

### M26 — Global squared-error risk

**Central question:** How do the construction and adaptive converse give a matching minimax law?

**Understanding target:** Connect the clipped unbiased estimator, the zero estimator and the two-point lower bound, including the small-data regime.

**Dependencies and story role:** M11, M19, M24. Connect the stated mechanism to the eventual memory law.

**Conceptual connection:** The factor-32 bounds concern all estimators on an interval containing zero, not only locally unbiased ones.

**Source pointers:** Watrous 1.2.2; 3.1.1; 5.2; [canonical scientific account](../science/adaptive_calibration.md).

### M27 — High-confidence accuracy

**Central question:** Where does the logarithm of inverse failure probability enter?

**Understanding target:** Explain the random number of usable signs, the no-success branch and binary relative-entropy lower bound under the stated epsilon and delta ranges.

**Dependencies and story role:** M11, M19, M24, M26. Connect the stated mechanism to the eventual memory law.

**Conceptual connection:** Both directions count every call and match confidence dependence rather than replacing it by a mean-square assertion.

**Source pointers:** Watrous 1.2.2; 5.1–5.2; [canonical scientific account](../science/adaptive_calibration.md).

### M28 — The single-qubit counterexample

**Central question:** Which universal no-ancilla claim is contradicted and why?

**Understanding target:** Reproduce the six-outcome factor-three Fisher comparison and identify the unsupported pure-state restriction in the cited minimax argument.

**Dependencies and story role:** M16, M19, M25. Connect the stated mechanism to the eventual memory law.

**Conceptual connection:** The counterexample is scoped to a precise equality and access model; standard-deviation improvement is not the Fisher ratio.

**Source pointers:** Watrous 1.2.1; 2.3.2; project source comparison; [canonical scientific account](../science/single_parameter_counterexample.md).

### M29 — Prior work and loss-dependent limits

**Central question:** What remains after inherited formulas and methods are credited?

**Understanding target:** Compare the finite-contrast detector law with depolarizing probes and Pauli learning, then explain why exact FI and divergence do not establish all-loss dominance.

**Dependencies and story role:** M17, M23, M24, M28. Connect the stated mechanism to the eventual memory law.

**Conceptual connection:** The balanced-qubit total-variation example separates a sound information optimum from an unsupported finite-sample optimum.

**Source pointers:** Watrous 3.1.1; 3.3.1; 5.2; [canonical scientific account](../science/interpretation.md).

### M30 — The complete memory law

**Central question:** What is the scientific conclusion, and which changes invalidate the comparison?

**Understanding target:** Integrate the exact c_r frontiers, the global query rate, disclosure timing, charged coherent memory, implementation and remaining scope limits.

**Dependencies and story role:** M21, M25, M26, M27, M29. Integrate the entire contribution and its boundaries.

**Conceptual connection:** The endpoint is one connected account with direct proof and reproduction routes, not a claim to cover every neighboring extension.

**Source pointers:** Watrous 2.1–2.3; 3.1.1; 5.2; [canonical scientific account](../science/model.md).

## Reading the result as a whole

After M12, the accessible input, output, memory and timing should form one precise experiment. After M30, the construction, exact information bounds and global statistical guarantee should form one connected explanation. The [verification guide](../verification/README.md) gives finite checks; their successful execution does not replace the written universal proofs or an external review.
