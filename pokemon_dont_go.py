def increase_value(list_, remove):
    list_ = [idx + remove for idx in list_ if idx <= remove]
    return list_

def decrease_value(list_, remove):
    list_ = [idx - remove for idx in list_ if idx > remove]
    return list_

sequence_of_distances = list(map(int, input().split()))
removed_indices = []

while sequence_of_distances:
    index = int(input())

    if index < 0:
        removed_indices = sequence_of_distances.pop(0)
        sequence_of_distances.insert(0, sequence_of_distances[-1])
        sequence_of_distances = [idx + removed_indices for idx in sequence_of_distances]

    elif index > len(sequence_of_distances) + 1 :
        removed_indices = sequence_of_distances.pop(-1)
        sequence_of_distances.append(sequence_of_distances[0])

