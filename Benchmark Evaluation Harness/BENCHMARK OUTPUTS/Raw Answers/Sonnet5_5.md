<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

## Short answer

No nucleic acid copies itself on its own. Replication depends on sequence features that allow templating, initiation, priming and completion, and on features that keep the copy accurate. The main ones are below.

## Features common to DNA and RNA

- **Complementarity.** Each strand acts as a template through Watson–Crick pairing (A–T/U, G–C), and the strands run antiparallel. This is why replication is semi-conservative and why each daughter duplex keeps the parental information. It is also why "self-replication" really means the molecule or its complement is copied.[^1_1][^1_2]
- **A 3′-OH primer end.** Polymerases extend only 5′→3′ and need a free 3′-OH on a base-paired primer. Primase makes short RNA primers for this, especially on the lagging strand. A sequence therefore needs a primable site. In RNA viruses and retrotransposons this is often a tRNA-binding site or a terminal hairpin.[^1_3][^1_4]
- **Accessible single-stranded templates.** Polymerases can copy a duplex only after the strands are separated, which needs helicases and single-strand-binding proteins. In origin-free RNA replicators and ribozymes, strong secondary structure impedes copying. Short templates, under about 30 nt, are easier to copy and easier to separate from their products.[^1_4][^1_5]
- **Sugar-phosphate backbone chemistry.** The polyanionic backbone makes information content largely independent of physical properties, which suits templating. Ring conformations are restricted, which stabilizes duplexes. Activation as triphosphates (NTPs) provides the energy for synthesis.[^1_5][^1_6]


## DNA-specific features

- **Origins of replication.** Initiation happens at defined sequences. Origins tend to be AT-rich because A–T pairs have fewer hydrogen bonds and melt more easily.[^1_1]
- **Initiator-protein binding sites.** In *E. coli*, the roughly 245-bp oriC has repeated 9-bp DnaA boxes. DnaA binding triggers opening, and each origin sets up two forks that expand bidirectionally. The unit copied from one origin is called a replicon.[^1_7]
- **Circular topology or telomeres.** Prokaryotic chromosomes are usually circular. Linear chromosomes need repetitive end sequences such as the telomeric TTAGGG, which telomerase extends. This solves the end-replication problem.[^1_1]
- **Proofreading compatibility.** Accuracy comes from base pairing plus polymerase selection and exonucleolytic proofreading. Sequences that cause mispairing, such as repeats or hairpins, raise error and instability rates.[^1_4]


## RNA and origin-of-life features

- **Replicase recognition sequences.** RNA viruses carry terminal and structured elements, such as 3′ end motifs, that their RdRp recognizes. This is a general principle I'm adding, not something the sources above cover.
- **Folding that makes catalysis possible.** RNA can be both genotype and phenotype. A sequence that folds into a replicase ribozyme can catalyze its own copying. Self-replication is described as catalysis coupled to information transfer.[^1_6][^1_5]
- **Template-friendly pools.** Before replicases existed, non-enzymatic copying would have favored sequences, and their complements, that are good templates. This primed sequence space for later enzymatic replication.[^1_5]
- **Robustness to mutation.** Simple sequence requirements and tolerance of mutations are cited as advantages of RNA in early replication.[^1_6]


## Why these features matter

They separate a replicating molecule from inert DNA or RNA. Templating gives heredity, and primers and origins give control over where and when copying starts. Strand-separation properties set the cost and speed of copying, and ends and proofreading set fidelity and genome stability. The same features guide design work, such as choosing origins and copy-number control elements for plasmids. They also show why folded RNA replicators need a balance: enough structure to be catalytic, but not so much that the strands can't be copied.

<span style="display:none">[^1_10][^1_8][^1_9]</span>

<div align="center">⁂</div>

[^1_1]: https://www.ncbi.nlm.nih.gov/sites/books/n/statpearls/article-20638/

[^1_2]: https://www.khanacademy.org/science/ap-biology/gene-expression-and-regulation/replication/a/hs-dna-structure-and-replication-review

[^1_3]: https://bio.libretexts.org/Bookshelves/Microbiology/Microbiology_Laboratory_Manual\_(Hartline)/01:\_Labs/1.30:\_DNA_RNA_and_DNA_Replication

[^1_4]: https://www.ncbi.nlm.nih.gov/books/NBK26850/

[^1_5]: https://www.cambridge.org/core/journals/quarterly-reviews-of-biophysics/article/nucleic-acids-function-and-potential-for-abiogenesis/842529B9BDAD6E86F7919827725C1931

