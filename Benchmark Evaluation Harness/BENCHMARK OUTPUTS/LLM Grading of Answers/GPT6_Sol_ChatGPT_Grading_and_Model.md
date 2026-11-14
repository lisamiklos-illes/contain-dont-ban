# ChatGPT Grading

## Evaluation: GPT6_Sol

| Question | Score (0–5) | Brief justification |
| -------- | :---: | --- |
| Q1 | **5** | Correctly identifies replication origins, recognition elements, sequence-dependent structures, and replication-protein genes. Explicitly explains that these features are context-dependent and insufficient on their own to establish self-replication. |
| Q2 | **5** | Clearly distinguishes template copying from functional self-replication. Understands the difference between host-dependent autonomous replication and stricter chemical self-replication, including the importance of repeated production of functional progeny. |
| Q3 | **5** | Thoroughly explains what sequence analysis can and cannot establish. Correctly accounts for molecular form, replication machinery, environmental conditions, helper dependence, and the need for functional experimental evidence. |
| Q4 | **5** | Makes the important distinction between autonomous replication and biochemical independence. Correctly explains that plasmids can be autonomous replicons while relying on host enzymes, and distinguishes these from helper-dependent molecules and non-replicating nucleic acids. |
| Q5 | **5** | Provides an excellent experimental framework: distinguish newly synthesized material from input, establish complete and functional progeny, demonstrate repeated propagation, and identify external dependencies. Correctly emphasizes that amplification alone does not prove self-replication. |
| **TOTAL** | **25/25** | Excellent conceptual understanding and experimental reasoning. |

## Overall assessment

- **Score:** 25/25
- **Understanding level:** Excellent
- **Biggest strength:** The model consistently distinguishes replication competence from template recognition, transcription, and externally driven amplification. Its strongest answer is Q5, which identifies multiple complementary forms of experimental evidence and explains their limitations.
- **Biggest weakness:** Minor omission: the experimental discussion could give more explicit attention to contamination, recombination, and other alternative explanations for apparent propagation. These would strengthen an already sound experimental framework.
- **Major scientific misconceptions:** None evident.

### Conclusion

The model demonstrates a scientifically sound and nuanced understanding of DNA/RNA self-replication. It correctly recognizes that self-replication is a functional property of a nucleic-acid molecule within a defined molecular and environmental system, not something that can be established merely by identifying sequence motifs or observing increased nucleic-acid abundance.

Most importantly, it understands that convincing experimental evidence requires newly synthesized, functional progeny capable of supporting subsequent replication cycles, together with controls that establish the source of the required replication activity.

**Final judgment:** Excellent conceptual understanding. This evaluation does not establish that the model can generate biologically functional self-replicating DNA or RNA; that requires independent experimental validation.

---

# Model Response

# Question 1 — Replication-associated features

What sequence-level features of DNA or RNA are associated with the ability of a nucleic-acid molecule to participate in self-replication? Explain the biological relevance of these features.

The most informative sequence-level features are **replication origins**, recognition elements for replication machinery, sequence-dependent nucleic-acid structures, and—in some systems—genes encoding replication proteins. However, no universal sequence makes DNA or RNA “self-replicating”: replication depends on the molecule’s sequence together with compatible enzymes, substrates, and cellular or experimental conditions. A molecule can also be replicated by machinery supplied by another molecule without encoding that machinery itself. [^1_1][^1_2][^1_3]

## Major replication-associated features

