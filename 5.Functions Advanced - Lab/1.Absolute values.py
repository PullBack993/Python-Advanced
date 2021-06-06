def abs_iter_el(nums_list):
    result = list(map(lambda x: abs(x), nums_list)) # [abs(el) for el in nums_list]
    return result


nums = map(lambda el: float(el), input().split())
print(abs_iter_el(nums))



# def text_to_iterable(string):
#     return map(float, string.split())
#
#
# def list_of_abs(iter):
#     return list(map(abs, iter))
#
#
# text = input()
# print(list_of_abs(text_to_iterable(text)))