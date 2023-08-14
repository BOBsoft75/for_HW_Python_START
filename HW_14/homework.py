

import pytest                      # необходимо установить в окружение


from task13_5 import UserWorkshop
from task13_3 import AccesErorr, LevelError
from task13_4 import User


@pytest.fixture()
def set_up():
    return UserWorkshop()   # данные для теста


# тест на проверку того, что  будет выброс исключения AccesErorr при вводе невалидных данных, AccesErorr  прописан в Exceptions.py
def test_access_fail_1(set_up):

    with pytest.raises(AccesErorr, match='Access denied'):
        # передаются невалидные данные
        set_up.login('Ivanovs', '1')


# тест на проверку валидных данных, то что должна вернуться
def test_access(set_up):
    # вводятся валидные данные и проверяется на совпадение с результатом
    assert set_up.login('Ivanov', '1') == '5'


# тест на проверку того, что  будет выброс исключения AccesErorr при вводе невалидных данных, AccesErorr  прописан в Exceptions.py
def test_access_fail_2(set_up):
    with pytest.raises(LevelError):
        set_up.login('Ivanov', '1')
        set_up.create_user('New_user', '1', '3')


if __name__ == '__main__':
    pytest.main(['-v'])
