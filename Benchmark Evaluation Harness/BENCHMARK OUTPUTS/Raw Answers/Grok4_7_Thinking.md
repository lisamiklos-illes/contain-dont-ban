<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Question 1 — Replication-associated features

What sequence-level features of DNA or RNA are associated with the ability of a nucleic-acid molecule to participate in self-replication? Explain the biological relevance of these features.

A nucleic acid participates in self-replication when its sequence can be read as a template and, in cellular or viral systems, can also recruit the machinery that copies it. The sequence does not copy itself unaided. It supplies complementarity, meltability, accessibility, and recognition sites that make templated copying possible.

## Complementarity and polarity

The core sequence feature is Watson–Crick complementarity. Adenine specifies thymine in DNA or uracil in RNA, and guanine specifies cytosine. In RNA, G–U wobble pairs are also allowed. Because each strand stores the information needed to rebuild the other, one strand can direct synthesis of its complement, and that complement can regenerate the original. That is the basis of semiconservative replication [^1_1][^1_2].

Strands are directional, with a 5′ and a 3′ end, and known polymerases add nucleotides only to a 3′-OH. A molecule therefore needs a sequence region that can anneal a primer, or a folded end that can act as one. Without that paired 3′ end, ordinary polymerases cannot start a new chain [^1_3][^1_4].

## Sequences that open and start copying

Double-stranded DNA must be locally unwound before it can be copied. Origins are enriched in A–T base pairs, which are held by two hydrogen bonds rather than three and stack less tightly than G–C pairs. That AT-rich DNA unwinding element (DUE) is where the helix first melts [^1_5][^1_6][^1_7].

Opening is not just bulk AT content. Functional origins also contain repeated motifs whose sequence, length, spacing, and orientation matter:

- Bacterial origins use DnaA boxes plus an AT-rich DUE, often with repeated 13-mers [^1_6][^1_8].
- Plasmid origins use iterons and related repeats that position the initiator and help load helicase [^1_6][^1_9].
- Budding-yeast origins use an essential ARS consensus sequence plus nearby B elements [^1_10][^1_8].

These motifs matter because they place initiator proteins so that torsional stress is focused on the easily melted region. In many eukaryotes, origins are less sequence-specific, but AT richness, CpG islands, and structural motifs such as G-quadruplexes are still associated with origin activity [^1_11][^1_8].

Linear chromosomes add another sequence requirement at the ends. Telomeric repeats, such as TTAGGG in humans, give telomerase a template so the lagging-strand end can be extended rather than shortened each cycle [^1_5].

## Template accessibility

A sequence is a poor replication participant if it folds into a stable structure over the region being copied. Hairpins, long stems, and G-quadruplexes block primer annealing and stall polymerases or nonenzymatic copying [^1_2][^1_12]. Shorter strands, roughly under 30 nucleotides, separate from their products more readily and are easier to copy than long, structured templates [^1_2].

This creates the central constraint on RNA self-replication. A ribozyme needs a stable fold to catalyze copying, but a good template needs to stay unfolded. G–U wobble pairing is one sequence solution: it can stabilize a folded catalyst more than it stabilizes the template duplex that must later be copied [^1_12]. Another solution is fragmentation. The replicase is copied as short, weakly structured pieces and reassembled afterward, so catalytic structure and template accessibility do not have to coexist in one long strand [^1_2][^1_13].

For nonenzymatic copying, helical geometry matters as well. A-form geometry, typical of RNA, supports template-directed polymerization better than B-form DNA [^1_14]. Composition also matters: copying of A/U-rich RNA has historically been much less efficient than copying of G/C-rich sequence, although mixed oligonucleotide substrates can reduce that bias [^1_15].

## Recognition by a replicase

Some molecules replicate only because their sequence is a specific substrate for a polymerase. Qβ bacteriophage RNA is copied by Qβ replicase and is a poor substrate for unrelated replicases. Under selection for speed in a test tube, that RNA loses coat and other genes and shrinks to a few hundred nucleotides that still bind the replicase and get copied efficiently. Those residual recognition sequences, not protein-coding capacity, are what let it keep participating in replication [^1_16][^1_17].

An RNA that itself encodes or folds into a polymerase has a further sequence requirement: a catalytic core plus a site that binds primer and template, while the same sequence, or its complement, must remain copyable. No simple sequence motif guarantees that dual role. It is a selected fold that must also survive the template-accessibility constraint above [^1_2][^1_12][^1_18].

## What these features are for

