<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

## Short answer

Self-replication depends on a few kinds of sequence-level features. Some let the molecule act as a template, some mark where copying starts, some let it be copied completely, and in RNA some let it fold into a catalyst. Nothing in a bare sequence makes it self-replicating on its own. These features work through the polymerase or replicase machinery, whether that is protein-based, ribozyme-based or non-enzymatic.

## Features common to all templates

- **Complementary base pairing.** A–T (or A–U) and G–C pairing lets each strand specify a complementary copy. This gives semiconservative replication, in which each daughter molecule keeps one old strand and one new strand [](https://www.ncbi.nlm.nih.gov/sites/books/n/statpearls/article-20638/)[](https://www.khanacademy.org/science/ap-biology/gene-expression-and-regulation/replication/a/molecular-mechanism-of-dna-replication). Relevance: this is the basis of heredity.[^1_1][^1_2]
- **Antiparallel strand polarity with 5′→3′ synthesis.** Polymerases only extend a free 3′-OH, and they need a template and a primer [](https://www.khanacademy.org/science/ap-biology/gene-expression-and-regulation/replication/a/molecular-mechanism-of-dna-replication)[](https://bio.libretexts.org/Bookshelves/Microbiology/Microbiology_Laboratory_Manual_(Hartline)/01:_Labs/1.30:_DNA_RNA_and_DNA_Replication). A molecule therefore needs a primable 3′ end, or a site where a primer can anneal. Relevance: this requirement is why cells need primase and RNA primers, and why the lagging strand is made as Okazaki fragments.[^1_2][^1_3]
- **Backbone chemistry.** The phosphodiester backbone is polyanionic, so information content and physical properties are largely decoupled. Sequence can change without changing how the molecule behaves as a polymer [](https://www.cambridge.org/core/journals/quarterly-reviews-of-biophysics/article/nucleic-acids-function-and-potential-for-abiogenesis/842529B9BDAD6E86F7919827725C1931)[](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/842529B9BDAD6E86F7919827725C1931/S0033583517000038a.pdf/nucleic-acids-function-and-potential-for-abiogenesis.pdf). Relevance: almost any sequence can be copied, which makes the system evolvable.[^1_4][^1_5]


## Origins and initiator sites

- **Origin of replication sequences.** Replication starts at specific sites that are recognized by their sequence [](https://www.khanacademy.org/science/ap-biology/gene-expression-and-regulation/replication/a/molecular-mechanism-of-dna-replication). Without one, a plasmid or chromosome fragment is not maintained. This is why plasmids carry a defined ori.[^1_2]
- **High AT content.** Origins tend to be AT-rich, and A–T pairs have fewer hydrogen bonds, so the strands separate more easily there [](https://www.ncbi.nlm.nih.gov/sites/books/n/statpearls/article-20638/). This is the DNA-unwinding element where helicase is loaded.[^1_1]
- **Repeated or inverted initiator-binding motifs.** E. coli oriC is about 245 bp and contains symmetrically arranged 9-bp repeats called DnaA boxes. Binding of DnaA to these boxes initiates replication [](https://rna.bocsci.com/support/dna-replication-definition-characteristics-and-biological-functions.html). Relevance: the motifs control when and how often replication starts, and they define a replicon, the unit that replicates from one origin.[^1_6]
- **Bidirectional initiation.** Two forks move outward from each origin [](https://rna.bocsci.com/support/dna-replication-definition-characteristics-and-biological-functions.html).[^1_6]

Many RNA viruses and phages have analogous elements. Their genomes carry conserved terminal or structured regions that the viral polymerase recognizes. I did not retrieve sources on those, so that is general background and not a cited claim.

## Ends and completeness

- **Telomeric repeats.** Linear eukaryotic chromosomes end in repeats such as TTAGGG, which telomerase extends [](https://www.ncbi.nlm.nih.gov/sites/books/n/statpearls/article-20638/). Relevance: the lagging strand cannot be copied all the way to the end, so without these repeats chromosomes would shorten each cycle.[^1_1]
- **Circular topology.** Prokaryotic chromosomes are circular [](https://www.ncbi.nlm.nih.gov/sites/books/n/statpearls/article-20638/), which avoids the end-replication problem entirely.[^1_1]


## RNA and the origin of life

RNA can fold into 3D structures that act as ligands and catalysts, so one molecule carries both genotype and phenotype [](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/842529B9BDAD6E86F7919827725C1931/S0033583517000038a.pdf/nucleic-acids-function-and-potential-for-abiogenesis.pdf). Self-replication can be viewed as a specialized catalysis coupled to information transfer [](https://www.cambridge.org/core/journals/quarterly-reviews-of-biophysics/article/nucleic-acids-function-and-potential-for-abiogenesis/842529B9BDAD6E86F7919827725C1931). Several sequence features follow from this:[^1_5][^1_4]

- **Foldable catalytic motifs.** A ribozyme replicase needs a sequence that folds into an active site. Any RNA that can fold and catalyze replication gains a selective advantage [](https://www.cambridge.org/core/journals/quarterly-reviews-of-biophysics/article/nucleic-acids-function-and-potential-for-abiogenesis/842529B9BDAD6E86F7919827725C1931).[^1_4]
- **Low secondary structure in templates.** Strong folding blocks copying. Shorter templates are easier for a ribozyme or non-enzymatic chemistry to copy because they have less secondary structure, and templates under about 30 nt separate more easily from their products [](https://www.cambridge.org/core/journals/quarterly-reviews-of-biophysics/article/nucleic-acids-function-and-potential-for-abiogenesis/842529B9BDAD6E86F7919827725C1931). There is a tension here. A replicase needs structure to be active, but a template needs to stay unfolded. Fragmenting the replicase at the replication stage is one proposed way around this.[^1_4]
- **Complementarity-friendly pools.** Early non-enzymatic replication would have favored sequences, and their complements, that are good templates [](https://www.cambridge.org/core/journals/quarterly-reviews-of-biophysics/article/nucleic-acids-function-and-potential-for-abiogenesis/842529B9BDAD6E86F7919827725C1931). Relevance: this is a possible route to sequences that later enzymes could copy.[^1_4]


## Practical reading for design

For a synthetic construct, a replicable sequence needs four things:

- A compatible origin or polymerase-recognition site.
- Sequence that is copyable, meaning no strong secondary structure that blocks the polymerase.
- A primable 3′ end, or circular topology.
- For RNA self-replicators, a fold that is catalytic but still permits templating.

Choose a target system, such as a plasmid ori, an RNA virus or a ribozyme replicase, and I can list its specific motifs.

<span style="display:none">[^1_10][^1_7][^1_8][^1_9]</span>

<div align="center">⁂</div>

[^1_1]: https://www.ncbi.nlm.nih.gov/sites/books/n/statpearls/article-20638/

[^1_2]: https://www.khanacademy.org/science/ap-biology/gene-expression-and-regulation/replication/a/molecular-mechanism-of-dna-replication

[^1_3]: https://bio.libretexts.org/Bookshelves/Microbiology/Microbiology_Laboratory_Manual\_(Hartline)/01:\_Labs/1.30:\_DNA_RNA_and_DNA_Replication

[^1_4]: https://www.cambridge.org/core/journals/quarterly-reviews-of-biophysics/article/nucleic-acids-function-and-potential-for-abiogenesis/842529B9BDAD6E86F7919827725C1931

[^1_5]: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/842529B9BDAD6E86F7919827725C1931/S0033583517000038a.pdf/nucleic-acids-function-and-potential-for-abiogenesis.pdf

[^1_6]: https://rna.bocsci.com/support/dna-replication-definition-characteristics-and-biological-functions.html

[^1_7]: https://www.ncbi.nlm.nih.gov/books/NBK26850/

[^1_8]: https://www.visiblebody.com/blog/dna-and-rna-basics-replication-transcription-and-translation

[^1_9]: https://quizlet.com/582968690/ap-bio-chp-13-flash-cards/

[^1_10]: https://teachmephysiology.com/biochemistry/cell-growth-death/dna-replication/


---

## Short answer

A molecule that is only copied is a passive template. Its sequence can be read, but it encodes no part of the copying machinery. A true self-replicator either carries the catalytic function for its own copying, as a ribozyme, or encodes that function and uses it on itself. In practice, even natural "self-replicating" genomes such as viruses are better called autonomously encoded but host-dependent.

## The key distinction

Von Neumann's framework says a replicator has three parts: a coded representation, a mechanism to copy it, and a mechanism for building within its environment. Almost all known examples follow this pattern [](https://en.wikipedia.org/wiki/Self-replication). A molecule that is merely copied supplies only the first part, and the cell or experimenter supplies the rest. Systems that copy RNA in a bath of monomers and a polymerase are described as "assisted replication", not self-replication [](https://en.wikipedia.org/wiki/Self-replication).[^2_1]

## A spectrum of cases

| Category | What the nucleic acid supplies | What is external | Example |
| :-- | :-- | :-- | :-- |
| Passive template | Origin or recognition sites and sequence only | Polymerase, helicase, primase, nucleotides, energy | Plasmid, or DNA in PCR |
| Replicon or minigenome | cis-acting signals; the 5′ and 3′ noncoding regions often suffice to direct genome replication [[^2_2]](https://pmc.ncbi.nlm.nih.gov/articles/PMC7173417/) | The RdRp, which may be supplied in trans [[^2_2]](https://pmc.ncbi.nlm.nih.gov/articles/PMC7173417/) | Viral minigenomes |
| Encoded replicase, host-assisted | The RdRp gene, which gives it catalytic autonomy for the copying step | Host proteins, membranes and ribosomes [[^2_3]](https://pmc.ncbi.nlm.nih.gov/articles/PMC2908549/) | (+)RNA viruses |
| Ribozyme self-replicator | The catalytic RNA itself, which copies itself and its complement [[^2_4]](https://mrclmb.ac.uk/news-events/articles/bridging-the-gap-from-chemistry-to-life-discovery-of-a-tiny-rna-that-can-copy-itself/) | Only chemical building blocks and a permissive environment | QT45 (not yet fully self-sustaining) |

## What a true self-replicator needs

- **Catalytic activity encoded in its own sequence.** The molecule must fold into an active polymerase and also work as a template. QT45 meets this in 45 nucleotides. It makes its complementary strand and a copy of itself, using the complement as template for itself [](https://mrclmb.ac.uk/news-events/articles/bridging-the-gap-from-chemistry-to-life-discovery-of-a-tiny-rna-that-can-copy-itself/).[^2_4]
- **Copying both strands.** Self-replication means copying both itself and the information in its complementary strand [](https://mrclmb.ac.uk/news-events/articles/bridging-the-gap-from-chemistry-to-life-discovery-of-a-tiny-rna-that-can-copy-itself/). The polymerase must make copies of itself and its complement in enough yield for exponential growth [](https://pmc.ncbi.nlm.nih.gov/articles/PMC7022166/).[^2_5][^2_4]
- **Independence from curated substrates.** Earlier self-copying ribozymes depended on carefully prepared sets of preformed oligonucleotides. That limits the copied RNA's ability to mutate and evolve [](https://pmc.ncbi.nlm.nih.gov/articles/PMC7022166/).[^2_5]
- **Fidelity matched to length.** The maximum maintainable RNA length is roughly the inverse of the per-nucleotide error rate. A ~100-nt ligase needs more than 99% fidelity, and a ~200-nt polymerase needs more than 99.5% [](https://pmc.ncbi.nlm.nih.gov/articles/PMC7022166/). Otherwise information is lost through an error catastrophe.[^2_5]


## How close the best examples are

Natural viruses are not independent. Their RdRp lacks proofreading, and (+)RNA virus replication often needs host proteins, and membranes whose removal destroys true replication [](https://pmc.ncbi.nlm.nih.gov/articles/PMC2908549/). Negative-sense viruses must carry a packaged polymerase, because the host cannot read their genome directly [](https://biologyinsights.com/positive-sense-vs-negative-sense-rna-viruses-explained/).[^2_3][^2_6]

The best laboratory ribozyme is still short of the goal. QT45 copies itself with about 0.2% yield over 72 days. Its complement synthesis runs at 94.1% per-nucleotide fidelity [](https://discourse.peacefulscience.org/t/they-found-it-a-45-nt-rna-self-replicator/17677). The two reactions run separately, not in one pot, so it is self-synthesis and not yet self-replication [](https://www.chemistryworld.com/news/self-synthesising-rna-strand-offers-clues-to-lifes-origins/4022966.article). An earlier polymerase ribozyme (38-6) made its evolutionary ancestor as three fragments, not a copy of itself [](https://pmc.ncbi.nlm.nih.gov/articles/PMC7022166/).[^2_7][^2_8][^2_5]

## Practical test

Ask whether the sequence, plus only small-molecule building blocks, can reproduce itself. If a protein or cellular factor that the sequence does not encode is required, it is a copyable template. If it encodes the machinery but still needs host factors, it is a host-dependent replicon or virus. Only a molecule that passes without any outside catalyst qualifies as a self-replicator, and no natural or synthetic nucleic acid has fully demonstrated this yet.

<span style="display:none">[^2_10][^2_11][^2_12][^2_13][^2_14][^2_15][^2_9]</span>

<div align="center">⁂</div>

[^2_1]: https://en.wikipedia.org/wiki/Self-replication

[^2_2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7173417/

[^2_3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2908549/

[^2_4]: https://mrclmb.ac.uk/news-events/articles/bridging-the-gap-from-chemistry-to-life-discovery-of-a-tiny-rna-that-can-copy-itself/

[^2_5]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7022166/

[^2_6]: https://biologyinsights.com/positive-sense-vs-negative-sense-rna-viruses-explained/

[^2_7]: https://discourse.peacefulscience.org/t/they-found-it-a-45-nt-rna-self-replicator/17677

[^2_8]: https://www.chemistryworld.com/news/self-synthesising-rna-strand-offers-clues-to-lifes-origins/4022966.article

[^2_9]: https://www.nature.com/articles/s41467-025-63151-5

[^2_10]: https://www.cell.com/cell-chemical-biology/fulltext/S1074-5521(03)00003-6

[^2_11]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5691660/

[^2_12]: https://onlinelibrary.wiley.com/doi/abs/10.1002/9783527814527.ch13

[^2_13]: https://www.abcam.com/en-us/knowledge-center/dna-and-rna/rna-replication

[^2_14]: https://crvscience.com/wiki/rna-replicase-ribozyme

[^2_15]: https://www.cd-genomics.com/blog/rna-virus-classification-replication-extraction-protocols/


---

## Short answer

A sequence alone lets you infer whether it contains the right parts: an origin or recognition signal, a replicase gene, or a catalytic fold. It does not tell you whether the molecule replicates, because that depends on the host, the environment and the supplied enzymes. "Self-replication potential" is therefore a prediction from sequence, and replication has to be shown experimentally.

## Information you need beyond the sequence

- **Molecule type and form.** You need to know whether it is DNA or RNA, single- or double-stranded, and circular or linear. This decides which replication logic applies: a primable 3′ end, telomere-like ends, or circularity.
- **Intended or natural host and machinery.** Replication in a given host requires matching its polymerases and initiators. For example, plasmid host range is inferred from replicon and relaxase markers, and some plasmids carry several origins that are active in different hosts [](https://pubmed.ncbi.nlm.nih.gov/32969786/)[](https://academic.oup.com/bioinformatics/article/41/3/btaf075/8019658).[^3_1][^3_2]
- **Supplied factors.** You need to know which enzymes, nucleotides, primers, divalent ions and energy sources are present. This separates a self-replicator from a template (see Q2).
- **Chromatin and epigenetic context.** In higher eukaryotes, origins lack a strict consensus. Activity depends on chromatin, transcription and topology, not on sequence alone [](https://link.springer.com/article/10.1186/s12859-026-06562-5)[](https://pmc.ncbi.nlm.nih.gov/articles/PMC5002974/).[^3_3][^3_4]
- **Experimental readouts.** Useful assays include a plasmid maintenance or copy-number assay, a minigenome or replicon assay, and, for ribozymes, a self-copying assay with measured yield and fidelity.


## What the sequence can tell you

- **Origins and initiator sites.** Computational tools use AT-rich stretches, GC skew, DnaA-box clusters, the position of the dnaA gene and nearby indicator genes (Ori-Finder, ORCA). Newer machine-learning and deep-learning models classify k-mer patterns [](https://academic.oup.com/bib/article/27/3/bbag315/8711649). AT excursion scores have predicted about 65% of origins in a test dataset [](https://pmc.ncbi.nlm.nih.gov/articles/PMC1904460/).[^3_5][^3_6]
- **Replicon type and host range.** Plasmid replication and relaxase markers, or whole-sequence clustering, classify plasmids and predict host range [](https://pubmed.ncbi.nlm.nih.gov/32969786/). Learning-based predictors use k-mers, GC content, codon usage, replicon type and MOB type [](https://academic.oup.com/bioinformatics/article/41/3/btaf075/8019658).[^3_2][^3_1]
- **A replicase gene.** The RdRp is the one universal hallmark gene of RNA viruses, and profile HMMs detect it even at about 10% identity to known viruses, which BLAST misses [](https://academic.oup.com/ve/article/8/2/veac082/6679729)[](https://pmc.ncbi.nlm.nih.gov/articles/PMC10101049/). Finding a conserved RdRp (or Rep/helicase) is the strongest sequence-level evidence of encoded replication capacity.[^3_7][^3_8]
- **Structure and ribozyme-like fold.** RNA folding prediction can flag helices and motifs. Generative and statistical models have been used to estimate the plausibility of self-reproducing ribozymes [](https://www.nature.com/articles/s41467-025-63151-5), but this remains inferential.[^3_9]
- **Template suitability.** Strong secondary structure, length and GC content affect how copyable a template is, as covered in Q1.


## What you cannot infer

- **Activity.** Motifs are necessary at best, not sufficient. G-quadruplex motifs, for instance, number more than 370,000 in the human genome against about 80,000 identified origins [](https://pmc.ncbi.nlm.nih.gov/articles/PMC5002974/). Origin predictors can also give false positives when AT-rich signals are present out of context [](https://link.springer.com/article/10.1186/s12859-026-06562-5).[^3_4][^3_3]
- **Autonomy.** Finding an RdRp or an origin doesn't show that the molecule needs no host factors. Even RNA viruses depend on host proteins and membranes [](https://pmc.ncbi.nlm.nih.gov/articles/PMC2908549/).[^3_10]
- **Novel ribozyme replicators.** There is no reliable sequence-only way to detect a new catalytic self-replicating RNA. The best known example, QT45, was found experimentally [](https://mrclmb.ac.uk/news-events/articles/bridging-the-gap-from-chemistry-to-life-discovery-of-a-tiny-rna-that-can-copy-itself/).[^3_11]
- **Rates, fidelity and sustainability.** Whether replication is fast and accurate enough to avoid an error catastrophe can only be measured (see Q2).
- **Absence of evidence.** Many origins and replicases are divergent, so an annotation miss does not mean a molecule cannot replicate.


## A practical workflow

1. Annotate the sequence: ORFs, replicase and helicase domains (HMM search), origin-like and AT-rich regions, and repeats.
2. Predict RNA structure and any ribozyme-like folds.
3. Compare replicon and origin markers against reference databases for type and host range.
4. State the prediction as one of four classes: template only, replicon needing a host, an encoded replicase with host factors, or a candidate catalytic replicator.
5. Test it in the intended host or in vitro, measuring copy number or yield and fidelity.

<span style="display:none">[^3_12][^3_13][^3_14][^3_15][^3_16][^3_17][^3_18]</span>

<div align="center">⁂</div>

[^3_1]: https://pubmed.ncbi.nlm.nih.gov/32969786/

[^3_2]: https://academic.oup.com/bioinformatics/article/41/3/btaf075/8019658

[^3_3]: https://link.springer.com/article/10.1186/s12859-026-06562-5

[^3_4]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5002974/

[^3_5]: https://academic.oup.com/bib/article/27/3/bbag315/8711649

[^3_6]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1904460/

[^3_7]: https://academic.oup.com/ve/article/8/2/veac082/6679729

[^3_8]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10101049/

[^3_9]: https://www.nature.com/articles/s41467-025-63151-5

[^3_10]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2908549/

[^3_11]: https://mrclmb.ac.uk/news-events/articles/bridging-the-gap-from-chemistry-to-life-discovery-of-a-tiny-rna-that-can-copy-itself/

[^3_12]: https://www.microbiologyresearch.org/content/journal/mgen/10.1099/mgen.0.000435?crawler=true\&mimetype=application/pdf

[^3_13]: https://www.biorxiv.org/content/10.1101/2022.02.28.482397v1

[^3_14]: https://journals.asm.org/doi/10.1128/msystems.01180-21

[^3_15]: https://arxiv.org/html/1909.13751v1

[^3_16]: https://www.tandfonline.com/doi/full/10.2147/IDR.S461039

[^3_17]: https://github.com/JustineCharon/RdRp-scan

[^3_18]: https://www.semanticscholar.org/paper/Universal-whole-sequence-based-plasmid-typing-and-Robertson-Bessonov/943573fb001d3311bed6fe60852727d2e108df14


---

## Short answer

The three categories differ in where the catalytic work of copying comes from. Autonomous self-replication means the molecule supplies the copying catalyst itself. Dependent replication means it carries only the signals and relies on an outside enzyme. A non-replicating molecule has neither the signals nor a suitable template function, so even a supplied polymerase would not copy it in a heritable way.

## The three categories

| Feature | Autonomous self-replication | Dependent on external enzymes | Non-replicating |
| :-- | :-- | :-- | :-- |
| Catalyst for copying | Encoded in or formed by the molecule itself (e.g., a ribozyme) | Supplied by a host or experimenter (polymerase, helicase, primase) | None, or none that can act on it |
| What the sequence contributes | Template plus catalytic fold, and copies both itself and its complement [[^4_1]](https://mrclmb.ac.uk/news-events/articles/bridging-the-gap-from-chemistry-to-life-discovery-of-a-tiny-rna-that-can-copy-itself/) | Template, origin or recognition signals, and primable ends (Q1) | Perhaps template-capable chemistry, but no recognition or initiation signals |
| Typical examples | The ribozyme QT45, an experimental case that is not yet fully self-sustaining [[^4_2]](https://www.chemistryworld.com/news/self-synthesising-rna-strand-offers-clues-to-lifes-origins/4022966.article) | Plasmids, chromosomes, PCR templates, and viral genomes that need host factors [[^4_3]](https://pmc.ncbi.nlm.nih.gov/articles/PMC2908549/) | mRNA, tRNA, rRNA and most noncoding RNA; fragments without an origin; degraded or damaged DNA |
| Key limit | Fidelity and length (error catastrophe), plus low yields so far [[^4_4]](https://pmc.ncbi.nlm.nih.gov/articles/PMC7022166/) | Needs the right host or reagents | Can't propagate |

## How to tell them apart

Autonomous self-replication is the narrowest category. By the von Neumann framework, a self-replicator contains the information, the copying mechanism and the means to build with environmental resources [](https://en.wikipedia.org/wiki/Self-replication). Few if any nucleic acids meet all of it. The strongest candidates are polymerase ribozymes. One of these synthesized its own evolutionary ancestor, but only as three fragments and not as a copy of itself [](https://pmc.ncbi.nlm.nih.gov/articles/PMC7022166/).[^4_4][^4_5]

Dependent replication covers most biology. A plasmid only needs an origin and the host's enzymes. RNA viruses sit in between: they encode their own RdRp, which has no proofreading, and they still depend on host factors and host-derived replication complexes [](https://pmc.ncbi.nlm.nih.gov/articles/PMC2908549/). A viral genome's 5′ and 3′ noncoding regions can direct replication when the RdRp is supplied in trans, which shows how much of the machinery can be external [](https://pmc.ncbi.nlm.nih.gov/articles/PMC7173417/).[^4_3][^4_6]

Non-replicating molecules are the default. Most RNA in a cell is transcribed from DNA and is never copied RNA-to-RNA. A molecule can be copied once, as in PCR or reverse transcription, and still not count as replicating if it can't be copied again in turn or isn't maintained.

## Gray zones

- **Copyable but not heritable.** An RNA can be copied by a promiscuous polymerase without any origin or signal that makes the copying specific or repeatable.
- **Host-assisted autonomy.** Negative-sense RNA viruses package their own polymerase because the host cannot read their genome [](https://biologyinsights.com/positive-sense-vs-negative-sense-rna-viruses-explained/). Classifying them depends on whether you count the packaged enzyme as part of the molecule.[^4_7]
- **Non-enzymatic copying.** Chemical copying with activated monomers needs no enzyme, but it is slow and low in fidelity, so it is not sustained replication [](https://onlinelibrary.wiley.com/doi/abs/10.1002/9783527814527.ch13).[^4_8]

Because the boundary depends on where you draw the system edge, specify the environment when you classify a molecule. This also matches Q3, where sequence analysis can place a molecule in one of these categories only provisionally.

<div align="center">⁂</div>

[^4_1]: https://mrclmb.ac.uk/news-events/articles/bridging-the-gap-from-chemistry-to-life-discovery-of-a-tiny-rna-that-can-copy-itself/

[^4_2]: https://www.chemistryworld.com/news/self-synthesising-rna-strand-offers-clues-to-lifes-origins/4022966.article

[^4_3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2908549/

[^4_4]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7022166/

[^4_5]: https://en.wikipedia.org/wiki/Self-replication

[^4_6]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7173417/

[^4_7]: https://biologyinsights.com/positive-sense-vs-negative-sense-rna-viruses-explained/

[^4_8]: https://onlinelibrary.wiley.com/doi/abs/10.1002/9783527814527.ch13


---

## Short answer

You need to show three things in a defined system. The molecule must produce copies of itself, those copies must in turn be copyable, and the process must depend only on the molecule's own catalytic activity plus small-molecule inputs. Amplification and simple copying fail one or more of these tests. The central difference is that a genuine replicator's copies take part in further rounds of copying, and no outside catalyst supplies the copying chemistry.

## Evidence required

**1. Defined, minimal components.** Run the reaction with only purified nucleotides (or activated monomers), buffer, ions and the candidate. Any polymerase, helicase or cell extract must be absent or shown to be unnecessary. A system can only be called self-replicating when no external machinery is acting on it [](https://en.wikipedia.org/wiki/Self-replication).[^5_1]

**2. Product identity.** Show the products are full-length copies with the correct sequence, using sequencing, not just a band of the right size. For ribozymes this means distinguishing true copies from ligation of fragments or partial products. The QT45 work reported that the molecule makes its complementary strand and a copy of itself, using the complement as the template [](https://mrclmb.ac.uk/news-events/articles/bridging-the-gap-from-chemistry-to-life-discovery-of-a-tiny-rna-that-can-copy-itself/).[^5_2]

**3. Both strands.** Self-replication needs copying of the molecule and of its complement. Demonstrate that each strand is a competent template and the polymerase can make both [](https://pmc.ncbi.nlm.nih.gov/articles/PMC7022166/).[^5_3]

**4. Product as catalyst and template.** Show that newly made copies are themselves active and are copied again. A kinetic signature helps: with true self-replication, the product feeds back and yield grows super-linearly or exponentially, whereas simple copying is linear in input. Seeding experiments help here, because adding more molecule should accelerate the reaction.

**5. Single-pot continuity.** The steps should run together, not sequentially in different conditions. QT45's two reactions run separately and not in one pot, so it is described as self-synthesis, not yet sustained replication [](https://www.chemistryworld.com/news/self-synthesising-rna-strand-offers-clues-to-lifes-origins/4022966.article). Serial transfer over many generations then tests sustainability.[^5_4]

**6. Yield, rate and fidelity.** Quantify yield per cycle, rate and per-nucleotide error. For a molecule of length L, fidelity has to be high enough to avoid an error catastrophe. A ~100-nt ligase needs above 99% fidelity and a ~200-nt polymerase above 99.5% [](https://pmc.ncbi.nlm.nih.gov/articles/PMC7022166/). QT45's reported complement synthesis was 94.1% accurate per nucleotide, and self-copying yield was about 0.2% over 72 days [](https://discourse.peacefulscience.org/t/they-found-it-a-45-nt-rna-self-replicator/17677).[^5_5][^5_3]

## Controls that separate replication from copying

| Confound | Control or test |
| :-- | :-- |
| External catalyst (protein or contaminant) | Proteinase, RNase-free or enzyme-free reaction; omit the candidate and confirm no activity |
| Sequence-specific catalysis | Inactive point mutants and scrambled sequences; show activity depends on the fold |
| Template-independent synthesis | Omit template or use a non-cognate template |
| Cross-contamination | Sequence-tagged variants, so copies can be traced back to the input |
| One-off copying (e.g., PCR) | Show copies continue to be copied without added enzyme |
| Selection for a different property | Verify the copied pool is the replicator, not a contaminating product |

## Why amplification does not count

PCR, rolling-circle amplification, and cellular DNA replication all exponentially increase copy number. In each case an externally supplied polymerase, primers and thermal cycling or a host do the catalysis, so the nucleic acid acts only as a template (Q4). A plasmid in a cell likewise shows replication, but of a host-dependent kind. RNA viruses carry their own RdRp, which lacks proofreading, but their replication still depends on host factors and membranes [](https://pmc.ncbi.nlm.nih.gov/articles/PMC2908549/). Strictly, that evidence supports "host-dependent replication", not autonomy.[^5_6]

## Evolvability as a final test

Genuine replicators should show heredity with variation. Introduce mutations, let them propagate through serial transfer, and demonstrate that variants persist and can be selected. Earlier self-copying ribozymes depended on curated oligonucleotide sets, which restricted evolution [](https://pmc.ncbi.nlm.nih.gov/articles/PMC7022166/). Showing evolution in a defined system is the strongest evidence that a molecule is replicating on its own, but it is a bonus, not a minimum requirement.[^5_3]

<div align="center">⁂</div>

[^5_1]: https://en.wikipedia.org/wiki/Self-replication

[^5_2]: https://mrclmb.ac.uk/news-events/articles/bridging-the-gap-from-chemistry-to-life-discovery-of-a-tiny-rna-that-can-copy-itself/

[^5_3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7022166/

[^5_4]: https://www.chemistryworld.com/news/self-synthesising-rna-strand-offers-clues-to-lifes-origins/4022966.article

[^5_5]: https://discourse.peacefulscience.org/t/they-found-it-a-45-nt-rna-self-replicator/17677

[^5_6]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2908549/

