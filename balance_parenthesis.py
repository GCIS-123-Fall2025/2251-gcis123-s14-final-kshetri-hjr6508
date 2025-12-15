
"""
Course: GCIS 123 (2251)
Exam: Final Exam
Question: Question #3 (25 points)
Filename: balance_parenthesis.py

Complete the bracket balancing function below. It checks if (  and  ) brackets are balanced, using a stack.

Function returns 0 if brackets are balanced,
-1 if there are more closing brackets than needed,
and x otherwise, where x is the index of the most recent
unbalanced left bracket.

Examples:
"--(---(------)--"  returns  2 'this should return 1' 
"()----)" returns -1
"-----() -- ( () )" returns 0

"""
from node_stack import Stack

def balance_parenthesis(a_string):
    stack = Stack()
    balence = 0
    for s in a_string:
        stack.push( s )
    
    while not stack.is_empty():
        s = stack.pop()
        if s == "(": balence += 1
        if s == ")": balence -= 1
    return balence


def main():
    assert balance_parenthesis("(--(---(------)--") == 2
    assert balance_parenthesis("()----)") == -1
    assert balance_parenthesis("-----() -- ( () )") == 0


if __name__ == "__main__":    main()