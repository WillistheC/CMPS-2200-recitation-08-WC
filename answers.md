# CMPS 2200 Recitation 08 Answers

**Name:**_________________________
**Name:**_________________________


Place all written answers from `recitation-10.md` here for easier grading.



- **2) (2 pts)** What is the work of `reachable`, assuming $n$ nodes and $m$ edges?

Assuming adding each node is constant, and accessing each node across an edge is constant, $W(n,m) = O(n+m) because the worst case is you visit each node once and traverse each edge once

- **4) (1 pt)** What is the worst case number of times we need to call `reachable` to determine if a graph is connected?

The way I have implemented `connected` calls `reachable` exactly once for best or worst case

- **5) (2 pts)** What is the work of `connected`, assuming $n$ nodes and $m$ edges?

Since my implementation calls `reachable` once and does one comparison, $W(n,m) = O(n+m) + O(1) = O(n,m)$ (work of `reachable` plus the work from comparison)

- **7) (1 pt)** What if we switched the graph representation to an adjacency matrix? Would the work of `reachable` change? If so, what would it be? If not, why not?

The work would change to $O(n^{2})$ because you are scanning $n$ nodes $n$ neighbors in the worst case

