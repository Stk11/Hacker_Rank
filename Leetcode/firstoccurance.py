class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Remove the double quotes from input strings
        haystack = haystack.replace('"', '')
        needle = needle.replace('"', '')

        if not needle:
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            # print(i)
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1

def main():
    haystack_input = input()
    needle_input = input()

    # Create an instance of the Solution class
    solution = Solution()

    # Call the strStr method with user input
    result = solution.strStr(haystack_input, needle_input)

    # Display the result
    print(result)