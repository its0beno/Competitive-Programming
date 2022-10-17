

# s = "(]"
# stack = []
# symbol = {')': '(', ']': '[', '}': '{'}
# for i in s:
#     if i.isalpha():
#         continue

#     if i == "[" or i == "[" or i == "{":
#         print("i", i)
#         stack.append(i)
#         print(stack)
#         continue
#     else:
#         if not stack:
#             print('flase')
#         elif symbol[i] == stack[-1]:
#             stack.pop(-1)
#         else:
#             print('flase')

#     # if len(stack) == 0:
#     #     print("False")
#     # if i == p_dict[stack]:
#     #     stack.pop()
#     # if len(stack) == 0:
#     #     print('true')
#     # else:
#     #     print('false')


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = ['(', '{', '[']
        closing = [')', '}', ']']

        for i in s:
            if i in opening:
                stack.append(i)
            else:
                ind = closing.index(i)
                if (len(stack) > 0 and (opening[ind] == stack[len(stack)-1])):
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
