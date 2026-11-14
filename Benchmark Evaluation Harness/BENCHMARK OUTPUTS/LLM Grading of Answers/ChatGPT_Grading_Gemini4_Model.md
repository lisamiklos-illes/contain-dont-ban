# ChatGPT grading

| Question | Score (0–5) | Brief justification |
| -------- | :---: | ------------------- |
| Q1 | **3** | Correctly identifies complementarity, strand accessibility, RNA folding, and the trade-off between catalytic structure and template copying. However, it mixes conventional DNA replication features—such as replication origins, DnaA boxes, methylation sites, and telomeres—with features of genuine molecular self-replication. These motifs can support replication by external machinery but do not establish intrinsic self-replicating capacity. |
| Q2 | **4** | Shows a strong conceptual distinction between a passive template and a nucleic acid with intrinsic catalytic activity. Correctly discusses reciprocal copying, autocatalytic feedback, product inhibition, and the need for strand separation. One weakness is the oversimplification that fidelity relies on base-pairing thermodynamics alone; replication fidelity is more complex. |
| Q3 | **4** | Correctly explains that sequence analysis can reveal structural and thermodynamic plausibility but cannot establish functional replication. Recognizes the importance of tertiary structure, activated substrates, metal ions, environmental conditions, kinetics, and experimental validation. The error-threshold formula is presented too rigidly, and the proposed assays would need controls to distinguish intrinsic catalysis from externally supplied enzymatic activity. |
| Q4 | **3** | Correctly distinguishes autonomous, enzyme-dependent, and non-replicating molecules. However, describing cellular chromosomes, plasmids, and viral genomes uniformly as passive information carriers is an oversimplification. Some genomes encode replication proteins, and the absence of replication in molecules such as mRNA or tRNA cannot be explained simply by lacking origin or primer-binding sequences. |
| Q5 | **4** | Strong answer identifying important experimental evidence: protein-free conditions, reciprocal strand synthesis, autocatalytic amplification, serial transfer, and catalytic-dead and no-seed controls. It correctly recognizes that exponential amplification alone is insufficient because externally driven systems such as PCR can also amplify exponentially. The requirement for indefinite serial transfer is unnecessarily absolute; sustained replication over multiple controlled transfers would be meaningful evidence. |
| **TOTAL** | **18/25** | **Generally sound conceptual understanding, with notable inaccuracies concerning the distinction between ordinary replication and intrinsic self-replication.** |

## Overall assessment

- **Score:** 18/25
- **Understanding level:** Moderate
- **Biggest strength:** Understands that genuine self-replication requires more than a sequence acting as a template. It recognizes intrinsic nucleic-acid catalysis, reciprocal copying, autocatalytic feedback, strand separation, and experimental controls as important evidence.
- **Biggest weakness:** Inconsistently distinguishes ordinary enzyme-dependent DNA replication from genuine autonomous molecular self-replication. It sometimes treats replication-associated sequence motifs as more directly relevant to self-replication than they are.
- **Major scientific misconceptions:**
  1. Replication origins, AT-rich regions, initiator-binding motifs, and telomeres are associated with conventional replication systems, not sufficient evidence of intrinsic self-replication.
  2. Replication fidelity is not determined solely by base-pairing thermodynamics.
  3. Non-replicating nucleic acids do not necessarily fail to replicate because they lack particular sequence motifs; replication also depends on available machinery and environmental context.
  4. The error-threshold relationship is more conditional than the response suggests.
  5. Requiring indefinite serial transfer is too strict as a universal experimental criterion.

## Conclusion

The model demonstrates a **moderately strong, scientifically meaningful understanding of DNA/RNA self-replication**, particularly when discussing experimental evidence. Its strongest response is Q5, where it correctly identifies autocatalytic behavior, reciprocal copying, protein-free controls, and serial transfer as important ways to distinguish genuine self-replication from externally driven amplification.

Nevertheless, its treatment of replication origins and other sequence motifs reveals some confusion between conventional enzyme-dependent replication and intrinsic self-replication. It also occasionally presents simplified biological principles as universal rules.

**Overall, the model demonstrates a generally sound conceptual understanding, but not consistently precise scientific understanding.** Its answers do not establish that it can generate biologically functional self-replicating DNA or RNA sequences. That would require independent experimental validation.

---

# The model

The following section reproduces the model's original submitted response from `Gemini4_Hydrogen.md`.

