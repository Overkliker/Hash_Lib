import hashlib
import csv
from tabulate import tabulate


def writer_csv(array):
    """
    Записывает данные в файл
    :param array: список пользователей с обновлёнными данными
    :return: ничего
    """
    with open("data.csv", 'w', encoding="windows-1251") as w:
        wr = csv.writer(w, delimiter=",")
        wr.writerows(array)


def read_csv():
    """
    Читает данные из файла
    :return: список значений из файла
    """
    with open("data.csv", 'r', encoding="windows-1251") as r:
        data = csv.reader(r)

        users = []
        for i in data:
            if i:
                users.append(i)

        return users


def change_password(user_number):
    """
    Генерирует новое значение хэша
    :param user_number: порядковый номер пользователя в списке данных
    :return: ничего
    """
    data = read_csv()
    new_passw = input("Введите новый пароль: ")
    salt = "pivo"
    new_passw = hashlib.sha256(new_passw.encode() + salt.encode()).hexdigest()
    data[user_number - 1][1] = new_passw
    writer_csv(data)


def admin_intf():
    """
    Создаёт интерфейс для администратора системы
    :return: ничего
    """
    headers = ["Имя", "Пароль", "Роль"]
    while True:
        print("Пользователи системы:")
        data = read_csv()
        print(tabulate(data, headers=headers))

        print("Введите номер строки пользователя, пароль которго вы хотите сменить:")
        number = int(input())
        print(len(data))
        if len(data) == number:
            change_password(number)

        else:
            print("Такой строки нету")


def user_intf():
    """
    Заготовка пользовательского интерфейса
    :return: ничего
    """
    print("Вы вошли в личный кабинет покупателя. Скоро здесь появится функционал для данной роли пользователя")


def seller_intf():
    """
    Заготовка интерфейса кассира
    :return: ничего
    """
    print("Вы вошли в личный кабинет продавца. Скоро здесь появится функционал для данной роли пользователя")


def autorization(array):
    """
    Функция проверяет наличия пользователя в системе
    :param array: список вида [логин, хэш пароля]
    :return: ничего
    """
    users = read_csv()

    for i in users:
        if i[0] == array[0] and i[1] == array[1]:
            if users[users.index(i)][2] == "admin":
                admin_intf()

            elif users[2] == "user":
                user_intf()

            elif users[2] == "seller":
                seller_intf()

    print("Неверный логин или пароль")


login = input("Login: ")
password = input("Password: ")
salt = "pivo"
password = hashlib.sha256(password.encode() + salt.encode()).hexdigest()
user = [login, password]
autorization(user)


