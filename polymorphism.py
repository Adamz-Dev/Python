class IBM:
     def get_processor_speed(self):
        print(f"16GHz")

     def login(self, user_name, password):
        print("Login progress........")

     def registration(self, email, password, phone_number=None, dob=None):
        print(f"email: {email}\n")
        print(f"password: {password}\n")
        if phone_number !=None: 
            print(f"phone number: {phone_number}")
        if dob != None:
             print(f"Date of birth: {dob}")
        


class Nyawira(IBM):
    def get_processor_speed(self):
        print(f"32Ghz")



ibm = IBM()
ibm.get_processor_speed()
nyawira = Nyawira()
nyawira.get_processor_speed()
ibm.login("ADAMU", "password")
ibm.registration("adamu.muhammad@gmail.com", "123456789")

