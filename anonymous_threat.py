def merge(sequence, start, end):
    start = max(0, start)
    end = min(len(sequence) - 1, end)

    if start <= end:
        merged = "".join(sequence[start:end + 1])
        sequence[start:end + 1] = [merged] # Заменя предишните стойности на списъка с  вече merged.


def divide(sequence, index, partitions):
    element = sequence[index]

    if partitions <= 1:
        return

    part_len = len(element) // partitions
    parts_ = []
    pos = 0

    for _ in range(partitions - 1):
        parts_.append(element[pos:pos + part_len])
        pos += part_len

    parts_.append(element[pos:])
    sequence[index:index + 1] = parts_


sequence_of_strings = input().split()

while True:
    command_line = input()

    if command_line == "3:1":
        break

    parts = command_line.split()
    command = parts[0]

    if command == "merge":
        start_idx = int(parts[1])
        end_idx = int(parts[2])
        merge(sequence_of_strings, start_idx, end_idx)

    elif command == "divide":
        index_ = int(parts[1])
        partitions_ = int(parts[2])
        divide(sequence_of_strings, index_, partitions_)

print(" ".join(sequence_of_strings))
