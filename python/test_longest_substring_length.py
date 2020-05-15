import unittest
from longest_substring_length import LongestSubstringLength

class TestLongestSubstringLength(unittest.TestCase):
  def setUp(self):
    self.soluction = LongestSubstringLength()

  def test_when_empty_string(self):
    result = self.soluction.lengthOfLongestSubstring('')
    self.assertEqual(result, 0)  
  def test_when_string_has_same_chars(self):
    result = self.soluction.lengthOfLongestSubstring('bbbb')
    self.assertEqual(result, 1)

  def test_when_all_chars_are_different(self):
    result = self.soluction.lengthOfLongestSubstring('abcde')
    self.assertEqual(result, 5)

  def test_when_string_has_two_possibles_substrings(self):
    result = self.soluction.lengthOfLongestSubstring('abcddcb')
    self.assertEqual(result, 4)
    
  def test_when_the_longest_is_the_second_substring(self):
    result = self.soluction.lengthOfLongestSubstring('abczzabcde')
    self.assertEqual(result, 6)

  def test_when_the_longest_substring_is_in_the_middle(self):
    result = self.soluction.lengthOfLongestSubstring('abczzabcdeesa')
    self.assertEqual(result, 6)

  def test_when_the_repeated_char_appears_after_others_chars(self):
    result = self.soluction.lengthOfLongestSubstring('abcaer')
    self.assertEqual(result, 5)

  def test_when_the_repeated_and_separeted_chars(self):
    result = self.soluction.lengthOfLongestSubstring('pwwkew')
    self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()