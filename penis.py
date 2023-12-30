from src.models.Model import Model
from src.models.Users import Users

print("chuj")

usr = Users("test", "test@test000.com", "test")
# res = usr.addUser()

# print(res)
# if(res):
#     print("dodano")
# else:
#     print("nie dodano")

print(usr.getUsers())

# mod = Model()
# print(mod.executeQuery('INSERT INTO "Users" (name, email, password) VALUES (\'test\', \'test10\', \'test\') RETURNING *'))
# print(mod.executeQuery('SELECT * FROM "Users"'))