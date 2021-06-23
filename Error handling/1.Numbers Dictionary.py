def fill_dict():
    numbers_dictionary = {}

    while True:
        key = input()
        if key == "Search":
            break
        value = input()
        if value == 'Search':
            break
        number = int(value)
        numbers_dictionary[key] = number

    return numbers_dictionary


def find_in_dict(nums_dict):
    while True:
        key = input()
        if key == 'Remove':
            break
        print(nums_dict.get(key, 'Number does not exist in dictionary'))
    return nums_dict


def remove_from_dict(nums_dict):
    line = input()
    while line != 'End':
        searched = line
        try:
            del numbers_dictionary[searched]
        except Exception:
            print("Number does not exist in dictionary")
            continue
        line = input()
        print(nums_dict)


numbers_dictionary = fill_dict()
find_in_dict(numbers_dictionary)
remove_from_dict(numbers_dictionary)
