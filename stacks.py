# A stack is a LIFO(last in first out) data structure.
# Push and Pop elements O(1)

# Use cases for stack
# Function calling is any programming language is managed using a stack.
# Undo (Ctrl+Z) functionality in any editor uses stack to track down last set of operations.

# It is not recommended to use lists or linked lists to create a stack, but to rather use deque

# https://docs.python.org/3/library/collections.html#collections.deque
from collections import deque

stack = deque()

stack.append('First Visited')
stack.append('Second Visited')
stack.append('Third Visited')
stack.append('Last Visited')
print(stack)

stack.pop()

print(stack)

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)

def reverse_string(s):
    stack = Stack()

    for ch in s:
        stack.push(ch)

    rstr = ''
    while stack.size()!=0:
        rstr += stack.pop()

    return rstr


if __name__ == '__main__':
    print(reverse_string("We will conquere COVID-19"))
    print(reverse_string("I am the king"))



def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2


def is_balanced(s):
    stack = Stack()
    for ch in s:
        if ch=='(' or ch=='{' or ch == '[':
            stack.push(ch)
        if ch==')' or ch=='}' or ch == ']':
            if stack.size()==0:
                return False
            if not is_match(ch,stack.pop()):
                return False

    return stack.size()==0 


if __name__ == '__main__':
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("((a+g))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))