# SLE-2: Profiling Report — Dijkstra vs Greedy Best-First Search

## 📌 Project Overview

This project is the **SLE-2 assignment** for the AI course. It profiles and compares two classic search algorithms on the same weighted graph:

- **Algorithm A:** Dijkstra's Algorithm (Uniform Cost Search — uninformed)
- **Algorithm B:** Greedy Best-First Search (Informed, heuristic-based)

Both algorithms solve the same problem:
- **Graph:** 8 nodes (A–H), directed, weighted
- **Start node:** A
- **Goal node:** H

---

## 🎯 What I Have Done (Summary)

For this SLE-2 assignment, I completed the following tasks:

### 1. Problem Design
- Designed a **weighted directed graph** with 8 nodes (A–H) and 9 edges.
- Ensured the graph had **multiple paths** from A to H with **different costs** — so that optimality differences between the algorithms would be visible.
- Created a **heuristic h(n)** table for each node, estimating its distance to goal H.

### 2. Algorithm Implementation
- Wrote `dijkstra_code.py` — an uninformed search using a **min-heap priority queue** sorted by cost-so-far.
- Wrote `greedy_code.py` — an informed search using a **min-heap priority queue** sorted by heuristic h(n) with a visited set.
- Added a **manual `nodes_expanded` counter** inside each search loop for fair comparison.

### 3. Profiling Setup
- Used Python's built-in **`timeit`** module with `number=10,000` and `repeat=5` → **50,000 runs per algorithm**.
- Converted total seconds to **microseconds per run** for meaningful comparison.
- Installed and configured **`py-spy 0.4.2`** on Windows (debugged the "module not found" issue by using the full executable path).
- Generated **flame graphs** for both algorithms to visualize hot functions.

### 4. Data Collection
- Ran both benchmarks (`python run_dijkstra.py`, `python run_greedy.py`).
- Recorded **average time, best time, and nodes expanded** for each algorithm.
- Captured **416 samples** for Dijkstra and **135 samples** for Greedy via py-spy.
- Traced the actual paths found by each algorithm.

### 5. Analysis
- Interpreted the flame graphs and identified `heapq.heappush` / `heapq.heappop` as the **hot functions** (priority queue is the bottleneck).
- Compared the **speed vs optimality trade-off**:
  - Greedy is ~2.4× faster but returned a suboptimal path (cost 12)
  - Dijkstra is slower but found the optimal path (cost 6)
- Verified that both algorithms expand all nodes when the goal is unreachable (matches O(V + E) theory).

### 6. Documentation
- Authored this **README.md** for the project overview.
- Wrote the **SLE-2 Profiling Report** (`SLE2_25UAM0XX_YourName.docx`) with comparison table, justification, and conclusion.
- Created the **AI Contribution Log** (`AI_CONTRIBUTION_LOG.md`) for transparency.
- Added `.gitignore` to exclude `__pycache__`, `*.pyc`, and `*.prof` files.

### 7. Version Control
- Initialized a **git repository** in the project folder.
- Committed all source files, flame graphs, and documentation.
- Pushed the project to **GitHub** for submission and grading.

---

## 🧠 Problem Graph

