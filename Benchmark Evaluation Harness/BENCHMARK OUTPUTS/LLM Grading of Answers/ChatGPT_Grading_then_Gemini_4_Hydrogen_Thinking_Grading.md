# ChatGPT grading

| Question | Score (0–5) | Brief justification |
| -------- | :---: | ------------------- |
| Q1 | 2 | Identifies relevant sequence features, including replication origins, primer-binding sites, and RNA catalytic motifs. However, it conflates features supporting replication by external machinery with features enabling intrinsic self-replication. For example, bacterial origins and retroviral primer-binding sites do not establish autonomous replication. Telomeric repeats are also primarily involved in chromosome-end maintenance, not independent replication. |
| Q2 | 3 | Correctly recognizes the distinction between a passive template and a molecule or system providing catalytic replication functions. It also discusses reciprocal strand synthesis, fidelity, substrate requirements, folding, and strand separation. However, it defines autonomy too narrowly by requiring no externally supplied host enzymes. Self-encoded replication systems can depend on external translation machinery and other environmental resources. It also treats general substrates and reciprocal synthesis as overly universal requirements. |
| Q3 | 4 | Demonstrates a strong understanding that sequence analysis can identify candidate motifs, coding capacity, and structural tendencies, but cannot prove functional self-replication. Correctly emphasizes the need for biochemical, environmental, structural, and kinetic evidence. Minor weakness: some sequence-based indicators could be more carefully distinguished from evidence of intrinsic replication. |
| Q4 | 3 | Provides a useful distinction among autonomous, enzyme-dependent, and non-replicating nucleic acids. Correctly notes that plasmids can replicate independently of chromosome replication while still depending on host enzymes. However, its classification is somewhat inconsistent: it calls a self-encoded genome autonomous despite requiring external transcription–translation machinery, and it makes overly broad claims about which molecules cannot be replicated. |
| Q5 | 4 | Strongest answer. Identifies important experimental evidence: defined reaction conditions, contamination controls, catalytic-dead mutants, synthesis of complementary and regenerated strands, autocatalytic kinetics, and serial transfer beyond the original seed. Correctly distinguishes externally driven amplification from intrinsic replication. However, it overstates the necessity of exponential kinetics, reaction order near 1, indefinite serial transfer, and heritable variation. The latter is evidence of evolvability, not a universal prerequisite for self-replication. |
| **TOTAL** | **16/25** | **Moderate understanding. Strong experimental reasoning, but important conceptual distinctions remain imprecise.** |

## Overall assessment

- **Score:** 16/25
- **Understanding level:** Moderate
- **Biggest strength:** Recognizes that sequence motifs alone cannot establish self-replication and identifies meaningful experimental tests, particularly reciprocal strand synthesis, catalytic controls, and serial transfer.
- **Biggest weakness:** Does not consistently distinguish intrinsic molecular self-replication from replication by a self-encoded system that depends on external biological machinery.
- **Major scientific misconceptions:**
  1. Treats replication origins, primer-binding sites, telomeric repeats, and other sequence features as more directly related to autonomous replication than they actually are. Many are signals for externally supplied replication machinery.
  2. Imposes an overly strict definition of autonomy that excludes systems relying on external translation machinery, even when the replication machinery is encoded by the replicating system.
  3. Treats exponential kinetics, reaction order near 1, and indefinite serial transfer as universal requirements rather than strong evidence whose interpretation depends on the replication mechanism.
  4. Conflates self-replication with Darwinian evolvability in places. Heritable variation and selection are important for demonstrating evolution, but are not strictly necessary to establish molecular self-replication.

## Final conclusion

The model demonstrates a **moderately sound scientific understanding of DNA/RNA self-replication**. It understands that genuine replication requires more than sequence similarity, template copying, or externally driven amplification, and it proposes several meaningful experimental tests. Its strongest contribution is the emphasis on reciprocal synthesis, catalytic dependence, and serial-transfer experiments.

However, its definitions of autonomy and its proposed quantitative requirements are too rigid. It needs to distinguish more carefully between molecular self-replication, self-encoded replication systems, and externally assisted replication.

**Overall, it demonstrates useful conceptual and experimental understanding, but not yet consistently precise scientific reasoning about what constitutes genuine self-replication.**

This assessment evaluates conceptual understanding and experimental reasoning only. It does not establish that the model can generate functional self-replicating DNA or RNA; that would require independent experimental validation.