| Sequence feature | What it enables | Why it matters |
| :-- | :-- | :-- |
| Complementary bases and 5′–3′ polarity | Template-directed synthesis from a primer 3′-OH | Information can be copied rather than invented each generation [^1_1] |
| AT-rich unwinding element | Local helix opening | Initiation requires single-stranded template [^1_6][^1_7] |
| Initiator motifs (DnaA boxes, ARS, iterons) | Recruitment and once-per-cycle firing | Copies the genome at the right place and time [^1_8] |
| Low stable secondary structure | Polymerase or monomer access | Structured templates stall copying [^1_12] |
| Replicase-binding sites | Specific amplification | Explains why some RNAs replicate and others do not [^1_17] |
| Telomeric repeats | End extension on linear DNA | Prevents terminal sequence loss [^1_5] |

In short, self-replication depends on a sequence that can specify its complement, be opened and kept accessible, present a primer junction, and, in evolved systems, be recognized by the replicase that copies it.

<span style="display:none">[^1_19][^1_20][^1_21][^1_22][^1_23][^1_24][^1_25][^1_26][^1_27][^1_28][^1_29][^1_30][^1_31][^1_32][^1_33][^1_34][^1_35][^1_36][^1_37][^1_38][^1_39][^1_40]</span>

<div align="center">⁂</div>

[^1_1]: https://en.wikipedia.org/wiki/DNA

[^1_2]: https://www.cambridge.org/core/journals/quarterly-reviews-of-biophysics/article/nucleic-acids-function-and-potential-for-abiogenesis/842529B9BDAD6E86F7919827725C1931

[^1_3]: https://en.wikipedia.org/wiki/DNA_replication

[^1_4]: https://bartellab.wi.mit.edu/publication_reprints/Lawrence_Biochem03.pdf

[^1_5]: https://www.ncbi.nlm.nih.gov/sites/books/n/statpearls/article-20638/

[^1_6]: https://academic.oup.com/femsre/article/36/2/408/565738

[^1_7]: https://en.wikipedia.org/wiki/Origin_of_replication

[^1_8]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6742236/

[^1_9]: https://www.pnas.org/doi/10.1073/pnas.0805662105

[^1_10]: https://www.nature.com/articles/s41467-020-18964-x

[^1_11]: https://genesdev.cshlp.org/content/30/15/1683.full

[^1_12]: https://labs.chem.ucsb.edu/chen/irene/Chen_lab_at_UCSB/Publications_files/art%253A10.1007%252Fs00239-013-9584-x.pdf

[^1_13]: https://onlinelibrary.wiley.com/doi/full/10.1002/anie.202417370

[^1_14]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2759813/

[^1_15]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11662926/

[^1_16]: https://profiles.nlm.nih.gov/spotlight/px/feature/monster

[^1_17]: https://en.wikipedia.org/wiki/Spiegelman's_Monster

[^1_18]: https://crvscience.com/wiki/rna-replicase-ribozyme

[^1_19]: https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/rna-replication

[^1_20]: https://bio.libretexts.org/Bookshelves/Microbiology/Microbiology_Laboratory_Manual\_(Hartline)/01:\_Labs/1.30:\_DNA_RNA_and_DNA_Replication

[^1_21]: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/842529B9BDAD6E86F7919827725C1931/S0033583517000038a.pdf/nucleic-acids-function-and-potential-for-abiogenesis.pdf

[^1_22]: https://quizlet.com/25827119/genetics-chapter-11-flash-cards/

[^1_23]: https://quizlet.com/71334280/microbiology-chapter-7-flash-cards/

[^1_24]: https://www.vaia.com/en-us/textbooks/biology/genetics-analysis-principles-6-edition/chapter-11/problem-1-c1-what-key-structural-features-of-the-dna-molecul/

[^1_25]: https://blog.addgene.org/plasmid-101-origin-of-replication

[^1_26]: https://www.sciencedirect.com/topics/neuroscience/origin-of-replication

[^1_27]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8794818/

[^1_28]: https://www.mi.fu-berlin.de/wiki/pub/ABI/RnaAnalysis/rna.pdf

[^1_29]: https://med.stanford.edu/glennlab/research-1/rnastructure.html

[^1_30]: https://bio.libretexts.org/Bookshelves/Computational_Biology/Book:_Computational_Biology_-_Genomes_Networks_and_Evolution_(Kellis_et_al.)/10:\_RNA_Folding/10.04:\_RNA_Structure

[^1_31]: http://rcn.montana.edu/Publications/Pdf/2005/FEBS J rev.pdf

[^1_32]: https://rna.bocsci.com/support/what-is-self-replicating-rna.html

