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
