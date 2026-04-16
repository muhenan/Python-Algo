# Agent Guide

## Repository Overview

Personal LeetCode / algorithm study repo. Problems are solved in Python, organized by algorithm technique. The goal is deep understanding — each file typically explores 2–4 approaches to the same problem with documented trade-offs.

## Directory Structure

```
topics/          # Main problem solutions, organized by technique
  array/
  bfs/
  binary-search/
  bit-manipulation/
  design/
  dfs/
  dfs-backtracking/
  dp/
  graph/
  greedy/
  hashmap/
  heap/
  linked-list/
  math/
  monotonic-stack/
  prefix-sum-and-diff-array/
  regex/
  segment-tree/
  sliding-window/
  sorting/
  stack/
  string/
  tree/
  trie/
  two-pointers/
  union-find/
  zip/
companies/       # Company OA / interview problems
utils/           # Shared data structures (ListNode, TreeNode)
test/            # Scratch files, company interview practice, I/O test utils
```

## File Naming Conventions

- **LeetCode problems**: `{LC_ID}-{kebab-case-name}.py` — e.g. `322-coin-change.py`
- **Learning / framework files**: `{topic}-easy.py`, `labuladong-{topic}.py`, `{DataStructure}.py`
- **Company problems**: `{company}-{problem}.py`

## ACM Competition Style

This repo targets ACM-style competitive programming. When writing or reviewing solutions, prioritize:

- **Conciseness over verbosity** — fewer lines wins. Collapse obvious steps, avoid over-engineering.
- **Speed of writing** — code must be writable under contest pressure. Prefer idioms that are easy to recall and type quickly.
- **No unnecessary abstractions** — inline logic rather than extracting helper functions unless reuse is clear.
- **Standard contest imports at the top** — use a minimal, memorizable import block (see Imports section).
- **Skip defensive programming** — assume input is valid per problem constraints; no need to guard against edge cases not in the problem statement.

When there are multiple correct approaches, prefer the one a contestant could write fastest from memory.

## Code Style

### Solution structure

Use a class named `Solution` (matching LeetCode convention). Multiple approaches go as separate methods; the final / optimal method uses the plain LeetCode method name.

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """Optimal DP solution — final answer."""
        ...

    def coinChange_brute(self, coins: List[int], amount: int) -> int:
        """DFS / backtracking for comparison."""
        ...
```

### Docstrings

Every `Solution` class and every non-trivial method gets a docstring that includes:
- Problem description (short)
- Example input/output
- Tags (e.g. `Dynamic Programming`, `Greedy`)
- Approaches summary (on the class)
- Time Complexity / Space Complexity (on each method)

### Imports

```python
from typing import List, Dict, Set, Tuple, Optional
from collections import defaultdict, Counter, deque, OrderedDict
import heapq
from bisect import bisect_left, bisect_right
```

### Type hints

Always annotate function signatures with full type hints.

### `if __name__ == "__main__"` block

Include a small smoke-test at the bottom of each file to verify the solution manually.

```python
if __name__ == "__main__":
    solu = Solution()
    print(solu.coinChange2([1, 2, 5], 11))  # 3
```

## README Index

`README.md` maintains a hand-curated index of all problems. When adding a new problem, append an entry under the correct topic section using this format:

```markdown
- **{LC_ID}** [{English Name} · {中文名}]({relative_path})
```

For learning / framework files (no LC ID):

```markdown
- [{English Name} · {中文名}]({relative_path})
```

## Commit Message Convention

Follow Conventional Commits scoped by topic:

```
feat(dp): add LC 322 Coin Change
refactor(string): simplify LC 647 expand logic
fix(heap): correct off-by-one in LC 215
```

## Shared Utilities

- `utils/ListNode.py` — singly-linked list node
- `utils/TreeNode.py` — binary tree node

Import them at the top of any file that needs them.

## Resources

- [Labuladong](https://labuladong.github.io/algo/home/) — primary algorithmic framework reference
- [Cyc2018 CS-Notes](https://github.com/CyC2018/CS-Notes) — supplementary reference
- Personal Notion notes: linked in README