[^1_33]: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6003772/

[^1_34]: https://www.cell.com/article/S1074-5521(03)00003-6/pdf

[^1_35]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7337528/

[^1_36]: https://www.biorxiv.org/content/10.1101/2020.02.18.955120v1.full.pdf

[^1_37]: https://nccr-rna-and-disease.ch/news/newsletter/no-1/looking-back-50-years-ago

[^1_38]: https://www.quantamagazine.org/in-test-tubes-rna-molecules-evolve-into-a-tiny-ecosystem-20220505/

[^1_39]: https://www.mdpi.com/2075-1729/16/2/219

[^1_40]: https://cbe.uqam.ca/Papers/Oliver_2019.pdf


---

# Question 2 — Requirements for self-replication

What distinguishes a nucleic-acid molecule that can self-replicate from one that can only be copied using externally supplied biological machinery?

The distinction is functional closure, not a special sequence motif. A molecule that can only be copied is a template for an outside catalyst. A self-replicating nucleic acid is, or mutually produces, the catalyst that copies its own sequence.

## What external copying requires

Any complementary DNA or RNA can be copied if a polymerase, a primer, nucleotides, and usually helicase and strand-separation conditions are supplied. The nucleic acid contributes sequence information and, in cells or viruses, recognition sites such as an origin or a replicase-binding motif. Those sites recruit machinery. They do not replace it.

Qβ RNA and its shortened laboratory descendants are the clear example. They are preferred substrates for Qβ replicase, but the replicase protein is added from outside. Remove that protein and replication stops, even if the recognition sequence is intact. PCR templates, plasmids, and cellular genomes are the same kind of object at a larger scale: the genome may encode polymerases, but a naked nucleic acid cannot express or use those genes without ribosomes and the rest of the cell. Supplying a transcriptase and monomers and then copying a strand is assisted replication, not self-replication.[^2_1][^2_2]

## What self-replication adds

Self-replication requires that the informational polymer also supply the activity that builds the next copy, and that the product include another functional copy of that activity. For an RNA-world-style replicator, that means an RNA-dependent RNA polymerase activity that copies both itself and its complement, from simpler substrates, fast and accurately enough for the copies to outpace decay and support exponential growth.[^2_3][^2_4][^2_5][^2_1]

Three requirements separate that system from a template:

- The catalyst is a nucleic acid in the system, not an externally supplied protein or host enzyme.
- The product regenerates that catalyst, either as a direct copy or through a cross-replicating partner. Copying some unrelated sequence is not enough.
- Strand separation and sufficient fidelity let the new copies act again. A duplex that never opens, or a copy too error-ridden to remain catalytic, does not sustain replication.[^2_4][^2_5]

Von Neumann’s split is the same idea in engineering language. A replicator needs a description and a constructor that can copy that description. A gene is only the description. A polymerase that cannot copy the sequence encoding itself is only a constructor.

## Borderline systems

| System | Catalyst | What is copied | Still external |
| :-- | :-- | :-- | :-- |
| Genomic DNA, PCR template, plasmid | Protein polymerase | The nucleic acid | Polymerase, primers, and usually a cell or reagent mix |
| Qβ RNA and Spiegelman-type RNAs | Qβ replicase protein | RNAs that bind that replicase | The protein enzyme |
| Self-amplifying viral RNA | Encoded protein replicase | The RNA genome | Host translation machinery to make the protein |
| Cross-replicating ligase ribozymes | Two RNAs that build each other | The ribozymes themselves | Preformed oligonucleotide substrates, not free NTPs [^2_6] |
| Polymerase ribozymes | The RNA itself | Other RNAs, and in the latest cases its own sequence | Sustained, general self-copying from NTPs is still limited [^2_7][^2_5][^2_8] |

The ligase systems show the logical difference cleanly. Two RNA enzymes assemble each other from four oligonucleotides, amplify exponentially, and do so with no protein present. They are self-replicating only within that substrate pool. They cannot invent new sequence from single nucleotides, so their evolutionary range is narrow.[^2_5][^2_6][^2_7]

Polymerase ribozymes close more of the chemical gap because they add NTPs one at a time. Some can amplify short RNAs or synthesize a functional ancestor, and a recent small polymerase ribozyme can synthesize itself and the strand that encodes it. The remaining bar for a fully autonomous replicator is sustained, accurate copying of both itself and its complement, in yields that grow exponentially, without a protein polymerase and without a curated set of long oligonucleotide substrates.[^2_7][^2_8][^2_4][^2_5]

