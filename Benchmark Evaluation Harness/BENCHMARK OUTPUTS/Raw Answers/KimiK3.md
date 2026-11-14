<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Question 1 — Replication-associated features

What sequence-level features of DNA or RNA are associated with the ability of a nucleic-acid molecule to participate in self-replication? Explain the biological relevance of these features.

Self-replication is not specified by one universal “replication motif.” It depends on a combination of template complementarity, initiation signals, suitable primer and end structures, manageable secondary structure, and—when the molecule supplies its own copying machinery—sequence encoding polymerase or catalytic activity.

## Universal sequence requirements

| Sequence-level feature | Replication role | Biological relevance |
| :-- | :-- | :-- |
| Watson–Crick complementarity | A pairs with T in DNA or U in RNA, and G pairs with C, allowing either strand to specify its complement. | This is the chemical basis of semiconservative inheritance: each parental strand can direct synthesis of a complementary daughter strand while preserving sequence information. [^1_1][^1_2] |
| Polymerase-compatible directionality and priming | Polymerases extend a primer from its free 3′-OH in the 5′→3′ direction. Sequences must therefore provide a usable primer–template junction. | This explains why DNA synthesis uses RNA primers, why the two strands replicate differently, and why terminal sequences can be difficult to copy. [^1_3] |
| Initiation or promoter motifs | Specific motifs recruit replication proteins or RNA polymerases to defined sites. | Initiation signals determine where copying begins and help distinguish a replicating genome from unrelated nucleic acids. |
| Accessible template sequence | Extremely stable hairpins, highly structured regions, or very long duplexes can obstruct polymerization or prevent product–template separation. | Replication machinery or environmental cycling must expose single-stranded template; inefficient strand separation limits both cellular and prebiotic replication. [^1_4][^1_5] |
| Fidelity-compatible sequence composition | Long homopolymers and tandem repeats are especially vulnerable to polymerase slippage, insertions, deletions, and rearrangements. | Such sequences can generate useful variation but also destabilize genomes; elevated repetition therefore trades replication robustness against mutability and evolution. [^1_6][^1_7] |
| Trans-encoded replication functions | Coding sequences for polymerases, helicases, primases, single-strand-binding proteins, or viral Rep proteins provide the machinery needed to copy the molecule. | A genome supporting autonomous propagation must contain or obtain instructions for initiating, elongating, proofreading, and separating replicated strands. |

## DNA-specific features

### Origin organization

Cellular DNA origins combine initiator-binding sites with an AT-rich DNA-unwinding element. Bacterial origins often contain repeated DnaA boxes, while plasmids and phages commonly use repeated iterons that bind their own replication-initiator proteins. A-T pairs form fewer hydrogen bonds than G-C pairs, so AT-rich tracts melt more readily and permit assembly of the replication fork. [^1_8][^1_9]

Budding-yeast autonomously replicating sequences provide a clear experimental example: an approximately 100–200 bp region can allow a plasmid to replicate once during the cell cycle. These origins contain a short, highly conserved ARS consensus sequence plus less-conserved flanking elements. Metazoan origins are generally less sequence-specific, illustrating that origin function can also depend on chromatin and genomic context rather than sequence alone. [^1_10][^1_11]

Biologically, origin motifs allow a cell or virus to:

- Start replication at controlled genomic positions
- Coordinate genome duplication with the cell cycle
- Regulate replicon copy number
- Prevent either under- or over-replication


### Terminal and end-maintenance sequences

Viral DNA often contains inverted terminal repeats that fold into hairpins. After a viral Rep protein binds and introduces a nick at an appropriate site, the resulting 3′-OH can act as a primer for copying the genome. Thus, the repeat sequence performs both protein-recognition and structural-priming roles. [^1_12]

Linear chromosomes require telomeric repeats because conventional replication cannot completely copy chromosome ends. Human telomeres contain repeated 5′-TTAGGG-3′ sequences, form a G-rich 3′ overhang, and can be extended by telomerase. Telomerase RNA carries a short template complementary to the telomeric repeat, allowing repeated cycles of alignment and extension. These sequences protect coding DNA from progressive loss and distinguish natural chromosome ends from accidental breaks. [^1_13][^1_12]

### Fidelity-control motifs

Sequence can also participate indirectly in faithful replication by marking the daughter strand for repair. In *E. coli*, palindromic GATC sites are transiently hemimethylated after replication: the parental strand is methylated while the newly synthesized strand is not. Mismatch-repair proteins use this difference to remove the erroneous daughter strand rather than the correct template. [^1_14][^1_15]

This distinction is biologically important because copying is not merely about making DNA rapidly; it must preserve information across generations. Methyl-directed repair substantially reduces the mutation rate and helps maintain genome stability.

## RNA-specific features

RNA replication uses sequence both as information and as a determinant of folded structure. Consequently, RNA cis-signals often involve stem-loops, pseudoknots, bulges, exposed loops, and long-range base pairing rather than a simple linear consensus.

Important features include:

- Conserved 5′ and 3′ replication promoters that recruit an RNA-dependent RNA polymerase
- Accessible 3′ initiation nucleotides or weak A-U/G-U-rich stem regions that can be opened by the polymerase
- Stem-loop or Y-shaped receptor elements that bind viral or host replication factors
- Long-range complementarity between 5′ and 3′ ends that circularizes the genome and coordinates translation with replication
- Terminal poly(A), cap-like sequences, tRNA-like structures, or protein-linked ends that stabilize the genome and assist initiation

For example, flavivirus stem-loop A is a polymerase-recognition promoter at the 5′ end, although negative-strand initiation occurs after long-range interactions position the polymerase at the 3′ end. Viral replication therefore depends on both local RNA structures and distant sequence complementarity. [^1_16][^1_17]

RNA viruses commonly also encode a replicase or polymerase. Experimental evolution shows how decisive this distinction is: parasitic RNAs can delete much of the replicase-coding region and continue to replicate as long as they retain the terminal sequences recognized by a replicase supplied by another RNA. The terminal recognition signals—not simply the size of the coding sequence—make those molecules replication competitors. [^1_18]

## What would make RNA genuinely self-replicating?

A truly autonomous RNA system must do more than act as a template. Its sequence would need to:

1. Fold into an RNA-copying catalyst or encode one
2. Copy its own sequence
3. Copy the complementary strand
4. Achieve adequate fidelity
5. Separate template and product strands
6. Repeat the process at rates exceeding degradation

Stable intramolecular structure helps an RNA form an active ribozyme, but the same structure can obstruct template copying or prevent strand release. Self-replicating sequences therefore face a design tradeoff between catalytic folding and template accessibility. Shorter molecules are easier to copy, whereas longer ones can encode more powerful catalytic functions. [^1_4][^1_5]

Engineered polymerase ribozymes illustrate this requirement. A 45-nucleotide ribozyme reported as QT45 can copy diverse templates and synthesize both itself and its encoding template—the two reactions required for self-replication—while using activated trinucleotide precursors. Even that system depends on highly specific laboratory chemistry, demonstrating that sequence alone does not confer autonomous replication under arbitrary conditions. [^1_19]

## Practical interpretation

