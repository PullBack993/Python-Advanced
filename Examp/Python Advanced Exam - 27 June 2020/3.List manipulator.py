# import ast
#
# def list_manipulator(*args):
#     list_to_manipulate, command, place, *args = args
#     rest = args
#
#     if command == 'remove':
#         if place == 'end':
#             if check_parameters(rest):
#                 rest = rest[0]
#                 list_to_manipulate = list_to_manipulate[:int(rest) - 1]
#             else:
#                 list_to_manipulate = list_to_manipulate[:-1]
#         if place == 'beginning':
#             if check_parameters(rest):
#                 rest = rest[0]
#                 list_to_manipulate = list_to_manipulate[int(rest):]
#             else:
#                 list_to_manipulate = list_to_manipulate[1:]
#         return list_to_manipulate
#
#     elif command == 'add':
#         rest = "".join(str(args))
#         rest = rest[1:-1]
#         list_to_manipulate = "".join(str(list_to_manipulate))
#         list_to_manipulate = list_to_manipulate[1:-1]
#         if place == 'end':
#             rest = ', ' + rest
#             list_to_manipulate = list_to_manipulate + rest
#         if place == 'beginning':
#             rest += ', '
#             list_to_manipulate = rest + list_to_manipulate
#
#     return print_prep(list_to_manipulate)
#

def list_manipulator(nums, *args):
    action, location, *values = args
    if action == 'add':
        if location == 'beginning':
            nums = values + nums
        else:
            nums = nums + values
    else:
        if location == 'beginning':
            if values:
                for _ in range(values[0]):
                    nums.pop(0)
            else:
                nums.pop(0)
        else:
            if values:
                for _ in range(values[0]):
                    nums.pop()
            else:
                nums.pop()
    return nums


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
