students = [
    {'name': 'Amit', 'semesters': [
        {'Math': 88, 'Science': 91, 'English': 85},
        {'Math': 90, 'Science': 92, 'English': 84}
    ]},
    {'name': 'Pooja', 'semesters': [
        {'Math': 79, 'Science': 95, 'English': 88},
        {'Math': 82, 'Science': 81, 'English': 85}
    ]},
    {'name': 'Ravi', 'semesters': [
        {'Math': 87, 'Science': 88, 'English': 89},
        {'Math': 91, 'Science': 90, 'English': 93}
    ]}
]

result = {
    student['name']: sum(sum(marks.values()) for marks in student['semesters'])
    for student in students
    if all(mark > 80 for semester in student['semesters'] for mark in semester.values())
}

print(result)
