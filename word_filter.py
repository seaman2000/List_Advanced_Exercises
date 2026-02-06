fruits = input().split()

even_fruits = [fruit for fruit in fruits if len(fruit) % 2 == 0]

print("\n".join(even_fruits))