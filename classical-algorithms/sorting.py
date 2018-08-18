import random


def bubble_sort(numbers):
    '''Sorts by using the classic bubble sort:
       https://en.wikipedia.org/wiki/Bubble_sort'''
    sorted_list = []
    swapped = True
    while swapped is True:
        swapped = False
        for i in range(len(numbers) - 1):
            first_number = numbers[i]
            second_number = numbers[i + 1]
            if first_number > second_number:
                numbers[i] = second_number
                numbers[i + 1] = first_number
                swapped = True
        # Last number will always be the highest so add to already sorted_list
        # and remove it from original number list
        sorted_list = [numbers[-1]] + sorted_list
        del numbers[-1]
    return numbers + sorted_list


def merge_sort(numbers):
    '''Sorts a list based on the traditional merge-sort'''

    if len(numbers) <= 1:
        return numbers

    result = []

    mid = len(numbers) // 2

    left = merge_sort(numbers[mid:])
    right = merge_sort(numbers[:mid])

    l_idx = 0
    r_idx = 0

    # compare all numbers in the two lists
    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx] > right[r_idx]:
            result.append(right[r_idx])
            r_idx += 1
        else:
            result.append(left[l_idx])
            l_idx += 1

    # make sure leftover numbers are added to result
    result += left[l_idx:]
    result += right[r_idx:]

    return result
