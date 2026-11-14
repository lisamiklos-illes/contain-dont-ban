<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

## Self-Replication and Nucleic-Acid Sequence Features

A nucleic-acid molecule can serve as a template for its own replication only when its primary sequence encodes physical and chemical properties that allow it to be copied, recognized by replication machinery, and faithfully propagated. Sequence-level features fall into two classes: **sequence-specific signals** (binding sites and motifs that recruit proteins or catalytic RNAs) and **sequence-influenced biophysical properties** (base composition and folding behavior that control strand separation and polymerase progression). Below are the major features, with their biological relevance.

### 1. Origin-of-replication sequences

**What they are:** Short, specific DNA sequences where replication begins. In bacteria, the *oriC* typically contains DnaA-box motifs (about 9 bp) arranged with particular spacing and orientation; in budding yeast, origins include an essential A element plus auxiliary B elements forming autonomously replicating sequences (ARSs). [^1_1]

**Biological relevance:** These sequences act as landing pads for initiator proteins (DnaA in bacteria, ORC in eukaryotes). Recognition is sequence-specific, so replication initiates at defined sites rather than randomly. This ensures that every chromosome is replicated once per cell cycle, with coordinated timing and regulated copy number. [^1_1][^1_2]

### 2. AT-rich DNA unwinding elements (DUEs)

**What they are:** Regions of elevated adenine-thymine content, often located adjacent to origin recognition sites. A·T base pairs form only two hydrogen bonds (versus three for G·C), so AT-rich duplexes melt more easily. [^1_3][^1_1]

**Biological relevance:** The lower melting temperature makes these regions the preferred site for initial strand separation by initiator proteins and helicases. In bacterial *oriC*, the DUE is where DnaA melts the duplex to load the replicative helicase; in plasmids such as RK2, specific short repeats within the AT-rich region are required for either origin opening or helicase loading. [^1_4][^1_1] AT-richness is thus a physical “weak spot” in the sequence that lets replication start without excessive energy input.

### 3. Directionality (5′→3′ polarity and primer requirement)

**What they are:** All nucleic-acid strands have an inherent 5′ to 3′ chemical direction. DNA and RNA polymerases can add nucleotides only to the free 3′-OH end of a growing chain, meaning synthesis proceeds strictly 5′→3′ on the new strand. DNA polymerases cannot initiate de novo and require a short RNA primer with an exposed 3′-OH. [^1_5][^1_3]

**Biological relevance:** Directionality imposes a mechanical constraint on replication: on the antiparallel template strands, one daughter strand (leading) is synthesized continuously, while the other (lagging) must be made discontinuously as Okazaki fragments. The primer requirement means every replication fork needs primase activity to lay down starting points. This polarity is universal across cellular life and many viruses, and it fundamentally shapes how replication forks are organized.

### 4. Complementary base pairing and duplex stability

**What they are:** Watson–Crick pairing rules—A with T (or U in RNA), G with C—allow each strand of a duplex to specify the sequence of its complement. Stacking interactions between adjacent bases further stabilize the helix. [^1_3][^1_6]

**Biological relevance:** Complementarity is the molecular basis of semi-conservative replication: when strands separate, each one templates a new partner, so the information is duplicated without loss. It also provides an intrinsic error-checking mechanism—mismatched pairs are energetically unfavorable and are recognized by polymerase proofreading. [^1_6]

### 5. Telomeric repeats (for linear molecules)

**What they are:** Tandem short repeats at chromosome ends (e.g., TTAGGG in vertebrates) synthesized by the specialized reverse transcriptase telomerase, which carries its own RNA template. [^1_3]

**Biological relevance:** Conventional DNA polymerases cannot fully copy the very ends of linear chromosomes (the “end-replication problem”). Telomeric repeats provide a disposable, non-coding buffer that is replenished by telomerase, preventing progressive loss of genes with each division and protecting chromosome ends from being mistaken for broken DNA. [^1_3]

### 6. RNA secondary-structure and catalytic motifs (for RNA self-replication)

**What they are:** RNA sequences that fold into three-dimensional catalytic shapes (ribozymes), including RNA polymerase ribozymes capable of copying RNA templates. In vitro evolution has produced ribozymes that synthesize both strands of an RNA molecule and can copy segments of themselves. [^1_7]

**Biological relevance:** RNA is the only nucleic acid known to combine genetic information storage with catalytic function in one molecule. RNA self-replication is central to the RNA-world hypothesis for the origin of life and to the replication cycles of RNA viruses. Sequence features that permit folding into active catalytic pockets—without forming structures so stable that they block strand separation—are what allow an RNA to participate in its own copying. [^1_8][^1_9]

### 7. Low-complexity and repetitive sequences (structural facilitation)

**What they are:** Tracts of repeated bases or simple repeats that can adopt non-B-DNA structures (e.g., G-quadruplexes in G-rich DNA, hairpins in AT-rich or palindromic sequences). [^1_10]

**Biological relevance:** Such sequences are found at some eukaryotic replication origins, where G-quadruplex structures may help position initiation machinery, although they are neither necessary nor sufficient by themselves. In RNA, repetitive or self-complementary sequences can facilitate rolling-circle replication by providing polymerase pause or restart sites. [^1_10][^1_11]

______________________________________________________________________