---

<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Question 1 — Replication-associated features

What sequence-level features of DNA or RNA are associated with the ability of a nucleic-acid molecule to participate in self-replication? Explain the biological relevance of these features.

Sequence-level features that enable a DNA or RNA molecule to participate in self-replication fall into two categories: thermodynamic and structural motifs that allow strand separation and enzyme recruitment, and sequence-encoded folding or complementarity that supports template-directed copying [^1_1][^1_2]. In cellular DNA, these features center on replication origins and end-maintenance repeats, whereas in self-replicating RNA systems, they balance catalytic folding against template accessibility [^1_2][^1_3][^1_4].

## Complementary Base-Pairing and Directionality

The foundational requirement for nucleic-acid replication is **complementarity** via Watson–Crick base pairing (A–T/U and G–C), which allows a single strand to specify the exact sequence of a daughter strand [^1_5][^1_1]. Antiparallel 5'→3' strand polarity and a uniform polyanionic phosphodiester backbone decouple sequence information from bulk physicochemical properties, ensuring that diverse sequences can be copied by a single chemical mechanism [^1_6][^1_1].

## Replication Origins and AT-Rich Elements

In double-stranded DNA, replication begins at **origins** containing two distinct sequence-level features [^1_2]$$
7
$$:

- **AT-rich DNA unwinding elements (DUEs):** High adenine and thymine content reduces local thermodynamic stability because A–T pairs form two hydrogen bonds rather than three, allowing the double helix to melt and expose single-stranded templates [^1_6][^1_2][^1_8].
- **Initiator-binding repeats:** Conserved motifs—such as 9-bp DnaA boxes in bacterial *oriC*, plasmid iterons, or the AT-rich ARS consensus sequence (`WAAAYATAAAW`) in yeast—recruit initiator proteins that nucleate helicase loading [^1_9][^1_2][^1_10].
- **Regulatory methylation motifs:** Sequences like `GATC` in *E. coli* *oriC* act as molecular switches, where full methylation permits initiation while hemimethylation blocks premature re-replication [^1_2][^1_10].


## Secondary Structure and Template Accessibility

For autonomous or ribozyme-catalyzed RNA self-replication, sequence composition governs a central trade-off between **phenotype** (catalytic folding) and **genotype** (template copying) [^1_11][^1_4].

- **Low secondary structure in templates:** Heavily base-paired stems and hairpins stall polymerases; consequently, unstructured C-rich templates or variants with reduced secondary structure replicate much faster than tightly folded RNAs [^1_3][^1_4].
- **Short or fragmented templates:** Shorter RNA segments (e.g., under ~30 nucleotides) minimize inhibitory self-folding and dissociate more easily from complementary product strands after synthesis [^1_1].
- **Balanced GC/AU content:** While GC-rich regions stabilize ribozyme active sites, AU-rich regions are easier to unwind; prebiotic and ribozyme systems using short oligonucleotide (triplet) substrates can invade structured templates and stabilize weak AU-rich junctions through base stacking [^1_12].


## End-Maintenance and Fidelity-Length Limits

Linear eukaryotic chromosomes require **telomeric** tandem repeats (such as `TTAGGG`) at their ends to recruit telomerase and prevent progressive sequence loss during lagging-strand synthesis [^1_6]. For self-replicating RNA systems lacking protein proofreading, sequence length is strictly constrained by copying accuracy: the maximum maintainable genome length scales roughly with the inverse of the per-nucleotide error rate, requiring >99% fidelity to sustain a ~100-nucleotide ribozyme [^1_4].

<span style="display:none">[^1_13][^1_14][^1_15][^1_16][^1_17][^1_18][^1_19][^1_20][^1_21][^1_22][^1_23][^1_24][^1_25][^1_7]</span>

<div align="center">⁂</div>

[^1_1]: https://www.cambridge.org/core/journals/quarterly-reviews-of-biophysics/article/nucleic-acids-function-and-potential-for-abiogenesis/842529B9BDAD6E86F7919827725C1931

[^1_2]: https://academic.oup.com/femsre/article/36/2/408/565738

[^1_3]: https://www.science.org/doi/10.1126/science.1470913

[^1_4]: https://www.pnas.org/doi/10.1073/pnas.1914282117

[^1_5]: https://www.ncbi.nlm.nih.gov/books/NBK26850/

