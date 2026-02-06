sequence_of_numbers = list(map(int, input().split(", ")))

borders = 10
while sequence_of_numbers:

    sequence = [num for num in sequence_of_numbers if num <= borders]
    sequence_of_numbers = [num for num in sequence_of_numbers if num > borders]

    print(f"Group of {borders}'s: {sequence}")
    borders += 10
    sequence = []


