# # # from module1 import add
# # from lessons.lesson1 import *
# # from my_package import module1 as m
# #
# # print(m.add(12, 13))
# # #
# # ardager = Hero("Ardager", 100, 12)
# # print(ardager.name)
#
# # from my_package.module1 import add
# # from my_package.module2 import Hero
# from my_package import add, Hero
#
#
# import random
# import abc
#
# from colorama import Fore, Back, Style
# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')
#
#
#
#
# print("TEXT")
#





my_list = [ 1,2,3,4,5,6,7,8,9,10,11]


def get_item(n):
    for i in my_list:
        if i == n:
            return i

# print(get_item(7))

nums = [2, 7, 11, 15]
target = 26

for i, j in enumerate(nums):
    print(i, j)
# print(range(len(nums)))
def two_sum(nums, target):

    num_map = {
        # 2 : 0
        # 7 : 1
        # 11 : 2
    }

    for i, j in enumerate(nums):
        item_num = nums[i]
        need_num = target - item_num
        if need_num in num_map:
            return [num_map[need_num], i]
        num_map[item_num] = i

    return []

# print(two_sum(nums, target))