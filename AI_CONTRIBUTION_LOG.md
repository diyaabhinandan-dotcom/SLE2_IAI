# AI Contribution Log — SLE-2

**Course:** 02AML204 – Introduction to Artificial Intelligence  
**PRN:** 25UAM015 
**Name:** DIYA ABHINANDAN TELNADE  
**Division:** A  
**Date:** 22-09-2026  
**Assignment:** SLE-2 — Profiling Report (Empirical Performance Analysis)

---

## 🤖 AI Tools Used

| Tool | Version / Model | Purpose |
|------|----------------|---------|
| ChatGPT | GPT-5 | Code scaffolding, syntax help, wording of analysis |
| GitHub Copilot | N/A | Not used in this SLE |

---

## ✅ What AI Helped With

### 1. Code Boilerplate
- **Prompt used:** "Give me a clean Python implementation of Dijkstra's algorithm using heapq with node-count tracking."
- **What AI provided:** The initial structure of `dijkstra_code.py` including the priority queue setup, best_cost dictionary, and heap push/pop logic.
- **My modifications:** Added the `nodes_expanded` counter, renamed variables for consistency, and integrated with my `common.py`.

### 2. Greedy Best-First Search Implementation
- **Prompt used:** "Write Greedy Best-First Search in Python with a visited set and heuristic priority."
- **What AI provided:** The core loop of `greedy_code.py`.
- **My modifications:** Ensured the path and cost were tracked alongside the priority, tested against my graph.

### 3. Timing Syntax
- **Prompt used:** "Show me the correct timeit.repeat syntax to measure a function and convert to microseconds."
- **What AI provided:** The `per_run_us = [(t / NUMBER) * 1e6 for t in results]` formula used in `run_dijkstra.py` and `run_greedy.py`.

### 4. py-spy Command Syntax (Windows)
- **Prompt used:** "py-spy record fails on Windows with 'not recognized'. How do I invoke it?"
- **What AI provided:** Guidance to use the full path (`C:\Users\...\Scripts\py-spy.exe`) instead of relying on PATH.

### 5. Wording of Analysis
- **Prompt used:** "Help me write a 5-8 line justification comparing Dijkstra and Greedy based on runtime and nodes expanded."
- **What AI provided:** The initial phrasing of the justification paragraph.
- **My modifications:** Inserted my actual measured numbers (7.86 µs, 3.213 µs, 7 vs 4 nodes) and rewrote parts to match my results.

---

## 🧑‍💻 What I Did Myself

### Design & Setup
- Chose the **weighted directed graph** (8 nodes, A→H) with multiple paths of different costs.
- Designed the **heuristic h(n)** values for each node.
- Created `common.py` to share graph + heuristic between both algorithms.

### Execution
- Installed and configured **py-spy** on Windows.
- Debugged the "No module named py_spy" issue and switched to full-path invocation.
- Ran all benchmarks: `python run_dijkstra.py` and `python run_greedy.py`.
- Generated both flame graphs using py-spy.
- Collected **all 15+ data points** in the results table.

### Analysis
- Interpreted the flame graphs and identified `heapq.heappush` / `heappop` as the hot functions.
- Wrote the **justification** based on my own measured data — specifically the speed vs optimality trade-off (Dijkstra: 7.86 µs, cost 6; Greedy: 3.213 µs, cost 12).
- Verified that both algorithms expanded all nodes in the unreachable-goal scenario.
- Wrote the conclusion based on personal learning.

### Documentation
- Created `README.md` for the GitHub repo.
- Created this `AI_CONTRIBUTION_LOG.md`.
- Prepared the final Word report.
- Uploaded the repo and pushed via git.

---

## 🚫 What AI Did NOT Do

- ❌ Did NOT run any benchmarks
- ❌ Did NOT decide the graph structure or heuristic
- ❌ Did NOT generate flame graphs
- ❌ Did NOT collect or fabricate any measured numbers
- ❌ Did NOT write the final conclusion (only helped with phrasing)
- ❌ Did NOT push code to GitHub

All **measured results and interpretations are my own**.

---

## 📝 Honest Note

I used ChatGPT as a **learning assistant**, not as a code generator that did the assignment for me. The AI helped me understand unfamiliar syntax (timeit, py-spy on Windows) and provided starting templates for standard algorithm implementations. Every number in the report was measured by me on my machine, every flame graph was generated from my code, and every analysis sentence reflects my own understanding of the results.

The purpose of this log is to be **transparent** about my AI usage, as required by the SLE-2 guidelines (Section 5: AI Contribution Note).

---

**Signed:**  
DIYA ABHINANDAN TELANDE  
PRN: 25UAM015
Date: 22-09-2026