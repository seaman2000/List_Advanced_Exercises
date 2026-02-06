numbers = input().split(", ")

positive_lst = []
negative_lst = []
even_lst = []
odd_lst = []

for num in numbers:
    if int(num) >= 0:
        positive_lst.append(num)
    elif int(num) < 0:
        negative_lst.append(num)

    if int(num) % 2 -- 0:
        even_lst.append(num)
    elif