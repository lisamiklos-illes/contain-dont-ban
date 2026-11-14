# Evaluation outputs

Outputs from running the Phase 0 benchmark (`Phase 0 model evaluation harness/benchmark_questions.txt`) against candidate models.

| Folder | Contents |
| :-- | :-- |
| `raw benchmark answers/` | Each model's unedited answers to the 5 benchmark questions, one file per model |
| `LLM grading of answers/` | Grader output scoring those answers, one file per graded run |

Keeping the two separate means a grading rubric can be revised and re-run without touching the raw answers it was applied to.
