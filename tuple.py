# tuple is collection which ordered and unchangeable used to group together related data

student = ("bro", 21, "male")

print(student.count("bro"))
print(student.index("male"))

for x in student:
    print(x)

if "bro" in student:
    print("bro is here!")
