import configuration
import requests
import data

def create_order(order_data):
    # Создание нового заказа
    response = requests.post(configuration.URL_SERVICE + configuration.ORDERS_PATH, 
                              json=order_data)
    return response

def get_order_by_track_path(track_number):
    # Получение заказа по трек-номеру
    order_url = f"{configuration.URL_SERVICE}{configuration.ORDERS_TRACK_PATH}"

    params = {"t": track_number}
    response = requests.get(order_url, params=params)
    return response