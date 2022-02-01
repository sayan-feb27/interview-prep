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


if __name__ == "__main__":
    exp = "921 * - 8 - 4 +"
    print(evaluate_postfix(exp))

    nge = next_greater_element([4, 6, 3, 2, 8, 1, 9, 9, 9])
    print(nge)
