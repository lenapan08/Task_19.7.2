import os.path
from api import PetFriends
from settings import valid_email, valid_password

pf = PetFriends()

def test_get_api_key_for_valid_user(email = valid_email, password = valid_password):
    """Тест проверяет получение api_key и статус запроса 200 в ответ на запрос при введении
    валидных: эл.почты и пароля"""

    # Cохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сравниваем фактический и ожидаемый результат
    assert status == 200
    assert 'key' in result

def test_get_api_key_for_not_valid_email(email = 'panaskoelena106gmail.com', password = valid_password):
    """Тест проверяет получение ошибки 403  и отсутсвие ключа в ответе на запрос при введении
    невалидной эл.почты и валидного пароля"""

    # Cохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сравниваем фактический и ожидаемый результат
    assert status == 403
    assert 'key' not in result

def test_get_api_key_for_empty_password(email = valid_email, password = ''):
    """Тест проверяет получение ошибки 403  и отсутсвие ключа в ответе на запрос при введении
    валидной эл.почты и пустого поля пароля"""

    # Cохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сравниваем фактический и ожидаемый результат
    assert status == 403
    assert 'key' not in result

def test_get_api_key_for_not_valid_password(email = valid_email, password ='timyrka2705'):
    """Тест проверяет получение ошибки 403  и отсутсвие ключа в ответе на запрос при введении
    валидной эл.почты и невалидного пароля"""

    # Cохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сравниваем фактический и ожидаемый результат
    assert status == 403
    assert 'key' not in result

def test_get_api_key_empty_password_and_email(email = '', password =''):
    """Тест проверяет получение ошибки 403  и отсутсвие ключа в ответе
    на запрос при пустых полях эл.почты и пароля"""

    # Cохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сравниваем фактический и ожидаемый результат
    assert status == 403
    assert 'key' not in result


def test_get_all_pets_with_valid_key(filter=''):
    """Тест проверяет ,что запрос возвращает список всех питомцев/не пустой список"""

    # Запрашиваем, получаем api key и сохраняем его в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Получаем ответ на запрос и записываем статут ответа в status, список - в result
    status, result = pf.get_list_of_pets(auth_key, filter)

    # Сравниваем фактический и ожидаемый результат
    assert status == 200
    assert len(result['pets']) > 0

def test_add_new_pet_with_valid_data(name= "Самира", animal_type= 'Британка', age = "8", pet_photo = 'images\cat.jpg'):
    """Тестируем добавление нового питомца с валидными данными """

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем, получаем api key и сохраняем его в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Отправляем запрос на добавление питомца и записываем статут ответа в status,
    # добавленного питомца - в result
    status, result = pf.post_add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

def test_add_new_pet_with_not_valid_data_1(name= " ", animal_type= 'овчарка', age = "1", pet_photo = 'images\cat.jpg'):
    """Тестируем добавление нового питомца с валидными данными, но с пустым полем name """

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем, получаем api key и сохраняем его в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Отправляем запрос на добавление питомца и записываем статут ответа в status,
    # добавленного питомца - в result
    status, result = pf.post_add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400
    assert 'animal_type' not in result

def test_add_new_pet_with_not_valid_data_2(name= "Кеша", animal_type= '', age = "1", pet_photo = 'images\cat.jpg'):
    """Тестируем добавление нового питомца с валидными данными, но с пустым полем animal_type """

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем, получаем api key и сохраняем его в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Отправляем запрос на добавление питомца и записываем статут ответа в status,
    # добавленного питомца - в result
    status, result = pf.post_add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400
    assert 'name' not in result

def test_add_new_pet_with_not_valid_data_3(name= "Багс", animal_type= 'питбуль', age = "-2", pet_photo = 'images\cat.jpg'):
    """Тестируем добавление нового питомца с валидными данными, но с отрицательным age"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем, получаем api key и сохраняем его в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Отправляем запрос на добавление питомца и записываем статут ответа в status,
    # добавленного питомца - в result
    status, result = pf.post_add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400
    assert 'name' not in result

def test_add_new_pet_with_not_valid_data_4(name="Барсик", animal_type='мэйкун', age="12345", pet_photo='images\cat.jpg'):
    """Тестируем добавление нового питомца с валидными данными, но с пятизначным age"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем, получаем api key и сохраняем его в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Отправляем запрос на добавление питомца и записываем статут ответа в status,
    # добавленного питомца - в result
    status, result = pf.post_add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400
    assert 'name' not in result