[^1_6]: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/842529B9BDAD6E86F7919827725C1931/S0033583517000038a.pdf/nucleic-acids-function-and-potential-for-abiogenesis.pdf

[^1_7]: https://rna.bocsci.com/support/dna-replication-definition-characteristics-and-biological-functions.html

[^1_8]: https://www.visiblebody.com/blog/dna-and-rna-basics-replication-transcription-and-translation

[^1_9]: https://teachmephysiology.com/biochemistry/cell-growth-death/dna-replication/

[^1_10]: https://quizlet.com/582968690/ap-bio-chp-13-flash-cards/


---

## Short answer

A true self-replicator encodes, or itself is, the catalytic function that copies it. It also has to copy both its own strand and its complement. A molecule that is only copied is a passive template. It carries the signals that host or experimenter-supplied machinery recognizes, but it supplies no copying activity. In practice this is a spectrum, not a binary.

## Defining criteria

RNA self-replication is defined as the ability to copy both itself and its complementary strand, which is its template. For sustained replication, the molecule must make both strands in yields high enough for exponential growth. The distinction rests on four properties:[^2_1][^2_2]

- **Catalysis comes from the molecule or its products.** A polymerase ribozyme is the clearest case because the RNA is both template and catalyst. A plasmid or viral genome instead encodes proteins or signals that recruit machinery.[^2_1]
- **Closing the cycle.** The (+) strand must copy the (−) strand and vice versa. One direction alone is not self-replication.
- **Fidelity sufficient to keep the information.** The maximum maintainable length is roughly the inverse of the per-nucleotide error rate. A ~100-nt ribozyme needs >99% fidelity, and a ~200-nt one needs >99.5%.[^2_2]
- **Independence from curated inputs.** Past ribozyme "self-copying" depended on carefully prepared preformed oligonucleotides, which limited mutation and evolution.[^2_2]


## Externally dependent copying

A plasmid origin is a recognition site. It works through plasmid-encoded initiators plus host proteins, and its replication is coupled to the host cell cycle. In vitro, ColE1 needs only host enzymes (RNA polymerase, RNase H, DNA polymerase I, ligase, topoisomerase I), while pSC101 additionally needs its own RepA protein. "Autonomous replicon" therefore means autonomous from the chromosome, not from the cell. A replicon is formally defined by an initiator and a replicator.[^2_3][^2_4]

Viruses are further along toward dependence. They rely on the host for nucleoside triphosphates, protein synthesis and other functions. RNA viruses encode their own RNA-replicating enzymes, because uninfected cells lack them. Replicative autonomy is graded by how much of the replication machinery the genome encodes versus borrows. Viral replicons that lack structural genes can be copied in a cell without producing infectious progeny. Research plasmids, with only an ori and a selection marker, are on the fully dependent end.[^2_4][^2_5][^2_6][^2_7]

## Obstacles for real self-replicators

Two conflicting constraints define the problem for RNA. The molecule must be a folded catalyst and also an unfolded template. It must also avoid being inhibited by pairing with its complementary strand, which blocks strand separation. Size makes this worse. Polymerase ribozymes of ~150–300 nt carry a high synthetic burden and complex folds, so they have not achieved full self-replication.[^2_8]

The best current case is QT45, a 45-nt polymerase ribozyme. It synthesizes its complementary strand at 94.1% per-nucleotide fidelity and a copy of itself using defined substrates. Yields were about 0.2% over 72 days. This is self-synthesis, not yet full self-replication. The two reactions run separately, and the self-copy needs defined triplets plus a hexamer. Its small size lowers the error threshold.[^2_9][^2_10][^2_8]

## Comparison

| Property | Plasmid or host-copied DNA | RNA virus | Polymerase ribozyme |
| :-- | :-- | :-- | :-- |
| Encodes copying catalyst | Initiator only, sometimes | Yes (replicase) | Is the catalyst |
| Supplies NTPs, ribosomes | Host | Host | Experimenter or environment |
| Copies both strands | By host machinery | Yes | Partly (QT45) |
| Status | Replicon, host-dependent | Partly autonomous | Closest to true self-replication |

<span style="display:none">[^2_11][^2_12][^2_13][^2_14][^2_15]</span>

<div align="center">⁂</div>

[^2_1]: https://mrclmb.ac.uk/news-events/articles/bridging-the-gap-from-chemistry-to-life-discovery-of-a-tiny-rna-that-can-copy-itself/

