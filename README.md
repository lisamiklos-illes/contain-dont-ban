# contain-dont-ban

## Phased LLM Clearance for Biological Sequence Generation Features

- **The risk:** One of the most significant risks of applying LLMs to biology is their potential to generate DNA or RNA sequences that enable biological self-replication, such as viral genomes or other replication-capable constructs.

- **Our proposed approach:** We propose a **Phased Clearance model** that governs access to sequence-generation capabilities based on the level of evaluation and expert review a model has undergone. Rather than granting unrestricted access, models progress through successive clearance phases as they demonstrate that they meet increasingly rigorous evaluation requirements.

- **Technical implementation:**
-- The **Phased Clearance MCP** is a prototype implementation of this approach. It provides a mechanism for controlling access to biological sequence-generation capabilities according to a model's clearance status.
-- **Phase 0 evaluation:** The **Benchmark Evaluation Harness** automates the initial benchmarking process, assessing a model's understanding of nucleic-acid self-replication. This is the first step in a broader evaluation pathway, followed by Phase 1, Phase 2, and Phase 3 assessments involving increasingly rigorous testing and expert review. Progression through these phases determines the level of sequence-generation capability a model may access.

## Repository contents

| Path | Contents |
| :-- | :-- |
| `Benchmark Evaluation Harness/WORKING PROTOTYPE/` | The harness. Sends each benchmark question to up to 10 models at once and writes one PDF of answers per model |
| `Benchmark Evaluation Harness/BENCHMARK OUTPUTS/Raw Answers/` | Unedited model answers, one file per model |
| `Benchmark Evaluation Harness/BENCHMARK OUTPUTS/LLM Grading of Answers/` | Grader output scoring those answers |

The benchmark itself is the 5 questions in `Benchmark Evaluation Harness/WORKING PROTOTYPE/benchmark_questions.txt`, covering replication-associated sequence features, the requirements for self-replication, what can be inferred from sequence alone, autonomous versus dependent replication, and the experimental evidence that would establish genuine self-replication.

## Results so far

Ten models have been run against the benchmark; eight have been graded, all by ChatGPT, out of 25.

| Model | Score |
| :-- | --: |
| GPT6 Sol | 25 |
| Kimi K3 | 24 |
| Grok 4.7 Thinking | 20 |
| Nemotron 3.5 Super VL | 20 |
| Gemini 4 Hydrogen | 18 |
| Sonnet 5.5 Thinking | 17 |
| GLM 5.3 | 16 |
| Gemini 4 Hydrogen Thinking | 16 |

GPT6 Sol Thinking and Sonnet 5.5 have answers but are not yet graded.

These are early results and should be read with three caveats. Every score comes from a single grader, so none of them separates the model's performance from the grader's judgment. The answers were collected through a web-search-enabled interface rather than through the harness, so they are not clean model-only outputs. And the gradings repeatedly fault models for how they define autonomy, which suggests the questions touch a boundary where expert usage itself varies — worth resolving in the rubric before any score functions as a gate.

## Running the harness

```bash
cd "Benchmark Evaluation Harness/WORKING PROTOTYPE"
pip install -r requirements.txt
python app.py
```

Add a model, paste an API key, and press Run. See that folder's README for the demo mode and the full set of supported providers.
