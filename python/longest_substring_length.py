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
    window_being = 0
    for position, char in enumerate(s):
      window_being = self.slide_window(dict_substring, char, window_being, position)
      size = position - window_being + 1
      if size > longest_length:
        longest_length = size

    return longest_length

  def slide_window(self, dict_substring, new_value, window_being, position):
    try:
      old_position = dict_substring[new_value]
      dict_substring[new_value] = position
      if old_position >= window_being:
        window_being = old_position + 1
      return window_being
    except KeyError:
      dict_substring[new_value] = position
      return window_being


