first_sequence = input().split(", ")
second_sequence = input().split(", ")
my_lst = []

for string in first_sequence:
    for string_ in second_sequence:
        if string in string_ and string not in my_lst:
            my_lst.append(string)

print(my_lst)