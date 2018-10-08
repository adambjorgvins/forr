def get_strings(number):
    strings = []
    for x in range(number):
        string_from_user = input("enter a number or a letter:")
        strings.append(string_from_user)
    return strings

def get_numbers(number):
    numbers = []
    for x in range(number):
        number_from_users = int(input("enter a number: "))
        numbers.append(number_from_users)
    return numbers


def how_many_occurs(target, strings):
    count = 0
    for single_string in strings:
        if single_string == target:
            count += 1
    return count


#finnur hæstu tölu í lista af tölum
#numbers: þetta þarf að vera listi af tölum
def highest(numbers):
    high = None
    for single_num in numbers:
        if high == None or single_num > high:
            high = single_num
    return high


def lowest(numbers):
    low = None
    for single_num in numbers:
        if low == None or single_num < low:
            low = single_num
    return low

def sum_all_numbers(numbers):
    nums = 0
    for single_num in numbers:
        nums += single_num
    return nums


def average(numbers):
    summa = sum_all_numbers(numbers)
    av = summa / len(numbers)
    return av

def not_duplicates(numbers):
    new_list = []
    for single_num in numbers:
        if single_num not in new_list:
            new_list.append(single_num)
    return new_list


def strings():
    strings_from_user = get_strings(int(input("Please enter the size of the list: ")))
    target_string = input("enter a target: ")
    how_many_times = how_many_occurs(target_string, strings_from_user)
    print("{} occurs {} times in the list".format(target_string, how_many_times))



def nums():

    numbers_from_users = get_numbers(int(input("Please enter the size of the list: ")))
    print("{} is the highest number".format(highest(numbers_from_users)))
    print("{} is the lowest number".format((lowest(numbers_from_users))))
    print("{} is the sum of numbers".format(sum_all_numbers(numbers_from_users)))
    print("{} is the average of numbers".format(average(numbers_from_users)))
    print("{} <-- no duplicate list".format(not_duplicates(numbers_from_users)))


nums()