def test_add_new_pet_with_not_valid_data_5(name="Боня", animal_type='мэйкун', age='12', pet_photo=' '):
    """Тестируем добавление нового питомца с валидными данными, но без загрузки файла фото"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем, получаем api key и сохраняем его в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Отправляем запрос на добавление питомца и записываем статут ответа в status,
    # добавленного питомца - в result
    status, result = pf.post_add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400
    assert 'name' not in result

def test_add_new_pet_with_valid_data_6(name= "Самира", animal_type= 'Британка', age = "8", pet_photo = 'images\Big_cat.jpeg'):
    """Тестируем добавление нового питомца с фотографией большего размера """

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем, получаем api key и сохраняем его в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Отправляем запрос на добавление питомца и записываем статут ответа в status,
    # добавленного питомца - в result
    status, result = pf.post_add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_delete_pet_by_id():
    """Тест на проверку удаления питомца с определенным ID"""

    # Получаем api_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    # Проверяем длину списка питомцев при необходимости добавляем нового и снова запрашиваем список питомцев
    if len(my_pets['pets']) == 0:
        pf.post_add_new_pet(auth_key, 'Бублик', 'шотландский', '5', 'images/cat.jpg')
        _, my_pets = pf.get_list_of_pets(auth_key, my_pets)

    #Сохраняем ID первого питомца в списке и сохраняем в pet_id, отправляем запрос на удаление питомца с pet_id
    pet_id = my_pets['pets'][0]['id']
    status, _= pf.delete_pet(auth_key, pet_id)

    #Отправляем запрос на список питомцев, чтобы проверить есть ли в ответе pet_id и соответственно удаленный питомец
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')
    assert status == 200
    assert 'pet_id' not in my_pets.values()

def test_put_update_pet_info(name= 'Барби', animal_type= 'Бурма', age= '3'):
    """Тест на проверку обновления информации о питомце """

    # Запрашиваем, получаем api key и сохраняем его в переменную auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    # Проверяем список питомцев - не пустой ли
    if len(my_pets['pets']) > 0:
        # Отправляем запрос на оюновление информации о питомце, сохраняем статус ответа в Status,
        # обновленную информация о питомце в result
        status, result = pf.put_update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        #Проверка статуса и наличия нового имени питомца
        assert status == 200
        assert result['name'] == name
    #Если список пуст , выдаем сообщение об этом
    else:
        raise Exception('The list of pets is empty')

def test_add_new_pet_without_photo(name = 'Софа', animal_type = 'двортерьер', age = '6'):
    """Тест на проверку добавления информации о новом питомце без фото"""

    # Запрашиваем, получаем api key и сохраняем его в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Отправляем запрос на добавление питомца и записываем статут ответа в status,
    # информацию о добавленном питомце - в result
    status, result = pf.post_add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert 'name' in result

def test_add_photo_of_pet( pet_photo='images\cat.jpg'):
    """Тест проверяет возможность добавления фотографии питомца к уже существующему питомцу по ID"""
    # К сожалению, тест так и не прошел. Ошибка 503. Не понятно это временная проблема сервера или
    # все таки проблема в коде.

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем, получаем api key и сохраняем его в переменную auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    # Проверяем список питомцев - не пустой ли
    if len(my_pets['pets']) > 0:
        # Отправляем запрос на добавление фото питомца, сохраняем статус ответа в Status,
        # обновленную информация о питомце в result
        status, result = pf.post_add_photo_of_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)

        #Проверка статуса и наличия нового фото питомца
        assert status == 200
        assert result['pet_photo'] == pet_photo
    #Если список пуст , выдаем сообщение об этом
    else:
        raise Exception('The list of pets is empty')



