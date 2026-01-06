info = [
("alice" ,"math", "bio"),
("charlie" ,"math"),
("bob" ,"math"),
("alice" ,"science"),
("alice" ,"english"),
("bob" ,"science"),
("charlie", "english"),

]


dict1 = {}

# for name, course in info:

#     if(dict1.get(name)==None):
#         dict1.update({name:set()})
#         dict1[name].add(course)
#     else:
#         dict1[name].add(course)


for item in info:
    name = item[0]
    courses = item[1:]

    if name not in dict1:
        dict1[name] = set()

    dict1[name].add(courses)

print(dict1)