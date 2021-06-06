def round_iter_el(nums_list):
    result = list(map(lambda x: round(x), nums_list)) ## [abs(el) for el in nums_list]
    return result


nums = map(lambda el: float(el), input().split())
print(round_iter_el(nums))


""" or """
# def text_to_iterable(string):
#     return map(float, string.split())
#
#
# def list_of_rounded(iter):
#     return list(map(round, iter))
#
#
# text = input()
# print(list_of_rounded(text_to_iterable(text)))