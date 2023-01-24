#Question2
dog={'name':'Jack',
    'color':'White',
    'breed':'Husky',
    'legs':4,
    'age':9
}
student={
    'first_name':'Daniel',
    'last_name':'Warner',
    'gender':'Male',
    'age':'34',
    'marital_status':'Single',
    'skills':['.Net','C#','Java'],
    'country':'USA',
    'city':'Missouri',
    'address':'36th street'
}
print("Student dictionary length: ",len(student))
print("Student skills values: ",student['skills'])
print("Data type of student skills: ",type(student['skills']))
student['skills'].append('SQL')
student['skills'].append('python')
print("Student skills updated: ",student['skills'])
print(dog.keys())
print(dog.values())