# AI Contribution Log — SLE-2

## 1. Task-Wise Contribution Table

| # | Task | Done By | AI Tool Used | AI's Role | My Role | Evidence |
|---|------|---------|--------------|-----------|---------|----------|
| 1 | Designing the weighted graph (8 nodes A–H, 9 edges) | Me | — | — | Full design | `common.py` line 4–13 |
| 2 | Creating the heuristic h(n) values | Me | — | — | Full design | `common.py` line 16–19 |
| 3 | Dijkstra algorithm structure | Me + AI | ChatGPT | Provided boilerplate `heapq` skeleton | Modified variables, added `nodes_expanded` counter | `dijkstra_code.py` |
| 4 | Greedy Best-First Search structure | Me + AI | ChatGPT | Provided core search loop | Added path + cost tracking, tested on my graph | `greedy_code.py` |
| 5 | `timeit` benchmark syntax | AI | ChatGPT | Gave `timeit.repeat()` + µs conversion formula | Wrote full `run_*.py` scripts, chose runs | `run_dijkstra.py`, `run_greedy.py` |
| 6 | py-spy installation + Windows debugging | Me + AI | ChatGPT | Explained full-path invocation on Windows | Ran install, debugged "module not found" | Terminal history |
| 7 | Running 50,000 benchmark iterations | Me | — | — | Executed all runs | Terminal output |
| 8 | Generating flame graphs | Me | — | — | Ran py-spy on both scripts | `profile_*.svg` |
| 9 | Collecting all measured numbers | Me | — | — | Recorded 15+ data points | Results table |
| 10 | Interpreting flame graphs (heapq hot spot) | Me | — | — | Own analysis | Justification section |
| 11 | Writing justification & conclusion | Me + AI | ChatGPT | Phrasing suggestions | Inserted real numbers, rewrote parts | Report §4, §6 |
| 12 | Creating README.md | Me | — | — | Full authoring | `README.md` |
| 13 | Creating this AI log | Me | — | — | Full authoring | `AI_CONTRIBUTION_LOG.md` |
| 14 | Pushing to GitHub | Me | — | — | Full git workflow | GitHub repo |

---

## 2. Contribution Percentage Summary

| Contributor | Role | Approx. Contribution |
|-------------|------|---------------------|
| **Me (Student)** | Design, execution, measurement, analysis, documentation | **~85%** |
| **ChatGPT** | Syntax help, boilerplate templates, wording suggestions | **~15%** |

---

## 3. What AI Did NOT Do

| Task | Status |
|------|--------|
| Running any benchmark | ❌ Not done by AI |
| Choosing the graph structure | ❌ Not done by AI |
| Deciding heuristic values | ❌ Not done by AI |
| Generating flame graphs | ❌ Not done by AI |
| Fabricating measured numbers | ❌ Not done by AI |
| Pushing code to GitHub | ❌ Not done by AI |
| Writing final conclusion | ❌ Not done by AI (only phrasing) |

---

## 4. AI Tool Details

| Tool | Version / Model | Total Prompts Used | Purpose |
|------|----------------|-------------------|---------|
| ChatGPT | GPT-5 | ~6 prompts | Code scaffolding, syntax, wording |

---

## 5. Sample Prompts Used

| # | Prompt | What AI Returned | How I Used It |
|---|--------|------------------|---------------|
| 1 | "Write Dijkstra's algorithm in Python using heapq." | Basic implementation | Rewrote with my variable names, added node counter |
| 2 | "Write Greedy Best-First Search in Python with heuristic priority." | Core loop | Added path + cost tracking |
| 3 | "How to use timeit.repeat to measure a function in microseconds?" | Syntax formula | Used in `run_*.py` |
| 4 | "py-spy not recognized on Windows — how to invoke?" | Full-path command | Ran flame graphs |
| 5 | "Help me phrase a 5-line justification for Dijkstra vs Greedy based on time and nodes." | Draft paragraph | Inserted my real numbers |

---

## 6. Honest Declaration

I used ChatGPT as a **learning assistant and syntax reference**, not as a code generator that completed the assignment for me. Every measured number, every flame graph, and every analysis sentence in my report reflects my own work. The purpose of this log is to be fully transparent about my AI usage, as required by the SLE-2 guidelines.
