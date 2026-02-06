number_of_electrons = int(input())

shell = []
position = 0

while number_of_electrons > 0:
    position += 1
    current_shell = 2 * position ** 2

    if number_of_electrons < current_shell:
        shell.append(number_of_electrons)
        break

    shell.append(current_shell)
    number_of_electrons -= current_shell

print(shell)