So the practical test is simple. Remove every externally supplied polymerase, ribosome, and host protein, and leave only the nucleic acid plus small-molecule substrates. If functional copies continue to appear and themselves catalyze further copying, the molecule is participating in self-replication. If copying stops, it was only a template.

<span style="display:none">[^2_10][^2_11][^2_12][^2_13][^2_14][^2_15][^2_16][^2_17][^2_18][^2_19][^2_20][^2_21][^2_22][^2_23][^2_24][^2_25][^2_26][^2_27][^2_28][^2_29][^2_9]</span>

<div align="center">⁂</div>

[^2_1]: https://link.springer.com/rwe/10.1007/978-3-642-11274-4_1423

[^2_2]: https://en.wikipedia.org/wiki/Self-replication

[^2_3]: https://www.nature.com/articles/s41570-020-0196-x

[^2_4]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6120706/

[^2_5]: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7022166/

[^2_6]: https://pubmed.ncbi.nlm.nih.gov/19131595/

[^2_7]: https://www.pnas.org/doi/10.1073/pnas.1610103113

[^2_8]: https://www.science.org/doi/pdf/10.1126/science.adt2760

[^2_9]: https://pubs.acs.org/doi/10.1021/acs.biochem.3c00091

[^2_10]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4979536/

[^2_11]: https://www.sciencedirect.com/science/article/pii/S1074552103000036

[^2_12]: https://arstechnica.com/science/2026/02/researchers-find-small-rnas-that-can-make-copies-of-themselves/

[^2_13]: https://www.scripps.edu/newsandviews/e_20141103/joyce.html

[^2_14]: https://en.wikipedia.org/wiki/RNA-dependent_RNA_polymerase

[^2_15]: https://sciencevivid.com/transcription-vs-replication-differences-rna-polymerase-structure-and-transcription-termination-mechanisms/

[^2_16]: https://joyce.salk.edu/research/

[^2_17]: http://www.molecularassembler.com/KSRM/4.1.htm

[^2_18]: https://scienceandculture.com/2023/05/long-story-short-debunks-another-tall-tale-of-self-replication/

[^2_19]: https://www.pnas.org/doi/10.1073/pnas.1914282117

[^2_20]: https://pubs.acs.org/doi/10.1021/jacs.9b10796

[^2_21]: https://fab.cba.mit.edu/classes/865.18/replication/Sipper.pdf

[^2_22]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5496545/

[^2_23]: https://www.salk.edu/scientist/gerald-joyce/publications/

[^2_24]: https://pmc.ncbi.nlm.nih.gov/articles/PMC13684603/

[^2_25]: https://www.sciencedirect.com/science/article/pii/S1074552113004262

[^2_26]: https://onlinelibrary.wiley.com/doi/abs/10.1002/9783527814527.ch13

[^2_27]: https://www.sciencedaily.com/releases/2009/01/090109173205.htm

[^2_28]: http://www.sciencedaily.com/releases/2024/03/240304195250.htm

[^2_29]: https://rna.bocsci.com/support/what-is-self-replicating-rna.html


---

# Question 3 — Replication potential

Given a DNA or RNA sequence, what information would you need to determine whether it has self-replication potential? Explain what can and cannot be inferred from the sequence alone.

Sequence alone can rank candidates. It cannot establish self-replication potential. That judgment needs the chemical form of the molecule, the substrates and catalyst available, both strands, and a measured cycle in which functional copies appear and copy again.

## Decide which claim is being tested

“Self-replication potential” covers four different bars, and they do not use the same evidence.

- A replicon is a sequence that a specified external polymerase can initiate on and copy.
- A privileged template is a sequence recognized by one replicase, such as Qβ RNA.
- An encoded replicase is a genome that contains a polymerase gene but still needs translation.
- A molecular replicator is a nucleic acid that itself supplies the activity that regenerates itself and its complement.

A sequence that passes the first test can fail the last. The information you need is the information that distinguishes those cases.

## What else you need

The sequence is one input. The rest is context and a functional measurement.

- You need the molecule’s identity and topology: DNA or RNA, single- or double-stranded, linear or circular, and whether you have both the sequence and its complement. Replication fails if only one strand can be copied.[^3_1]
- You need the chemistry and conditions: 2′-OH or 2′-deoxy, end chemistry, temperature, magnesium and monovalent ions, and whether the substrates are NTPs, dNTPs, or activated monomers. Folding and catalysis shift with salt and crowding, so parameters measured in one buffer do not transfer cleanly.[^3_2]
- You need the catalyst, or proof that none is being supplied. A naked genome that encodes a polymerase is still only a template unless ribosomes or an equivalent expression system are present.
- You need a cycle, not a single extension. Useful measurements are initiation, full-length complementary product, strand separation, regeneration of activity, rate versus decay, and fidelity. Exponential growth of functional copies is the bar used for self-sustained replication.[^3_3][^3_4]

