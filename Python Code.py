class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        max_len = 0
        start = 0

        for i, char in enumerate(s):
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1
            char_index[char] = i
            max_len = max(max_len, i - start + 1)

        return max_len

if __name__ == "__main__":
    s = input("Enter the string:")
    solution = Solution()
    res=solution.lengthOfLongestSubstring(s)
    print(f"Lenght of longest substring: {res}")
