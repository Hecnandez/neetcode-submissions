class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "": return []
        mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        lists = []  # lists of chars [[a, b, c], [d, e, f]]
        for digit in digits:
            lists.append(mapping[digit])

        res = []
        current = []

        def dfs(i):
            if i >= len(lists):
                res.append("".join(current))
                return

            for j in range(len(lists[i])):
                current.append(lists[i][j])
                dfs(i + 1)
                current.pop()

        dfs(0)
        return res
