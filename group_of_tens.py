def num_to_ten(list_of_numbers):
    group_num = 10
    current_borders = [num for num in list_of_numbers if num <= 10]
    return group_num, current_borders


def num_to_twenty(list_of_numbers):
    current_borders = [num for num in list_of_numbers if num <= 20]
    group_num = 20
    return group_num, current_borders


def num_to_thirty(list_of_numbers):
    current_borders = [num for num in list_of_numbers if num <= 30]
    group_num = 30
    return group_num, current_borders


def num_to_forty(list_of_numbers):
    group_num = 40
    current_borders = [num for num in list_of_numbers if num <= 40]
    return current_borders


def num_to_fifty(list_of_numbers):
    group_num = 50
    current_borders = [num for num in list_of_numbers if num <= 50]
    return group_num, current_borders


sequence_of_numbers = list(map(int, input().split(", ")))
print(f"Group of {}'s: {list_of_numbers}")
print(f"Group of {num_to_twenty(sequence_of_numbers)}'s: {list_of_numbers}")
print(f"Group of {group}'s: {list_of_numbers}")
print(f"Group of {group}'s: {list_of_numbers}")
print(f"Group of {group}'s: {list_of_numbers}")

