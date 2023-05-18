import json


def read_file_operations(path):

    """Получает список операций из файла json
    """

    with open(path, "r", encoding='utf-8') as file:
        json_list = file.read()
        json_operations = json.loads(json_list)
    return json_operations


def load_operations(list_operations, transaction_type):

    """Получает список операций исходя из типа транзакции
    """

    list_executed_operation = []
    for dict_operation in list_operations:
        if dict_operation.get("state") == transaction_type:
            list_executed_operation.append(dict_operation)
    return list_executed_operation


def sort_list_operations_by_date(list_executed_operation):

    """Сортирует список операций по дате
    """

    sorted_list = sorted(list_executed_operation, key=lambda date: date["date"])
    return sorted_list


def load_list_last_transactions(count_operations, sorted_list):

    """Возвращает список последних операций
    """

    return list(reversed(sorted_list[-count_operations:]))


def convert_date(dict_operation):

    """Преоразует дату операции в нужный формат
    """

    date = dict_operation.get("date")
    if date is None:
        return "Нет даты"

    date_split_t = date.split("T")
    date_split = date_split_t[0].split("-")
    return f"{date_split[2]}.{date_split[1]}.{date_split[0]}"


def print_description(dict_operation):

    """Печатает описание перевода операции
    """

    return f"{dict_operation.get('description')}"


def print_from(dict_operation):

    """Печатает название и номер карты from. Номер карты замаскирован и не отображается целиком в формате
    XXXX XX** **** XXXX
    """

    str_from = dict_operation.get("from")

    if str_from is None:
        return "Нет данных по счету"

    split_str_from = str_from.split(" ")
    split_name_card_from = []
    number_card_from = ""

    for index in split_str_from:
        if index.isdigit():
            number_card_from = index[:4] + " " + index[4:6] + "*" * 2 + " " + "*" * 4 + " " + index[-4:]
        else:
            split_name_card_from.append(index)

    name_card_from = " ".join(split_name_card_from)

    return f"{name_card_from} {number_card_from}"


def print_to(dict_operation):

    """Печатает название и номер счета to. Номер счета замаскирован и не отображается целиком в формате  **XXXX
    """

    str_to = dict_operation.get("to")

    if str_to is None:
        return "Нет данных по счету"

    split_str_to = str_to.split(" ")
    split_name_card_to = []
    number_card_to = ""

    for index in split_str_to:
        if index.isdigit():
            number_card_to = "*"*2 + index[-4:]
        else:
            split_name_card_to.append(index)

    name_card_to = " ".join(split_name_card_to)

    return f"{name_card_to} {number_card_to}"


def print_sum_of_transfer(dict_operation):

    """Печатает сумму перевода и валюту
    """

    dict_operation_amount = dict_operation.get("operationAmount")
    if dict_operation_amount is None:
        return None

    amount = dict_operation_amount.get("amount")
    dict_currency = dict_operation_amount.get("currency")
    name_currency = dict_currency.get("name")
    return f"{amount} {name_currency}"
