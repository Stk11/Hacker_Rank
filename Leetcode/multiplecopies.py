# Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 

# Example 1:

# Input: s = "abab"
# Output: true
# Explanation: It is the substring "ab" twice.
# Example 2:

# Input: s = "aba"
# Output: false
# Example 3:

# Input: s = "abcabcabcabc"
# Output: true
# Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
 

# Constraints:

# 1 <= s.length <= 104
# s consists of lowercase English letters.


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                substring = s[:i]
                repetitions = n // i
                constructed_string = substring * repetitions

                if constructed_string == s:
                    return True 
                    break
        return False
    
sol = Solution()

# Example 1
s1 = "abcabcabcabc"
print(sol.repeatedSubstringPattern(s1))  # Output: True

# Example 2
s2 = "aba"
print(sol.repeatedSubstringPattern(s2))  # Output: False