---

# Model response — Gemini4 Hydrogen Thinking

<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Question 1 — Replication-associated features

What sequence-level features of DNA or RNA are associated with the ability of a nucleic-acid molecule to participate in self-replication? Explain the biological relevance of these features.

The ability of a DNA or RNA molecule to participate in self-replication depends on sequence-level features that govern strand separation, initiator recognition, primer positioning, and—in catalytic RNAs—three-dimensional folding [^1_1][^1_2]. Across biological and prebiotic systems, these motifs couple passive information storage (Watson–Crick base-pairing) with the structural and thermodynamic cues needed to initiate and complete polymer synthesis [^1_1][^1_2].

## DNA origin and initiation motifs

Double-stranded DNA requires localized destabilization and protein recruitment before polymerases can access a single-stranded template [^1_3][^1_4]. Sequence motifs within replication origins solve both problems:

- **AT-rich** DNA unwinding elements (DUEs) contain elevated proportions of adenine and thymine, which form two hydrogen bonds and exhibit weaker base-stacking interactions than G–C pairs, lowering the thermal energy required for initial helix melting [^1_5][^1_6][^1_7].
- Conserved 13-mer tandem repeats (such as the L, M, and R 13-mers in *Escherichia coli* `oriC`) and proximal triplet repeats (DnaA-trios) sit within the DUE, where initiator filaments stretch single-stranded DNA and prevent reannealing while helicases load [^1_8][^1_2][^1_7].
- Initiator-binding repeats—such as 9-bp DnaA-boxes in bacteria or the 11-bp ARS consensus sequence (ACS) paired with flanking B elements in *Saccharomyces cerevisiae*—provide sequence-specific docking sites for initiator complexes (DnaA or ORC) to license replication at defined loci [^1_9][^1_2][^1_7].
- Regulatory sequence cues, including palindromic `GATC` methylation sites in bacteria and CpG islands or G-quadruplex (G4) motifs in metazoans, coordinate origin firing timing, prevent premature re-initiation, and modulate local DNA topology [^1_8][^1_2][^1_7].


## Chromosome ends and primer sites

Because nucleic-acid polymerases extend chains strictly in the 5'-to-3' direction from a pre-existing free 3'-OH group, genomes must encode sequences that preserve termini and nucleate synthesis [^1_10][^1_11].

- **Telomeric** tandem repeats (such as vertebrate `TTAGGG` arrays) cap linear eukaryotic chromosomes, serving as templates for telomerase and protecting coding sequences from progressive shortening during lagging-strand synthesis [^1_5].
- Primer-binding sites (PBS), exemplified by the conserved 18-nucleotide motif and adjacent hairpin loop in retroviral RNA genomes, recruit host tRNA primers whose 3'-OH initiates reverse transcription [^1_12].


## RNA folding and catalytic motifs

Unlike double-stranded DNA, single-stranded RNA molecules must balance two competing sequence demands: remaining accessible enough to act as a linear template while folding into functional secondary and tertiary structures [^1_1].

- **Stem-loops**, hairpins, three-way junctions, and pseudoknots arise from intramolecular base-pairing and serve as recognition signals for viral replicases or as scaffolds for catalytic ribozymes [^1_13][^1_14][^1_15].
- Conserved catalytic cores—such as the ~17-nucleotide invariant core adjacent to a three-helix junction in evolved ligase ribozymes—position `Mg2+` cofactors and align a 3'-OH nucleophile with a 5'-triphosphate to catalyze template-directed 5'-to-3' phosphodiester bond formation [^1_14].
- Self-cleaving motifs (including hammerhead, hairpin, and Varkud satellite ribozymes) embedded in viral satellite or plasmid RNAs process multimeric rolling-circle replication transcripts into unit-length monomers and mediate self-ligation into circles [^1_16][^1_15].
- Low-structure or fragmented template regions (typically under ~30 nucleotides in model ribozyme systems) minimize inhibitory intramolecular folding, allowing a replicase to copy the strand and permitting product–template separation afterward [^1_1].


## DNA versus RNA replication features