### Summary table

| Sequence-level feature | What it does | Biological relevance |
| :-- | :-- | :-- |
| Origin motifs (DnaA boxes, ARS, ORBs) | Recruit initiator proteins | Defines where replication starts; ensures once-per-cycle, regulated initiation |
| AT-rich unwinding elements | Lowers duplex melting temperature | Enables strand separation for helicase loading and fork formation |
| 5′→3′ directionality + primer requirement | Constrains polymerase chemistry | Creates leading/lagging-strand asymmetry; requires primase to initiate synthesis |
| Complementary base pairing | Each strand templates its complement | Basis of semi-conservative copying and information fidelity |
| Telomeric repeats (linear DNA) | Buffers chromosome ends | Solves the end-replication problem; protects gene-bearing DNA |
| RNA catalytic/structural motifs | Ribozyme polymerase activity | Enables RNA to copy itself; central to RNA viruses and origin-of-life models |
| Low-complexity/repetitive tracts | Form non-canonical structures | Can influence origin positioning and replication termination/restart |

**Bottom line:** No single sequence feature makes a nucleic acid “self-replicating” in isolation. Instead, replication capability emerges from the combination of (1) specific recognition sequences that recruit machinery, (2) base-composition patterns that control strand melting, (3) the universal 5′→3′ chemical polarity of nucleic-acid synthesis, and (4) complementary base pairing that lets each strand serve as a template. For RNA, catalytic folding ability adds a fifth dimension: the molecule can both store the information and perform the copying chemistry.

[^1_3] [^1_5] [^1_6] [^1_4] [^1_10] [^1_7] [^1_1] [^1_9] [^1_11] [^1_2]

<span style="display:none">[^1_12][^1_13][^1_14][^1_15][^1_16][^1_17][^1_18][^1_19][^1_20][^1_21][^1_22][^1_23][^1_24][^1_25]</span>

<div align="center">⁂</div>

[^1_1]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6742236/

[^1_2]: http://rcn.montana.edu/Publications/Pdf/2005/FEBS J rev.pdf

[^1_3]: https://www.ncbi.nlm.nih.gov/sites/books/n/statpearls/article-20638/

[^1_4]: https://www.pnas.org/doi/10.1073/pnas.0805662105

[^1_5]: https://bio.libretexts.org/Bookshelves/Microbiology/Microbiology_Laboratory_Manual\_(Hartline)/01:\_Labs/1.30:\_DNA_RNA_and_DNA_Replication

[^1_6]: https://en.wikipedia.org/wiki/DNA

[^1_7]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7022166/

[^1_8]: https://www.cambridge.org/core/journals/quarterly-reviews-of-biophysics/article/nucleic-acids-function-and-potential-for-abiogenesis/842529B9BDAD6E86F7919827725C1931

[^1_9]: https://elifesciences.org/articles/35255

[^1_10]: https://genesdev.cshlp.org/content/30/15/1683.full

[^1_11]: https://en.wikipedia.org/wiki/Origin_of_replication

[^1_12]: https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/rna-replication

[^1_13]: https://en.wikipedia.org/wiki/DNA_replication

[^1_14]: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/842529B9BDAD6E86F7919827725C1931/S0033583517000038a.pdf/nucleic-acids-function-and-potential-for-abiogenesis.pdf

[^1_15]: https://quizlet.com/25827119/genetics-chapter-11-flash-cards/

[^1_16]: https://quizlet.com/71334280/microbiology-chapter-7-flash-cards/

[^1_17]: https://www.vaia.com/en-us/textbooks/biology/genetics-analysis-principles-6-edition/chapter-11/problem-1-c1-what-key-structural-features-of-the-dna-molecul/

[^1_18]: https://www.nature.com/articles/s41467-025-63151-5

[^1_19]: https://www.nature.com/articles/s41467-020-18964-x

[^1_20]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3783049/

[^1_21]: https://www.sciencedirect.com/topics/neuroscience/origin-of-replication

[^1_22]: https://onlinelibrary.wiley.com/doi/abs/10.1002/9783527814527.ch13

[^1_23]: https://www.frontiersin.org/research-topics/64933/dna-replication-origins-in-microbial-genomes-volume-iii

[^1_24]: https://fse.studenttheses.ub.rug.nl/14917/1/MasterLS_MBB_2017_JGEdens.pdf

[^1_25]: https://crvscience.com/wiki/rna-replicase-ribozyme


---

## The Core Distinction

A **self-replicating** nucleic-acid molecule carries, within itself or its immediate progeny, both the information to be copied *and* the means to perform the copying. An **externally copied** molecule is a passive template: it holds sequence information but contributes no replication chemistry, so every copying step depends on enzymes, energy, primers, and substrates supplied from outside.

This is the classic template-versus-machine distinction described by von Neumann: a replicator needs both a coded representation of itself and a mechanism to read and duplicate that code. In modern molecular terms, the difference maps onto whether the molecule encodes or constitutes its own replicase.[^2_1]

______________________________________________________________________

### 1. Information-plus-catalyst vs. template-only

**Self-replicating molecule:** It either *is* a catalyst (an RNA polymerase ribozyme) or encodes one (self-amplifying RNA carrying an RNA-dependent RNA polymerase gene). The same molecule population provides the template and the polymerase activity needed to synthesize both strands and initiate new rounds.[^2_2][^2_3]