[^1_6]: https://www.ncbi.nlm.nih.gov/sites/books/n/statpearls/article-20638/

[^1_7]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3783049/

[^1_8]: https://blog.addgene.org/plasmid-101-origin-of-replication

[^1_9]: https://rna.bocsci.com/support/dna-replication-definition-characteristics-and-biological-functions.html

[^1_10]: http://www.bx.psu.edu/~ross/workmg/Replication2Ch6.htm

[^1_11]: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/842529B9BDAD6E86F7919827725C1931/S0033583517000038a.pdf/nucleic-acids-function-and-potential-for-abiogenesis.pdf

[^1_12]: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6003772/

[^1_13]: https://bio.libretexts.org/Bookshelves/Microbiology/Microbiology_Laboratory_Manual\_(Hartline)/01:\_Labs/1.30:\_DNA_RNA_and_DNA_Replication

[^1_14]: https://www.khanacademy.org/science/ap-biology/gene-expression-and-regulation/replication/a/hs-dna-structure-and-replication-review

[^1_15]: https://www.visiblebody.com/blog/dna-and-rna-basics-replication-transcription-and-translation

[^1_16]: https://quizlet.com/582968690/ap-bio-chp-13-flash-cards/

[^1_17]: https://teachmephysiology.com/biochemistry/cell-growth-death/dna-replication/

[^1_18]: https://genesdev.cshlp.org/content/17/15/1894.full

[^1_19]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12373953/

[^1_20]: https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/at-rich-sequence

[^1_21]: https://www.biorxiv.org/content/10.1101/2022.08.23.504927v2.full-text

[^1_22]: https://durham-repository.worktribe.com/OutputFile/1268282

[^1_23]: https://www.sciencedirect.com/science/article/pii/S1074552104002777

[^1_24]: https://en.wikipedia.org/wiki/Self-replication

[^1_25]: https://onlinelibrary.wiley.com/doi/full/10.1002/bies.70018


---

# Question 2 — Requirements for self-replication

What distinguishes a nucleic-acid molecule that can self-replicate from one that can only be copied using externally supplied biological machinery?

A nucleic-acid molecule capable of **self-replication** must encode both the genetic information (genotype) and the catalytic activity (phenotype) needed to direct its own synthesis, whereas a molecule copied by external biological machinery acts solely as a passive information template.[^3_1][^3_2]

## Genotype–Phenotype Duality vs. Passive Templates

In extant biology, DNA and mRNA are chemically stable information carriers that rely entirely on externally supplied protein enzymes—such as helicases, primases, and DNA or RNA polymerases—to unwind strands and catalyze phosphodiester bond formation. By contrast, a self-replicating nucleic acid (such as an RNA polymerase or ligase ribozyme) must fold into a catalytically active three-dimensional structure while still remaining legible as a template.[^3_2][^3_3][^3_1]


| Feature | Self-Replicating Nucleic Acid | Externally Copied Template |
| :-- | :-- | :-- |
| **Primary Role** | Dual: both catalyst and template [^3_2] | Single: passive information carrier [^3_1] |
| **Catalytic Source** | Intrinsic ribozyme active site [^3_3] | External protein polymerases and helicases [^3_1] |
| **Structural Constraint** | Must balance folding with template accessibility [^3_4][^3_1] | Optimized for stability and enzyme recognition |
| **Fidelity Mechanism** | Base-pairing thermodynamics alone [^3_5] | Active proofreading and mismatch repair |

## Intrinsic Catalysis and Autocatalytic Feedback

To self-replicate without proteins, a nucleic acid must catalyze the formation of 3'–5' phosphodiester bonds—either by ligating pre-formed oligonucleotide fragments (as in the R3C ligase ribozyme) or by polymerizing activated monomers or triplets along a template (as in class I polymerase derivatives or the 45-nucleotide QT45 ribozyme). Crucially, the newly synthesized product must itself be catalytically active, establishing **autocatalytic** feedback where the rate of synthesis scales with the concentration of the replicator.[^3_3][^3_6][^3_7][^3_8]

## Reciprocal Copying and Strand Separation

A true self-replicator cannot merely copy a single easy sequence; it must complete a full replication cycle by synthesizing both its **complementary** strand and a new copy of itself from that complement. This requires overcoming two major physical hurdles that external cellular machinery normally solves:[^3_1][^3_2]

