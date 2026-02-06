number_of_rooms = int(input())

room_number = 0
chair_count = 0

for room in range(1, number_of_rooms + 1):
    chairs, people = input().split()
    room_number += 1
    difference = len(chairs) - int(people)
    chair_count += difference

    if len(chairs) < int(people):
        print(f"{abs(chair_count)} more chairs needed in room {room_number}")

if chair_count >= 0:
    print(f"Game On, {chair_count} free chairs left")