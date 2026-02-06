sequence_of_distances = list(map(int, input().split()))
removed_indices = []

while sequence_of_distances:
    index = int(input())
    current_removed = 0

    if index < 0:
        current_removed = sequence_of_distances.pop(0)
        sequence_of_distances.insert(0, sequence_of_distances[-1])
        removed_indices.append(current_removed)

    elif index >= len(sequence_of_distances):
        current_removed = sequence_of_distances.pop(-1)
        sequence_of_distances.append(sequence_of_distances[0])
        removed_indices.append(current_removed)

    else:
        current_removed = sequence_of_distances.pop(index)
        removed_indices.append(current_removed)

    sequence_of_distances = [
        idx + current_removed
        if idx <= current_removed
        else idx - current_removed
        for idx in sequence_of_distances
    ]

print(sum(removed_indices))

