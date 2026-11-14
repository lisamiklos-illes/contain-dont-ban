# contain-dont-ban

Contain, Don't Ban: Phased Clearance for AI That Designs Self-Replicating Biology.

## Phased Clearance for Biological Sequence Generation

- **The risk:** One of the most significant risks of applying LLMs to biology is their potential to generate DNA or RNA sequences that enable biological self-replication, such as viral genomes or other replication-capable constructs.

- **Our proposed approach:** We propose a **Phased Clearance model** that governs access to sequence-generation capabilities based on the level of evaluation and expert review a model has undergone. Rather than granting unrestricted access, models progress through successive clearance phases as they demonstrate that they meet increasingly rigorous evaluation requirements.

- **Technical implementation:**
-- The **Phased Clearance MCP** is a prototype implementation of this approach. It provides a mechanism for controlling access to biological sequence-generation capabilities according to a model's clearance status.
-- **Phase 0 evaluation:** The **Phase 0 evaluation harness** automates the initial benchmarking process, assessing a model's understanding of nucleic-acid self-replication. This is the first step in a broader evaluation pathway, followed by Phase 1, Phase 2, and Phase 3 assessments involving increasingly rigorous testing and expert review. Progression through these phases determines the level of sequence-generation capability a model may access.
