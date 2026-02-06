numbers = input().split(", ")

positive_lst = [num for num in numbers if int(num) >= 0]
negative_lst = [num for num in numbers if int(num) < 0]
even_lst = [num for num in numbers if int(num) % 2 == 0]
odd_lst = [num for num in numbers if int(num) % 2 != 0]

print(f"Positive: {', '.join(positive_lst)}")
print(f"Negative: {', '.join(negative_lst)}")
print(f"Even: {', '.join(even_lst)}")
print(f"Odd: {', '.join(odd_lst)}")