- **Template unfolding:** Highly structured ribozymes resist copying because intramolecular base pairs block polymerase progression, whereas unstructured templates lack catalytic function.[^3_9][^3_1]
- **Product inhibition:** After synthesis, a newly made copy tends to remain tightly hybridized to its template, preventing exponential amplification unless strand separation is driven by thermal cycling, eutectic freezing, or short triplet substrates that invade duplexes.[^3_10][^3_3]


## Fidelity and Length Constraints

Without external proofreading subunits, self-replicating nucleic acids face a strict **error threshold**: copying fidelity must exceed $1 - 1/L$ (where $L$ is sequence length in nucleotides) to prevent functional information from decaying over generations. Consequently, autonomous replicators are constrained to compact catalytic motifs—such as the 45-nucleotide QT45 ribozyme—whereas externally replicated genomes can scale to millions or billions of base pairs.[^3_4][^3_5][^3_6]

<span style="display:none">[^3_11][^3_12][^3_13][^3_14][^3_15][^3_16][^3_17]</span>

<div align="center">⁂</div>

[^3_1]: https://www.pnas.org/doi/pdf/10.1073/pnas.1610103113

[^3_2]: https://mrclmb.ac.uk/news-events/articles/bridging-the-gap-from-chemistry-to-life-discovery-of-a-tiny-rna-that-can-copy-itself/

