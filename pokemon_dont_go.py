def increase_value():
    pass


def decrease_value():
    pass





sequence_of_distances = list(map(int, input().split()))
removed_indices = []

while sequence_of_distances:
    index = int(input())
    if index < 0:

        sequence_of_distances[0] = sequence_of_distances[-1]