When assessing whether a DNA or RNA sequence can participate in replication, the central questions are:

- Can each strand specify its complement accurately?
- Is there an origin, promoter, or replicase-recognition element?
- Can a primer or equivalent 3′-OH initiation substrate form?
- Can the molecule’s ends be completely copied?
- Is the template sufficiently accessible for polymerase traversal?
- Can the product and template strands separate and be reused?
- Does the molecule encode, recruit, or exist with the required copying machinery?
- Are repeats, homopolymers, or secondary structures likely to cause excessive errors?

In biological terms, these features jointly determine inheritance, genome stability, viral host-range and replication specificity, copy-number control, and evolutionary potential. The essential distinction is that cellular DNA and RNA are **replication-competent components of a molecular system**; they are rarely autonomous self-copying molecules by themselves.

<span style="display:none">[^1_20][^1_21][^1_22][^1_23][^1_24][^1_25][^1_26][^1_27][^1_28][^1_29][^1_30][^1_31][^1_32][^1_33][^1_34][^1_35][^1_36][^1_37][^1_38][^1_39][^1_40][^1_41][^1_42][^1_43][^1_44][^1_45][^1_46][^1_47][^1_48][^1_49][^1_50][^1_51][^1_52][^1_53][^1_54]</span>

<div align="center">⁂</div>

[^1_1]: https://www.ncbi.nlm.nih.gov/books/NBK26850/

[^1_2]: https://www.khanacademy.org/science/ap-biology/gene-expression-and-regulation/replication/a/hs-dna-structure-and-replication-review

[^1_3]: https://bio.libretexts.org/Bookshelves/Microbiology/Microbiology_Laboratory_Manual\_(Hartline)/01:\_Labs/1.30:\_DNA_RNA_and_DNA_Replication

[^1_4]: https://www.cambridge.org/core/journals/quarterly-reviews-of-biophysics/article/nucleic-acids-function-and-potential-for-abiogenesis/842529B9BDAD6E86F7919827725C1931

[^1_5]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6120706/

[^1_6]: https://www.nature.com/scitable/topicpage/dna-replication-and-causes-of-mutation-409/

[^1_7]: https://pmc.ncbi.nlm.nih.gov/articles/PMC37438/

[^1_8]: https://www.ncbi.nlm.nih.gov/sites/books/n/statpearls/article-20638/

[^1_9]: https://academic.oup.com/femsre/article/36/2/408/565738

[^1_10]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4993324/

[^1_11]: http://rcn.montana.edu/Publications/Pdf/2005/FEBS J rev.pdf

[^1_12]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2713563/

[^1_13]: https://pmc.ncbi.nlm.nih.gov/articles/PMC13208914/

[^1_14]: https://pubmed.ncbi.nlm.nih.gov/3019677/

[^1_15]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8785607/

[^1_16]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7158166/

[^1_17]: https://www.mdpi.com/1999-4915/13/6/1107

[^1_18]: https://www.nature.com/articles/s41467-022-29113-x

[^1_19]: https://www.science.org/doi/10.1126/science.adt2760

[^1_20]: https://www.visiblebody.com/blog/dna-and-rna-basics-replication-transcription-and-translation

[^1_21]: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/842529B9BDAD6E86F7919827725C1931/S0033583517000038a.pdf/nucleic-acids-function-and-potential-for-abiogenesis.pdf

[^1_22]: https://teachmephysiology.com/biochemistry/cell-growth-death/dna-replication/

[^1_23]: https://rna.bocsci.com/support/dna-replication-definition-characteristics-and-biological-functions.html

[^1_24]: https://quizlet.com/582968690/ap-bio-chp-13-flash-cards/

[^1_25]: https://www.cell.com/trends/genetics/fulltext/S0168-9525(24)00077-5

[^1_26]: https://www.pnas.org/doi/10.1073/pnas.1503157112

[^1_27]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9898300/

[^1_28]: https://www.sciencedirect.com/topics/neuroscience/origin-of-replication

[^1_29]: https://bio.libretexts.org/Bookshelves/Introductory_and_General_Biology/General_Biology\_(Boundless)/14:\_DNA_Structure_and_Function/14.03:\_DNA_Replication/14.3D:\_Telomere_Replication

[^1_30]: https://www.khanacademy.org/science/biology/dna-as-the-genetic-material/dna-replication/a/telomeres-telomerase

[^1_31]: https://en.wikipedia.org/wiki/Cis-acting_replication_element

[^1_32]: https://quizlet.com/777470791/biol-4000-lecture-8-telomerase-rna-flash-cards/

[^1_33]: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7172556/

[^1_34]: https://www.nature.com/articles/s41467-023-37206-4

[^1_35]: https://www.pnas.org/doi/10.1073/pnas.1914282117

[^1_36]: https://www.pnas.org/doi/10.1073/pnas.2313332121

[^1_37]: https://www.pnas.org/doi/10.1073/pnas.2505720122

[^1_38]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4959843/

[^1_39]: https://www.biorxiv.org/content/10.64898/2026.08.06.743385.full.pdf

[^1_40]: https://journals.asm.org/doi/10.1128/jvi.01754-10

[^1_41]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10080680/

[^1_42]: https://en.wikipedia.org/wiki/RNA-dependent_RNA_polymerase

[^1_43]: https://dash.harvard.edu/entities/publication/72dd7734-5cea-4c61-b0f3-d55ed3a487f2

[^1_44]: https://www.nature.com/articles/srep07346

[^1_45]: https://www.pnas.org/doi/10.1073/pnas.1505370112

[^1_46]: https://ui.adsabs.harvard.edu/abs/2014NatSR...4.7346S/abstract

[^1_47]: https://www.jbc.org/article/S0021-9258(19)52145-7/fulltext

[^1_48]: https://academic.oup.com/nar/article/53/14/gkaf679/8210550

[^1_49]: https://www.pnas.org/doi/10.1073/pnas.1205063109

[^1_50]: https://pmc.ncbi.nlm.nih.gov/articles/PMC125466/

[^1_51]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4740232/

[^1_52]: https://en.wikipedia.org/wiki/DNA_mismatch_repair

[^1_53]: https://www.microbiosci.com/posts/overcoming-template-secondary-structure-in-pcr-a-comprehensive-guide-for-reliable-amplification

[^1_54]: https://www.bohrium.com/en/sciencepedia/feynman/keyword/replication_slippage


---

# Question 2 — Requirements for self-replication

What distinguishes a nucleic-acid molecule that can self-replicate from one that can only be copied using externally supplied biological machinery?

The essential distinction is **informational and catalytic closure**: a self-replicating nucleic acid contains the instructions—or is itself the catalytic structure—needed to generate the machinery that copies it. A merely copyable molecule supplies only template and recognition sequences, while the polymerase, translation system, primers, and other required machinery come from elsewhere.

Strictly speaking, no isolated nucleic acid polymerizes itself while remaining intact. “Self-replication” therefore means a recursive loop in which sequence information produces copying activity, and that activity produces additional copies of the sequence.[^2_1]

## Key distinction

