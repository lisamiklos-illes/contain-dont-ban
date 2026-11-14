# Benchmark outputs

Results from running the benchmark (`../WORKING PROTOTYPE/benchmark_questions.txt`) against candidate models.

| Folder | Contents |
| :-- | :-- |
| `Raw Answers/` | Each model's unedited answers, one file per model |
| `LLM Grading of Answers/` | Grader output scoring those answers, one file per graded run |

Keeping the two separate means a grading rubric can be revised and re-run without touching the raw answers it was applied to.

Grading files are named `Grader_<grader> Model_<model graded>`; answer files are named for the model that produced them.