| Feature category | DNA sequence examples | RNA sequence examples | Biological relevance |
| :-- | :-- | :-- | :-- |
| Thermodynamic destabilization | AT-rich DUEs, 13-mer repeats [^1_8][^1_2] | Unstructured or short (\<30 nt) template segments [^1_1] | Lowers energetic barrier for strand separation [^1_1][^1_4] |
| Initiator or primer recruitment | DnaA-boxes, ARS consensus sequence [^1_9][^1_7] | 18-nt retroviral PBS and flanking hairpin [^1_12] | Specifies origin site and provides a 3'-OH start [^1_10][^1_12] |
| Topological and end maintenance | `TTAGGG` telomeric repeats, G4 motifs [^1_5][^1_2] | Self-cleaving ribozymes (hammerhead, VS) [^1_16][^1_15] | Prevents end loss and resolves replication intermediates [^1_5][^1_15] |
| Catalytic assembly | Not typically catalytic in vivo | Three-way junctions and conserved catalytic cores [^1_13][^1_14] | Enables autonomous, protein-free RNA ligation or polymerization [^1_1][^1_14] |

<span style="display:none">[^1_17][^1_18][^1_19][^1_20][^1_21][^1_22][^1_23][^1_24][^1_25]</span>

<div align="center">⁂</div>

[^1_1]: https://www.cambridge.org/core/journals/quarterly-reviews-of-biophysics/article/nucleic-acids-function-and-potential-for-abiogenesis/842529B9BDAD6E86F7919827725C1931