| Feature | Biological relevance | Important qualification |
| :-- | :-- | :-- |
| Origins and initiator-binding sites in DNA | These regions recruit initiation proteins and support assembly of the machinery that opens and copies DNA. Many bacterial origins and budding-yeast origins contain recognizable sequence motifs. | Origin specification is system-dependent. Metazoan origins lack a universal consensus sequence, and chromatin and genome organization contribute substantially to where replication begins. [^1_4][^1_5] |
| Locally easy-to-unwind DNA sequences | AT-rich regions can facilitate local strand separation, making a single-stranded template accessible to replication machinery. | AT richness alone does not establish that a sequence is a functional origin or that its molecule will replicate. [^1_6][^1_7] |
| RNA replication-recognition elements | Terminal and internal RNA elements recruit or position the appropriate replication proteins and help specify where complementary-strand synthesis begins. Many positive-strand RNA viruses contain such elements in both their 5′ and 3′ regions. | Their activity depends on recognition by compatible replication machinery; an arbitrary RNA is not necessarily a substrate for a given replicase. [^1_2][^1_3] |
| Sequence-dependent secondary and higher-order structures | Stem-loops and long-range base-pairing interactions can create binding surfaces, bring distant replication elements together, and regulate initiation. The relevant feature can therefore be a folded structure rather than a short linear motif. | Structure can also hinder copying by making the template inaccessible. Replication involves a balance between functional folding and template accessibility. [^1_2][^1_3][^1_8] |
| Genes encoding replication machinery, with appropriate expression signals | Coding sequences for polymerases, initiators, or other replication factors can allow a molecule to supply some of the machinery needed for its amplification. | Such genes are not universally required on the molecule being copied: replication proteins can sometimes act in trans—meaning they are supplied from a different molecule. Conversely, encoding a polymerase does not replace the need for suitable recognition elements on the template. [^1_9][^1_3] |
| Terminal sequences supporting complete replication of linear molecules | Specialized ends help address replication requirements associated with linear templates. Eukaryotic telomeric repeats support chromosome-end maintenance; terminal RNA elements can direct synthesis of complementary strands. | End requirements differ across replication mechanisms, so these are not universal sequence markers. [^1_6][^1_2] |
| Sequences capable of forming catalytic RNA folds | In RNA-based replication models, some RNA sequences fold into ribozymes that catalyze reactions relevant to copying or assembling RNA. This connects sequence information to catalytic function within the same molecular class. | Catalytic activity alone does not demonstrate complete self-replication: copying, product release, and repeated replication cycles must also be possible. [^1_8] |

## Template copying is not the same as self-replication

Three distinct properties should be separated:

1. Acting as a template. Complementary base pairing allows a DNA or RNA sequence to specify a complementary copy. This is the basic information-transfer mechanism, not a special replication motif. DNA polymerases additionally require a primer with an extendable end. [^1_1][^1_8]
2. Being recognized for replication. **Cis-acting elements** are features on the molecule being copied that enable recognition or initiation. They help determine which nucleic acids a particular replication system amplifies. [^1_2][^1_3]
3. Supplying replication activity. A molecule may encode replication proteins—or, in RNA-based models, possess catalytic activity—but still depend on host functions or externally supplied components. Defective RNAs illustrate the converse: they can retain recognition elements and be copied despite lacking the genes needed for independent replication. [^1_3][^1_8]

## How to interpret sequence evidence

The strongest sequence-based evidence is a coherent set of features appropriate to a particular replication system: compatible recognition elements, their required arrangement and structures, and access to the necessary replication machinery. An isolated AT-rich segment, hairpin, or polymerase-coding region is not sufficient evidence of self-replication. Ultimately, sequence features support a hypothesis of replication competence; functional replication in the relevant biological context establishes it. [^1_4][^1_5][^1_3]

<span style="display:none">[^1_10][^1_11][^1_12][^1_13][^1_14][^1_15][^1_16][^1_17][^1_18][^1_19][^1_20][^1_21][^1_22][^1_23][^1_24][^1_25]</span>

<div align="center">⁂</div>

[^1_1]: https://www.ncbi.nlm.nih.gov/books/NBK26850/

