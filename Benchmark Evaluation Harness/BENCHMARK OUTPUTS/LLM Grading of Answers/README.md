# LLM Grading of Answers

Grader output scoring the files in `../Raw Answers/`. One file per graded run.

Files are named `Grader_<grader> Model_<model graded>`, so the grader and the model under test are both readable from the filename.

| Model graded | Grader | Score |
| :-- | :-- | --: |
| GPT6 Sol | ChatGPT | 25/25 |
| Kimi K3 | ChatGPT | 24/25 |
| Grok 4.7 Thinking | ChatGPT | 20/25 |
| Nemotron 3.5 Super VL | ChatGPT | 20/25 |
| Gemini 4 Hydrogen | ChatGPT | 18/25 |
| Sonnet 5.5 Thinking | ChatGPT | 17/25 |
| GLM 5.3 | ChatGPT | 16/25 |
| Gemini 4 Hydrogen Thinking | ChatGPT | 16/25 |

Each grading file should record which model was graded, which model did the grading, the rubric or prompt used, and the date. Sign-off rests on the regulator's own biologists rather than on an automated score, so grading output here is evidence for that review, not a substitute for it.

Two models in `../Raw Answers/` have no grading yet: GPT6 Sol Thinking and Sonnet 5.5.

**All scores above come from a single grader.** A second grader on the same answers would show how much of each score is the rubric and how much is the grader, which matters before any score is used as a gate.
