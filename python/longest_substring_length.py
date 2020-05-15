"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

longest_length = 3
counter = 3

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class LongestSubstringLength:
  def lengthOfLongestSubstring(self, s: str) -> int:
    longest_length = 0
    substring = []
    for char in s:
      substring = self.slide_window(substring, char)
      size = len(substring)
      if size > longest_length:
        longest_length = size

    return longest_length

  def slide_window(self, array, new_value):
    for i, value in enumerate(array):
      if value == new_value:
        return array[i+1:] + [new_value]
    return array + [new_value]

