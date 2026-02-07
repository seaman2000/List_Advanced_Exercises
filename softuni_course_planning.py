def add(lesson, list_of_lessons):
    if lesson not in list_of_lessons:
        list_of_lessons.append(lesson)


def insert(lesson, index_, list_of_lessons):
    if lesson not in list_of_lessons:
        list_of_lessons.insert(index_, lesson)


def remove(lesson, list_of_lessons):
    if lesson in list_of_lessons:
        list_of_lessons.remove(lesson)


def swap(first, second, list_of_lessons):
    if first and second in list_of_lessons:
        indices = [
            idx
            for idx, string in enumerate(list_of_lessons)
            if string == first or string == second
        ]
        a, b = indices
        list_of_lessons[a], list_of_lessons[b] = list_of_lessons[b], list_of_lessons[a]


def


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
        index = parts[2]
        insert(lesson_title, index, lessons)

    elif current_command == "Remove":
        remove(lesson_title, lessons)

    elif current_command == "Swap":
        first_lesson = parts[1]
        second_lesson = parts[2]
        swap(first_lesson, second_lesson, lessons)


