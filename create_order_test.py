import sender_stand_request
import data

def test_create_order():
    # Тест на создание заказа и получение его по трек-номеру
    # Создание заказа
    create_response = sender_stand_request.create_order(data.order_body)
    assert create_response.status_code == 201, "Успешное создание заказа"
 
    # Сохранение трек-номера
    track_number = create_response.json().get("track")
    print("Заказ создан. Номер трека:", track_number)
    assert track_number, "Трек номер не получен"

    # Получение заказа по трек номеру
    get_response = sender_stand_request.get_order_by_track_path(track_number)

    # Проверка статуса ответа
    assert get_response.status_code ==200, "Заказ найден"
    print("Тест пройден успешно. Код 200.")