Without those, the strongest honest statement is that the sequence is compatible with copying under some assumed system.

## What sequence can support

Sequence can supply negative evidence and weak positive evidence.

Composition and known motifs are useful filters. AT-rich segments are candidate unwinding sites. GC skew can approximate a bacterial origin, but it often marks a point rather than the origin boundaries and can be wrong unless checked against species-specific DnaA-box clusters and local gene context. A budding-yeast ARS consensus is also not enough: the genome contains more than 12,000 matches and only about 500 functional origins under normal conditions. In higher eukaryotes, origins lack a strict consensus and depend on chromatin and transcription.[^3_5][^3_6]

Predicted secondary structure is the main sequence-only clue for RNA. A stable fold over the region to be copied argues against template activity. A fold that matches a known catalytic scaffold argues for possible ribozyme activity. Minimum-free-energy prediction recovers only about 73% of known canonical pairs on average, and it is weaker for long RNAs, pseudoknots, and tertiary contacts. Qβ-type recognition is especially easy to overread. A 3′-terminal CCCA and a second CCC in the right structural context can make an RNA a template for Qβ replicase, but recognition also depends on distributed secondary structure that prediction handles poorly.[^3_7][^3_8][^3_9][^3_10][^3_2]

Homology is stronger than de novo prediction. A close match to a characterized replicase gene, origin, or ribozyme scaffold is evidence that the sequence belongs to a known functional family. It is not evidence that this variant is active. Catalytic sequence–activity maps show substantial epistasis, and conservation does not rank activity reliably.[^3_11][^3_12]

## What sequence cannot establish

Sequence cannot show that the predicted fold is the fold adopted, or that the fold is catalytic. Tertiary contacts, metal geometry, and alternative conformations are largely invisible to a primary sequence. Models that preserve a known secondary structure generate active autocatalytic ribozymes only slightly more often than random mutagenesis once many positions change. Covariation models do better, and they still require an activity assay.[^3_12][^3_2]

Sequence also cannot show that both strands are usable. Polymerase ribozymes have strong template biases, including a preference for unstructured, cytidine-rich templates. A functional ribozyme is usually structured. Its complement then tends to violate the same bias, so one readable strand does not imply a replication cycle.[^3_1]

Finally, sequence cannot show growth. A motif match, a plausible origin, or a predicted polymerase fold does not tell you whether initiation occurs, whether the copy is full length, whether the strands separate, or whether the product can catalyze the next round. Those are properties of the molecule in a specified reaction, not properties of the string.

<span style="display:none">[^3_13][^3_14][^3_15][^3_16][^3_17][^3_18][^3_19][^3_20][^3_21][^3_22][^3_23][^3_24][^3_25][^3_26][^3_27][^3_28][^3_29][^3_30][^3_31][^3_32]</span>

<div align="center">⁂</div>

[^3_1]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5024611/

[^3_2]: https://pubs.rsc.org/en/content/articlehtml/2025/cb/d5cb00105f

[^3_3]: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7022166/

[^3_4]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6120706/

[^3_5]: https://academic.oup.com/bib/article/27/3/bbag315/8711649

[^3_6]: https://link.springer.com/article/10.1186/s12859-026-06562-5

[^3_7]: https://www.nature.com/articles/s41467-019-13395-9

[^3_8]: https://www.pnas.org/doi/10.1073/pnas.1003015107

[^3_9]: https://pmc.ncbi.nlm.nih.gov/articles/PMC432825/

[^3_10]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5362092/

[^3_11]: https://www.frontiersin.org/journals/molecular-biosciences/articles/10.3389/fmolb.2022.893864/full

[^3_12]: https://www.nature.com/articles/s41467-025-63151-5

[^3_13]: https://febs.onlinelibrary.wiley.com/doi/10.1002/1873-3468.14833

[^3_14]: https://www.sciencedirect.com/science/article/pii/S0303264726001966

[^3_15]: http://pmc.ncbi.nlm.nih.gov/articles/PMC4678825/

[^3_16]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3868306/

[^3_17]: https://www.tbi.univie.ac.at/papers/Abstracts/03-020.pdf

[^3_18]: https://www.sciencedirect.com/science/article/pii/S0021925820874262