**Externally copied molecule:** It is copied only by proteins (DNA polymerase, RNA polymerase, reverse transcriptase) that the molecule itself did not produce and cannot recruit without a cell or a reconstituted in-vitro system. A plasmid, a chromosomal fragment, or a standard mRNA is inert without host machinery.[^2_4][^2_5]

### 2. Strand-completeness and directionality of synthesis

**Self-replicating:** Must synthesize *both* the complementary strand and then use that complement as a template to regenerate the original sense strand. It must also handle initiation without a pre-existing primer (or carry the means to make one), because a molecule waiting for an externally supplied primer is not self-starting.[^2_3]

**Externally copied:** DNA replication in cells always requires a primase-synthesized RNA primer and a replisome loaded at an origin by initiator proteins. Standard in-vitro copying (PCR, reverse transcription, in-vitro transcription) likewise depends on externally added primers, polymerases, and NTPs/dNTPs. The molecule supplies sequence but not chemistry.[^2_4]

### 3. Autonomy of the replication cycle

**Self-replicating:** A complete round can, in principle, proceed from molecule + monomers alone. In vitro demonstrations (e.g., the 45-nt QT45 polymerase ribozyme) show an RNA synthesizing its own complementary strand and then a copy of itself from nucleotide substrates, albeit at low yield and fidelity.[^2_2]

**Externally copied:** Each round is a discrete biochemical reaction orchestrated by an external agent. A virus is the borderline case: its genome carries replication genes, but it can express them only after infecting a cell and hijacking host ribosomes, energy, and nucleotides. Biologists therefore classify viruses as obligate intracellular parasites, not autonomous self-replicators.[^2_1]

### 4. Error threshold and evolvability

**Self-replicating:** Because the copying chemistry is part of the system, mutation rate is coupled to genome size. The copied molecule must replicate fast enough to outpace its own degradation, and accurate enough to avoid error catastrophe (the “error threshold” that limits how large a self-replicating RNA genome can be before mutations accumulate faster than selection can purge them).[^2_6][^2_3]

**Externally copied:** Fidelity is imposed by the host polymerase and its proofreading machinery. The template molecule itself bears no burden for copying accuracy, and its “survival” depends on the host cell’s maintenance, not on its own replication kinetics.

### 5. Illustrative comparison

| Feature | Self-replicating nucleic acid | Externally copied nucleic acid |
| :-- | :-- | :-- |
| Copying chemistry | Encoded by or intrinsic to the molecule (ribozyme or replicase gene) | Supplied by cell or experimenter (polymerase, primase, helicase) |
| Primer requirement | Must initiate de novo or make its own primer | Requires externally supplied primer (DNA replication) |
| Both-strand synthesis | Molecule population regenerates both + and – strands | One strand copied per reaction; strand separation needs external activity |
| Monomer/energy source | Must be available in environment; molecule does not gather them | Supplied by host cell or reaction mix |
| Autonomous cycle | Template + monomers can, in principle, yield progeny | Each round needs a new external initiation event |
| Example | RNA polymerase ribozyme (QT45); self-amplifying RNA (srRNA) | Plasmid, chromosomal DNA, standard mRNA, viral genome outside a cell |

### 6. The gray zone: “self-amplifying” RNA in cells

Self-amplifying RNA (srRNA) used in vaccine and research vectors carries an RNA replicase gene. Once delivered into a cell, the cell’s ribosomes translate the replicase, which then copies the RNA. The RNA is *genetically* self-replicating (it encodes its own copier) but *physically* dependent on the host for translation, nucleotides, energy, and compartmentalization. It is therefore self-replicating only relative to a plain mRNA, not in the absolute, origin-of-life sense of a molecule that copies itself from monomers alone.[^2_5]

______________________________________________________________________

### Bottom line

The distinguishing property is **causal closure of the replication loop**: a self-replicating nucleic acid is part of a system where template, catalyst, and product are the same molecular lineage, so the molecule can be a cause of its own copying. An externally copied nucleic acid is only a passive information carrier; it can be duplicated, but never initiates or completes a replication cycle without machinery it did not produce and does not contain.[^2_3][^2_6][^2_1][^2_2]

[^2_5][^2_6][^2_1][^2_2][^2_3][^2_4]

<span style="display:none">[^2_10][^2_11][^2_12][^2_13][^2_14][^2_15][^2_7][^2_8][^2_9]</span>

<div align="center">⁂</div>

[^2_1]: https://en.wikipedia.org/wiki/Self-replication

[^2_2]: https://www.science.org/doi/10.1126/science.adt2760

