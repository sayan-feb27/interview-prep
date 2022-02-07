from typing import Any, Union


class Stack:
    def __init__(self):
        self.stack_list = []
        self.stack_size = 0

    def push(self, elem: Any):
        # O(1)
        self.stack_list.append(elem)
        self.stack_size += 1

    def pop(self) -> Any:
        # O(1)
        if not self.is_empty():
            self.stack_size -= 1
            return self.stack_list.pop()
        return None

    def peek(self) -> Any:
        # O(1)
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def is_empty(self) -> bool:
        # O(1)
        return self.stack_size == 0

    def size(self) -> int:
        # O(1)
        return self.stack_size


def evaluate_postfix(exp: str) -> Union[int, str]:
    """
    :param exp: string
    :return: float
    >>> evaluate_postfix(exp = "921 * - 8 - 4 +")
    3
    """
    stack = Stack()
    try:
        for char in exp:
            if char.isspace():
                continue

            if char.isdigit():
                stack.push(char)
            else:
                right = stack.pop()
                left = stack.pop()
                res = str(eval(left + char + right))
                stack.push(res)
        return int(float(stack.pop()))
    except TypeError:
        return "Invalid input"


def next_greater_element(lst):
    stack = Stack()
    res = [-1] * len(lst)

    for i in range(len(lst)-1, -1, -1):
        while not stack.is_empty() and stack.peek() <= lst[i]:
            stack.pop()
        if not stack.is_empty():
            res[i] = stack.peek()
        stack.push(lst[i])
    return res


def is_valid_parentheses(s: str) -> bool:
    """
    >>> is_valid_parentheses('()[]{}')
    True
    """
    if not s or len(s) % 2 != 0:
        return False

    stk = []
    for bracket in s:
        if bracket not in "({[)]}":
            return False

        if bracket in "({[":
            stk.append(bracket)
            continue

        opening = stk.pop() if stk else None
        if not opening:
            return False

        closing = bracket
        if "([{".index(opening) != ")]}".index(closing):
            return False

    if stk:
        return False
    return True

