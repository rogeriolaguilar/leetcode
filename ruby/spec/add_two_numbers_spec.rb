# frozen_string_literal: true

require 'spec_helper'
require 'add_two_numbers'

RSpec.describe '.add_two_numbers' do
  subject { add_two_numbers(l1, l2) }

  context 'sum numbers that result in one digit number' do
    let(:l1) { ListNode.new(3) }
    let(:l2) { ListNode.new(6) }

    it { expect(subject.next).to be_nil }
    it { expect(subject.val).to eq(9) }
  end

  context 'sum 5 + 9' do
    let(:l1) { ListNode.new(5) }
    let(:l2) { ListNode.new(9) }

    it { expect(subject.val).to eq(4) }
    it { expect(subject.next.val).to eq(1) }
  end

  context 'sum 1 + 99' do
    let(:l1) { ListNode.new(1) }
    let(:l2) do
      list = ListNode.new(9)
      list.next = ListNode.new(9)
      list
    end
    it { expect(subject.val).to eq(0) }
    it { expect(subject.next.val).to eq(0) }
    it { expect(subject.next.next.val).to eq(1) }
  end

  context 'sum 342 + 465' do
    let(:l1) do
      l1 = ListNode.new(2)
      l1.next = ListNode.new(4)
      l1.next.next = ListNode.new(3)
      l1
    end
    let(:l2) do
      l2 = ListNode.new(5)
      l2.next = ListNode.new(6)
      l2.next.next = ListNode.new(4)
      l2
    end
    it { expect(subject.val).to eq(7) }
    it { expect(subject.next.val).to eq(0) }
    it { expect(subject.next.next.val).to eq(8) }
  end

  context 'sum 9342 + 465' do
    let(:l1) do
      l1 = ListNode.new(2)
      l1.next = ListNode.new(4)
      l1.next.next = ListNode.new(3)
      l1.next.next.next = ListNode.new(9)
      l1
    end
    let(:l2) do
      l2 = ListNode.new(5)
      l2.next = ListNode.new(6)
      l2.next.next = ListNode.new(4)
      l2
    end
    it { expect(subject.val).to eq(7) }
    it { expect(subject.next.val).to eq(0) }
    it { expect(subject.next.next.val).to eq(8) }
    it { expect(subject.next.next.next.val).to eq(9) }
  end
end
