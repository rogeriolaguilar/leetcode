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
    dict_substring = {}
    window_begin = 0
    for position, char in enumerate(s):
      if char in dict_substring:
        old_position = dict_substring[char]
        if old_position >= window_begin:
          window_begin = old_position + 1      

      size = position - window_begin + 1
      if size > longest_length:
        longest_length = size
      dict_substring[char] = position
    return longest_length