[^3_19]: https://www.sciencedirect.com/science/article/pii/S0141813026024049

[^3_20]: https://viralzone.expasy.org/292

[^3_21]: https://onlinelibrary.wiley.com/doi/abs/10.1002/9783527814527.ch33

[^3_22]: https://scholarworks.boisestate.edu/td/2012/

[^3_23]: https://www.nature.com/articles/s41467-021-21180-w

[^3_24]: https://www.sciencedirect.com/org/science/article/pii/S2161506318001249

[^3_25]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5641303/

[^3_26]: https://ieeexplore.ieee.org/document/6999394

[^3_27]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5287236/

[^3_28]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6482342/

[^3_29]: https://rna.urmc.rochester.edu/RNAstructureWeb/

[^3_30]: http://rna.tbi.univie.ac.at/cgi-bin/RNAWebSuite/RNAfold.cgi

[^3_31]: https://rna.urmc.rochester.edu/RNAstructure.html

[^3_32]: https://pubs.acs.org/doi/10.1021/acs.biochem.3c00091


---

# Question 4 — Autonomous versus dependent replication

Explain the difference between autonomous self-replication, replication dependent on external enzymes, and non-replicating nucleic-acid molecules.

The three categories differ in who supplies the copying activity. Autonomous self-replication means the nucleic acid itself, or a nucleic-acid partner it regenerates, is the catalyst. Enzyme-dependent replication means a protein polymerase copies a template. A non-replicating nucleic acid is not a template in that cycle at all.

## Autonomous self-replication

In the molecular sense, autonomous self-replication means the catalyst is a nucleic acid in the system. No protein polymerase, ribosome, or host enzyme is required. Two RNA enzymes can build each other from oligonucleotide substrates and amplify exponentially at constant temperature with no protein present [^4_1][^4_2]. A polymerase ribozyme that copies itself and its complement from NTPs would meet the same logical test, although sustained general self-copying of that kind remains limited [^4_3][^4_4].

“Autonomous” does not mean chemically closed. These systems still need substrates, magnesium, and conditions that let strands separate. What they do not need is an externally supplied biological catalyst. The product must also be able to catalyze the next round. Copying some other RNA once is not self-replication.

## Enzyme-dependent replication

Here the nucleic acid is information, and a protein enzyme does the chemistry. Cellular chromosomes, PCR templates, and Qβ RNA copied by added Qβ replicase are all in this class. Remove the polymerase and copying stops, even if the sequence contains an origin or a replicase-binding site.

Plasmid language is easy to misread. Microbiologists call a plasmid an autonomous replicon because its origin lets it replicate separately from the chromosome [^4_5][^4_6]. It still uses host DNA polymerase, helicase, and usually primase. ColE1 needs host RNA polymerase, RNase H, and DNA polymerases. R1 needs its own RepA protein plus the host replication machinery [^4_5]. Genetic autonomy and catalytic autonomy are different claims.

Viral RNA sits in between only in appearance. A positive-strand RNA genome can encode an RNA-dependent RNA polymerase, but the first copy of that protein is made by host ribosomes [^4_7]. Until that protein exists, the genome is a non-replicating template that happens to be translatable. Self-amplifying RNA therapeutics work the same way: they replicate only after the cell supplies translation [^4_8][^4_9].

## Non-replicating nucleic acids

A non-replicating nucleic acid is used, then degraded or diluted, without serving as the template for a new copy of itself. Ordinary mRNA therapeutics are the practical example. They are translated in one round and do not generate more RNA, unlike a replicon RNA that amplifies inside the cell [^4_8][^4_9]. tRNA, rRNA, ribozymes, aptamers, and guide RNAs are also non-replicating in their biological roles. They are products of transcription, not replicons.

Non-replicating does not mean chemically incapable of being copied. Almost any complementary strand can be copied if a polymerase and primer are added in a tube. The category is about the cycle the molecule actually participates in. An mRNA that a researcher later reverse-transcribes has not become a self-replicator. It has been moved into an enzyme-dependent copying reaction.

## How to place a molecule

| Category | Who copies it? | Does the product continue the cycle? | Examples |
| :-- | :-- | :-- | :-- |
| Autonomous self-replication | The nucleic acid, or its nucleic-acid partner | Yes, without a protein catalyst | Cross-replicating ligase ribozymes [^4_1] |
| Enzyme-dependent replication | A protein polymerase, sometimes after host translation | Yes, while the enzyme is supplied | Chromosomes, plasmids, PCR templates, Qβ RNA plus replicase, viral replicons [^4_5][^4_7] |
| Non-replicating | Nobody in that cycle | No | mRNA therapeutics, tRNA, rRNA, aptamers [^4_9] |