| Property | Externally copied nucleic acid | Self-replicating nucleic-acid system |
| :-- | :-- | :-- |
| Information carried by the molecule | Template sequence plus primer sites, origins, or replicase-recognition elements | Those features plus instructions for producing the copying catalyst, or the catalyst folded within the molecule itself |
| Origin of polymerization activity | Provided by a polymerase, replicase, ribozyme, translation system, or laboratory reaction not generated by the nucleic acid | Generated directly by RNA catalysis or indirectly by sequence → gene product → copying enzyme → copies of sequence [^2_1] |
| Effect of removing the molecule | Little effect, because the supplied machinery still exists | The replicating system loses the genetic instructions or catalytic structure needed to regenerate its copying machinery |
| Products | Copies contain the template information but need not recreate the external machinery | Successful products retain the ability to initiate another replication cycle |
| Complete cycle required | One round or one strand may be copied | Complete molecule must be copied, strands must separate or be released, and products must become usable templates or catalysts [^2_2] |
| Use of supplied matter and energy | Requires nucleotides and chemical or biological energy | Also requires nucleotides and energy; external building blocks do not disqualify a replicator |
| Inheritance | Transmits information only when artificial or host machinery is continuously available | Transmits both information and the potential to reconstruct replication competence |

The boundary is therefore not “uses external monomers.” Every replicating system consumes externally supplied building blocks and free energy. The boundary is whether the external reaction supplies the generic physical inputs or supplies the information-processing machinery that the molecule cannot regenerate.[^2_1]

## Illustrative biological contrast

The Qβ RNA host–parasite system gives an especially clean example. The host RNA encodes the catalytic β-subunit of the Qβ RNA replicase; after translation, the resulting replicase copies the host RNA. A shorter parasitic RNA that has deleted the replicase-coding sequence retains the terminal signals needed for recognition and is also copied, but only when effective replicase is supplied by a host RNA.[^2_3][^2_4]

Thus:

- The host RNA is self-replicating relative to the parasite because it specifies its own copying function.
- The parasite is replication-competent but not self-specifying because it has the template signals without the information needed to produce the necessary enzyme.
- Both remain dependent on translation factors, nucleotides, and other components of the experimental system, so “self-replicating” describes autonomy within a defined system, not absolute chemical independence.[^2_4]

Spiegelman’s classic experiments reveal the same distinction. When viral RNA was serially transferred with purified Qβ replicase and nucleotides, selection stripped it down to a short molecule essentially sufficient to bind and recruit the supplied replicase. The resulting “monster” replicated extremely efficiently in that environment, but it was better understood as a highly optimized parasite of external machinery than as an autonomous replicator.[^2_5]

## Degrees of autonomy

### 1. Template-only replicators

These molecules can be amplified rapidly but contain no instructions for their own copying machinery.

Examples include:

- A purified Qβ parasite RNA copied by externally supplied Qβ replicase[^2_3]
- An RNA retaining viral terminal recognition signals but lacking a replicase gene
- A minimal synthetic template copied by a supplied polymerase
- A DNA amplicon copied with externally supplied primers and polymerase

The molecule can evolve under replication selection, but the replication function itself is not inherited unless the surroundings continue supplying it.

### 2. Self-encoded but machinery-dependent replicators

These molecules encode a polymerase or replicase but require translation and cellular factors.

Alphavirus-derived self-amplifying RNAs encode the nonstructural proteins nsP1–nsP4. Host ribosomes translate these proteins, nsP4 supplies RNA-dependent RNA-polymerase activity, and the resulting complex copies the RNA through a negative-strand intermediate. Such molecules are called self-replicating or self-amplifying because they carry the replicase instructions, even though they rely on host translation, membranes, metabolites, and antiviral-state-dependent factors.[^2_6][^2_7]

An engineered DNA module-genome takes this one step further: it encodes all 26 proteins needed for its own rolling-circle replication. The proteins are synthesized using an externally supplied PURE transcription–translation system, after which they replicate the DNA that encoded them. It is therefore self-encoding for DNA replication but still dependent on externally supplied translation machinery, amino acids, nucleotides, and energy sources.[^2_8]

### 3. RNA-catalytic replicators

An RNA polymerase ribozyme removes the need to translate a protein polymerase. In principle, one RNA molecule can act both as genetic information and as the catalyst that copies another RNA corresponding to itself.

The 45-nucleotide QT45 ribozyme can synthesize a copy of itself and a copy of its encoding template strand, demonstrating the direct and indirect copying reactions needed for RNA self-replication. However, it works with chemically activated oligonucleotide substrates and under specialized conditions. Demonstrating these reactions separately does not by itself establish a robust, continuous replication cycle in which template and product routinely separate, both copies become active, and replication proceeds over many generations.[^2_2][^2_9][^2_10]

### 4. Fully regenerating molecular systems

Stronger self-replication requires regeneration not just of one molecule, but of the complete functional reaction system:

- The informational molecule
- Its complementary strands
- Its copying machinery
- Structures that prevent productive copies from being trapped in duplexes
- Sufficient fidelity to preserve function
- Repeated copying faster than component degradation

Cellular chromosomes satisfy many of these requirements only as part of a cell. They encode many replication functions but also require inherited polymerases, ribosomes, RNAs, membranes, metabolites, and daughter-cell organization. This is why complete self-replication is properly a property of a bounded system rather than of a sequence read in isolation.

## Diagnostic test

A useful three-question test is:

1. **Does the molecule specify the copying function?**\
If it merely contains an origin, promoter, primer-binding site, or terminal replicase-recognition sequence, it is copyable but not self-sufficient.
2. **Do the products retain recursive replication competence?**\
A legitimate replicator must generate full-length daughter molecules that can produce copying function and initiate another cycle.
3. **Which machinery must be supplied uninterrupted?**\
If removing a polymerase, replicase, translation system, or other externally generated component stops replication, that component must be recognized as part of the replicating system.

In short, a copyable nucleic acid is **information waiting for a machine**. A self-replicating nucleic-acid system directs the reconstruction of the machine that copies the information—though the machine may still need external monomers, energy, and, in most biological examples, substantial cellular infrastructure.

<span style="display:none">[^2_11][^2_12][^2_13][^2_14][^2_15][^2_16][^2_17][^2_18][^2_19][^2_20][^2_21][^2_22][^2_23][^2_24][^2_25][^2_26][^2_27][^2_28][^2_29][^2_30]</span>

<div align="center">⁂</div>

[^2_1]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10077596/

