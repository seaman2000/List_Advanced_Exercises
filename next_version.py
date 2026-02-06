type_of_version = input().split(".")

current_version = "".join(type_of_version)
next_version = int(current_version) + 1
next_version_lst = [digit for digit in str(next_version)]

print(".".join(next_version_lst))