class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return _uniquePaths(0, 0, m, n)

def _uniquePaths(m, n, fm, fn):
    if m == fm - 1 and n == fn - 1:
        return 1
    if m >= fm or n >= fn:
        return 0
    down_paths = _uniquePaths(m + 1, n, fm, fn)
    right_paths = _uniquePaths(m, n + 1, fm, fn)
    return down_paths + right_paths