[^2_2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7022166/

[^2_3]: https://www.zubairkhalid.com/knowledge/molecular-biology/plasmid-replicate-independently

[^2_4]: https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/replicon

[^2_5]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7158166/

[^2_6]: https://www.news-medical.net/life-sciences/Are-Viruses-a-Lifeform.aspx

[^2_7]: https://en.vectorbuilder.com/resources/vector-academy/lessons/plasmid-components.html

[^2_8]: https://www.biorxiv.org/content/10.1101/2024.10.11.617851v1.full-text

[^2_9]: https://pubmed.ncbi.nlm.nih.gov/41678588/

[^2_10]: https://www.chemistryworld.com/news/self-synthesising-rna-strand-offers-clues-to-lifes-origins/4022966.article

[^2_11]: https://www.pnas.org/doi/10.1073/pnas.2606892123

[^2_12]: https://pmc.ncbi.nlm.nih.gov/articles/PMC328809/

[^2_13]: https://www2.mrc-lmb.cam.ac.uk/groups/ph1/rna_self.html

[^2_14]: https://www.reddit.com/r/evolution/comments/1r3x1eb/selfreplicating_rna_is_more_abundant_than/

[^2_15]: https://jackwestin.com/resources/mcat-content/viral-life-cycle/self-replicating-biological-units-that-must-reproduce-within-specific-host-cell


---

## Short answer

A sequence alone can show that replication is plausible, because it can reveal origins, encoded replicases, primer sites and structural elements. It cannot show that replication happens. That depends on the host or reaction context, the supplied enzymes and substrates, and measured copying of both strands.

## What you would need

- **Molecule type and topology.** You need to know whether it is DNA or RNA, single- or double-stranded, circular or linear, and whether it has terminal elements such as telomeres or hairpins. These determine the replication mode and how the ends are handled.
- **Origin and initiator signals.** Replicons are defined by an initiator and a replicator. Look for origin-like sequences such as AT-rich unwinding regions and repeated initiator-binding boxes, plus any gene encoding the initiator protein.[^3_1][^3_2]
- **Encoded replication enzymes.** Search for ORFs that resemble polymerases, replicases, helicases or primases. This is the main sign of autonomy. RNA viruses encode their own RNA-replicating enzymes because host cells lack them.[^3_3]
- **Ribozyme potential.** For short RNAs, you need a predicted or tested fold that supports polymerase activity. The best current example, QT45, is 45 nt long and synthesizes its complementary strand and a copy of itself.[^3_4]
- **Template-compatible structure.** The sequence needs primable 3′ ends or primer-binding sites. It also needs a fold that can open enough for copying without blocking strand separation.[^3_5]
- **Context.** You need the host or cell type, the supplied proteins and the available NTPs and primers. A plasmid's replication relies on host enzymes, and some origins also need their own initiator protein.[^3_2]
- **Empirical data.** The proof is observed copying of both strands, at high enough fidelity and yield for continued propagation. That requires an assay, not sequence analysis.[^3_6][^3_7]


## What can be inferred

- **Likely replication mode.** Origins, a rolling-circle motif or an RdRp-like ORF suggest a specific replication class.
- **Degree of autonomy.** If the sequence encodes the initiator or replicase, it is closer to autonomous. If it holds only an origin, it depends on host machinery.[^3_1][^3_2]
- **Host range.** Origin type and initiator homology suggest which hosts support replication.
- **Fidelity limits.** Length constrains maintainability. A ~100-nt ribozyme needs >99% fidelity, and a ~200-nt one needs >99.5%. Longer sequences therefore face tougher requirements.[^3_7]
- **Plausible but unproven catalysis.** Sequence similarity to known ribozymes or polymerases supports a hypothesis.


## What cannot be inferred

- **Whether it works.** Predicted folds are uncertain, and ribozyme function is highly sensitive to small sequence changes. Complex polymerase ribozymes have not achieved full self-replication despite their size.[^3_5]
- **Efficiency.** QT45 produced about 0.2% yields over 72 days and ran its two reactions separately. A sequence cannot reveal such kinetics.[^3_8][^3_4]
- **Strand-separation behavior.** The balance between folded catalyst and copyable template, and inhibition by the complement, depends on conditions such as salt, temperature and concentration.[^3_5]
- **Dependence on supplied reagents.** Experimental self-copying often uses defined, preformed substrates. The sequence will not tell you whether natural precursors suffice.[^3_7][^3_5]
- **Regulation and compatibility.** Copy-number control and cell-cycle coupling depend on host factors. Origins of human sequences, for instance, were studied by density labelling because function was not predictable from sequence.[^3_9][^3_2]


## Practical workflow

1. Annotate origins, ORFs and motifs, and compare them to replicon and viral replicase databases.
2. Predict the structure and identify primer sites.
3. Choose the context (host, cell-free extract, or defined ribozyme reaction).
4. Test copying of both strands with labeled substrates or sequencing.
5. Measure fidelity, yield and serial propagation.

<div align="center">⁂</div>

[^3_1]: https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/replicon

[^3_2]: https://www.zubairkhalid.com/knowledge/molecular-biology/plasmid-replicate-independently

[^3_3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7158166/

[^3_4]: https://pubmed.ncbi.nlm.nih.gov/41678588/

[^3_5]: https://www.biorxiv.org/content/10.1101/2024.10.11.617851v1.full-text

[^3_6]: https://mrclmb.ac.uk/news-events/articles/bridging-the-gap-from-chemistry-to-life-discovery-of-a-tiny-rna-that-can-copy-itself/

[^3_7]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7022166/

[^3_8]: https://www.chemistryworld.com/news/self-synthesising-rna-strand-offers-clues-to-lifes-origins/4022966.article

[^3_9]: https://pmc.ncbi.nlm.nih.gov/articles/PMC328809/


---

## Short answer

The three categories differ in who supplies the copying catalysis and whether the molecule carries the signals that allow copying at all. Autonomous replicators supply their own catalysis. Dependent replicators supply only recognition signals and rely on outside enzymes. Non-replicating molecules have neither. These are graded categories, not sharp boundaries.[^4_1]

## Autonomous self-replication

The molecule is both template and catalyst, or encodes its own catalyst. It copies both strands, and the copies keep that ability. The clearest case is a polymerase ribozyme, such as the 45-nt QT45, which can synthesize its complementary strand and a copy of itself. Even QT45 is not fully autonomous in practice. Its reactions run separately, it needs defined triplet substrates, and its yields were about 0.2% over 72 days. No known natural or artificial molecule meets the strict standard of sustained replication from simple precursors, which is why the field treats it as an open goal.[^4_2][^4_3][^4_4][^4_5][^4_6]

## Dependence on external enzymes

These molecules carry the signals for replication but not the machinery.

- **Plasmids.** A plasmid is autonomous only relative to the chromosome. A ColE1-type origin works with host enzymes alone (RNA polymerase, RNase H, DNA polymerase I and others). pSC101 also needs its own RepA protein. Copying is tied to the host cell cycle.[^4_7]
- **Viruses.** Viruses rely on the host for NTPs, protein synthesis and other functions. RNA viruses encode a replicase because cells lack one. They sit partway along the spectrum, as partly autonomous replicators.[^4_8][^4_1]
- **Lab constructs.** A cloned insert with an origin and a marker is copied by bacterial machinery or by PCR polymerase. It has no catalytic role.[^4_9]

Formally, replicons have an initiator and a replicator element. The origin (replicator) is only a site, and the initiator is a protein that must be supplied, by the host or by the replicon itself.[^4_10]

## Non-replicating molecules

These carry no origin or primer site and encode no replication function. Examples are mRNA, tRNA and rRNA, plus most genomic fragments. They may still be copied if an enzyme acts on them, such as by reverse transcription, PCR or transcription. That is passive copying, not replication in the genetic sense. A sequence with an origin placed in a host that lacks the matching initiator is also non-replicating in that context. Replication depends on context as well as sequence. Studies of autonomously replicating human sequences relied on measured copy number per cell cycle.[^4_11]

## Summary table

| Feature | Autonomous | Enzyme-dependent | Non-replicating |
| :-- | :-- | :-- | :-- |
| Catalysis | Own (ribozyme or encoded) | External | None |
| Replication signals | Yes | Yes | No |
| Copies both strands | Yes | Via host machinery | No |
| Examples | Polymerase ribozymes (QT45, partially) | Plasmids, viruses, templates | mRNA, tRNA, fragments |

<div align="center">⁂</div>

[^4_1]: https://www.news-medical.net/life-sciences/Are-Viruses-a-Lifeform.aspx

[^4_2]: https://mrclmb.ac.uk/news-events/articles/bridging-the-gap-from-chemistry-to-life-discovery-of-a-tiny-rna-that-can-copy-itself/

[^4_3]: https://pubmed.ncbi.nlm.nih.gov/41678588/

[^4_4]: https://www.chemistryworld.com/news/self-synthesising-rna-strand-offers-clues-to-lifes-origins/4022966.article

[^4_5]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7022166/

[^4_6]: https://www.biorxiv.org/content/10.1101/2024.10.11.617851v1.full-text

[^4_7]: https://www.zubairkhalid.com/knowledge/molecular-biology/plasmid-replicate-independently

[^4_8]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7158166/

[^4_9]: https://en.vectorbuilder.com/resources/vector-academy/lessons/plasmid-components.html

[^4_10]: https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/replicon

[^4_11]: https://pmc.ncbi.nlm.nih.gov/articles/PMC328809/


---

## Short answer

You would need to show that the molecule itself, or something it encodes, drives copying of both strands. The copies must be functional and must carry that ability forward through repeated generations, in a defined system where no outside enzyme can account for the result. Copying a template once, or amplifying it with supplied enzymes, does not meet that bar.

## Evidence required

- **Defined, minimal reaction.** Use purified components and name every ingredient, such as NTPs or primers. The experiments on QT45 used defined substrates (triplets plus a hexamer) so the source of catalysis was clear. Cell lysates or crude extracts leave host enzymes as an alternative explanation.[^5_1][^5_2]
- **Catalyst identity.** Show that the molecule is the catalyst. For a ribozyme, test inactive mutants, scrambled sequences and catalytic-site mutations, which should abolish copying. Also show that it needs no contaminating protein, with nuclease and protease controls. For an encoded replicase, show that the encoded protein, made in vitro or in vivo, drives copying.
- **Both strands.** Demonstrate synthesis of the complementary strand and then of a copy of the original. QT45's reported ability to do both is what made it notable. A single direction is not self-replication.[^5_3][^5_4]
- **Product verification.** Sequence the products to confirm they are full-length and match the template or its complement. Check that the copy is functional by testing its activity, not just its length.
- **Fidelity.** Measure error rates. A ~100-nt ribozyme needs >99% fidelity, and a ~200-nt one needs >99.5%, to maintain information. QT45's reported fidelity was 94.1% per nucleotide, which shows why the field treats fidelity as a central limit.[^5_5][^5_1]
- **Exponential, serial propagation.** Demonstrate that copies copy. Run serial transfers or dilutions where each generation seeds the next, and show growth over several rounds. The quantity that matters is net yield per cycle, since QT45's yields were about 0.2% over 72 days.[^5_2][^5_3]
- **Template independence controls.** Run no-template and no-catalyst reactions to rule out spontaneous or contaminant-driven products, and use unrelated or mutated templates to show sequence specificity.


## Distinguishing true replication from copying or amplification

| Feature | Genuine self-replication | Copying or amplification |
| :-- | :-- | :-- |
| Catalyst | The molecule or its encoded product | External polymerase (PCR, host) [^5_6] |
| Strands | Both, and copies are functional | Template-driven; function irrelevant |
| Product role | Copies catalyze the next round | Copies are inert products |
| Growth | Self-sustained through serial passage | Limited by supplied enzyme and primers |
| Controls | Dead mutants fail | Enzyme omitted, nothing happens |

PCR and cloning are amplification. The molecule only has to hold primer sites. In a host, plasmid copying is also dependent, because the host provides enzymes and sets copy number. A virus is intermediate. It encodes its replicase, but needs host resources.[^5_7][^5_8][^5_9]

## Common pitfalls

- **Contamination.** Carry-over of template, polymerase or product can mimic growth. Use no-template controls and distinctive sequence markers.
- **Ligation or recombination.** Assembly of fragments into longer products can look like synthesis, so check for primer-extension chemistry.
- **Misinterpreting yield.** A single detectable copy proves catalysis. It does not prove sustained replication.[^5_5]
- **Prepared substrates.** Preformed oligonucleotide inputs can hide the difficulty of the task. Note the supplied components in your conclusion.[^5_1][^5_5]

<div align="center">⁂</div>

[^5_1]: https://www.biorxiv.org/content/10.1101/2024.10.11.617851v1.full-text

[^5_2]: https://www.chemistryworld.com/news/self-synthesising-rna-strand-offers-clues-to-lifes-origins/4022966.article

[^5_3]: https://pubmed.ncbi.nlm.nih.gov/41678588/

[^5_4]: https://mrclmb.ac.uk/news-events/articles/bridging-the-gap-from-chemistry-to-life-discovery-of-a-tiny-rna-that-can-copy-itself/

[^5_5]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7022166/

[^5_6]: https://en.vectorbuilder.com/resources/vector-academy/lessons/plasmid-components.html

[^5_7]: https://www.zubairkhalid.com/knowledge/molecular-biology/plasmid-replicate-independently

[^5_8]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7158166/

[^5_9]: https://www.news-medical.net/life-sciences/Are-Viruses-a-Lifeform.aspx