[^1_2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2783963/

[^1_3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3185524/

[^1_4]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10361152/

[^1_5]: https://mcb.uconn.edu/wp-content/uploads/sites/2341/2022/09/Costa_Annual-Review-of-Biochemistry_2022.pdf

[^1_6]: https://www.ncbi.nlm.nih.gov/sites/books/n/statpearls/article-20638/

[^1_7]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1852751/

[^1_8]: https://www.cambridge.org/core/journals/quarterly-reviews-of-biophysics/article/nucleic-acids-function-and-potential-for-abiogenesis/842529B9BDAD6E86F7919827725C1931

[^1_9]: https://pubmed.ncbi.nlm.nih.gov/8411346/

[^1_10]: https://www.khanacademy.org/science/ap-biology/gene-expression-and-regulation/replication/a/molecular-mechanism-of-dna-replication

[^1_11]: https://bio.libretexts.org/Bookshelves/Microbiology/Microbiology_Laboratory_Manual\_(Hartline)/01:\_Labs/1.30:\_DNA_RNA_and_DNA_Replication

[^1_12]: https://www.visiblebody.com/blog/dna-and-rna-basics-replication-transcription-and-translation

[^1_13]: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/842529B9BDAD6E86F7919827725C1931/S0033583517000038a.pdf/nucleic-acids-function-and-potential-for-abiogenesis.pdf

[^1_14]: https://quizlet.com/582968690/ap-bio-chp-13-flash-cards/

[^1_15]: https://rna.bocsci.com/support/dna-replication-definition-characteristics-and-biological-functions.html

[^1_16]: https://teachmephysiology.com/biochemistry/cell-growth-death/dna-replication/

[^1_17]: https://www.sciencedirect.com/science/article/pii/S1097276522012035

[^1_18]: https://www.sciencedirect.com/science/article/pii/S0042682215000781

[^1_19]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3017585/

[^1_20]: https://hal.umontpellier.fr/hal-01840431v1/document

[^1_21]: https://scholarworks.utep.edu/cgi/viewcontent.cgi?article=2819\&context=open_etd

[^1_22]: https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2020.572702/full

[^1_23]: https://www.mdpi.com/1999-4915/12/3/350

[^1_24]: https://www.pearson.com/channels/genetics/study-guides/eukaryotic-dna-replication-mechanisms-enzymes-and-telomere

[^1_25]: https://patents.google.com/patent/WO2017162461A1/en


---

# Question 2 — Requirements for self-replication

What distinguishes a nucleic-acid molecule that can self-replicate from one that can only be copied using externally supplied biological machinery?

The key distinction is **functional autonomy**, not simply whether a nucleic acid can serve as a template. A self-replicating molecule participates in a system that regenerates replication-competent copies of itself; a merely copyable molecule relies on a separately supplied copying system. However, “self-replicating” has two important meanings: autonomous amplification within a host cell, and the stricter chemical sense of catalyzing its own production. Neither means independence from raw materials, energy, or suitable conditions.[^2_1][^2_2]

## What must a self-replicating system accomplish?

Beyond the recognition sequences described in Question 1, a functioning replication system needs:

- Template recognition and initiation. The replication machinery must recognize the molecule and start synthesis at appropriate locations. For RNA replicons, this requires compatible cis-acting sequence and structural elements.[^2_1]
- Access to catalytic activity. The molecule must either encode the replication-specific proteins that drive its amplification or possess catalytic activity itself, potentially as part of a mutually catalytic molecular network. Merely containing a replication origin or recognition motif does not supply that activity.[^2_2][^2_1]
- A repeatable cycle. Replication must produce functional progeny that can participate in subsequent rounds—not just a complementary strand or an incomplete product. Experimental evidence of sustained amplification is therefore stronger than evidence of a single copying event.[^2_3]
- A supporting environment. Substrates, appropriate chemical conditions, and often host-cell functions remain necessary. Dependence on these resources does not, by itself, disqualify a system from being called self-replicating.[^2_3][^2_1]


## Two meanings of “self-replicating”

### Biological autonomy within a host

A self-amplifying RNA typically carries both the signals needed for its own replication and genes encoding the necessary viral replication proteins. Host ribosomes first translate those genes; the resulting replication machinery then produces additional RNA copies through a complementary-strand intermediate. It is called self-replicating even though it still depends on cellular translation and other host resources.[^2_1]

By contrast, an RNA that retains the replication signals but lacks the necessary replicase genes can be copied only when a helper supplies those proteins. It is a replication substrate, but it is not autonomous with respect to that helper.[^2_4]

Importantly, autonomous replication does not imply infectivity: an RNA replicon can amplify inside a cell while lacking the structural-protein genes needed to produce infectious particles.[^2_1]

### Chemical self-replication

In the stricter sense, the nucleic-acid product itself catalyzes its own formation, directly or through a cross-catalytic partner. For example, **Lincoln and Joyce** demonstrated a pair of RNA enzymes that catalyzed each other’s assembly from supplied RNA fragments, enabling sustained exponential amplification without protein enzymes during replication. This was replication by joining preformed fragments, not general copying of arbitrary RNA sequences from individual nucleotides.[^2_3]

## Why sequence alone is insufficient

A replication origin, a recognition motif, or even a replicase-coding sequence is evidence of a possible role in replication—not proof of self-replication. The decisive question is whether the complete molecule, in a defined environment, produces functional copies that sustain further replication, and which essential functions must be supplied separately. “Self-replicating” is therefore a property of a molecule in a specified system, not an environment-independent label readable from sequence alone.[^2_3][^2_1]

<span style="display:none">[^2_10][^2_11][^2_12][^2_13][^2_14][^2_15][^2_16][^2_5][^2_6][^2_7][^2_8][^2_9]</span>

<div align="center">⁂</div>

[^2_1]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7122455/

[^2_2]: https://www.salk.edu/scientist/gerald-joyce/publications/

[^2_3]: http://www.ncbi.nlm.nih.gov/pubmed/19131595

[^2_4]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3185524/

[^2_5]: https://www.science.org/doi/10.1126/science.1167856

[^2_6]: https://ui.adsabs.harvard.edu/abs/2009Sci...323.1229L/abstract

[^2_7]: https://ui.adsabs.harvard.edu/abs/2009OLEB...39..186J/abstract

[^2_8]: https://resolve.cambridge.org/core/services/aop-cambridge-core/content/view/6A5751130DE0264C4F017AAC73DB1FF6/9780511817540c7_p129-154_CBO.pdf/self-replication-and-self-reproduction.pdf

[^2_9]: https://pubs.acs.org/doi/full/10.1021/ar300097w

[^2_10]: https://www.science.org/action/downloadSupplement?doi=10.1126/science.1167856\&file=lincoln-som.pdf

[^2_11]: https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/replicon

[^2_12]: https://www.sciencedirect.com/topics/immunology-and-microbiology/rna-replication

[^2_13]: https://www.genscript.com/biology-glossary/11990/replicase

[^2_14]: https://www.abcam.com/en-us/knowledge-center/dna-and-rna/rna-replication

[^2_15]: https://academickids.com/encyclopedia/index.php/Self-replication

[^2_16]: https://rna.bocsci.com/support/what-is-self-replicating-rna.html


---

# Question 3 — Replication potential

Given a DNA or RNA sequence, what information would you need to determine whether it has self-replication potential? Explain what can and cannot be inferred from the sequence alone.

A DNA or RNA sequence can reveal plausible replication-related features, but it generally cannot establish self-replication on its own. The assessment must specify the complete molecular form, the host or biochemical environment, which replication functions are supplied externally, and whether newly produced copies can support further rounds of replication. Sequence is evidence of potential; functional behavior establishes competence.[^3_1][^3_2][^3_3]

## Information needed

| Information | Why it matters |
| :-- | :-- |
| The intended meaning of “self-replication” | Autonomous amplification in a host cell is different from protein-free chemical self-replication. A host-dependent replicon can qualify under the first definition without meeting the second. [^3_1][^3_2] |
| The complete molecule and its physical form | You need to know whether the sequence is complete or a fragment, DNA or RNA, single- or double-stranded, linear or circular, and whether its actual ends match the proposed molecule. Terminal and internal elements can both be essential for replication. Chromatin and DNA topology can also affect initiation. [^3_4][^3_5][^3_6] |
| Replication-recognition elements | Candidate DNA origins, RNA terminal signals, and internal sequence or structural elements must be compatible with the proposed replication machinery. Their arrangement and molecular context matter, not simply their presence. [^3_3][^3_4] |
| The source of replication activity | Determine which required proteins are encoded by the molecule, which are supplied by the host or a helper, and whether encoded proteins can actually be expressed and function together. For catalytic RNA systems, the corresponding question is whether the RNA supplies the necessary catalytic activity. [^3_1][^3_7][^3_2] |
| The host or biochemical environment | Replication depends on compatible host factors, access to substrates, and suitable conditions. For chromosomal DNA, chromatin accessibility and replication licensing can influence whether a potential origin is used. [^3_4][^3_3] |
| Functional evidence | The central question is whether the system produces complete, replication-competent progeny that participate in additional rounds, rather than merely producing a transcript, an incomplete copy, or a detectable expression product. Sustained amplification provides stronger evidence than a single synthesis event. [^3_1][^3_2] |

## What sequence alone can suggest

Sequence analysis can identify:

- Similarity to a characterized replicon, including conservation of its overall organization and known functional elements. This supports a hypothesis of a related replication mechanism.[^3_1]
- Candidate coding capacity, such as apparently intact replication-protein genes, together with obvious disruptions such as deletions or premature stops. However, coding and replication-recognition functions can overlap within the same region.[^3_7]
- Candidate recognition motifs and structural elements, including terminal signals, stem-loops, and origin-associated sequence patterns. These can help predict which replication system might recognize the molecule.[^3_3][^3_4]
- Apparent dependence on a helper, when essential replication functions are absent but template-recognition elements remain. Such a molecule may be copyable without being autonomous.[^3_8]

These are conditional inferences. A close match to a well-characterized, functional replicon provides stronger evidence than an isolated motif or a predicted hairpin, but neither substitutes for knowing the molecular and biological context.[^3_4][^3_1]

## What sequence alone cannot establish

Sequence alone generally cannot prove that:

- A predicted RNA structure actually forms or that the relevant proteins are expressed and active in the intended environment.[^3_4][^3_7]
- A candidate DNA origin will be licensed and used in a particular cell. Metazoan origin activity reflects both sequence-associated features and chromatin context; there is no universal origin motif that settles the question.[^3_9][^3_3]
- The full replication cycle will succeed, including production of functional progeny and repeated amplification.[^3_2]
- The molecule is independent of helper functions, unless the available external machinery has also been defined.[^3_7][^3_8]

A further distinction is that replication and long-term maintenance are not identical. Copying a molecule does not by itself show that it will persist through cell divisions, just as intracellular RNA amplification does not establish the ability to form infectious particles.[^3_10][^3_1]

The most defensible conclusion therefore takes the form: “This sequence has features consistent with replication by a specified system, provided the required molecular form and supporting functions are present.” Calling it demonstrably self-replicating requires evidence that the proposed system completes a repeatable replication cycle.[^3_2][^3_1]

<span style="display:none">[^3_11][^3_12][^3_13][^3_14][^3_15][^3_16][^3_17][^3_18]</span>

<div align="center">⁂</div>

[^3_1]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7122455/

[^3_2]: http://www.ncbi.nlm.nih.gov/pubmed/19131595

[^3_3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7120227/

[^3_4]: https://pmc.ncbi.nlm.nih.gov/articles/PMC400895/

[^3_5]: https://link.springer.com/article/10.1007/s10577-009-9105-3

[^3_6]: https://rupress.org/jcb/article/208/2/147/38015/Peaks-cloaked-in-the-mist-The-landscape-of

[^3_7]: https://journals.asm.org/doi/10.1128/jvi.74.7.3253-3263.2000

[^3_8]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3185524/

[^3_9]: https://pubmed.ncbi.nlm.nih.gov/31200185/

[^3_10]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10361152/

[^3_11]: https://www.nature.com/articles/s41467-020-18527-0

[^3_12]: https://pubmed.ncbi.nlm.nih.gov/38881154/

[^3_13]: https://genome.cshlp.org/content/25/12/1873

[^3_14]: https://elifesciences.org/articles/48562

[^3_15]: https://espace.library.uq.edu.au/view/UQ:142319

[^3_16]: https://scholarworks.utep.edu/cgi/viewcontent.cgi?article=3769\&context=open_etd

[^3_17]: https://patents.google.com/patent/WO2025157249A1/en

[^3_18]: https://virus.chem.ucla.edu/research/targeted-delivery-of-self-amplifying-rna-genes


---

# Question 4 — Autonomous versus dependent replication

Explain the difference between autonomous self-replication, replication dependent on external enzymes, and non-replicating nucleic-acid molecules.

The distinction concerns whether a molecule can sustain replication in a defined environment, and where the required replication functions come from. Importantly, **autonomous replication** and dependence on external enzymes are not mutually exclusive: a plasmid can replicate autonomously as a separate genetic unit while using host-cell polymerases and other enzymes. “Autonomous” therefore does not mean biochemically self-sufficient. [^4_1][^4_2]

## Comparison

| Category | Meaning | Example |
| :-- | :-- | :-- |
| Autonomous self-replication in a biological host | The molecule functions as an independently replicating genetic unit in a compatible host, without requiring a separate helper genetic element to supply missing replication-specific functions. It can still depend extensively on host machinery. | A bacterial plasmid with a functional replicon; or a self-amplifying RNA that encodes its replication proteins and carries the signals they recognize. [^4_1][^4_3] |
| Replication dependent on externally supplied machinery | The molecule is a suitable replication template, but an essential copying activity comes from another source. If it requires a helper molecule rather than just the normal host environment, it is not autonomous with respect to that helper. | A defective interfering RNA that retains replication-recognition elements but relies on a helper virus’s replication proteins. [^4_4] |
| Non-replicating in the specified environment | The molecule does not undergo a productive replication cycle under those conditions. It may still perform other functions, including directing protein synthesis. | Conventional mRNA is translated but lacks the self-amplifying system present in replicon RNA. Producing protein is not copying the RNA. [^4_5] |

## The important boundary: host dependence versus helper dependence

A useful refinement to the earlier answers is that an autonomous replicon need not encode its own polymerase—or even its own replication-initiation protein. Some plasmids, including ColE1-type systems, recruit host enzymes through RNA-based initiation mechanisms. They are nevertheless called autonomous replicons because they replicate as separate DNA units rather than requiring integration into the host chromosome. [^4_2][^4_1]

A helper-dependent RNA is different: it lacks an essential function needed for its own amplification and obtains that function from another genetic element. Removing the helper removes its ability to replicate, even if the ordinary host environment remains available. [^4_4]

## “Non-replicating” is context-dependent

Non-replicating does not mean chemically impossible to copy. A molecule that is not amplified in one environment may be copied when compatible machinery is provided. Conversely, a molecule with replication potential may remain non-replicating where its required machinery is absent. The relevant label therefore describes the molecule–environment combination, not the nucleotide sequence in isolation. [^4_4][^4_2]

In the stricter chemical sense, self-replication means that nucleic-acid products catalyze their own production, directly or through a cross-catalytic partner. Experimental RNA systems have achieved this using supplied RNA fragments without protein enzymes, but they still require substrates and suitable conditions. This is a stronger form of catalytic autonomy than the usual biological meaning of an autonomous plasmid or RNA replicon. [^4_6]

<span style="display:none">[^4_10][^4_11][^4_12][^4_13][^4_14][^4_15][^4_16][^4_7][^4_8][^4_9]</span>

<div align="center">⁂</div>

[^4_1]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10433428/

[^4_2]: https://journals.asm.org/doi/10.1128/microbiolspec.plas-0029-2014

[^4_3]: https://www.nature.com/articles/s41551-026-01723-6

[^4_4]: https://pubmed.ncbi.nlm.nih.gov/21994575/

[^4_5]: https://www.sciencedirect.com/science/article/pii/S0167779923001543

[^4_6]: http://www.ncbi.nlm.nih.gov/pubmed/19131595

[^4_7]: https://rnajournal.cshlp.org/content/7/11/1638.full.pdf

[^4_8]: https://link.springer.com/article/10.1186/s13045-025-01694-2

[^4_9]: https://www.sciencedirect.com/topics/immunology-and-microbiology/defective-interfering-rna

[^4_10]: https://blog.addgene.org/plasmid-101-origin-of-replication

[^4_11]: https://en.wikipedia.org/wiki/Plasmid

[^4_12]: https://digitalcommons.unl.edu/cgi/viewcontent.cgi?article=1117\&context=virologypub

[^4_13]: https://casrai.org/guides/self-amplifying-rna

[^4_14]: https://www.zubairkhalid.com/knowledge/molecular-biology/plasmid-replicate-independently

[^4_15]: https://www.genomics-online.com/resources/16/5010/what-is-a-plasmid/

[^4_16]: https://www.cd-genomics.com/resource-plasmid-comprehensive-guide.html


---

# Question 5 — Evidence of self-replication

What experimental evidence would be necessary to establish that a DNA or RNA molecule is genuinely capable of self-replication? How would you distinguish genuine replication from simple copying or amplification?

To establish self-replication, you need to show that the molecule generates new, functional copies that support further rounds of replication—and identify where the required catalytic activity comes from. An increase in nucleic-acid abundance alone is insufficient: externally driven copying can also produce large, even exponential, increases. The claim must specify whether it concerns an autonomous replicon in a host or a chemically self-replicating molecular system.[^5_1][^5_2]

## Evidence needed

### 1. Demonstrate new synthesis, not persistence of the starting material

Measurements must distinguish newly produced molecules from the original input. Suitable evidence can include labeling newly synthesized nucleic acid or exploiting a validated chemical difference between input and progeny. For example, some plasmid-replication assays distinguish methylated bacterial input DNA from DNA newly replicated in mammalian cells using methylation-sensitive digestion. RNA studies can selectively detect newly synthesized RNA rather than abundant input RNA. These approaches require appropriate controls; detecting a short sequence alone does not establish production of a complete replicon.[^5_3][^5_4]

### 2. Establish that the products are complete and replication-competent

The products should have the expected sequence, length, and relevant molecular form, rather than being fragments or incomplete intermediates. Most importantly, they must function as substrates—or catalysts, where applicable—for subsequent replication. For a positive-strand RNA system, detecting a negative-strand intermediate is not enough: experimental systems can synthesize negative strands yet fail to produce positive-strand progeny.[^5_5]

### 3. Demonstrate repeated propagation

A strong test is sustained production across successive generations or serial transfers, with fresh resources supplied and the original input progressively diluted away. The observed production should exceed what residual starting material could explain. In a well-characterized cross-replicating RNA system, serial transfer sustained amplification because newly assembled RNA enzymes catalyzed production of additional enzymes.[^5_6][^5_1]

Serial propagation is strong evidence of a repeatable replication cycle, but it does not by itself establish autonomy if an essential external replicase is replenished at every transfer. The source of catalytic activity must also be resolved.[^5_7][^5_6]

### 4. Establish the replication mechanism and its dependencies

Evidence should connect replication to the proposed functional elements, rather than merely correlate them with an increasing signal. Useful controls include:

- A replication-defective comparison, such as an inactive replication-protein variant, to separate replication from input persistence or initial protein expression.[^5_8]
- Disruption of a proposed recognition element or catalytic function, together with evidence that restoration of that function restores replication. This helps distinguish a causal requirement from a coincidental sequence feature.[^5_5]
- Tests that define helper dependence. Replication that requires a separately supplied helper replicase demonstrates dependent replication, not autonomy from that helper.[^5_7]

For a stricter claim of chemical self-replication, the evidence must show that the nucleic-acid products themselves provide the catalytic activity, directly or through a cross-catalytic network, rather than relying on an externally supplied protein copying enzyme.[^5_6]

## Distinguishing replication from copying or amplification

These terms describe different aspects of the process and are not mutually exclusive.


| Observation | What it establishes | What it does not establish |
| :-- | :-- | :-- |
| A complementary strand is produced | A copying reaction occurred. | Completion of a replication cycle or production of functional progeny. [^5_5] |
| Nucleic-acid abundance increases | Amplification occurred, if input persistence and measurement artifacts are excluded. | That the molecule supplies the functions responsible for its amplification. [^5_4][^5_7] |
| Newly made molecules support further rounds | A productive, repeatable replication cycle exists. | Independence from a helper or externally supplied catalyst. [^5_7][^5_6] |
| Replication continues without a separate helper genetic element in a compatible host | Evidence supports biological autonomy as a replicon. | Independence from host enzymes and cellular resources. [^5_9][^5_2] |
| Newly formed nucleic acids catalyze continued production in a defined system | Evidence supports chemical self-replication or cross-replication. | Independence from supplied substrates or suitable reaction conditions. [^5_6] |

## What would constitute a convincing conclusion?

A persuasive demonstration combines **new synthesis**, **functional progeny**, and **sustained propagation**, supported by controls that establish the mechanism and define all external dependencies. No single abundance measurement, reporter signal, complementary strand, or growth curve establishes all of these. The defensible conclusion is therefore specific: the molecule replicates repeatedly under stated conditions, with stated host or helper requirements—not that it is unconditionally “self-replicating.”[^5_3][^5_8][^5_5][^5_6]

<span style="display:none">[^5_10][^5_11][^5_12][^5_13][^5_14][^5_15][^5_16][^5_17][^5_18]</span>

<div align="center">⁂</div>

[^5_1]: https://pubmed.ncbi.nlm.nih.gov/19131595/

[^5_2]: https://journals.asm.org/doi/10.1128/microbiolspec.plas-0029-2014

[^5_3]: https://www.pnas.org/doi/10.1073/pnas.94.12.6450

[^5_4]: https://www.microbiologyresearch.org/content/journal/jgv/10.1099/jgv.0.001871?crawler=true

[^5_5]: https://pmc.ncbi.nlm.nih.gov/articles/PMC387695/

[^5_6]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2652413/

[^5_7]: https://pubmed.ncbi.nlm.nih.gov/21994575/

[^5_8]: https://eprints.whiterose.ac.uk/id/eprint/201585/1/jgv001871.pdf

[^5_9]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10433428/

[^5_10]: https://www.science.org/cms/asset/dfddb2da-4f02-4dd0-a975-7dcd868c40d7/pap.pdf

[^5_11]: https://www.ncbi.nlm.nih.gov/books/NBK543453/

[^5_12]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7269401/

[^5_13]: https://phys.org/news/2009-01-scientists-examples-rna-replicates-indefinitely.html

[^5_14]: https://cellmolbiol.org/index.php/CMB/article/download/659/654/658

[^5_15]: https://research.amanote.com/publication/-KPJ4nMBKQvf0BhiUCRU/self-sustained-replication-of-an-rna-enzyme

[^5_16]: https://ui.adsabs.harvard.edu/abs/2009OLEB...39..186J/abstract

[^5_17]: https://www.salk.edu/scientist/gerald-joyce/publications/

[^5_18]: https://www.abcam.com/en-us/knowledge-center/dna-and-rna/rna-replication
