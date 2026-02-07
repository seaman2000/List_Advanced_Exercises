def add(lesson, list_of_lessons):
    if lesson not in list_of_lessons:
        list_of_lessons.append(lesson)


def insert(lesson, index_, list_of_lessons):
    if lesson not in list_of_lessons:
        list_of_lessons.insert(index_, lesson)


def remove(lesson, list_of_lessons):
    exercise_item = f"{lesson}-Exercise"
    if lesson in list_of_lessons:
        list_of_lessons.remove(lesson)
    if exercise_item in list_of_lessons:
        list_of_lessons.remove(exercise_item)

def swap(first, second, list_of_lessons):
    exercise_item_first = f"{first}-Exercise"
    exercise_item_second = f"{second}-Exercise"

    if first in list_of_lessons and second in list_of_lessons:
        idx_first = list_of_lessons.index(first)
        idx_second = list_of_lessons.index(second)

        a, b = idx_first, idx_second
        list_of_lessons[a], list_of_lessons[b] = list_of_lessons[b], list_of_lessons[a]


def exercise(lesson, list_of_lessons):
    exercise_item = f"{lesson}-Exercise"

    if "-" in lesson:
        return

    if lesson in list_of_lessons:
        idx = list_of_lessons.index(lesson)

        if idx + 1 < len(list_of_lessons) and list_of_lessons[idx + 1] == exercise_item:
            return

        list_of_lessons.insert(idx + 1, exercise_item)
    else:
        list_of_lessons.append(lesson)
        list_of_lessons.append(exercise_item)


lessons = input().split(", ")

while True:
    command = input()
    if command == "course start":
        break
    parts = command.split(":")
    current_command = parts[0]
    lesson_title = parts[1]

    if current_command == "Add":
        add(lesson_title, lessons)

    elif current_command == "Insert":
        index = int(parts[2])
        insert(lesson_title, index, lessons)

    elif current_command == "Remove":
        remove(lesson_title, lessons)

    elif current_command == "Swap":
        first_lesson = parts[1]
        second_lesson = parts[2]
        swap(first_lesson, second_lesson, lessons)

    elif current_command == "Exercise":
        exercise(lesson_title, lessons)

for idx, current_lesson in enumerate(lessons):
    print(f"{idx + 1}.{current_lesson}.")