[^3_3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC130529/

[^3_4]: https://www.pnas.org/doi/10.1073/pnas.1914282117

[^3_5]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7022166/

[^3_6]: https://www.biorxiv.org/content/10.1101/2024.10.11.617851v1

[^3_7]: https://en.wikipedia.org/wiki/Ligase_ribozyme

[^3_8]: https://www.scilit.com/publications/4005da80322168026bbabbc55619cd1e

[^3_9]: https://www.science.org/doi/10.1126/science.1470913

[^3_10]: https://news.ycombinator.com/item?id=47000592

[^3_11]: https://fab.cba.mit.edu/classes/S62.12/bio.html

[^3_12]: https://bartellab.wi.mit.edu/publication_reprints/Lawrence\&Bartel%20RNA_05.pdf

[^3_13]: https://www.sciencedirect.com/science/article/pii/S1074552103000036

[^3_14]: https://scottlab.ucsc.edu/L1/ligase_inf.html

[^3_15]: https://www.ioc.kit.edu/pianowski/downloads/9 SoSe22 RNA World.pdf

[^3_16]: https://sciencecast.org/casts/tgzpx69o4qfi

[^3_17]: https://epigenie.com/newly-evolved-ribozyme-is-proof-of-principle-for-the-origin-of-life/


---

# Question 3 — Replication potential

Given a DNA or RNA sequence, what information would you need to determine whether it has self-replication potential? Explain what can and cannot be inferred from the sequence alone.

Determining whether a DNA or RNA sequence has self-replication potential requires knowing both its **intrinsic sequence-encoded properties** and the **extrinsic chemical and physical environment** in which it operates. From the sequence alone, you can evaluate structural plausibility, motif presence, and thermodynamic constraints, but you cannot determine whether the molecule will actually fold into an active catalyst, achieve sufficient copying fidelity, or overcome product inhibition without experimental and environmental context.

## What Can Be Inferred from Sequence Alone

Computational analysis of a primary sequence reveals several necessary—though not sufficient—indicators of replication potential:

- **Secondary structure and folding stability:** Thermodynamic folding algorithms (e.g., minimum free energy and partition function models) predict whether an RNA can form compact catalytic motifs (stems, loops, pseudoknots) or whether excessive intramolecular base-pairing will block its use as a template.
- **Template accessibility and melting behavior:** Base composition (GC vs. AT/AU content) and local sequence complexity indicate how easily a duplex can unwind and whether repetitive regions or homopolymers might cause polymerase slippage.
- **Known functional or origin motifs:** Sequence alignment can detect conserved ribozyme cores (e.g., ligase or polymerase motifs) or, for DNA, origin-of-replication features such as AT-rich unwinding elements and initiator-binding repeats.
- **Length relative to the error threshold:** Sequence length $L$ sets a strict upper bound on the tolerable per-nucleotide error rate ($p < 1/L$); a 500-nucleotide sequence, for example, is far harder to sustain autonomously than a 45-nucleotide motif.


## What Cannot Be Inferred from Sequence Alone

A primary sequence is a static blueprint; it does not specify the physical conditions or kinetic rates required for autonomous copying:

- **Tertiary catalysis and active-site geometry:** Secondary-structure prediction rarely captures non-canonical base pairs, long-range tertiary contacts, or metal-ion coordination pockets that create a functional ribozyme active site.
- **Chemical and environmental context:** Self-replication depends on externally supplied activated substrates (such as nucleoside triphosphates, phosphorimidazolides, or oligonucleotide triplets), divalent cations (typically $\text{Mg}^{2+}$) for catalysis, and specific pH, temperature, or freeze–thaw cycles to drive strand separation.
- **Reaction kinetics and fidelity:** Sequence alone cannot predict catalytic turnover rate ($k_{\text{cat}}$), substrate binding affinity ($K_m$), or actual nucleotide misincorporation rates—all of which determine whether synthesis outpaces hydrolysis and mutational decay.
- **Presence of external machinery:** A sequence that looks like a passive template (e.g., a plasmid or viral genome) cannot be distinguished from a non-replicating fragment without knowing whether host polymerases, helicases, or trans-acting ribozymes are present.


## Additional Information Needed

To conclusively assess self-replication potential, you would need:

1. **Environmental and chemical parameters:** Substrate identity and concentration, ionic strength, $\text{Mg}^{2+}$ levels, temperature, and whether strand-separation mechanisms (e.g., thermal cycling or eutectic phases) exist.
2. **3D structural data or in vitro activity assays:** Experimental verification (e.g., primer-extension or ligation assays) demonstrating that the molecule catalyzes phosphodiester bond formation on both itself and its complementary strand.
3. **Fidelity and stability measurements:** Empirical error rates per nucleotide and backbone half-life under the reaction conditions to confirm that replication outpaces degradation and mutational meltdown.

---

# Question 4 — Autonomous versus dependent replication

Explain the difference between autonomous self-replication, replication dependent on external enzymes, and non-replicating nucleic-acid molecules.

Nucleic-acid molecules fall into three distinct functional tiers based on whether they supply their own catalytic machinery and whether they can be copied at all: **autonomous self-replicators** encode both template and catalyst, **enzyme-dependent replicators** serve as passive templates for external proteins, and **non-replicating molecules** lack the sequence or structural features required for copying in their given environment.

## Comparison of Replication Tiers

| Property | Autonomous Self-Replication | Enzyme-Dependent Replication | Non-Replicating Molecule |
| :-- | :-- | :-- | :-- |
| **Catalytic Source** | Intrinsic (ribozyme active site) | External protein enzymes (polymerases, helicases) | None |
| **Information Role** | Dual: genotype and phenotype | Single: passive template | Terminal product or structural scaffold |
| **Typical Examples** | RNA polymerase/ligase ribozymes (e.g., QT45, R3C) | Cellular genomes, plasmids, viral RNA/DNA | mRNA, tRNA, rRNA, degraded fragments |
| **Length \& Complexity** | Constrained (~45–200 nt) by error threshold | Scales to millions or billions of base pairs | Variable |
| **Environmental Needs** | Activated monomers/triplets, $\text{Mg}^{2+}$, physical cycling | Full cellular or *in vitro* enzymatic machinery | Not applicable |

## Autonomous Self-Replication

An autonomous self-replicating nucleic acid—almost exclusively studied in RNA—possesses intrinsic catalytic activity that directs the synthesis of its own complementary strand and, subsequently, a new copy of itself. Because it operates without protein enzymes, the molecule must fold into a precise three-dimensional active site while remaining accessible enough to be read as a template. Its maximum length is strictly limited by the **error threshold**, as it lacks protein proofreading subunits.

## Replication Dependent on External Enzymes

Enzyme-dependent nucleic acids—including all cellular chromosomes, plasmids, and viral genomes—act solely as passive information carriers. They rely on externally supplied protein machinery (such as DNA/RNA polymerases, helicases, primases, and ligases) to unwind duplexes, initiate synthesis, and proofread errors. At the sequence level, they only need cis-acting recognition motifs, such as **origins of replication** (e.g., *oriC* or ARS elements) or viral promoter/replicase-binding sites, to recruit those external enzymes.

## Non-Replicating Nucleic-Acid Molecules

Non-replicating nucleic acids—such as messenger RNA (mRNA), transfer RNA (tRNA), ribosomal RNA (rRNA), or random oligonucleotide fragments—are synthesized by transcription or chemical assembly but are not copied into daughter strands. They lack both intrinsic polymerase/ligase activity and the cis-acting origin or primer-binding sequences required to recruit external replication machinery, serving instead as transient messages, structural scaffolds, or regulatory elements.

---

# Question 5 — Evidence of self-replication

What experimental evidence would be necessary to establish that a DNA or RNA molecule is genuinely capable of self-replication? How would you distinguish genuine replication from simple copying or amplification?

Establishing that a DNA or RNA molecule is genuinely capable of **self-replication** requires demonstrating sustained, autocatalytic exponential growth in the complete absence of external biological catalysts—not merely single-round template copying.[^6_1][^6_2]

## Core Experimental Evidence Required

To prove autonomous self-replication, an experimental system must satisfy four benchmarks:

- **Protein-free reaction conditions:** The assay must contain only the nucleic-acid replicator, defined chemical substrates (such as activated monomers or oligonucleotide fragments), buffer, and inorganic ions (e.g., $\text{Mg}^{2+}$), with rigorous controls confirming no contaminating protein polymerases or ligases.[^6_3][^6_1]
- **Complete reciprocal cycle:** The molecule must be shown to direct the synthesis of both its complementary strand and a new, catalytically active copy of itself (or, in cross-catalytic systems, two partners that mutually synthesize each other).[^6_4][^6_1]
- **Exponential amplification kinetics:** Product formation must follow logistic/exponential growth rather than linear accumulation, proving that newly synthesized copies actively catalyze further rounds of synthesis.[^6_1][^6_3]
- **Indefinite serial transfer:** When a small fraction of a completed reaction is repeatedly diluted into fresh substrate mixtures (e.g., 25-fold dilution across 6–20+ transfers), the replicator must maintain its concentration and achieve massive net amplification (e.g., $>10^8$- to $10^{25}$-fold) without losing activity.[^6_2][^6_1]


## Distinguishing Genuine Replication from Simple Copying

Simple template-directed copying or non-autonomous amplification (such as PCR or primer extension) differs fundamentally from genuine self-replication in kinetics, catalysis, and heritability:[^6_5][^6_2][^6_1]


| Criterion | Genuine Self-Replication | Simple Copying / External Amplification |
| :-- | :-- | :-- |
| **Growth Kinetics** | Exponential (autocatalytic feedback) [^6_1][^6_3] | Linear (single-round copying) or externally driven (e.g., PCR thermal cycling) [^6_5] |
| **Catalytic Independence** | Proceeds without protein enzymes [^6_1][^6_2] | Requires external polymerases (e.g., *Taq*, Qβ replicase) [^6_6][^6_5] |
| **Serial Dilution Survival** | Sustained across indefinite transfers [^6_4][^6_1] | Dilutes out once external enzyme or initial template is exhausted |
| **Heritable Variation** | Mutants or recombinants arise, compete, and evolve [^6_1][^6_7] | Sequence changes only reflect external enzyme error rates without intrinsic selection |

To rule out false positives—such as spontaneous uncatalyzed ligation or non-specific background polymerization—researchers run **no-seed controls** (omitting the initial replicator) and **catalytically dead mutant controls** (altering active-site residues while preserving template sequence), confirming that exponential amplification depends strictly on the folded, active nucleic-acid catalyst.[^6_3]

<span style="display:none">[^6_10][^6_8][^6_9]</span>

<div align="center">⁂</div>

[^6_1]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2652413/

[^6_2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2891321/

[^6_3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5103853/

[^6_4]: https://www.pnas.org/doi/10.1073/pnas.2413668121

[^6_5]: https://fse.studenttheses.ub.rug.nl/14917/1/MasterLS_MBB_2017_JGEdens.pdf

[^6_6]: https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/rna-replication

[^6_7]: https://www.salk.edu/news-release/modeling-the-origins-of-life-new-evidence-for-an-rna-world/

[^6_8]: https://academic.oup.com/nar/article/54/13/gkag663/8724181

[^6_9]: https://www.nature.com/articles/s41467-023-36940-z?error=cookies_not_supported\&code=f07c2884-48ab-45e6-89f1-dd12f13346df

[^6_10]: https://fab.cba.mit.edu/classes/S62.12/docs/Lincoln_RNA.pdf

