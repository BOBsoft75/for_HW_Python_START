# Доработать класс Project
# Доработайте классы исключения так, чтобы они выдали подробную информацию об ошибках. 
# Передавайте необходимые данные из основного кода проекта.


import json
from task13_4 import  User
from task13_3 import AccesErorr, LevelError


class UserWorkshop:
    user_list = set()

    def __init__(self):
        UserWorkshop.load_users()
        pass


    @staticmethod
    def load_users(path: str = 'users2.json'):
        with open(path, 'r', encoding='UTF-8') as f:
            user_dict = json.load(f)
        for level, user_list in user_dict.items():
            for id, name in user_list.items():
                UserWorkshop.user_list.add(User(name, str(id), str(level)))  # создали объекты User и записали во множество


    def login(self, name: str, id: str) -> str:     # авторизация пользователя, если есть такой то возвращает уровень пользователя
        login_user = User(name, id)
        for user in UserWorkshop.user_list:
            if login_user == user:                  # проверка осуществляется благодаря __eq__ и __hash__ в классе User (равны когда имя и id равны)
                return user.level
        else:
            raise AccesErorr(name)                  # вызов ошибки прописанной в модуле task13_3.py

    def create_user(self, name: str, id: str, level: str): # создает пользоваетля если уровень меньше чем ваш уровень
        cur_name, cur_id = input("Введите имя авторизированного пользователя и его id через пробел: ").split() # авторизация пользователя (который есть в базе)
        if current_level := self.login(cur_name, cur_id):  # если есть пользователь и уровень у него не 0
            if int(current_level) > int(level):
                return User(name, id, level)        # создаем нового пользователя, если уровень авторизированного пользователя выше уровня создаваемого пользов

            raise LevelError(current_level, level)


b = UserWorkshop()
print(b.login('Ivanov', '1')) # (имя, id)  уровень = 5
print(b.create_user('New_user', '1', '3')) # создаст нового пользователя (имя, id, уровень) в случае если его уровень меньше, чем уровень указанного авторизированного пользователя
