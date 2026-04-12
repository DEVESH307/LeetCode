class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        n = len(arr)
        ans = [""] * n

        for i in range(n):
            s = arr[i]
            best = None

            for l in range(1, len(s) + 1):   # length
                candidates = set()

                for start in range(len(s) - l + 1):
                    sub = s[start:start + l]

                    # check if present in any other string
                    found = False
                    for j in range(n):
                        if i != j and sub in arr[j]:
                            found = True
                            break

                    if not found:
                        candidates.add(sub)

                if candidates:
                    ans[i] = min(candidates)
                    break

        return ans