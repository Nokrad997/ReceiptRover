from src.models.Model import Model
from src.models.Users import Users

print("chuj")

usr = Users("test", "test@test000.com", "test")
res = usr.addUser()

if(res):
    print("dodano")
else:
    print("nie dodano")

print(usr.getUsers())