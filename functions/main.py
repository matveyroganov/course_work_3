import os
from utils import read_file_operations, load_operations, sort_list_operations_by_date, load_list_last_transactions, \
    convert_date, print_description, print_from, print_to, print_sum_of_transfer


path = os.path.join('../pythonProject3', 'data', 'operations.json')


def main():

    # Читаем файл json с операциями и получаем список операций

    list_operations = read_file_operations(path)

    # Фильтруем список операций исходя из типа транзакции

    list_executed_operations = load_operations(list_operations, "EXECUTED")

    # Сортируем отфильтрованный список по дате

    list_sorted_by_date = sort_list_operations_by_date(list_executed_operations)

    # Получаем список с 5 последними транзакциями

    last_five_transactions = load_list_last_transactions(5, list_sorted_by_date)

    # Запускаем цикл по списку c  5 последними транзакциями

    for dict_operation in last_five_transactions:

        # Печатаем дату перевода и описание перевода

        print(f"{convert_date(dict_operation)} {print_description(dict_operation)}")

        # Печатаем, откуда и куда был сделан перевод

        print(f"{print_from(dict_operation)} -> {print_to(dict_operation)}")

        # Печатаем сумму перевода и валюту

        print(f"{print_sum_of_transfer(dict_operation)}\n")


main()