The test is to remove proteins and ask what remains. If functional nucleic-acid copies keep appearing from substrates alone, replication is autonomous. If copying continues only while a polymerase or a translating host is present, it is enzyme-dependent. If the molecule is consumed or expressed without producing another copy, it is non-replicating.

<span style="display:none">[^4_10][^4_11][^4_12][^4_13][^4_14][^4_15][^4_16][^4_17]</span>

<div align="center">⁂</div>

[^4_1]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2652413/

[^4_2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3943892/

[^4_3]: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7022166/

[^4_4]: https://www.science.org/doi/pdf/10.1126/science.adt2760

[^4_5]: https://pmc.ncbi.nlm.nih.gov/articles/PMC98921/

[^4_6]: https://en.wikipedia.org/wiki/Plasmid

[^4_7]: https://www.abcam.com/en-us/knowledge-center/dna-and-rna/rna-replication

[^4_8]: https://www.cell.com/molecular-therapy-family/nucleic-acids/fulltext/S2162-2531(25)00328-2

[^4_9]: https://www.cell.com/molecular-therapy-family/nucleic-acids/pdf/S2162-2531(26)00324-0.pdf

[^4_10]: https://www.sciencedirect.com/science/article/pii/S2162253126003240

[^4_11]: https://www.minipcr.com/what-is-a-plasmid-components/

[^4_12]: https://flexbooks.ck12.org/cbook/ck-12-advanced-biology/section/8.9/primary/lesson/protein-synthesis-advanced-bio-adv/

[^4_13]: https://en.vectorbuilder.com/resources/vector-academy/lessons/plasmid-components.html

[^4_14]: https://www.cd-genomics.com/resource-plasmid-comprehensive-guide.html

[^4_15]: https://casrai.org/guides/origin-of-replication-plasmid

[^4_16]: https://rna.bocsci.com/support/plasmids-definition-types-and-applications.html

[^4_17]: https://blog.addgene.org/plasmid-101-origin-of-replication


---

# Question 5 — Evidence of self-replication

What experimental evidence would be necessary to establish that a DNA or RNA molecule is genuinely capable of self-replication? How would you distinguish genuine replication from simple copying or amplification?

Genuine self-replication requires a closed cycle in which newly made nucleic acid is itself the catalyst, both strands are produced and separated, and functional copies keep appearing after the original seed has been diluted away. A band of the right length, or exponential PCR, shows copying. It does not show self-replication.

## What the experiment must show

The product has to be the catalyst. Isolate material made during the reaction and show that it, not the starting seed and not an added protein, drives the next round. In the Joyce cross-replicating ligases, two RNAs assemble each other from oligonucleotide substrates with no protein present, and only the newly formed enzymes carry the reaction forward.[^5_1]

Growth must be autocatalytic and exponential. Measure the initial rate at several seed concentrations. Exponential replication gives a reaction order of about 1: doubling the seed doubles the initial rate. Product-inhibited template systems usually give an order near 0.5, which is parabolic growth, not self-sustained replication. The unseeded reaction must be much slower. For the cross-chiral ligases, autocatalysis exceeded the spontaneous reaction by about 50-fold at 10 µM substrate.[^5_2][^5_3]

Serial transfer is the decisive dilution test. Move a small fraction of a completed reaction into fresh substrates and nothing else. Growth that continues after the original seed has been diluted by many orders of magnitude is coming from progeny. The ligase system maintained exponential growth through transfers, with overall amplification above 10⁸-fold, while later mixtures contained only enzyme carried over from the previous tube. Transfer into buffer without substrates must stop the reaction.[^5_1]

Both informational strands have to be made, separated, and reused. A polymerase ribozyme must synthesize its complement and then itself, at a yield high enough for net growth. QT45 can do those two syntheses, but only in separate reactions, at about 0.2% yield over 72 days. Its authors describe that result as self-synthesis, not self-replication, because the reactions are not sequential in one pot and the strands inhibit each other by hybridization.[^5_4][^5_5][^5_6]

The product must be the right molecule and must work. Sequencing should show full-length progeny whose sequence descends from the template, including inherited mutations. The isolated product should retain catalytic activity. Fidelity has to be high enough to keep function across rounds. A useful limit is that sustainable length is roughly the inverse of the per-nucleotide error rate, so a 100-nucleotide catalyst needs better than about 99% fidelity and a 200-nucleotide polymerase better than about 99.5%.[^5_4]

## What copying looks like instead

PCR, Qβ amplification, and transcription-based amplification are exponential, but the catalyst is added and is not a product of the reaction. Serial transfer works only if polymerase is supplied again. The template is multiplied. It does not replicate itself.[^5_7]

A single primer extension is linear copying. The product does not catalyze the next round, and stopping after one extension leaves the seed as the only catalyst.

Template-directed ligation can also look like replication while failing it. If the product duplex never dissociates, each template turns over less than once and growth is parabolic. Exponential growth requires release of two active copies per cycle, not accumulation of an inactive duplex.[^5_3]


| Observation | Copying or amplification | Genuine self-replication |
| :-- | :-- | :-- |
| Product appears | Yes | Yes |
| Catalyst | Added polymerase or a preformed enzyme that is not regenerated | The nucleic acid made in the reaction [^5_1] |
| Rate versus seed | Depends on added enzyme | Order about 1; unseeded rate much lower [^5_2] |
| Serial transfer | Continues only if enzyme is replenished | Continues on progeny plus substrates alone [^5_1] |
| Both strands | Often one amplicon | Both made, separated, and reused [^5_4] |
| Heredity | Sequence can be copied by the outside enzyme | Mutations in the catalyst are inherited by active progeny |

The controls follow from that table. Omit the seed, omit any protein, omit one partner of a cross-replicating pair, and sequence the population after enough dilution that the original molecules are gone. If functional copies are still increasing, the molecule is replicating. If the signal requires an added polymerase, or dies when the seed is diluted, it was copying.

<span style="display:none">[^5_10][^5_11][^5_12][^5_13][^5_14][^5_15][^5_16][^5_17][^5_18][^5_19][^5_20][^5_21][^5_22][^5_23][^5_24][^5_25][^5_26][^5_27][^5_28][^5_29][^5_30][^5_8][^5_9]</span>

<div align="center">⁂</div>

[^5_1]: https://www.science.org/cms/asset/dfddb2da-4f02-4dd0-a975-7dcd868c40d7/pap.pdf

[^5_2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11536142/

[^5_3]: https://www.nature.com/articles/ncomms8427

[^5_4]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7022166/

[^5_5]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7618777/

[^5_6]: https://www.chemistryworld.com/news/self-synthesising-rna-strand-offers-clues-to-lifes-origins/4022966.article

[^5_7]: https://www.tbi.univie.ac.at/~pks/Preprints/pks_251.pdf

[^5_8]: https://www.nature.com/articles/s41598-021-86357-1

[^5_9]: https://www.nature.com/articles/s41467-025-64221-4

[^5_10]: https://febs.onlinelibrary.wiley.com/doi/10.1002/1873-3468.14507

[^5_11]: https://ui.adsabs.harvard.edu/abs/2009Sci...323.1229L/abstract

[^5_12]: https://www.thermofisher.com/us/en/home/life-science/cloning/cloning-learning-center/invitrogen-school-of-molecular-biology/pcr-education/pcr-reagents-enzymes/pcr-component-considerations.html

[^5_13]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4846334/

[^5_14]: https://phys.org/news/2009-01-scientists-examples-rna-replicates-indefinitely.html

[^5_15]: https://eaglepubs.erau.edu/cellandmoleclab/chapter/dna-amplification/

[^5_16]: https://thisvsthat.io/dna-replication-vs-pcr

[^5_17]: https://websites.umich.edu/~rnapeopl/WalterLabPub/Walter(95).pdf

[^5_18]: https://link.springer.com/content/pdf/10.1007/978-3-642-78110-0_4.pdf

[^5_19]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4557357/

[^5_20]: https://www.biorxiv.org/content/10.1101/2024.10.11.617851.full.pdf

[^5_21]: https://mrclmb.ac.uk/news-events/articles/bridging-the-gap-from-chemistry-to-life-discovery-of-a-tiny-rna-that-can-copy-itself/

[^5_22]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10401722/

[^5_23]: https://link.aps.org/doi/10.1103/PhysRevE.100.022414

[^5_24]: https://www.sciencedirect.com/science/article/pii/S2451929424005965

[^5_25]: https://pmc.ncbi.nlm.nih.gov/articles/PMC13120700/

[^5_26]: https://datadryad.org/dataset/doi:10.5061/dryad.6hdr7sr9n

[^5_27]: https://www.reddit.com/r/evolution/comments/1r3x1eb/selfreplicating_rna_is_more_abundant_than/

[^5_28]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2652413/

[^5_29]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3943892/

[^5_30]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5496545/

