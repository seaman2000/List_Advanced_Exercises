number_of_rooms = int(input())

room_number = 0
chair_count = 0

for room in range(1, number_of_rooms + 1):
    chairs, people = input().split()
    people = int(people)
    difference = len(chairs) - people
    chair_count += difference

    if len(chairs) < people:
        print(f"{abs(difference)} more chairs needed in room {room}")

if chair_count >= 0:
    print(f"Game On, {chair_count} free chairs left")