# Input
#       Bulgaria, Romania, Germany, England
#       Sofia, Bucharest, Berlin, London

countries = input().split(', ')
cities = input().split(', ')
zipped = zip(countries, cities)
[print(f"{countries} -> {cities}") for countries, cities in zipped]

"""or"""
#
# def get_input():
#     return input().split(', ')
#
#
# def get_string(co, cit):
#     return f'{co} -> {cit}'
#
#
# countries = get_input()
# cities = get_input()
# [print(get_string(countries[i], cities[i])) for i in range(len(countries))]