[^2_2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7289000/

[^2_3]: https://www.pnas.org/doi/10.1073/pnas.1524404113

[^2_4]: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7378860/

[^2_5]: https://profiles.nlm.nih.gov/spotlight/px/feature/monster

[^2_6]: https://pmc.ncbi.nlm.nih.gov/articles/PMC13386960/

[^2_7]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12031284/

[^2_8]: https://academic.oup.com/nar/article/54/13/gkag663/8724181

[^2_9]: https://www.science.org/doi/pdf/10.1126/science.adt2760

[^2_10]: https://www.pnas.org/post/journal-club/short-strands-rna-nearly-self-replicate-recreating-possible-step-dawn-life

[^2_11]: https://academic.oup.com/mbe/article/43/5/msag084/8666424

[^2_12]: https://febs.onlinelibrary.wiley.com/doi/10.1002/1873-3468.14507

[^2_13]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8933500/

[^2_14]: https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/self-replication

[^2_15]: https://www.biorxiv.org/content/10.1101/728659v1.full-text

[^2_16]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7318430/

[^2_17]: https://www.quantamagazine.org/in-test-tubes-rna-molecules-evolve-into-a-tiny-ecosystem-20220505/

[^2_18]: https://www.eurekalert.org/news-releases/1130640

[^2_19]: https://rna.bocsci.com/support/what-is-self-replicating-rna.html

[^2_20]: http://www.molecularassembler.com/KSRM/5.5.htm

[^2_21]: https://www.pnas.org/doi/10.1073/pnas.1408677111

[^2_22]: https://www.biorxiv.org/content/10.1101/2024.10.11.617851v1

[^2_23]: https://www.lindahall.org/about/news/scientist-of-the-day/sol-spiegelman/

[^2_24]: https://journals.asm.org/doi/10.1128/jvi.01225-23

[^2_25]: https://nccr-rna-and-disease.ch/news/newsletter/no-1/looking-back-50-years-ago

[^2_26]: https://arstechnica.com/science/2026/02/researchers-find-small-rnas-that-can-make-copies-of-themselves/

[^2_27]: https://onlinelibrary.wiley.com/doi/10.1002/smll.75396

[^2_28]: https://en.wikipedia.org/wiki/Spiegelman's_Monster

[^2_29]: https://astrobiology.com/2026/02/16/a-small-polymerase-ribozyme-that-can-synthesize-itself-and-its-complementary-strand/

[^2_30]: https://www.mdpi.com/1422-0067/27/21/9457


---

# Question 3 — Replication potential

Given a DNA or RNA sequence, what information would you need to determine whether it has self-replication potential? Explain what can and cannot be inferred from the sequence alone.

A FASTA sequence alone cannot establish self-replication potential. Replication potential is a property of the molecule **plus** its physical form, modifications, environment, and available machinery; sequence analysis can generate a dependency hypothesis, but only context-aware molecular and full-cycle replication assays can establish autonomy.

## Information needed beyond the sequence

| Needed information | Why it matters |
| :-- | :-- |
| Molecular identity and physical form | The result can differ for the same primary sequence if it is DNA versus RNA, single- versus double-stranded, linear versus circular, intact versus nicked, or complete versus truncated. Terminal overhangs, end structure, and topology also determine whether priming, initiation, and complete copying are possible. [^3_1] |
| Exact terminal chemistry | Polymerases generally require an accessible 3′-OH or another suitable initiation substrate. Caps, phosphorylation, aminoacylation, terminal transferase additions, or covalently linked terminal proteins can block or facilitate recognition. A one-dimensional sequence does not report these forms. |
| DNA replication-initiation signals | Annotate initiator-binding motifs such as DnaA boxes or plasmid iterons, AT-rich unwinding elements, viral Rep sites, ARS-like elements, G-rich structures, and repeated origins. Motif databases are system-specific and must be tied to the intended organism or viral family. [^3_2] |
| RNA replication signals | Examine 5′ and 3′ untranslated regions, promoter stem-loops, terminal repeats, pseudoknots, tRNA-like structures, long-range complementarity, poly(A), and exposed initiation nucleotides. Several such structures are cis-acting and cannot be recognized reliably from a short consensus motif alone. [^3_3] |
| Replication-function annotation | Search for ORFs or RNA motifs capable of producing molecular machinery: polymerase or replicase genes, Rep/helicase/primase genes, helper dependencies, or RNA domains with known polymerase-ribozyme homology. This annotation identifies whether the molecule can regenerate copying activity or only recruit external activity. |
| Presumed biological environment | Specify the source organism and intended host, nuclear versus cytoplasmic location, replication phase, cell type, temperature, ionic conditions, metabolite supply, and whether helper molecules or translation are permitted. The same sequence may be autonomous in one setting and inert in another. |
| Epigenetic and epitranscriptomic state | CpG and GATC methylation, histone packaging, chromatin accessibility, RNA methylation, pseudouridine, m⁶A, alternative nucleobases, and editing or damage can alter replication, protein binding, folding, stability, and translation. All of these are largely invisible when the sequence is represented only as A, C, G, and T or U. [^3_4][^3_5][^3_6] |
| Structure under physiological conditions | RNA structures are modulated by temperature, ions, proteins, crowding, and interactions with other sequences. Pseudoknots, pseudouridylation, and noncanonical pairing further reduce confidence in thermodynamic prediction based only on the four standard bases. [^3_7][^3_6] |
| Environmental requirements for a full cycle | Determine whether products can be fully copied, template–product complexes can separate, both complementary strands can become active products, and daughter molecules can initiate additional cycles. Copying one strand once is not evidence of self-replication. [^3_8] |
| Growth and fidelity data | Establish whether replication is exponential, faster than degradation, sufficiently accurate to preserve function through repeated rounds, and stopped by deleting a predicted replication function. These are population-level measurements, not sequence annotations. |

## What sequence alone can establish

Sequence is substantially informative when interpreted against a particular biological system.

### Coding and motif content

A sequence can reveal:

- Long ORFs and recognizable polymerase, replicase, Rep, helicase, primase, or regulatory domains
- Putative promoter elements and terminators
- Known viral or plasmid replication origins
- Inverted terminal repeats, conserved terminal motifs, and telomere-like repeats
- DnaA-box clusters, iterons, ARS consensus-like regions, or other system-specific motifs
- Homopolymer runs and tandem repeats likely to generate copying errors
- Potential pairing between distant regions that might coordinate ends or circularization

These observations can support a concrete classification, such as “this RNA appears to encode a complete viral replicase and retain the appropriate terminal signals,” without proving that replication will occur in a given experiment. Alphavirus self-amplifying RNAs, for example, carry nsP1–nsP4 replicase genes and viral cis-elements but still require translation and host-cell factors.[^3_9][^3_10]

### Intrinsic physical and compositional properties

From sequence, one can estimate:

- GC or AT richness
- Compositional and GC/AT asymmetry
- Melting propensity and local DNA unwinding tendency
- Homopolymer and repeat instability
- Candidate G-quadruplexes, hairpins, pseudoknots, and RNAreplicase-recognition elements
- Putative antisense complementarity or long-range 5′–3′ pairing
- Minimum free-energy folding and ensemble base-pair probabilities

These features help prioritize likely origins or replication-blocking structures. They are predictions rather than measurements. RNA predictions are especially sensitive to assumptions about folding kinetics, ions, cellular crowding, protein interactions, pseudoknots, noncanonical pairs, and chemical modifications.[^3_7][^3_11]

### Conditional replication hypotheses

The strongest sequence-only conclusion is usually conditional:

- “This DNA contains motifs likely to function as a plasmid origin in host X.”
- “This RNA resembles a known viral replicon if translated by cytoplasmic ribosomes.”
- “This molecule likely depends on an externally supplied replicase because it lacks a polymerase ORF.”
- “This sequence has no known catalytic RNA architecture, making protein-free self-copying unlikely.”

These are useful hypotheses, but they do not by themselves quantify replication rate, product completeness, molecular stability, or repeated-cycle inheritance.

## What sequence alone cannot establish

### Actual origin activity

Sequence motifs are generally neither sufficient nor always necessary for origin use. In budding yeast, the genome contains about 12,000 motifs resembling the ARS consensus sequence, but only roughly 500 correspond to normally functional origins. Chromatin, transcriptional interference, nucleosome positioning, and broader genomic context determine which motif-bearing sites fire.[^3_12]

Higher-eukaryotic origins are even more context-dependent. Human sequences associated with open chromatin, CpG islands, GC enrichment, and G-quadruplex-forming motifs are neither necessary nor sufficient to make a locus an active origin. Transplantation experiments similarly show that the sequence at an origin does not independently determine origin activity after chromosomal organization changes.[^3_13][^3_14]

Modern machine-learning models can extract meaningful replication signals from sequence, but they remain species- and assay-dependent. Different origin-mapping methods capture protein binding, active firing, or broad replication domains, producing partly divergent training labels; predictive models consequently often generalize poorly across organisms and cell types.[^3_15]

### Physiologic RNA folding and function

A predicted stem-loop does not prove that it forms in the relevant compartment or that it is recognized by the relevant polymerase. Standard sequence models are commonly blind to scaffold effects, protein-dependent remodeling, alternative co-transcriptional folding, and environmental changes in ionic conditions. Experimental probing is needed to establish the structure actually used.[^3_7]

### Full chemical identity

A canonical four-letter sequence cannot reliably report:

- Whether a cytosine is methylated or otherwise modified
- Whether RNA contains m⁶A, pseudouridine, m⁵C, editing products, or another modification
- Whether an end is phosphorylated, capped, protected by a protein, or truncated
- Whether damage or mismatches prevent processive copying
- Whether a motif that appears intact will bind the intended protein in chromatin

More than 170 chemically distinct RNA modifications have been identified, and they can affect local structure, translation, stability, localization, and RNA–protein interactions.[^3_6]

### The degree of autonomy

The sequence alone cannot establish where the autonomy boundary lies:

- A parasite RNA may look replication-negative because it has no functional replicase ORF, yet replicate when helper RNA supplies that protein.
- A self-encoded viral RNA may amplify in a permissive cell but be inert outside the correct cytoplasmic environment.
- A bacterial or plasmid replicon may function only with the appropriate initiator and cell-cycle machinery.
- An RNA molecule with a plausible catalytic motif may copy short fragments but fail to reproduce both strands repeatedly.
- A synthetic module-genome may encode all of its DNA-replication proteins but still depend on externally supplied translation machinery.

Autonomy therefore has to be defined relative to an explicit functional system, with a list of components that the molecule must regenerate and components that are permitted as raw materials.

### Recursive copying, fidelity, and persistence

Sequence cannot establish that:

- Full-length positive and negative strands are synthesized
- Products separate from templates
- Daughter molecules acquire the correct active conformation
- Replication continues after dilution or serial transfer
- Error rates remain below the information-loss threshold
- Replication outpaces nuclease attack or degradation
- The system is not simply recycling undegraded input molecules

Serial propagation is the crucial distinction between one-time amplification and inherited self-replication.

## Evidence needed to classify the molecule

A rigorous evaluation would use the sequence to design a small set of decisive experiments:

1. **Full-molecule replication assay:** Measure production of both strands or both polarities, not merely a short reporter fragment or increased protein expression.
2. **Dependency-subtraction assay:** Remove or inhibit one predicted replication function at a time. If loss of an ORF-encoded polymerase stops replication and external rescue restores it, the molecule is self-encoding rather than catalytically autonomous.
3. **Sequence-function perturbation:** Introduce synonymous or minimally disruptive mutations into a terminal motif or predicted cis-element, accompanied by rescue controls. This establishes that replication depends on a specific sequence feature rather than generalized template quantity.
4. **No-helper versus helper comparison:** Determine whether the molecule replicates without externally supplied polymerase, replicase, translation factors, or helper RNA. This also defines which auxiliary cellular functions remain indispensable.
5. **Serial-transfer test:** Dilute products into fresh substrates and follow several generations. Genuine replication should create daughter molecules that themselves retain replication competence; input persistence or one-time expression does not.
6. **Topology and terminus reconstruction:** Verify circular versus linear state, capped and uncapped variants, single- versus double-stranded form, and active 3′ ends. Replication failure may result from an incorrect physical substrate even when the primary sequence is correct.
7. **Structure and modification profiling:** Compare computed folding with chemical probing and determine methylation, caps, or other modifications in physiologically relevant molecules.
8. **Growth-error analysis:** Quantify full-length product rate, strand-release efficiency, mutation rate, and mutational survival through repeated cycles.

The practical standard is therefore **sequence-in-context**: use sequence to annotate candidate modules and dependencies, use molecular data to establish physical form and modifications, and use full-cycle experiments to measure recursive replication. A sequence can support a strong prior and identify the missing functions; it cannot, by itself, certify self-replication.

<span style="display:none">[^3_16][^3_17][^3_18][^3_19][^3_20][^3_21][^3_22][^3_23][^3_24][^3_25][^3_26][^3_27][^3_28][^3_29][^3_30][^3_31][^3_32][^3_33][^3_34]</span>

<div align="center">⁂</div>

[^3_1]: https://www.ncbi.nlm.nih.gov/books/NBK21113/

[^3_2]: https://academic.oup.com/femsre/article/36/2/408/565738

[^3_3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7122455/

[^3_4]: https://www.nature.com/articles/s41467-026-78753-w?error=cookies_not_supported\&code=9794612c-90d0-4d9a-88bf-b82b3c789182

[^3_5]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10787112/

[^3_6]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12524911/

[^3_7]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12990806/

[^3_8]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7289000/

[^3_9]: https://pmc.ncbi.nlm.nih.gov/articles/PMC13386960/

[^3_10]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12031284/

[^3_11]: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5886407/

[^3_12]: https://link.springer.com/article/10.1186/s12859-026-06562-5

[^3_13]: https://www.biorxiv.org/content/biorxiv/early/2026/01/30/2026.01.29.702604.full.pdf

[^3_14]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9318681/

[^3_15]: https://academic.oup.com/bib/article/27/3/bbag315/8711649

[^3_16]: https://academic.oup.com/bioinformatics/article/39/11/btad664/7334464

[^3_17]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3329497/

[^3_18]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9667886/

[^3_19]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12332422/

[^3_20]: https://www.sciencedirect.com/science/article/pii/B9780128139394000012

[^3_21]: https://www2.mrc-lmb.cam.ac.uk/groups/ph1/rna_self.html

[^3_22]: https://www.activemotif.com/epigenetics-101

[^3_23]: https://bioengineer.org/interpretable-dnabert-models-predict-dna-replication-origins-in-s-cerevisiae/

[^3_24]: https://link.springer.com/article/10.1007/s41048-020-00114-x

[^3_25]: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1013904

[^3_26]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2811021/

[^3_27]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8769711/

[^3_28]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10924946/

[^3_29]: https://www.sciencedirect.com/science/article/pii/S0006291X26004377

[^3_30]: https://bio.libretexts.org/Bookshelves/Biochemistry/Fundamentals_of_Biochemistry\_(Jakubowski_and_Flatt)/03:\_Unit_III-\_Information_Pathway/24:\_DNA_Metabolism/24.01:\_DNA_Replication

[^3_31]: https://thebiologyprimer.com/dna-replication

[^3_32]: https://www.khanacademy.org/science/hs-bio/x230b3ff252126bb6:gene-expression-and-regulation/x230b3ff252126bb6:dna-structure-and-replication/a/dna-replication

[^3_33]: https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2020.612086/full

[^3_34]: https://rna.bocsci.com/support/what-is-self-replicating-rna.html


---

# Question 4 — Autonomous versus dependent replication

Explain the difference between autonomous self-replication, replication dependent on external enzymes, and non-replicating nucleic-acid molecules.

The main difference is where the machinery needed to execute replication comes from and whether the replication cycle is recursive. An autonomous replicator contains the catalytic function—or the instructions for producing it—needed to copy itself; an enzyme-dependent molecule supplies only a recognized template, while a non-replicating molecule does not support a productive replication cycle in the relevant environment.

## Three categories

| Category | Source of copying activity | Contribution of the nucleic acid | Typical consequence |
| :-- | :-- | :-- | :-- |
| Autonomous self-replication | Generated by the molecule or molecular system through its own catalytic structure or encoded instructions | Information, regulatory structure, and the ability to regenerate its copying function | Daughter molecules can remain replication-competent and participate in repeated cycles |
| Enzyme-dependent replication | Supplied by a polymerase, replicase, helicase, primase, translation system, or other machinery not produced from that nucleic acid | Template information and cis-acting recognition elements such as an origin, promoter, inverted terminal repeat, or 5′/3′ replication signal | The molecule is copied only while compatible external machinery is available |
| Non-replicating nucleic acid | No compatible replication cycle is initiated in the relevant system | Carries information or performs a catalytic, structural, or regulatory role, but is not copied as a replicon | The molecule is synthesized, performs its function, and is eventually degraded without producing inherited copies |

“External raw materials” and “external machinery” should not be conflated. Even an autonomous replicator needs nucleotides, energy, ions, and suitable environmental conditions. The critical distinction is whether the system must borrow a pre-existing catalyst or whether its genetic information regenerates the catalyst. Autocatalysis in its broad chemical sense means that a reaction product helps catalyze production of more of the same product or a closed network of products. [^4_1][^4_2]

## Autonomous self-replication

In the strictest sense, self-replication requires functional closure:

$$
\text{sequence} \rightarrow \text{copying function} \rightarrow \text{copies of sequence}
$$

The copying function may arise in two ways:

- Directly, when folded RNA acts as a polymerase ribozyme or as part of an autocatalytic RNA network
- Indirectly, when nucleic-acid sequence encodes a protein polymerase or other replication proteins, which then copy the sequence

To qualify as more than one-time amplification, the system must copy the complete replicative unit, release usable products, and make daughter molecules that can support another cycle. It must also transmit its informational sequences with enough fidelity for daughter molecules to retain the relevant catalytic or coding function.

Absolute molecule independence is rare. Most so-called self-replicating viruses and experimental genomes remain dependent on cellular translation, metabolic substrates, inherited protein pools, or at minimum a physical environment. “Autonomous” is therefore best read as autonomous relative to a defined functional boundary, not as completely independent of all matter, energy, or infrastructure.

## Replication dependent on external enzymes

An enzyme-dependent molecule is replication-competent but does not regenerate the enzymes that copy it. It may contribute:

- A DNA origin or ARS-like element
- Primer or initiator-binding sites
- Plasmid iterons and DnaA-box clusters
- Viral Rep recognition sites or inverted terminal repeats
- RNA 5′ and 3′ promoters recognized by an RNA-dependent RNA polymerase
- End structures that provide a primer–template junction

A plasmid illustrates why terminology can be confusing. It is conventionally called an autonomous replicon because it replicates independently of the chromosome, separated from the chromosomal origin. Mechanistically, however, that autonomy is limited: an ARS-bearing DNA still requires appropriate host replication proteins, and plasmids generally use host polymerases, helicases, ligases, and other cellular functions. [^4_3][^4_4]

Enzyme-dependent systems can still replicate extensively and evolve. If the molecule retains the signals required by the supplied enzyme, it may become a genetic parasite. Once the host enzyme is removed, propagation stops even though the molecule’s original template sequence and recognition sites remain intact. In this sense, externally driven amplification should often be called assisted replication rather than strict self-replication. [^4_5]

A common intermediate case is self-encoded RNA. A molecule may encode a replicase that it uses after translation. It is autonomous relative to an ordinary mRNA because it carries the copying instructions, but it is not autonomous relative to the entire cell because ribosomes and numerous host factors still help produce the functioning replicase. [^4_6][^4_7]

## Non-replicating nucleic acids

A non-replicating molecule lacks an active replication cycle in its normal context. Examples include:

- Conventional mRNA
- siRNA and antisense oligonucleotides
- tRNA and many other functional RNAs
- Isolated DNA or RNA fragments without an origin or promoter
- Molecules with incorrect strandedness, topology, or terminal chemistry
- Sequences whose recognition elements are missing or incompatible with available machinery

Such molecules can bind targets, encode proteins, catalyze reactions, regulate gene expression, or serve as structural or regulatory components without producing genomic copies. Modern therapeutic RNA is commonly divided into non-replicating modalities—such as messenger RNA, siRNA, and antisense RNA—and replicating modalities such as self-amplifying or defective interfering RNA. [^4_8][^4_9]

“Non-replicating” is likewise context-relative rather than absolute. In principle, almost any isolated sequence can be copied by suitably chosen primers, templates, or polymerases in a laboratory amplification reaction. The category normally means that the molecule has no operational origin or replication pathway in the biological environment under consideration—not that no imaginable engineering system could copy it.

## Practical classification test

To classify a molecule, ask three sequential questions:

1. **Is a complete copy produced?**\
If no full-length daughter nucleic acid appears, the molecule is non-replicating in that system.
2. **Does the molecule regenerate the copying function?**\
If copying stops when externally supplied polymerase or replicase is removed, it is enzyme-dependent.
3. **Can descendants repeat the cycle?**\
If daughter molecules remain competent for further copying while only generic building blocks, energy, and environmental cycling are resupplied, the system is self-replicating under that defined boundary.

The most useful distinction is therefore not simply “copied” versus “not copied.” A non-replicating molecule performs no replication cycle, an enzyme-dependent molecule is copied by machinery it cannot reproduce, and an autonomous self-replicator closes the causal loop by regenerating both its information and its copying competence.

<span style="display:none">[^4_10][^4_11][^4_12][^4_13][^4_14][^4_15][^4_16][^4_17]</span>

<div align="center">⁂</div>

[^4_1]: https://link.springer.com/rwe/10.1007/978-3-642-11274-4_138

[^4_2]: https://pubmed.ncbi.nlm.nih.gov/21554116/

[^4_3]: https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/autonomously-replicating-sequence

[^4_4]: https://en.wikipedia.org/wiki/Plasmid

[^4_5]: https://en.wikipedia.org/wiki/Self-replication

[^4_6]: https://pmc.ncbi.nlm.nih.gov/articles/PMC13386960/

[^4_7]: https://onlinelibrary.wiley.com/doi/10.1002/smll.75396

[^4_8]: https://www.cell.com/molecular-therapy-family/nucleic-acids/pdf/S2162-2531(26)00324-0.pdf

[^4_9]: https://www.sciencedirect.com/science/article/pii/S2162253126003240

[^4_10]: https://direct.mit.edu/isal/proceedings-pdf/ecal2013/25/240/1901389/978-0-262-31709-2-ch036.pdf

[^4_11]: https://academic.oup.com/bioscience/article/63/11/877/2389920

[^4_12]: https://www.sciencedirect.com/topics/earth-and-planetary-sciences/autocatalysis

[^4_13]: https://aiche.onlinelibrary.wiley.com/doi/10.1002/aic.11842

[^4_14]: https://www.weizmann.ac.il/Organic_Chemistry/Semenov/research-activities/autocatalysis

[^4_15]: https://en.wikipedia.org/wiki/Autocatalysis

[^4_16]: https://researchoutreach.org/articles/exploring-origins-life-autocatalytic-sets/

[^4_17]: https://www.zubairkhalid.com/knowledge/molecular-biology/plasmid-replicate-independently


---

# Question 5 — Evidence of self-replication

What experimental evidence would be necessary to establish that a DNA or RNA molecule is genuinely capable of self-replication? How would you distinguish genuine replication from simple copying or amplification?

Establishing true self-replication requires evidence of a recursive, functionally closed cycle—not merely evidence that the number or signal of a nucleic acid increased. The molecule or molecular system must produce complete descendants, generate or become its own copying activity, and leave offspring that can repeat the process after the original material has been substantially diluted or removed.

A minimal template-regenerating definition is that a full-length copy is synthesized and that copy itself serves as the template or active component for a subsequent round of full-length synthesis.[^5_1]

## Required lines of evidence

### 1. Direct synthesis of complete descendants

Investigators must directly measure newly synthesized molecules rather than infer replication from a reporter signal.

The evidence should show:

- The products contain the full input sequence or defined replicative unit
- All required complementary strands or polarities are produced
- Terminal sequences, not merely internal reporter regions, are copied
- Products have the correct strandedness and molecular form
- Product abundance is quantified relative to the number and persistence of input molecules
- The products persist as full-length molecules rather than dissociating into isolated fragments

For DNA, this may require strand-specific analysis, intact-plasmid recovery, origin-to-terminus sequencing, and verification of desired topology. For RNA, it requires separate detection of plus and minus strands and exclusion of cDNA or DNA-intermediate artifacts.

Expression of a reporter protein, increase in fluorescence, or qPCR signal for a short internal amplicon is not adequate evidence. Partial amplification, recombination, transcription, repair, or sequence regeneration can increase such signals without reproducing the complete replicator.

### 2. Daughter molecules must enter the next cycle

Copying alone becomes replication only when the copied product participates in another replication cycle. A strong experiment would:

1. Generate the initial products
2. Physically or genetically exclude most of the original seed material
3. Purify or transfer a defined amount of daughter product
4. Show that the daughter, rather than residual parent, directs additional full-length descendants

The products must retain the active molecular form, not merely have the same primary sequence. An RNA polymerase ribozyme, for example, must emerge from copying in a conformation capable of polymerization; an RNA or DNA encoding a replicase must be capable of producing that replicase.

### 3. Functional closure must be demonstrated

The system needs to regenerate its own copying function.

For a directly catalytic molecule or RNA network, that means showing that:

- De novo products are catalytically active
- The measured polymerization or ligation activity increases along with product sequence
- Activity cannot be explained by carryover of the original catalyst
- Inactivating the predicted catalytic sequence blocks propagation

For an indirectly coded system, it also means showing that:

- Replication proteins are synthesized after introduction of the nucleic acid
- Those proteins originate from the tested nucleic acid rather than contamination or helper molecules
- The nucleic acid is subsequently copied by its own encoded products
- Frameshift, catalytic-site, or translation-blocking mutations interrupt the cycle
- External complementation restores replication when the corresponding gene or protein is supplied

An engineered module-genome encoding 26 DNA-replication proteins illustrates this logic: the DNA is transcribed and translated, and the resulting proteins copy the DNA that encoded them. It is functionally self-encoding even though amino acids, tRNAs, and the tail-to-protein system are externally supplied.[^5_2]

### 4. Serial transfer must rule out parent carryover

One round of synthesis does not establish self-replication. Products need to survive repeated transfer into fresh substrates.

A rigorous design records:

- Initial active-molecule count
- Transfer fraction
- Number and activity of molecules recovered in the next vessel
- Fold increase per cycle
- Total dilution of the parent
- Product sequence and activity after each transfer
- No-template and no-seed controls

If a reaction transfers 1% of the product to each new vessel, after four transfers the theoretical parent carryover is one part in $10^8$, before accounting for degradation. Recovery of substantially more active sequence above that limit is much stronger evidence for regeneration than a single multiplication measurement.

Cross-replicating RNA enzymes provide a useful benchmark. They catalyzed each other’s synthesis from four substrates, doubled approximately once per hour, and remained in exponential growth through serial transfers. Continuation depended on fresh component substrates, while neither initial enzyme nor a preformed protein polymerase had to be resupplied. One reported transfer series survived more than $10^{25}$-fold cumulative amplification, with recombinant variants ultimately emerging and replacing the parental population.[^5_3]

Such serial transfers demonstrate inheritance of functional structure, but they do not themselves show that every original molecule retained the identical sequence. Long-term transfer should therefore be paired with genotype-specific sequencing and fidelity measurement.

### 5. Inheritance and fidelity must connect information to function

A genuine replicator transmits information in addition to increasing concentration. Evidence should include:

- Sequence comparison of input and descendants across multiple rounds
- Measurement of substitutions, insertions, deletions, and recombination
- Parallel propagation of distinguishable sequence variants
- Evidence that variant changes alter replication rate in a heritable way
- Confirmation that daughter products retain the required coding regions, terminal motifs, and catalytic structures

A product that becomes shorter after every round, progressively loses terminal sequences, or generates sequence copy through nonspecific concatenation is not faithfully inheriting the original information.

Replication fidelity need not be high enough to prevent all variation. It must be sufficient for functional descendants to persist frequently enough to sustain the lineage. In an autonomous tRNA-like hybridization system, measured per-nucleotide fidelity of roughly 85–90% was already adequate to propagate designed binary information through repeated thermal cycles.[^5_4]

### 6. Replication must outpace loss

Persistence under dilution is evidence only if net production exceeds degradation and transfer loss. The experiment should measure:

- Chemical or enzymatic degradation rate
- Loss during purification and transfer
- Net birth rate in fresh substrates
- Reaction inactivation as substrates are exhausted
- Population growth over several successive cycles

A lineage can be genuinely self-replicating without becoming abundant; abundance can be limited by resources or strongly concentration-dependent reactions. The essential test is whether the system can maintain or increase its informational and catalytic population under the intended non-equilibrium conditions.

## Distinguishing the situations

| Feature | Simple copying | Externally driven amplification | Genuine self-replication |
| :-- | :-- | :-- | :-- |
| Primary observation | A copy of some or all of the input is made | Concentration or signal increases, sometimes exponentially | Descendant molecules regenerate information and copying competence |
| Copying function | Supplied and maintained externally | Supplied repeatedly by the machine, enzyme, reaction protocol, host, or operator | Produced by the original nucleic acid or regenerated functionally closed network |
| Product role | Can be a molecular dead end | Serves successive cycles only while the external amplification system remains active | Products initiate later cycles and remain replication-competent |
| Recursion | More commonly one copying operation | Repeated copying can occur, but the causal center remains external | Repeated unless resources are exhausted |
| Heritability | Often present for one generation | May preserve sequence during technical amplification | Sequence variants and biological function are transmitted through descendants |
| Consequence of removing the externally supplied catalyst | Incomplete cycle continues only if the pre-existing product already exists | Amplification stops | No effect unless that catalyst is genuinely part of the permitted raw-material environment |
| Example interpretation | A full-length transcript synthesized using externally supplied RNA polymerase | PCR or rolling-circle amplification driven by added polymerase and scheduled thermocycling | RNA product acts as polymerase or produces a polymerase whose activity copies the original RNA |

An exponential increase alone is not decisive. Autocatalytic systems often display an acceleration phase because each product increases reaction rate, but exponential kinetics can also arise from externally programmed amplification, cross-catalytic helper systems, or expansion of catalytic activity without template-based sequence inheritance.[^5_5][^5_6]

Conversely, absence of exponential growth is not necessarily fatal. Template–product inhibition can yield subexponential or parabolic growth even though the underlying chemistry is self-replicating. Exponential expansion is evidence favoring productive closure and strand reuse; functional recursion and information inheritance are more decisive than the exact kinetic exponent.[^5_6]

## Controls needed for a self-replication claim

A convincing experiment should include controls that address both biological and chemical alternative explanations.

### Input and artifact controls

- Reaction without the putative replicator detects spontaneous synthesis from substrates
- Reaction without activated nucleotides or necessary raw inputs detects residual carryover
- Specific nuclease destruction of input and products confirms the claimed nucleic-acid class
- Heat-inactivated or catalytically inactive replicator tests the requirement for function
- Sequencing rules out contamination, recombination, unwanted helper molecules, and DNA intermediates


### Function-subtraction controls

- Delete or frameshift an encoded polymerase or replicase while retaining the terminal recognition motifs
- Mutate the predicted catalytic core without changing template accessibility
- Mutate a terminal origin or recognition sequence while preserving its coding information
- Supply proteins already present in the experimental source, such as suspected contaminating polymerase, in a controlled comparison
- Rescue the defective molecule with a trans-supplied version of the disrupted function

These experiments establish whether the nucleic acid, not an unmeasured component, supplies functional closure.

### Product-specific controls

- Distinguish de novo product from degraded or recycled input using sequence-tagged variants
- Quantify products by orthogonal methods, such as size-resolved analysis, sequencing-based end mapping, and direct molecular counting
- Use affinity capture to remove input before daughter generation, followed by sequence-specific recovery of progeny
- Show that purified descendants remain active after disruption of initial template–product duplexes when duplex separation is part of the mechanism
- Use negative controls against spurious signal from recombination or polymerase template switching


### Claim-specific controls

A protein-free RNA claim must demonstrate that no protein polymerase, translation machinery, or DNA intermediate is necessary. A DNA–protein self-replication claim should allow externally supplied raw amino acids and nucleotides but must show that replication proteins are produced from the DNA being replicated.

Physical environmental cycling is not inherently disqualifying. For example, temperature, freezing and thawing, evaporation, pH changes, or periodic substrate resupply may perform work such as strand separation and substrate renewal. Such cycling is analogous to feeding material and energy into the system; it excludes neither copying nor replication if the inherited nucleic acid governs the information-transfer reaction.[^5_7]

## Interpretation standard

The strongest conclusion would have this causal form:

1. The input nucleic acid produces a copying capacity or is itself active.
2. The copying capacity reproduces the complete nucleic-acid unit.
3. Daughter molecules structure themselves into functionally active states.
4. Daughters again generate or become copying activity.
5. This loop persists after parent dilution and resupplying generic substrates.
6. Sequence and function remain stably associated across descendants.

Recent protein-free RNA replication using an RNA polymerase ribozyme plus pH and freeze–thaw cycling illustrates these distinct requirements. Investigators showed full-length synthesis of both plus and minus strands, reuse of cycle-1 products as cycle-2 templates, exponential production of both strands through repeated cycling, and growth after serial dilution. The environment provided strand-separation and substrate-renewal work, but template-directed copying was performed by the RNA ribozyme rather than a protein enzyme.[^5_7]

Finally, cross-replication should be assigned to the correct unit. A cross-chiral system in which D- and L-RNA enzymes assemble each other can replicate indefinitely, even though neither partner self-replicates alone. That is evidence for a closed molecular replicator system, not for the isolated autonomy of either strand.[^5_5]

Accordingly, the decisive difference is:

- **Simple copying:** external activity produces one or more copies of the molecule.
- **Amplification:** external protocols or catalysts increase the number of copies, possibly recursively.
- **Genuine self-replication:** the nucleic-acid information regenerates its own replication capacity, produces complete replication-competent descendants, and transmits that capacity through repeated cycles.

<span style="display:none">[^5_10][^5_11][^5_12][^5_13][^5_14][^5_15][^5_16][^5_8][^5_9]</span>

<div align="center">⁂</div>

[^5_1]: https://www.science.org/doi/10.1126/science.aay0688

[^5_2]: https://academic.oup.com/nar/article/54/13/gkag663/8724181

[^5_3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2652413/

[^5_4]: https://elifesciences.org/articles/63431

[^5_5]: https://www.pnas.org/doi/10.1073/pnas.2413668121

[^5_6]: https://pmc.ncbi.nlm.nih.gov/articles/PMC164461/

[^5_7]: https://www.nature.com/articles/s41557-025-01830-y

[^5_8]: https://www.nature.com/articles/s41417-022-00435-8

[^5_9]: https://www.nature.com/articles/s42003-026-10372-z

[^5_10]: https://pubs.acs.org/jacsat/article/142/9/4184/1430609/Spontaneous-Emergence-of-Self-Replicating

[^5_11]: https://wires.onlinelibrary.wiley.com/doi/pdf/10.1002/wrna.1803

[^5_12]: https://www.tandfonline.com/doi/full/10.1080/15476286.2024.2405757

[^5_13]: https://www.medboundtimes.com/biotechnology/cambridge-rna-origins-of-life-discovery

[^5_14]: https://www.mdpi.com/2075-1729/11/4/308

[^5_15]: https://febs.onlinelibrary.wiley.com/doi/10.1002/1873-3468.14507

[^5_16]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7122455/