[^2_3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6120706/

[^2_4]: https://www.ncbi.nlm.nih.gov/books/NBK26850/

[^2_5]: https://rna.bocsci.com/support/what-is-self-replicating-rna.html

[^2_6]: https://www.ncbi.nlm.nih.gov/books/NBK26876/

[^2_7]: https://pubs.acs.org/doi/10.1021/ar200325v

[^2_8]: https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/self-replication

[^2_9]: https://quizlet.com/441435976/viral-genome-strategies-flash-cards/

[^2_10]: https://biologydictionary.net/nucleic-acid/

[^2_11]: https://www.pearson.com/channels/biology/study-guides/nucleic-acids-and-the-rna-world-structure

[^2_12]: https://www.reddit.com/r/evolution/comments/1r3x1eb/selfreplicating_rna_is_more_abundant_than/

[^2_13]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7022166/

[^2_14]: https://onlinelibrary.wiley.com/doi/abs/10.1002/9783527814527.ch13

[^2_15]: https://fse.studenttheses.ub.rug.nl/14917/1/MasterLS_MBB_2017_JGEdens.pdf


---

## What You Would Need to Assess Self-Replication Potential

Given only a raw DNA or RNA sequence, you cannot conclude that the molecule can self-replicate. You can only estimate the *probability* that it contains features associated with replication. A rigorous assessment would require the following categories of information:

### 1. Identity and context of the molecule

- **Molecule type:** DNA or RNA; single-stranded or double-stranded; linear or circular.
- **Length and topology:** Whether it is a fragment, plasmid, viral genome, or chromosome segment.
- **Source organism or environment:** Bacterial, archaeal, eukaryotic, viral, or synthetic. Replication signals are taxon-specific (e.g., DnaA boxes in bacteria, ARS elements in budding yeast, ORB boxes in archaea).[^3_1][^3_2]


### 2. Replication-origin signatures (DNA)

- **Initiator-binding motifs:** DnaA boxes (bacteria), ARS consensus/ACS (budding yeast), origin recognition boxes (archaea), or iterons (plasmids).[^3_2][^3_3][^3_1]
- **AT-rich unwinding element:** A stretch with elevated A·T content adjacent to initiator motifs, lowering the melting temperature for strand separation.[^3_1][^3_2]
- **Genomic neighborhood:** Proximity to replication-related genes (e.g., *dnaA*, *dnaN*, *recF* in bacteria; replication proteins in archaea).[^3_2][^3_1]
- **Compositional asymmetry:** GC-skew or AT-skew inversions (V-shaped shifts) that mark the origin/terminus in bacterial chromosomes.[^3_4][^3_1]
- **Tools:** Ori-Finder (bacteria), Ori-Finder 2 (archaea), Ori-Finder 3 (budding yeast), DoriC, Z-curve analysis.[^3_3][^3_5][^3_4][^3_2]


### 3. Replicase coding capacity (DNA or RNA)

- **Open reading frames (ORFs):** For DNA, look for genes encoding replicative or primase/polymerase proteins (DnaB helicase, DnaG primase, DNA polymerase III, RNA-dependent RNA polymerase, reverse transcriptase). For RNA (e.g., self-amplifying RNA), an ORF for an RNA replicase is the strongest genetic indicator of self-amplification potential.[^3_6]
- **ORF integrity:** Start/stop codons, frame integrity, absence of disruptive mutations. A frameshifted or truncated polymerase gene confers no replication potential.


### 4. RNA-specific features (if RNA)

- **Polymerase ribozyme motifs:** Known catalytic cores from in-vitro-evolved RNA polymerase ribozymes (e.g., R18, QT45, or the newer 45-nt polymerase ribozyme). A sequence must fold into a catalytic pocket capable of template-directed nucleotide polymerization.[^3_7][^3_8][^3_9]
- **Bipartite self-replication architecture:** Ability to copy both the “+” strand and its complementary “–” strand, regenerating the original sense strand. Copying only one strand is not self-replication.[^3_8]
- **Structure-versus-accessibility balance:** Secondary structure must be stable enough to form a catalytic core but not so stable that it blocks strand separation or primer binding.[^3_7]


### 5. Strand and end architecture

- **Telomeric repeats or circularization mechanism:** Linear DNA needs telomere-like ends or a protein-primed end-replication solution; circular DNA needs a functional origin and, often, a partitioning system.
- **Primer independence or self-priming:** DNA polymerases cannot start de novo. A self-replicating DNA molecule must either encode a primase or rely on a mechanism (e.g., protein priming, rolling-circle hairpin resolution) that does not require an externally supplied primer.[^3_4]


### 6. Environmental and cellular context (not in the sequence)

- **Host machinery:** Even a perfect bacterial *oriC* is inert without DnaA, DnaB, DnaG, DNA polymerase III, sliding clamp, SSB, and nucleotide pools. A self-amplifying RNA needs host ribosomes to translate its replicase, plus NTPs and a compatible ionic environment.[^3_6][^3_8]
- **Compartmentalization:** Membrane or protocell boundaries that retain monomers and products.[^3_10]
- **Growth conditions:** Temperature, pH, Mg²⁺ concentration, and redox state affect ribozyme folding and polymerase activity.[^3_10]

______________________________________________________________________

### What Can Be Inferred from Sequence Alone

| Inferable from sequence | Confidence / caveat |
| :-- | :-- |
| Presence of candidate initiator-binding motifs (DnaA boxes, ACS, ORBs) | Moderate; motifs are short and occur by chance |
| AT-rich unwinding regions | Moderate; base composition is directly readable |
| GC/AT skew inversions (chromosome-scale) | Moderate; approximate, can mispredict |
| Intact ORFs for known replication proteins | High for gene presence; does not prove expression or function |
| Candidate RNA polymerase ribozyme folds | Low to moderate; requires RNA folding prediction and comparison to known ribozymes; most random RNAs will not catalyze polymerization |
| Homology to known origins (BLAST/DoriC match) | Moderate; sequence similarity suggests but does not confirm activity [^3_11] |

### What Cannot Be Inferred from Sequence Alone

- **Whether the origin actually fires.** Origin activity in eukaryotes is strongly modulated by chromatin state, cell type, and developmental stage; identical sequences can be active in one cell type and silent in another.[^3_4]
- **Whether a polymerase gene is expressed.** Sequence says nothing about promoters, transcription, translation, or protein stability.
- **Whether a ribozyme is catalytically active.** Folding in silico does not demonstrate metal-ion binding, NTP polymerization, or strand displacement.
- **Whether replication is processive and faithful.** Error rate, speed, and the ability to complete both strands of a cycle are functional properties, not sequence properties.
- **Whether the molecule can obtain monomers and energy.** Nucleotide supply and compartmentalization are environmental.[^3_10]
- **Whether a circular plasmid is stably maintained.** Partitioning and copy-number control require trans-acting factors not encoded in the minimal origin sequence alone.


### Bottom line

From sequence alone you can compute a **candidate score**: motif matches, AT-richness, skew inversions, ORF integrity, and ribozyme-like folds. But you cannot determine self-replication potential definitively. The sequence tells you what *might* be there; only biochemical and genetic experiments (origin activity assays, polymerase activity measurements, plaque or transformation assays, replication-intermediate detection) can confirm that the molecule can initiate and complete a copying cycle without externally supplied replication machinery.[^3_11][^3_8][^3_4]

[^3_5][^3_9][^3_3][^3_8][^3_11][^3_1][^3_2][^3_6][^3_7][^3_4][^3_10]

<span style="display:none">[^3_12][^3_13][^3_14][^3_15][^3_16][^3_17]</span>

<div align="center">⁂</div>

[^3_1]: https://pmc.ncbi.nlm.nih.gov/articles/PMC506792/

[^3_2]: https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2014.00482/full

[^3_3]: https://ngdc.cncb.ac.cn/databasecommons/database/id/7062

[^3_4]: https://academic.oup.com/bib/article/27/3/bbag315/8711649

[^3_5]: https://arxiv.org/html/1909.13751v1

[^3_6]: https://rna.bocsci.com/support/what-is-self-replicating-rna.html

[^3_7]: https://pubmed.ncbi.nlm.nih.gov/12573693/

[^3_8]: https://mrclmb.ac.uk/news-events/articles/bridging-the-gap-from-chemistry-to-life-discovery-of-a-tiny-rna-that-can-copy-itself/

[^3_9]: https://www2.mrc-lmb.cam.ac.uk/groups/ph1/rna_self.html

[^3_10]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6120706/

[^3_11]: https://tubic.org/doric/tutorial/

[^3_12]: https://pubmed.ncbi.nlm.nih.gov/33962169/

[^3_13]: https://bartellab.wi.mit.edu/publication_reprints/Lawrence\&Bartel%20RNA_05.pdf

[^3_14]: https://creation.com/en/articles/rna-self-replication-and-abiogenesis

[^3_15]: https://www.nature.com/articles/s41467-025-63151-5

[^3_16]: https://onlinelibrary.wiley.com/doi/abs/10.1002/9783527814527.ch13

[^3_17]: https://www.reddit.com/r/evolution/comments/1r3x1eb/selfreplicating_rna_is_more_abundant_than/


---

## Three Classes of Nucleic-Acid Replication Behavior

Nucleic-acid molecules can be sorted by where the **initiation decision** and the **replication chemistry** come from. The distinction is not binary—most natural systems are hybrids—but it is useful for thinking about vectors, viruses, transposons, and synthetic constructs.

### 1. Autonomous self-replication

**Definition:** The molecule contains or encodes the signals that decide *when* and *where* replication starts, and—at minimum—the initiator function that recognizes those signals. Once triggered, the molecule can launch a copying cycle without relying on the host’s chromosomal origin-firing program.

**What it provides:** A replication origin (*ori*) plus a replication initiator (Rep protein, DnaA-like protein, or an RNA replicase). The initiator binds the origin, melts or nicks the duplex, and recruits the elongation machinery.

**What it still needs from the host:** Even an autonomous replicon is not chemically self-sufficient. It borrows the host’s DNA polymerases, helicases, primases, sliding clamps, SSB, topoisomerases, and nucleotide pools. Autonomy refers to **control of initiation**, not to synthesizing every enzyme from scratch.

**Examples:**

- Bacterial plasmids with a plasmid-encoded Rep protein and *oriV* (e.g., ColE1, R1, pT181). Initiation is plasmid-specific, though elongation uses host replisome components. [^4_1][^4_2]
- ICE*Bs1*, an integrative conjugative element that, when induced, excises and replicates autonomously by a plasmid-like rolling-circle mechanism using its own relaxase NicK and origin *oriT*, while borrowing host PolC, DnaN, and PcrA helicase. [^4_3]
- Eukaryotic episomal vectors (e.g., EBV-based oriP plasmids) that use the viral EBNA-1 protein to tether and replicate independently of the chromosome.

**Key property:** The molecule can be introduced into a compatible host and maintain itself as an extrachromosomal replicon, segregating to daughter cells without integrating into the host genome.

### 2. Replication dependent on external enzymes (dependent replication)

**Definition:** The molecule is copied only when external proteins recognize and act on it. The molecule supplies the template and sequence information, but contributes no replication initiator and no origin that can fire on its own. Every round of copying is launched by machinery encoded elsewhere.

**Subtypes:**


| Subtype | Mechanism | Example |
| :-- | :-- | :-- |
| **Host-dependent replicon** | Integrated element copied only as part of the host chromosome; initiation uses the host’s origin and initiator (DnaA/ORC). | ICEs in their integrated state replicate passively with the chromosome; only upon induction do some switch to autonomous plasmid-like replication. [^4_3] |
| **Parasitic/dependent virus** | Viral genome carries replication genes but cannot express them without infecting a cell and hijacking host ribosomes, energy, and nucleotides. | Most DNA and RNA viruses outside a cell are inert; inside a cell they become dependent on host translation and metabolic machinery. |
| **Viroid-like RNA** | Naked circular RNA that encodes no protein at all; copied entirely by host DNA-dependent RNA polymerase (often redirected to RNA templates) and host RNA-processing enzymes. | Plant viroids replicate in the nucleus or chloroplast using host polymerases; the RNA is a pure template with ribozymatic self-cleavage only. [^4_4] |
| **Non-replicating vector / synthetic nucleic acid** | Oligonucleotide, siRNA, antisense oligo, or standard mRNA lacking any origin or replicase gene. It may be transcribed or translated in a cell, but the molecule itself is never duplicated. | Non-replicating mRNA vaccines; synthetic oligonucleotides that “can neither replicate nor generate nucleic acids that can replicate in any living cell.” [^4_5] |

**Key property:** The molecule is a **passive substrate**. Copying occurs only when an external agent (host replisase, viral polymerase delivered in trans, or an in-vitro enzyme mix) acts on it. If that agent is removed, the molecule produces zero progeny.

### 3. Non-replicating nucleic-acid molecules

**Definition:** Molecules that are never copied as nucleic acids. They may be transcribed into RNA, translated into protein, degraded, or used as hybridization probes, but they do not generate daughter nucleic-acid molecules.

**What distinguishes them:** No origin of replication, no replicase gene, no primer mechanism, and no pathway to make a complementary copy of themselves. They are chemically stable or unstable, but replication-incompetent by design or by sequence.

**Examples:**

- Standard (non-self-amplifying) mRNA: translated into protein, but not copied. [^4_6]
- siRNA, antisense oligonucleotides, aptamers: functional as binding or silencing agents, not templates for their own duplication. [^4_5]
- Linearized plasmid DNA without an *ori*: can be transfected and transiently expressed, but is lost as cells divide because it cannot replicate or segregate.
- Non-replicating viral vectors: genetically modified so that essential replication genes are deleted; they can deliver a payload once but cannot spread or amplify. [^4_6]

______________________________________________________________________

### Comparison table

| Feature | Autonomous self-replication | Dependent (external-enzyme) replication | Non-replicating |
| :-- | :-- | :-- | :-- |
| **Initiation signal** | Molecule-encoded origin + initiator | Host or externally supplied origin/initiation machinery | None |
| **Decision to replicate** | Molecule-controlled (within host constraints) | Externally controlled | Never |
| **Copying chemistry** | Borrowed from host, but recruited by the molecule | Entirely external | Not applicable |
| **Can maintain itself without integration?** | Yes, as an extrachromosomal replicon | No (must integrate or be re-introduced each round) | N/A |
| **Progeny nucleic acid produced?** | Yes, multiple copies per host generation | Yes, but only when external machinery acts | No |
| **Typical examples** | Plasmids with Rep/ori, ICE*Bs1* (induced), oriP episomes | Integrated ICEs, viroids, most viruses inside cells, PCR products | mRNA, siRNA, oligos, non-replicating viral vectors |

### The crucial nuance: autonomy is about initiation, not self-sufficiency

A plasmid that replicates “autonomously” still requires the host’s DNA polymerase III, helicase, primase, and dNTPs. It is autonomous only in the sense that it carries its own **origin and initiator**, so it does not need to wait for the host chromosome to fire. Conversely, a “dependent” molecule like a viroid uses host polymerases exclusively, but its circular RNA structure and ribozyme self-cleavage give it some sequence-encoded control over how it is processed.

**Bottom line:** The three categories answer different questions.

- **Autonomous:** Does the molecule carry the switch that turns on its own copying?
- **Dependent:** Is the molecule copied only because something else acts on it?
- **Non-replicating:** Is the molecule never copied as a nucleic acid at all?

[^4_3] [^4_5] [^4_1] [^4_2] [^4_4] [^4_6]

<span style="display:none">[^4_10][^4_11][^4_12][^4_13][^4_14][^4_15][^4_7][^4_8][^4_9]</span>

<div align="center">⁂</div>

[^4_1]: https://journals.asm.org/doi/full/10.1128/mmbr.62.2.434-464.1998

[^4_2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC13149292/

[^4_3]: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2905045/

[^4_4]: https://en.wikipedia.org/wiki/RNA

[^4_5]: https://osp.od.nih.gov/wp-content/uploads/NIH_Guidelines.pdf

[^4_6]: https://www.news-medical.net/health/What-is-a-Non-Replicating-Vaccine.aspx

[^4_7]: https://www.britannica.com/science/nucleic-acid

[^4_8]: https://www.merriam-webster.com/medical/nonreplicating

[^4_9]: https://journals.asm.org/doi/10.1128/mmbr.00222-20

[^4_10]: https://www.sciencedirect.com/org/science/article/pii/S2379504219002984

[^4_11]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4379921/

[^4_12]: https://pmc.ncbi.nlm.nih.gov/articles/PMC115368/

[^4_13]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6822018/

[^4_14]: https://en.wikipedia.org/wiki/Nucleic_acid

[^4_15]: https://biologynotesonline.com/plasmid-replication/


---

## Evidence Required to Establish Genuine Self-Replication

To claim that a DNA or RNA molecule is **genuinely self-replicating**, an experiment must show that the molecule is a **cause of its own copying**, not merely a substrate that gets copied by something else. The minimal logical requirement is **closure of the replication loop**: the molecule (or its direct progeny) must supply the function that enables the next round of synthesis, so that template → catalyst/product → template repeats without a fresh external initiation event each cycle.

Below is the hierarchy of evidence, from minimal to definitive.

______________________________________________________________________

### 1. Minimal evidence: autocatalytic production of identical or near-identical molecules

You must demonstrate that starting from a defined molecule (or a small defined set of fragments), the reaction yields more of that same molecule—and that the yield depends on the molecule itself being present and active.

**Required observations:**

- **Time-course accumulation** of the target molecule above the starting amount, following a growth curve (linear, exponential, or logistic) rather than a single-shot conversion. In the Tracey–Lincoln–Joyce cross-replicating RNA system, two RNA enzymes catalyzed each other's synthesis from four substrates and sustained >10⁸-fold amplification over ~28 doublings for 30 hours.[^5_1]
- **Exponential or sigmoidal kinetics** consistent with replication (each copy can make another), rather than a one-time stoichiometric reaction. Real-time fluorescence detection of the Joyce self-replicating RNA ligase showed sigmoidal growth with a doubling time of ~1.1 h.[^5_2]
- **Serial transfer / serial dilution**: the activity persists after the original template is diluted away or removed, proving the product is itself a replicator. The Joyce system was maintained by serial transfer, and the Holliger group emphasized that continued replication requires the product to remain active.[^5_3][^5_1]

**Not sufficient by itself:** A single round of copying (e.g., one RNA makes one complement and stops) is **copying**, not replication. Even two or three rounds without serial transfer could be residual carryover of an enzyme or primer.

______________________________________________________________________

### 2. Both-strand synthesis and strand separation

For a nucleic acid to replicate, it must regenerate **both strands** of its duplex (the “+” and “–” strands) and release them so each can serve as a template again. A molecule that only makes a complementary strand, or that remains trapped in a stable duplex, has not replicated.

**Required observations:**

- Detection of both sense and antisense strands (e.g., by strand-specific RT-qPCR, northern blot with strand-specific probes, or sequencing). The Holliger air-water-interface study demonstrated sense-and-antisense RNA replication followed by strand dissociation.[^5_4]
- Evidence that strands separate after synthesis (thermal cycling, pH shift, or helicase/ribozyme activity), so the products are available for the next round. Duplex stability is a well-known bottleneck: thermodynamic trapping of product duplexes has prevented many ribozyme systems from achieving sustained replication.[^5_4]

______________________________________________________________________

### 3. Autocatalysis / molecular closure (the critical distinction from “copying”)

This is the strongest evidence that replication is **genuine**. The molecule must participate in producing its own successor. There are two architectures:

- **Direct self-copying:** An RNA polymerase ribozyme uses itself as a template and synthesizes its own sequence from monomers. (Complete, unaided self-copying of a folded ribozyme has not yet been achieved; this remains a major milestone. )[^5_5]
- **Fragment assembly / cross-replication:** The molecule catalyzes the joining of fragments to form another copy of itself (e.g., the Joyce RNA ligase, the Azoarcus group-I intron self-reproducing ribozyme, or the newer 45-nt QT45 polymerase ribozyme reported in 2026).[^5_6][^5_7][^5_1]

**Key control:** Remove or inactivate the candidate molecule and show that replication stops. Mutate the catalytic core and show loss of activity while the sequence remains otherwise intact. This distinguishes **molecule-driven** replication from contamination by an external enzyme.

______________________________________________________________________

### 4. Heritability and evolution (replication with information transfer)

Genuine replication propagates information, not just mass. If mutations arise during copying and those mutations are inherited by progeny—and if those progeny can be selected—the system is behaving like a genetic replicator.

**Required observations:**

- **Mutation inheritance:** Sequence progeny after several rounds and show that changes introduced during replication are passed on.
- **Demonstrated evolution:** Under selection pressure (e.g., ligand dependence, serial transfer at limiting substrate), the population changes in a direction consistent with Darwinian dynamics. The Spiegelman and TcRR systems showed mutation and inheritance, though the TcRR system required compartmentalization (emulsions) to sustain evolution beyond ~17 rounds.[^5_3][^5_5]

Without heritability, you may have chemical growth or crystal-like autocatalysis, but not nucleic-acid **replication** in the biological sense.

______________________________________________________________________

### 5. Distinguishing genuine replication from simple copying or amplification

| Observation | Simple copying / amplification | Genuine self-replication |
| :-- | :-- | :-- |
| **Stoichiometry** | One template → one (or a fixed number of) copy; reaction stops when enzyme/substrate is exhausted | Template → product → product can template the next round; cycle continues |
| **Dependence on original molecule** | Adding fresh external polymerase/primase restarts copying; the original template is required every time | The molecule's own activity (ribozyme, replicase gene, or self-ligating structure) drives subsequent rounds |
| **Kinetics** | Linear or single-exponential burst, then plateau | Sigmoidal or sustained exponential growth over serial transfers |
| **Strand products** | Only one strand synthesized; products remain duplexed | Both strands synthesized and separated; each can re-enter the cycle |
| **Sequence of progeny** | Exact copy of input, but no information about copying fidelity | Mutations observed and inherited; error rate measured |
| **Effect of catalyst removal** | Reaction stops if external enzyme is removed | Reaction continues as long as the replicator and monomers are present |
| **Serial transfer** | Activity lost after dilution of the original template | Activity persists after dilution because progeny are themselves replicators |

**Example of the distinction:** PCR is massive amplification, but it is **not self-replication**. Each cycle requires externally added thermostable polymerase, primers, and thermal cycling; the amplicon does not recruit or synthesize the polymerase for the next cycle. By contrast, the cross-replicating RNA enzymes of Joyce et al. catalyzed each other's synthesis from four substrates without added protein, and the population sustained itself through serial transfer.[^5_1]

______________________________________________________________________

### 6. Negative controls required to rule out artifacts

To rule out that an external enzyme or contaminant is doing the copying, you need:

- **No-template control:** Monomers and buffer without the candidate molecule—should show no product.
- **Catalytically dead mutant:** Same sequence with the active site disrupted—should not replicate.
- **RNase/DNase or protease treatment:** If activity disappears after nuclease treatment but is unaffected by protease (for RNA systems), the catalyst is nucleic-acid-based.
- **Fractionation / purification:** Show that the active fraction co-purifies with the candidate RNA and not with a co-purifying protein.
- **Substrate-only controls:** Confirm that the building blocks (NTPs, triplet substrates, or oligonucleotide fragments) do not spontaneously polymerize under the reaction conditions.

______________________________________________________________________

### 7. Definitive standard

The strongest claim would combine all of the above:

1. The molecule (or its encoded ribozyme/replicase) synthesizes both strands from monomers or defined fragments.
2. Products are strand-separated and capable of templating the next round.
3. Growth persists through multiple serial transfers after the original input is diluted beyond detection.
4. Kinetics are exponential (or at least autocatalytic), with a measurable doubling time.
5. Progeny sequences are faithful enough to be identifiable as copies, yet mutable, and mutations are heritable.
6. Catalytic-dead mutants and no-molecule controls are negative.

No existing natural or synthetic system meets all of these criteria perfectly for a long RNA genome; the closest demonstrations are short ribozymes that self-reproduce from fragments, cross-replicating RNA enzyme pairs, and RNA polymerase ribozymes that copy templates (including partial copies of themselves) but do not yet achieve complete, autonomous, high-fidelity self-replication of their full length.[^5_5][^5_6][^5_1][^5_4]

**Bottom line:** Simple copying is a one-way reaction (template → product). Genuine self-replication is a cycle in which the product becomes the next template, and the molecule itself is required to keep the cycle going. The evidence must therefore show **molecule-dependent, multi-round, heritable copying**, not merely the accumulation of copies in a single reaction tube.

[^5_7][^5_2][^5_6][^5_1][^5_3][^5_4][^5_5]

<span style="display:none">[^5_10][^5_11][^5_12][^5_13][^5_14][^5_15][^5_8][^5_9]</span>

<div align="center">⁂</div>

[^5_1]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2652413/

[^5_2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5108293/

[^5_3]: https://mrclmb.ac.uk/news-events/articles/how-the-earliest-life-on-earth-may-have-replicated-itself/

[^5_4]: https://www.nature.com/articles/s41467-023-37206-4

[^5_5]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5041002/

[^5_6]: https://www.science.org/doi/10.1126/science.adt2760

[^5_7]: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8320737/

[^5_8]: https://resolve.cambridge.org/core/services/aop-cambridge-core/content/view/6A5751130DE0264C4F017AAC73DB1FF6/9780511817540c7_p129-154_CBO.pdf/self-replication-and-self-reproduction.pdf

[^5_9]: https://www.caltech.edu/about/news/researchers-demonstrate-possible-primitive-mechanism-chemical-info-self-replication-4201

[^5_10]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12373953/

[^5_11]: https://pubs.rsc.org/cc/article/57/61/7517/717319/RNA-diversification-by-a-self-reproducing-ribozyme

[^5_12]: https://scienceandculture.com/2021/04/experiments-on-self-replicating-rna-indicate-the-need-for-intelligent-agency-in-lifes-origin/

[^5_13]: https://www.nature.com/articles/s41467-025-63151-5

[^5_14]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6120706/

[^5_15]: https://en.wikipedia.org/wiki/Self-replication

