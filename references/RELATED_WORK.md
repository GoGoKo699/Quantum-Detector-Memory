# Related work

The [detector model](../science/model.md) concerns a single unknown contrast in

```math
E_{P,s}(\theta)=\frac{I+s\theta P}{2(d^2-1)},\qquad d=2^n,
```

where a fresh, uniformly random nonidentity Pauli label $`P`$ is disclosed only after the input is consumed. The device returns $`(P,s)`$; it does not return a quantum output or the individual local readout bits. Every coherent register retained across a call is included in the dimension bound $`r`$, while classical records are unrestricted.

The results are an [exact one-use Fisher frontier](../science/fisher_information.md), an [attaining probe and readout for every integer $`r`$](../science/attaining_protocol.md), an [exact relative-entropy increment to the zero-contrast detector](../science/relative_entropy.md), and [adaptive global calibration bounds](../science/adaptive_calibration.md). Their coefficient is

```math
c_r=\frac{dr-1}{d^2-1}.
```

The comparisons below separate these detector-specific evaluations from established channel-estimation and discrimination methods. Source versions and access limits were checked on 30 October 2026. Citation keys match the anchors in this document and the entries in [references.bib](references.bib).

## Comparison of statistical models

| Work | Unknown and accessible output | Resource or access restriction | Relationship to this detector |
|---|---|---|---|
| Present model | One common contrast; fresh delayed Pauli label and one bit | Entire retained coherent register has dimension at most $`r`$; arbitrary adaptive control | Exact $`c_r/(1-\theta^2)`$ one-use FI and exact $`Nc_rh(\theta)`$ adaptive divergence to zero |
| [Frey–Collins–Gerlach](#frey2011) | Depolarizing contrast; quantum channel output | Entanglement of the input with a reference | Direct antecedent of the complete local Schmidt-coefficient form and the $`dr-1`$ numerator |
| [Chen et al.](#chen2022), [Chen–Gong](#chengong2025), [Kim–Oh](#kimoh2026) | Pauli-channel eigenvalues; quantum channel output | Ancillas, adaptation, and concatenation vary by model | Exponential memory–sample tradeoffs are established; the learning targets and returned systems differ |
| [Ion–Gessner](#ion2026) | Parameter encoded in a state; all local Pauli-shadow outcomes | Fixed randomized readout and entanglement within the sensed probe | Calibration response is presumed known; no retained-reference detector calibration law |
| [Naikoo](#naikoo2026) | Parameter of a general quantum channel; quantum output | Ancilla dimension, expressed through input Schmidt rank | General rank-constrained FI framework; the comparison here uses the identifiable v1 manuscript |
| [He](#he2026) | Thermal attenuator versus thermal replacer; quantum optical return | Parallel probes, energy budget, strict total retained-register dimension | Exact asymptotic memory-dependent detection is a prior theme; different output and operational criterion |

Here $`h(\theta)=[(1+\theta)\ln(1+\theta)+(1-\theta)\ln(1-\theta)]/2`$. Exact divergence to zero does not establish exact adaptive FI at every nonzero contrast or optimality for every finite-sample decision loss; see [interpretation](../science/interpretation.md).

## Depolarizing metrology and the inherited local form

<a id="frey2011"></a>
### Frey, Collins, and Gerlach (2011)

Michael Frey, David Collins, and Karl Gerlach, **“Probing the qudit depolarizing channel,”** *Journal of Physics A: Mathematical and Theoretical* **44**, 205306 (2011). [Publisher DOI](https://doi.org/10.1088/1751-8113/44/20/205306); [primary PDF](https://arxiv.org/pdf/1008.1557v1); [version record](https://arxiv.org/abs/1008.1557).

For $`\Gamma_\theta(\rho)=(1-\theta)I/d+\theta\rho`$, Section IV, Eqs. (22)–(24), evaluates uniform entanglement on a Schmidt subspace of dimension $`r`$:

```math
J_r^{\mathrm{unif}}(\theta)
=\frac{1}{(1-\theta)(\theta+1/(dr-1))}.
```

Their Eq. (41), with definitions (36)–(38), gives the general Schmidt dependence. At zero, writing the Schmidt probabilities as $`\lambda_a`$, it reduces to

```math
J_\psi(0)=d-1+d\sum_{a\lt b}\frac{4\lambda_a\lambda_b}{\lambda_a+\lambda_b}
=(d^2-1)F_\psi^{\mathrm{detector}}(0).
```

The final equality is the comparison with our detector calculation. Thus the all-$`r`$ local form inherits more than the endpoint ratio $`d+1`$. The source evaluates uniform subspaces and brackets general partial entanglement between the unassisted and fully entangled endpoints; it does not expressly state our fixed-$`r`$ detector optimization.

The finite-contrast behavior differs. From those expressions, for fixed $`0\lt\theta\lt1`$,

```math
\frac{J_d(\theta)}{J_1(\theta)}
=(d+1)\frac{1+(d-1)\theta}{1+(d^2-1)\theta}\longrightarrow1,
```

whereas $`F_d^{\mathrm{detector}}(\theta)/F_1^{\mathrm{detector}}(\theta)=d+1`$. The compulsory detector readout therefore suppresses unassisted information more severely. The factorization through a physical depolarizing channel applies only for $`\theta\ge-1/(d^2-1)`$; the detector is valid on the larger interval $`[-1,1]`$.

## Established tools used by the divergence and adaptive proofs

<a id="matsumoto2010"></a>
### Matsumoto (2010)

Keiji Matsumoto, **“Reverse Test and Characterization of Quantum Relative Entropy,”** [arXiv:1010.1030v1](https://arxiv.org/abs/1010.1030v1), submitted 5 October 2010. [Primary PDF](https://arxiv.org/pdf/1010.1030v1).

Theorem 2.4 characterizes the minimum classical relative entropy of a reverse test as the maximal, or Belavkin–Staszewski, relative entropy. This supplies the established reverse-test principle behind the upper bound on Umegaki relative entropy used in [relative_entropy.md](../science/relative_entropy.md). That proof also gives the explicit finite-dimensional reverse test, so the inequality orientation and support convention can be checked directly. The general reverse-test bound is an inherited tool; the sharp coefficient and equality construction are evaluated for this detector.

<a id="wilde2020"></a>
### Wilde, Berta, Hirche, and Kaur (2020)

Mark M. Wilde, Mario Berta, Christoph Hirche, and Eneet Kaur, **“Amortized Channel Divergence for Asymptotic Quantum Channel Discrimination,”** *Letters in Mathematical Physics* **110**, 2277–2336 (2020). [Publisher DOI](https://doi.org/10.1007/s11005-020-01297-7); [primary PDF, arXiv:1808.01498v2](https://arxiv.org/pdf/1808.01498v2); [version record](https://arxiv.org/abs/1808.01498).

Section VII.C, **Lemma 38, Eqs. (272)–(280)**, proves relative-entropy amortization collapse against a replacer channel. Its Eqs. (273)–(278) give the marginal-replacement argument used here. Theorem 39, Eqs. (281)–(282), provides testing consequences. These locations refer to the v2 preprint, revised 18 June 2020.

Our zero-contrast channel is a uniform replacer. The established argument applies to each classical-history branch without increasing the retained reference dimension. The detector-specific work is the exact evaluation $`c_rh(\theta)`$ and its attainment. Averaging over classical histories and telescoping yields the adaptive bound. This is an application of replacer amortization, not a new general amortization method.

<a id="wang2018"></a>
### Wang, Wu, and Song (2018)

Kun Wang, Nan Wu, and Fangmin Song, **“Uncertainty relations in the presence of quantum memory for mutually unbiased measurements,”** *Physical Review A* **98**, 032329 (2018). [Publisher DOI](https://doi.org/10.1103/PhysRevA.98.032329); [primary PDF](https://arxiv.org/pdf/1807.01047).

Theorem 1, Eq. (12), gives a conditional collision-entropy equality for random mutually unbiased measurements with quantum memory. Appendix B, Lemma 6, Eq. (B1), states the traceless orthonormal-operator completeness identity. This is relevant precedent for second-moment identities with a disclosed measurement label. The Pauli completeness identity in our proof is established algebra; collision entropy, Umegaki relative entropy, and SLD Fisher information must still be distinguished.

## Detector calibration and the single-parameter assertion

<a id="das2026"></a>
### Das et al. (2026)

Aritra Das, Simon K. Yung, Lorcán O. Conlon, Özlem Erkılıç, Angus Walsh, Yong-Su Kim, Ping K. Lam, Syed M. Assad, and Jie Zhao, **“Precision bounds for characterising quantum measurements,”** *Nature Communications* **17**, 1821 (2026). [Publisher DOI](https://doi.org/10.1038/s41467-026-68529-7); [published full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC12921330/); [arXiv:2512.20091v2](https://arxiv.org/html/2512.20091v2), revised 22 January 2026.

The published Methods, “Probing strategies for detector estimation,” explicitly permits ancilla measurements conditioned on the detector outcome and invokes Supplementary Theorem 4 for a single-parameter no-advantage statement. The proof comparison uses arXiv v2, Supplement II.F, Theorem 4 and Corollary 1. The [six-outcome counterexample](../science/single_parameter_counterexample.md) concerns this ancillary assertion. It identifies a purity inference that does not survive minimization of linear objectives. It does not challenge every detector-QFI upper bound or the commuting examples.

<a id="dariano2004"></a>
### D’Ariano, Maccone, and Lo Presti (2004)

Giacomo Mauro D’Ariano, Lorenzo Maccone, and Paoloplacido Lo Presti, **“Quantum Calibration of Measurement Instrumentation,”** *Physical Review Letters* **93**, 250407 (2004). [Primary publisher page](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.93.250407).

The primary abstract describes calibrating an unknown apparatus through bipartite correlations with a calibrated tomographer. This is an earlier detector-calibration strategy with an ancillary system. The comparison is based on the publisher abstract, not a theorem-level examination of the full paper.

<a id="brida2012"></a>
### Brida et al. (2012)

G. Brida, L. Ciavarella, I. P. Degiovanni, M. Genovese, A. Migdall, M. G. Mingolla, M. G. A. Paris, F. Piacentini, and S. V. Polyakov, **“Ancilla-Assisted Calibration of a Measuring Apparatus,”** *Physical Review Letters* **108**, 253601 (2012). [Primary publisher page](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.108.253601); [NIST record](https://www.nist.gov/publications/ancilla-assisted-calibration-measuring-apparatus).

The primary abstracts report photon-number-resolving detector calibration using twin-beam correlations and improved statistical robustness relative to classical-input reconstruction. Ancilla-assisted detector calibration and its practical benefit therefore precede the present model. Author order follows the publication, rather than the institution's reordered record.

## Pauli learning and memory–sample tradeoffs

<a id="chen2022"></a>
### Chen, Zhou, Seif, and Jiang (2022)

Senrui Chen, Sisi Zhou, Alireza Seif, and Liang Jiang, **“Quantum advantages for Pauli channel estimation,”** *Physical Review A* **105**, 032435 (2022). [Publisher DOI](https://doi.org/10.1103/PhysRevA.105.032435); [official accepted manuscript](https://link.aps.org/accepted/10.1103/PhysRevA.105.032435).

This work establishes exponential ancillary advantages for estimating Pauli-channel eigenvalues and distinguishes ancillary access, adaptation, and concatenation. Its nonadaptive nonconcatenating tradeoff already has an $`n2^{n-k}`$ scale. The returned channel system is quantum and the target is a family of eigenvalues. This is a direct antecedent of the broad memory–sample phenomenon, with a different estimation target and access model.

<a id="chengong2025"></a>
### Chen and Gong (2025)

Sitan Chen and Weiyuan Gong, **“Efficient Pauli Channel Estimation with Logarithmic Quantum Memory,”** *PRX Quantum* **6**, 020323 (2025). [Publisher DOI](https://doi.org/10.1103/PRXQuantum.6.020323); [primary PDF](https://journals.aps.org/prxquantum/pdf/10.1103/PRXQuantum.6.020323).

Concatenation can reduce ancillary and measurement requirements while the channel-query count remains large. Its lower bounds and fixed unknown Pauli-spike alternatives concern channel eigenvalue learning. Measurement count and query count are different resources. The present detector consumes each input and returns only its declared classical output; its exact exponent does not resolve a lower-bound gap in the same model as this paper.

<a id="kimoh2026"></a>
### Kim and Oh (2026)

Minsoo Kim and Changhun Oh, **“On the fundamental resource for exponential advantage in quantum channel learning,”** *Nature Communications* **17**, 1822 (2026). [Publisher DOI](https://doi.org/10.1038/s41467-026-68532-y); [primary full text, arXiv:2507.11089v2](https://arxiv.org/html/2507.11089v2); [version record](https://arxiv.org/abs/2507.11089), revised 25 February 2026.

Definition 1 permits classical adaptation of nonconcatenated channel experiments. Theorem 2, Eq. (6), and Supplement S3.4 give an all-eigenvalue lower bound $`\Omega(2^{n-k}/\epsilon^2)`$ at fixed confidence. Theorem 1 separates memory dimension from entanglement entropy. Supplement S3.1 samples a hidden Pauli spike once and reveals it after all measurements. Our setting instead chooses a fresh label on each call and has one unknown common contrast. Neither the generic exponent nor the importance of memory dimension is a new claim here.

<a id="kwon2026"></a>
### Kwon, Lie, and Jiang (2026)

Hyukgun Kwon, Seok Hyung Lie, and Liang Jiang, **“Universal Sample Complexity Bounds in Quantum Learning Theory via Fisher Information Matrix,”** *PRX Quantum* **7**, 033063 (2026), published 22 September 2026. [Publisher DOI](https://doi.org/10.1103/8k5v-ddtw); [primary PDF](https://journals.aps.org/prxquantum/pdf/10.1103/8k5v-ddtw).

Theorem 1 and Appendix C connect Fisher-information matrices to maximum-likelihood sample complexity under regularity and small-error conditions. The Pauli-channel analysis uses the same familiar purity identity. Section III.B.4 allows specified adaptive multichannel controls in a scheme forbidding system–ancilla entanglement; experiments are then repeated independently. The unrestricted charged-$`r`$ adaptive detector theorem has a different scope. The general FI-to-learning connection is an antecedent, not an independent contribution of this detector analysis.

## Recent and adjacent metrology results

<a id="ion2026"></a>
### Ion and Gessner (2026)

Luca Ion and Manuel Gessner, **“Quantum-enhanced metrology with classical shadows,”** [arXiv:2610.35632v1](https://arxiv.org/abs/2610.35632v1), submitted 26 October 2026. [Primary full text and supplement](https://arxiv.org/html/2610.35632v1).

The parameter is encoded in a state. Eqs. (2)–(5) combine local Pauli moments, assuming the calibrated response and its derivative are available; calibration cost is excluded. Eqs. (14)–(19) and Supplement Appendix D analyze independent local X/Y/Z measurements with all local outcomes recorded. Probe entanglement yields a constant-factor improvement. This is adjacent fixed-randomized-readout metrology, but it does not evaluate an unknown detector contrast or a retained-reference dimension frontier. The official history lists v1 at the stated check date.

<a id="naikoo2026"></a>
### Naikoo (2026)

Javid Naikoo, **“Entanglement depth and ancilla efficiency in quantum channel estimation,”** [arXiv:2608.11042](https://arxiv.org/abs/2608.11042). The text compared is an identifiable **v1, 11 August 2026**, available through a [manuscript reproduction](https://www.researchgate.net/publication/412164909_Entanglement_depth_and_ancilla_efficiency_in_quantum_channel_estimation).

Eq. (14) and Theorems 1–2 formulate rank-constrained channel FI. Theorem 3(i) states a fixed-POVM measure-and-prepare no-advantage condition; its proof additionally assumes in Eq. (35) that every prepared state is obtainable as a channel output of a parameter-independent input. Our natural fine-grained detector representation fails that realizability condition because no input forces an individual P-labelled branch. This observation is confined to v1 and its proof assumptions. Input/output dimension conventions also require care in any literal counterexample claim.

**Version boundary:** the official current revision history could not be verified. The mirror is not evidence of author upload or of the latest version. No assertion about an unseen revision is made.

<a id="song2024"></a>
### Song et al. (2024)

Xingrui Song, Flavio Salvati, Chandrashekhar Gaikwad, Nicole Yunger Halpern, David R. M. Arvidsson-Shukur, and Kater Murch, **“Agnostic Phase Estimation,”** *Physical Review Letters* **132**, 260801 (2024). [Primary publisher page](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.132.260801); [arXiv:2403.00054](https://arxiv.org/abs/2403.00054).

The primary abstract describes an ancillary strategy for an initially unknown rotation axis, retaining quantum outputs for an entangled measurement, and its experimental demonstration. It is an antecedent of the physical principle that retained quantum correlations can address information unavailable at preparation. The comparison is at abstract level and does not attribute the present destructive-detector memory law to this source.

<a id="he2026"></a>
### He (2026)

Zixuan He, **“The memory cost of quantum illumination,”** Zenodo preprint, version 1.0, 20 October 2026. [Primary deposit](https://zenodo.org/records/23485508); [DOI](https://doi.org/10.5281/zenodo.23485508). The deposit identifies the author with the University of Glasgow.

The visible record states an exact asymptotic detection exponent for a thermal attenuator versus a thermal replacer, with $`n`$ parallel uses, a mean photon budget, and strict total retained-register dimension $`\lfloor e^{nP}\rfloor`$. Its scope includes correlated mixed probes and collective measurements, under a phase-known, ideal-memory Stein criterion. Exact memory-dependent detection is therefore an existing theme; the destructive scalar detector and finite-$`N`$ adaptive criterion are different.

**Access boundary:** the deposit description was accessible, but the linked PDF could not be extracted. No theorem-level exclusion beyond the visible scope is claimed. The listed file is `The_memory_cost_of_quantum_illumination_v2_1.pdf`; the record version is 1.0. This is a preprint deposit, not a journal publication.

## Scope of the comparison

The exact detector evaluation is presented with its established ingredients: the local depolarizing metric, Pauli completeness, reverse-test relative-entropy bounds, and replacer amortization. Standard testing reductions and concentration bounds then yield the calibration rates. A search that found no identical detector theorem is not a proof that none exists; the two specific access gaps above remain explicit.

The delayed setting, destructive output, coherent-memory accounting, and query budget define the statistical problem. Revealing $`P`$ before probe preparation permits an eigenstate probe and removes the memory obstruction. Returning additional local bits or permitting hidden retained quantum registers changes the experiment. These distinctions are developed in [model.md](../science/model.md) and [interpretation.md](../science/interpretation.md).