[^1_2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6742236/

[^1_3]: https://www.ncbi.nlm.nih.gov/books/NBK26850/

[^1_4]: https://www.pnas.org/doi/10.1073/pnas.0805662105

[^1_5]: https://www.ncbi.nlm.nih.gov/sites/books/n/statpearls/article-20638/

[^1_6]: https://blog.addgene.org/plasmid-101-origin-of-replication

[^1_7]: https://en.wikipedia.org/wiki/Origin_of_replication

[^1_8]: https://academic.oup.com/femsre/article/36/2/408/565738

[^1_9]: https://rna.bocsci.com/support/dna-replication-definition-characteristics-and-biological-functions.html

[^1_10]: https://www.khanacademy.org/science/ap-biology/gene-expression-and-regulation/replication/a/molecular-mechanism-of-dna-replication

[^1_11]: https://bio.libretexts.org/Bookshelves/Microbiology/Microbiology_Laboratory_Manual\_(Hartline)/01:\_Labs/1.30:\_DNA_RNA_and_DNA_Replication

[^1_12]: https://pmc.ncbi.nlm.nih.gov/articles/PMC147018/

[^1_13]: https://www.pnas.org/doi/10.1073/pnas.202471099

[^1_14]: https://scottlab.ucsc.edu/scottlab/reprints/2007_Scott_Science_pdf/2007_Scott_Science.pdf

[^1_15]: https://en.wikipedia.org/wiki/VS_ribozyme

[^1_16]: https://doudnalab.org/Publications/arbiochem-69-597.pdf

[^1_17]: https://www.visiblebody.com/blog/dna-and-rna-basics-replication-transcription-and-translation

[^1_18]: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/842529B9BDAD6E86F7919827725C1931/S0033583517000038a.pdf/nucleic-acids-function-and-potential-for-abiogenesis.pdf

[^1_19]: https://quizlet.com/582968690/ap-bio-chp-13-flash-cards/

[^1_20]: https://teachmephysiology.com/biochemistry/cell-growth-death/dna-replication/

[^1_21]: https://www.nature.com/articles/s41467-020-18964-x

[^1_22]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12373953/

[^1_23]: https://www.biorxiv.org/content/10.1101/2022.05.17.492349v1.full-text

[^1_24]: https://www.sciencedirect.com/topics/neuroscience/origin-of-replication

[^1_25]: https://bartellab.wi.mit.edu/publication_reprints/Lawrence\&Bartel%20RNA_05.pdf


---

# Question 2 — Requirements for self-replication

What distinguishes a nucleic-acid molecule that can self-replicate from one that can only be copied using externally supplied biological machinery?

A truly self-replicating nucleic acid must act simultaneously as an instructive genetic template and as the catalyst (or self-encoded replicase system) that drives its own copying, whereas an externally copied molecule functions strictly as a passive template. In practice, autonomous replication requires a single sequence—or a closed, self-encoded network—to synthesize both its complementary strand and new copies of itself without pre-supplied host enzymes.[^2_1][^2_2][^2_3][^2_4]

## Dual template and catalytic capacity

Externally copied genomes, plasmids, and classic in vitro systems (such as bacteriophage Qβ RNA replicated by researcher-supplied Qβ replicase) provide sequence information and recognition motifs, while external protein polymerases, helicases, and primases execute catalysis. By contrast, an autonomous nucleic acid must supply the enzymatic machinery itself:[^2_5][^2_1]

- **Ribozyme** polymerases fold into a catalytic tertiary structure that binds a primer–template complex, aligns activated substrates, and catalyzes regiospecific 3'-to-5' phosphodiester bond formation.[^2_4][^2_6]
- Reciprocal synthesis requires the catalyst to copy itself into a complementary (`-`) strand and then use that complement as a template to regenerate active (`+`) copies, a two-step cycle recently demonstrated in separate reactions by the 45-nucleotide QT45 triplet polymerase ribozyme.[^2_2][^2_4]
- Autocatalytic ligases (such as redesigned R3C ribozymes) bypass step-by-step polymerization by templating and joining two pre-formed oligonucleotide halves (`A + B → T`), creating a product identical to the catalyst.[^2_7][^2_8]


## Substrate generality and evolvability

A major divide separates chemical self-assembly from Darwinian self-replication. Ligase-based systems depend on carefully curated, pre-synthesized oligonucleotide substrates, which locks the sequence in place and prevents heritable variation from propagating. To support open-ended evolution, a self-replicating nucleic acid must polymerize general, sequence-independent monomers (nucleoside triphosphates) or short random oligomers such as trinucleotides, allowing mutations to arise and persist across generations.[^2_3][^2_9][^2_10][^2_1]

## Fidelity, folding, and strand separation

Autonomous nucleic acids face severe biophysical constraints that externally assisted genomes offload onto dedicated protein machines:

- **Fidelity** must exceed the error threshold set by sequence length; copying a ~100-nucleotide ligase ribozyme, for example, demands >99% per-nucleotide accuracy to prevent mutational collapse, and synthesis must outpace spontaneous hydrolysis.[^2_6][^2_9]
- **Folding** creates an inherent structural paradox because the same sequence must adopt a stable, complex fold to function as a catalyst while unfolding readily to serve as an accessible template.[^2_2][^2_3]
- Strand separation after synthesis poses a persistent bottleneck, as tight Watson–Crick pairing traps newly made (`+`) and (`-`) strands in inactive duplexes unless relieved by thermal cycling, pH shifts, or co-evolved unwinding mechanisms.[^2_9][^2_3]


## Self-replicating versus externally copied systems

| Dimension | Autonomous self-replicator | Externally copied nucleic acid |
| :-- | :-- | :-- |
| Primary role | Both genetic template and active catalyst [^2_2][^2_3] | Passive information template and binding scaffold [^2_1][^2_5] |
| Catalytic machinery | Self-folded ribozyme or self-encoded replicase [^2_1][^2_4] | Host or researcher-supplied polymerases and helicases [^2_1] |
| Substrates | Activated monomers (NTPs), triplets, or curated oligomers [^2_9][^2_3] | Cellular or purified dNTPs/NTPs [^2_1] |
| Strand separation | Limited by product inhibition; relies on environmental cycling [^2_9][^2_3] | Actively driven by external helicases or thermal PCR cycling [^2_11][^2_10] |
| Evolvability | High only if using general monomers or short oligomers [^2_9][^2_3] | High, buffered by high-fidelity protein proofreading [^2_12][^2_1] |

<span style="display:none">[^2_13][^2_14][^2_15][^2_16][^2_17]</span>

<div align="center">⁂</div>

[^2_1]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5041002/

[^2_2]: https://mrclmb.ac.uk/news-events/articles/bridging-the-gap-from-chemistry-to-life-discovery-of-a-tiny-rna-that-can-copy-itself/

[^2_3]: https://www.biorxiv.org/content/10.1101/2024.10.11.617851v1.full-text

[^2_4]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7618777/

[^2_5]: https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/self-replication

[^2_6]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6120706/

[^2_7]: https://pubs.acs.org/doi/10.1021/jacs.9b10796

[^2_8]: https://pmc.ncbi.nlm.nih.gov/articles/PMC130529/

[^2_9]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7022166/

[^2_10]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5024611/

[^2_11]: https://bio.libretexts.org/Bookshelves/Microbiology/Microbiology_Laboratory_Manual\_(Hartline)/01:\_Labs/1.30:\_DNA_RNA_and_DNA_Replication

[^2_12]: https://www.ncbi.nlm.nih.gov/books/NBK26850/

[^2_13]: https://link.springer.com/article/10.1007/BF01582021

[^2_14]: https://bartellab.wi.mit.edu/publication_reprints/Lawrence_Biochem03.pdf

[^2_15]: https://www.biorxiv.org/content/10.64898/2026.07.25.740712v1.full

[^2_16]: https://www.reddit.com/r/Creation/comments/1t20he7/a_selfreplicating_polymerase_ribosyme_that_can/

[^2_17]: https://www.cambridge.org/core/journals/quarterly-reviews-of-biophysics/article/nucleic-acids-function-and-potential-for-abiogenesis/842529B9BDAD6E86F7919827725C1931


---

# Question 3 — Replication potential

Given a DNA or RNA sequence, what information would you need to determine whether it has self-replication potential? Explain what can and cannot be inferred from the sequence alone.

Determining whether a DNA or RNA sequence has self-replication potential requires combining primary sequence analysis with structural, biochemical, and environmental context. Sequence alone can flag known functional motifs and thermodynamic feasibility, but it cannot reliably predict novel catalytic activity, three-dimensional folding dynamics, or whether external conditions permit actual copying.[^3_1][^3_2][^3_3]

## What sequence alone can reveal

Primary sequence analysis is most informative when a molecule shares homology or structural grammar with characterized replicators or host-dependent replicons:[^3_4][^3_1]

- **Motif** and domain homology: Alignment and *k*-mer searches can detect bacterial DnaA-box clusters, AT-rich unwinding regions, Z-curve nucleotide disparities, yeast ARS consensus sequences, or conserved catalytic cores of known ligase and polymerase ribozymes.[^3_1][^3_4]
- **Coding** capacity for replicases: Open reading frames in viral or synthetic self-amplifying RNAs can be translated in silico to identify RNA-dependent RNA polymerases (RdRps) and flanking untranslated region (UTR) promoters required for intracellular amplification.[^3_5][^3_6]
- Secondary structure and thermodynamic stability: Folding algorithms estimate intramolecular base-pairing, stem-loops, and duplex melting temperatures (`Tm`), indicating whether a strand is likely to be overly structured (blocking template access) or sufficiently unstructured to permit copying.[^3_7][^3_4]
- Length and error-threshold bounds: Sequence length combined with expected replication fidelity indicates whether the molecule exceeds the mutational error threshold (for example, longer ribozymes require higher per-base accuracy to avoid mutational meltdown).[^3_7]


## Information required beyond the sequence

Even with an exact nucleotide string, assessing true self-replication potential requires external physical and biological parameters:[^3_8][^3_1]

- **Environment** and chemical context: Autonomous ribozymes and non-enzymatic replicators depend on specific `Mg2+` concentrations, pH, temperature cycling, or eutectic ice phases, as well as the chemical identity and concentration of activated substrates (monomer NTPs versus trinucleotide triphosphates or pre-formed oligomers).[^3_9][^3_10][^3_7]
- Host and epigenetic context: For DNA origins or self-amplifying viral RNAs, replication depends on host factors, chromatin accessibility, DNA bendability, and epigenetic marks rather than sequence motifs alone.[^3_8][^3_1]
- Experimental kinetic and yield data: Determining whether synthesis outpaces spontaneous RNA hydrolysis, avoids kinetic folding traps, and achieves exponential amplification across both `(+)` and `(-)` strands requires empirical assays.[^3_4][^3_9][^3_7]


## Limits of sequence-based inference

| Assessment dimension | Inferable from sequence alone | Cannot be reliably inferred from sequence alone |
| :-- | :-- | :-- |
| Known replicators | Homology to characterized origins, ribozymes, or viral RdRps [^3_4][^3_1] | Activity of novel folds absent from structural training sets [^3_7][^3_2] |
| Structural behavior | Predicted secondary stems, GC content, and local duplex `Tm` [^3_4][^3_7] | Dynamic 3D tertiary folding, misfolding, and catalytic site geometry [^3_2] |
| Mutational tolerance | Conservation patterns in aligned families [^3_4][^3_3] | Higher-order epistatic interactions beyond 5–7 mutations [^3_3] |
| Replication cycle | Presence of terminal primer sites or complementary symmetry [^3_10] | Strand-separation efficiency, product inhibition, and net copying yield [^3_7][^3_9] |

Because sequence conservation does not reliably predict relative catalytic activity and DNA or RNA molecules are inert without compatible substrates or machinery, primary sequence serves as a screening filter rather than proof of self-replication.[^3_3][^3_11][^3_8]

<span style="display:none">[^3_12][^3_13][^3_14][^3_15]</span>

<div align="center">⁂</div>

[^3_1]: https://academic.oup.com/bib/article/27/3/bbag315/8711649

[^3_2]: https://academic.oup.com/nar/article/54/16/gkag813/8769247

[^3_3]: https://www.biorxiv.org/content/10.1101/2022.05.31.494017v1.full

[^3_4]: https://www.nature.com/articles/s41467-025-63151-5

[^3_5]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7122455/

[^3_6]: https://rna.bocsci.com/support/what-is-self-replicating-rna.html

[^3_7]: https://www.science.org/doi/10.1126/science.adt2760

[^3_8]: https://plato.stanford.edu/archives/win2021/entries/replication/

[^3_9]: https://www.nature.com/articles/s41598-026-40325-9

[^3_10]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6003772/

[^3_11]: https://www.meer.com/en/33076-self-replication-and-self-reproduction

[^3_12]: https://resolve.cambridge.org/core/services/aop-cambridge-core/content/view/6A5751130DE0264C4F017AAC73DB1FF6/9780511817540c7_p129-154_CBO.pdf/self-replication-and-self-reproduction.pdf

[^3_13]: https://pubs.rsc.org/cc/article/57/61/7517/717319/RNA-diversification-by-a-self-reproducing-ribozyme

[^3_14]: http://ib.bioninja.com.au/a-self-replication/

[^3_15]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12373953/


---

# Question 4 — Autonomous versus dependent replication

Explain the difference between autonomous self-replication, replication dependent on external enzymes, and non-replicating nucleic-acid molecules.

Nucleic-acid molecules fall into three functional tiers based on whether they supply their own catalytic machinery, borrow external enzymes to copy themselves, or act strictly as non-copied information or structural elements [^4_1][^4_2][^4_3].

## Autonomous self-replication

Autonomous self-replicators encode or embody the catalytic function required to assemble copies of themselves from chemical building blocks without relying on externally supplied polymerases [^4_4][^4_5].

- **Catalytic** RNAs (ribozymes): Polymerase and ligase ribozymes fold into active three-dimensional structures that recognize a template, align activated nucleotides or short oligomers, and catalyze phosphodiester bond formation [^4_6][^4_5].
- Non-enzymatic chemical replicators: Short DNA or chimeric oligomers can undergo template-directed ligation or polymerization driven solely by chemical activation, thermodynamic free-energy gradients, and simple metal-ion cofactors [^4_7][^4_8].
- Self-encoded synthetic genomes: Advanced cell-free systems such as the Replication-Cycle Reaction (RCR) module-genome encode all 26 replication proteins needed to copy their own `oriC`-bearing DNA, though they still require an external transcription–translation (PURE) extract, amino acids, and nucleotides [^4_1].


## Replication dependent on external enzymes

Enzyme-dependent replicons carry the sequence signals required to initiate copying—and sometimes encode part of their own machinery—but cannot replicate without host or researcher-supplied enzymes [^4_4][^4_9][^4_10].

- **Plasmids** and chromosomes: Extrachromosomal plasmids are often described as "autonomously replicating" because they replicate independently of host chromosome division via an origin of replication (`ori` or yeast `ARS`), yet they depend entirely on host DNA polymerases, helicases, primases, and dNTPs [^4_11][^4_9][^4_10].
- Viral genomes and self-amplifying RNAs (saRNAs): Positive-sense RNA viruses and saRNA vaccines encode an RNA-dependent RNA polymerase (RdRp) alongside flanking promoter UTRs, but they rely on host ribosomes to translate the replicase and host nucleotides to amplify the RNA [^4_12][^4_2].
- In vitro amplification templates: Linear DNA fragments or viral RNAs used in PCR, isothermal nicking-polymerization cascades, or Qβ replicase assays are copied exponentially only because purified protein polymerases are supplied externally [^4_4][^4_13].


## Non-replicating nucleic-acid molecules

Non-replicating molecules lack both intrinsic catalytic activity and functional replication origins or replicase-recognition promoters, so they are neither self-copied nor amplified by cellular replication machinery [^4_2][^4_14].

- **Conventional** mRNA: Eukaryotic and therapeutic mRNAs carry a 5' cap, UTRs, coding sequence, and poly(A) tail for ribosomal translation into protein, after which they are degraded without generating new RNA copies [^4_15][^4_2].
- Linear DNA lacking an `ori`: Transfected PCR amplicons or sheared genomic fragments that do not integrate into a host chromosome and lack an origin of replication are diluted out across cell divisions [^4_14][^4_3].
- Regulatory and structural RNAs: Short interfering RNAs (siRNAs), antisense oligonucleotides, and mature cellular rRNAs or tRNAs perform catalytic, regulatory, or scaffolding roles without serving as templates for their own duplication.


## Comparison of replication modes

| Category | Catalytic source | Required sequence features | Examples |
| :-- | :-- | :-- | :-- |
| Autonomous self-replication | Intrinsic ribozyme fold or chemical autocatalysis [^4_7][^4_5] | Catalytic core, primer/template binding regions [^4_6][^4_5] | Ligase/polymerase ribozymes, non-enzymatic replicators [^4_7][^4_5] |
| Enzyme-dependent replication | External host or purified protein enzymes [^4_4][^4_10] | Origin (`ori`, `ARS`), viral UTR promoters, or RdRp ORF [^4_11][^4_2][^4_14] | Plasmids, viral genomes, saRNA vaccines, PCR templates [^4_16][^4_2][^4_9] |
| Non-replicating molecules | None (not copied) [^4_2] | Translation signals (5' cap, UTRs) or structural motifs [^4_2] | Conventional mRNA, siRNA, `ori`-less DNA fragments [^4_2][^4_14] |

<span style="display:none">[^4_17][^4_18]</span>

<div align="center">⁂</div>

[^4_1]: https://academic.oup.com/nar/article/54/13/gkag663/8724181

[^4_2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5906799/

[^4_3]: https://en.wikipedia.org/wiki/Plasmid

[^4_4]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5041002/

[^4_5]: https://en.wikipedia.org/wiki/RNA_world

[^4_6]: https://pmc.ncbi.nlm.nih.gov/articles/PMC130529/

[^4_7]: https://www.nature.com/articles/s41598-026-40325-9?error=cookies_not_supported\&code=a11296c5-a322-4c32-941a-73ad44ec18b4

[^4_8]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7059183/

[^4_9]: https://en.wikipedia.org/wiki/Vector\_(molecular_biology)

[^4_10]: https://microbenotes.com/plasmid-vectors/

[^4_11]: https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/autonomously-replicating-sequence

[^4_12]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7122455/

[^4_13]: https://pubs.acs.org/doi/10.1021/ac4013094

[^4_14]: https://www.sciencedirect.com/topics/medicine-and-dentistry/plasmid

[^4_15]: https://dnasu.org/DNASU/Resources/Plasmid.jsp

[^4_16]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5024611/

[^4_17]: https://academic.oup.com/nar/article/27/17/3389/2376259

[^4_18]: https://www.sciencedirect.com/science/article/pii/S2162253126003240


---

# Question 5 — Evidence of self-replication

What experimental evidence would be necessary to establish that a DNA or RNA molecule is genuinely capable of self-replication? How would you distinguish genuine replication from simple copying or amplification?

Establishing that a DNA or RNA molecule is genuinely capable of self-replication requires proving that the molecule—without external protein polymerases—catalyzes the complete synthesis of active copies of itself (or its reciprocal partner) at rates yielding exponential, indefinitely sustainable growth. Simple copying or linear amplification, by contrast, produces only single-turnover complements, sub-exponential bursts, or growth driven by external catalysts.[^5_1][^5_2][^5_3][^5_4][^5_5]

## Core experimental criteria for self-replication

To demonstrate autonomous self-replication rigorously, experiments must satisfy five connected benchmarks:

- **Protein-free** reaction validation: The reaction must proceed in a chemically defined medium containing only the nucleic acid, substrates (NTPs, triplets, or oligonucleotides), buffer, and cofactors such as `Mg2+`, with negative controls lacking the seed molecule or using catalytically dead active-site mutants to rule out spontaneous background ligation and protein contamination.[^5_2][^5_3][^5_1]
- Full-cycle reciprocal synthesis: Assays (such as PAGE, sequencing, or mass spectrometry) must confirm synthesis of both the complementary `(-)` strand and new functional `(+)` copies from the `(-)` template, rather than copying only a short, unstructured primer.[^5_6][^5_7]
- Autocatalytic exponential kinetics: Measuring initial synthesis rates across varying seed concentrations must show a reaction order (`ρ`) near `1.0`—meaning rate scales directly with existing replicator concentration—and logistic growth curves before substrate depletion.[^5_3][^5_8]
- Indefinite **serial** transfer: Repeatedly diluting a small fraction of a completed reaction (for example, 1:10 or 1:25) into fresh substrate mixtures across multiple generations must maintain steady-state or growing concentrations (producing characteristic "zigzag" amplification plots) well beyond the point where the original seed would be diluted to zero.[^5_5][^5_9][^5_2]
- Heritable variation and selection: Competing sequence variants or introducing mutations during serial transfer must demonstrate that modified sequences are faithfully copied and can outcompete slower variants or parasites.[^5_9][^5_1]


## Distinguishing genuine replication from simple copying

Many nucleic-acid systems appear to amplify at first glance but fall short of self-replication because they hit kinetic bottlenecks or rely on external enzymes.[^5_4][^5_8][^5_5]

- **Single-round** copying stops after one template-directed extension or ligation because the newly formed `(+)/(–)` duplex remains tightly annealed (product inhibition), whereas genuine replicators dissociate or turnover to seed subsequent rounds.[^5_8][^5_3][^5_6]
- Parabolic or linear growth occurs when dimerization or duplex trapping limits active catalyst release (`ρ ≈ 0.5` or `0`), producing an initial burst followed by a slow linear phase rather than true exponential doubling (`ρ ≈ 1.0`).[^5_3][^5_5]
- Externally driven amplification (such as PCR, isothermal nicking cascades, or Qβ replicase assays) achieves exponential growth only because purified protein polymerases, helicases, or thermal cyclers supply the catalysis and strand separation.[^5_10][^5_4]


## Experimental benchmarks compared

| Experimental test | Genuine self-replication | Simple copying or external amplification |
| :-- | :-- | :-- |
| Reaction composition | Defined buffer, salts, and substrates; zero protein enzymes [^5_1][^5_2] | Requires host extract or purified protein polymerases [^5_4] |
| Strand synthesis | Produces both `(-)` complement and functional `(+)` copies [^5_6][^5_7] | Copies only a single strand or short unstructured oligo [^5_6][^5_11] |
| Growth kinetics | Reaction order `ρ ≈ 1.0`; logistic exponential doubling [^5_8][^5_3] | Parabolic (`ρ ≈ 0.5`), linear burst, or protein-driven PCR [^5_10][^5_5][^5_3] |
| Serial dilution outcome | Sustained amplification over many transfers (`>10^6`-fold) [^5_2][^5_3] | Signals wash out as initial seed or template dilutes away [^5_9][^5_2] |
| Active-site mutant control | Abolishes exponential amplification above background [^5_3] | Unaffected if external polymerase copies the mutant passively [^5_4] |

<span style="display:none">[^5_12][^5_13][^5_14][^5_15][^5_16][^5_17][^5_18][^5_19]</span>

<div align="center">⁂</div>

[^5_1]: https://www.science.org/doi/10.1126/science.1167856

[^5_2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2652413/

[^5_3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11536142/

[^5_4]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5041002/

[^5_5]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2891321/

[^5_6]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7022166/

[^5_7]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7618777/

[^5_8]: https://pubs.acs.org/doi/10.1021/bi301646n

[^5_9]: https://www.nature.com/articles/s41467-023-36940-z?error=cookies_not_supported\&code=f07c2884-48ab-45e6-89f1-dd12f13346df

[^5_10]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5024611/

[^5_11]: https://mrclmb.ac.uk/news-events/articles/how-the-earliest-life-on-earth-may-have-replicated-itself/

[^5_12]: https://www.cell.com/article/S1074-5521(13)00426-2/fulltext

[^5_13]: https://www.sciencedirect.com/science/article/pii/S1074552113004262

[^5_14]: https://rfam.org/family/RF01787

[^5_15]: https://www.scripps.edu/newsandviews/e_20141103/joyce.html

[^5_16]: https://quizlet.com/1149618323

[^5_17]: https://resolve.cambridge.org/core/services/aop-cambridge-core/content/view/6A5751130DE0264C4F017AAC73DB1FF6/9780511817540c7_p129-154_CBO.pdf/self-replication-and-self-reproduction.pdf

[^5_18]: https://pmc.ncbi.nlm.nih.gov/articles/PMC130529/

[^5_19]: https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/self-replication

