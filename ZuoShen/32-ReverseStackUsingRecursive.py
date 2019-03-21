"""
用递归反转一个栈
"""


def reverse_stack(stack):
    if not stack:
        return
    i = get_and_remove_last_element(stack)
    reverse_stack(stack)
    stack.append(i)


def get_and_remove_last_element(stack):
    result = stack.pop()
    if not stack:
        return result
    else:
        last = get_and_remove_last_element(stack)
        stack.append(result)
        return last


if __name__ == '__main__':
    stack = [1, 2, 3, 4, 5]
    reverse_stack(stack)
    while stack:
        print(stack.pop())

