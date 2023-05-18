from functions.utils import read_file_operations, load_operations, sort_list_operations_by_date, \
    load_list_last_transactions, convert_date, print_description, print_from, print_to, print_sum_of_transfer


def test_read_file_operations(transaction_list):
    assert read_file_operations("test_operations.json") == transaction_list


def test_load_operations(transaction_list, executed_operations):
    assert load_operations(transaction_list, "EXECUTED") == executed_operations
    assert load_operations([], "EXECUTED") == []
    assert load_operations(transaction_list, "start") == []


def test_sort_list_operations_by_date(executed_operations, sorted_by_date):
    assert sort_list_operations_by_date(executed_operations) == sorted_by_date
    assert sort_list_operations_by_date([]) == []


def test_load_list_last_transactions(sorted_by_date, last_operations):
    assert load_list_last_transactions(3, sorted_by_date) == last_operations
    assert load_list_last_transactions(5, sorted_by_date) == last_operations
    assert load_list_last_transactions(0, sorted_by_date) == last_operations
    assert load_list_last_transactions(-3, sorted_by_date) == []


def test_convert_date(dict_operation, operation_without_fields):
    assert convert_date(dict_operation) == "06.09.2019"
    assert convert_date({}) == "Нет даты"
    assert convert_date(operation_without_fields) == "Нет даты"


def test_print_description(dict_operation, operation_without_fields):
    assert print_description(dict_operation) == "Перевод организации"
    assert print_description({}) == "None"
    assert print_description(operation_without_fields) == "None"


def test_print_from(dict_operation, transaction_from, operation_without_fields):
    assert print_from(dict_operation) == transaction_from
    assert print_from(operation_without_fields) == "Нет данных по счету"
    assert print_from({}) == "Нет данных по счету"


def test_print_to(dict_operation, transaction_to, operation_without_fields):
    assert print_to(dict_operation) == transaction_to
    assert print_to(operation_without_fields) == "Нет данных по счету"
    assert print_to({}) == "Нет данных по счету"


def test_print_sum_of_transfer(dict_operation, transaction_sum, operation_without_fields):
    assert print_sum_of_transfer(dict_operation) == transaction_sum
    assert print_sum_of_transfer(operation_without_fields) is None
    assert print_sum_of_transfer({}) is None
