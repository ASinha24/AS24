students={
	"male":["Ram", "Shyam", "Bittu", "Pinku", "Tinku"],
	"female":["Anu", "Indu", "Neetu", "sharnya", "Neha"]
	}
	
for key in students.keys():
	print(key)
for value in students.values():
	print(value)
for item in students.items():
	print(item)
for key in students.keys():
	print(students[key])

for key in students.keys():
    for name in students[key]:
        if "a" in name:
             print(name)



	

	
