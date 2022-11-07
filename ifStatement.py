name = input ("enter the name of person at the door:")
if (name =="Tiny"):
    print(f"Hello {name}")
elif (name =="Bunmi"):
    print(f"Hello Bunmi")

else: 
    print(f"Go back {name}")

username, password = input ("enter usename:"), input ("enter your password")
if (username == "admin" and password == "1234@admin"):
 print("you are log in as admin")

else: 
    print("invalid password")

users = ["Mandela", "Bunmi", "Nelson"]

for user in users:
 print( f"Hello {user} ")


number = 1
while (number <= 10):
    print(f"number {number}")
    number +=1

for number in range ( 0, 10):
  print(f"for Loop numbers: {number}")

