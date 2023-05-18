import pytest


@pytest.fixture
def transaction_list():
    return [
        {
            "id": 917824439,
            "state": "EXECUTED",
            "date": "2019-07-18T12:27:13.355343",
            "operationAmount": {
                "amount": "82139.20",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Platinum 6942697754917688",
            "to": "МИР 2956603572573342"
        },
        {
            "id": 121646999,
            "state": "CANCELED",
            "date": "2018-06-08T16:14:59.936274",
            "operationAmount": {
                "amount": "91121.62",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 7552745726849311",
            "to": "Счет 34799481846914116850"
        },
        {
            "id": 816266176,
            "state": "CANCELED",
            "date": "2018-06-24T00:46:32.422648",
            "operationAmount": {
                "amount": "60030.73",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "МИР 6381702861749111",
            "to": "Счет 27804394774631586026"
        },
        {
            "id": 736942989,
            "state": "EXECUTED",
            "date": "2019-09-06T00:48:01.081967",
            "operationAmount": {
                "amount": "6357.56",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Gold 3654412434951162",
            "to": "Счет 59986621134048778289"
        },
        {
            "id": 580054042,
            "state": "EXECUTED",
            "date": "2018-06-20T03:59:34.851630",
            "operationAmount": {
                "amount": "96350.51",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "МИР 3766446452238784",
            "to": "Счет 86655182730188443980"
        }
    ]


@pytest.fixture
def executed_operations():
    return [
        {
            "id": 917824439,
            "state": "EXECUTED",
            "date": "2019-07-18T12:27:13.355343",
            "operationAmount": {
                "amount": "82139.20",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Platinum 6942697754917688",
            "to": "МИР 2956603572573342"
        },
        {
            "id": 736942989,
            "state": "EXECUTED",
            "date": "2019-09-06T00:48:01.081967",
            "operationAmount": {
                "amount": "6357.56",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Gold 3654412434951162",
            "to": "Счет 59986621134048778289"
        },
        {
            "id": 580054042,
            "state": "EXECUTED",
            "date": "2018-06-20T03:59:34.851630",
            "operationAmount": {
                "amount": "96350.51",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "МИР 3766446452238784",
            "to": "Счет 86655182730188443980"
        }
    ]


@pytest.fixture
def sorted_by_date():
    return [
        {
            "id": 580054042,
            "state": "EXECUTED",
            "date": "2018-06-20T03:59:34.851630",
            "operationAmount": {
                "amount": "96350.51",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "МИР 3766446452238784",
            "to": "Счет 86655182730188443980"
        },
        {
            "id": 917824439,
            "state": "EXECUTED",
            "date": "2019-07-18T12:27:13.355343",
            "operationAmount": {
                "amount": "82139.20",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Platinum 6942697754917688",
            "to": "МИР 2956603572573342"
        },
        {
            "id": 736942989,
            "state": "EXECUTED",
            "date": "2019-09-06T00:48:01.081967",
            "operationAmount": {
                "amount": "6357.56",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Gold 3654412434951162",
            "to": "Счет 59986621134048778289"
        }
    ]


@pytest.fixture
def last_operations():
    return [
        {
            "id": 736942989,
            "state": "EXECUTED",
            "date": "2019-09-06T00:48:01.081967",
            "operationAmount": {
                "amount": "6357.56",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Gold 3654412434951162",
            "to": "Счет 59986621134048778289"
        },
        {
            "id": 917824439,
            "state": "EXECUTED",
            "date": "2019-07-18T12:27:13.355343",
            "operationAmount": {
                "amount": "82139.20",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Platinum 6942697754917688",
            "to": "МИР 2956603572573342"
        },
        {
            "id": 580054042,
            "state": "EXECUTED",
            "date": "2018-06-20T03:59:34.851630",
            "operationAmount": {
                "amount": "96350.51",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "МИР 3766446452238784",
            "to": "Счет 86655182730188443980"
        }
    ]


@pytest.fixture
def dict_operation():
    return {
            "id": 736942989,
            "state": "EXECUTED",
            "date": "2019-09-06T00:48:01.081967",
            "operationAmount": {
                "amount": "6357.56",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Gold 3654412434951162",
            "to": "Счет 59986621134048778289"
        }


@pytest.fixture
def operation_without_fields():
    return {
            "id": 736942989,
            "state": "EXECUTED",
    }


@pytest.fixture
def transaction_from():
    return "Visa Gold 3654 41** **** 1162"


@pytest.fixture
def transaction_to():
    return "Счет **8289"


@pytest.fixture
def transaction_sum():
    return "6357.56 USD"
