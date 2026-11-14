# Benchmark Evaluation Harness

Runs a fixed set of benchmark questions against up to 10 LLMs and produces one PDF of answers per model, so the answers can be read and graded side by side.

| Folder | Contents |
| :-- | :-- |
| `WORKING PROTOTYPE/` | The tool itself. Run it from here; `benchmark_questions.txt` holds the questions it asks |
| `BENCHMARK OUTPUTS/` | What came back: model answers, and gradings of those answers |

The questions live with the prototype that reads them, so that folder runs as a self-contained unit. Outputs are kept separate from the tool that produced them, so answers collected under one version of the questions are not confused with another.
