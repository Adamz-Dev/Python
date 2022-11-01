from abc import ABC, abstractmethod

class User:
    first_name =''
    last_name =''
    password = ''


class UserAbstract(ABC):
    @abstractmethod
    def create_user(self, user: User):
        pass


    @abstractmethod
    def get_all_users(self):
        pass

    @abstractmethod
    def get_user_by_id(self):
        pass




class UserManager(UserAbstract):

    def get_all_users(self):
        print("Hello Tiny we are getting all users here")

    def get_user_by_id(self):
        print("Get user id here")

    def create_user(self, user: User):
        print("Create user here")
    
       

user_manager = UserManager()
user_manager.get_all_users()



