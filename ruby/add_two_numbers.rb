'''
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

# Definition for singly-linked list by Leetcode for that problem.
class ListNode
  attr_accessor :val, :next
  def initialize(val)
    @val = val
    @next = nil
  end
end

# Implementation
def add_two_numbers(l1, l2)
  out_digit = 0
  current_digit1 = l1
  current_digit2 = l2
  result = nil

  until current_digit1.nil? && current_digit2.nil?
    p "Current digits: #{current_digit1.val} #{current_digit2.val} and out digit #{out_digit} #"
    sum = current_digit1.val + current_digit2.val + out_digit
    out_digit = sum < 10 ? 0 : 1
    digit_sum = sum % 10

    p "Current sum digit: #{digit_sum}"
    p "Current out digit: #{out_digit}"

    if result.nil?
      result = ListNode.new(digit_sum)
      last_node = result
    else
      last_node.next = ListNode.new(digit_sum)
      last_node = last_node.next
    end

    current_digit1 = current_digit1.next
    current_digit2 = current_digit2.next
  end

  result
end

###### Test

l1 = ListNode.new(2)
l1.next = ListNode.new(4)
l1.next.next = ListNode.new(3)

l2 = ListNode.new(5)
l2.next = ListNode.new(6)
l2.next.next = ListNode.new(4)

expected = ListNode.new(7)
expected.next = ListNode.new(0)
expected.next.next = ListNode.new(8)

result = add_two_numbers(l1, l2)

#########  some helper functions
def to_string(list)
  list.next.nil? ? list.val.to_s : "#{list.val} -> #{to_string(list.next)}"
end

def to_number(list)
  list.next.nil? ? list.val : "#{to_number(list.next)}#{list.val}".to_i
end

##########

p "Result: #{to_string(result)}"
p "Expected: #{to_string(expected)}"
