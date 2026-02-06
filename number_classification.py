numbers = input().split(", ")

positive_lst = [num for num in numbers if int(num) >= 0]
negative_lst = [num for num in numbers if int(num) < 0]
even_lst = [num for num in numbers if int(num) % 2 == 0]
odd_lst = [num for num in numbers if int(num) % 2 != 0]

print(f"")
