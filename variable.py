Age = 34
FullName = "Sirri"
full_Name = "Adamu"
Stipend = 600
gender = "F"

print(f"Hello {FullName}! your Age is {Age} and your stipend is {Stipend}.")
if FullName != full_Name:
    print("the name are not thesame")

if (FullName == "Sirri" and gender == "F"  ):
    print("TRUE - AND")

    if (full_Name == "Sirri" or gender == "F"):
        print("TRUE- OR")