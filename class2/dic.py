# person={
#     'name':'ram',
#     'age':'22',
#     'address':'gaushala',
#     'family_member':[
#         'father',
#         'daughter',
#         'son',
#         'mom',
        
#     ]
# }
# print(person['name'],person['family_member'])



person={
    'Name':'Mukta',
    'Age':'22',
    'City':'Gaushala',
    'Family_members':[
        'father',
        'mother',
        'sister',
        'brother',
    ]
}
# print(f"my name is {person['Name']},i m {person['Age']}years old,living in {person['City']},with my family members{person['Family_members']}")
# #print(f"my name is {'Name'} and i m {'Age'} years old living in {'City'} with my family members where i have {'Family_members'}")


print(person['Family_members'][1][2])


print(person['Family_members'][3][::])