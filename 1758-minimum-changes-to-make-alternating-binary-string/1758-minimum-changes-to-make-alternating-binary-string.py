class Solution:
    def minOperations(self, s: str) -> int:
        changes_start_0 = 0  # pattern: 010101...
        changes_start_1 = 0  # pattern: 101010...
        
        for i in range(len(s)):
            expected_0 = str(i % 2)           # 0,1,0,1...
            expected_1 = str((i + 1) % 2)     # 1,0,1,0...
            
            if s[i] != expected_0:
                changes_start_0 += 1
            
            if s[i] != expected_1:
                changes_start_1 += 1
        
        return min(changes_start_0, changes_start_1)