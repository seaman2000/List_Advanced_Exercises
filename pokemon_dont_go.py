
sequence_of_distances = list(map(int, input().split()))
removed_indices = []

while sequence_of_distances:
    index = int(input())

    if index < 0:
        removed_indices = sequence_of_distances.pop(0)
        sequence_of_distances.insert(0, sequence_of_distances[-1])

    elif index > len(sequence_of_distances) + 1 :
        removed_indices = sequence_of_distances.pop(-1)
        sequence_of_distances.append(sequence_of_distances[0])
        
