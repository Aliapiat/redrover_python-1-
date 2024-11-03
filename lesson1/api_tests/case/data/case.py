from lesson1.api_tests.case.pom.case import create_case

create_case_dict = {
    "id": 1,
    "name": "Имя",
    "description": "Описание",
    "steps": ["Шаг 1", "Шаг 2", "Шаг 3"],
    "expected_result": "Ожидаемый результат",
    "priority": "низкий",
}

create_case_dict_high = {
    "id": 1,
    "name": "Имя",
    "description": "Описание",
    "steps": ["Шаг 1", "Шаг 2", "Шаг 3"],
    "expected_result": "Ожидаемый результат",
    "priority": "высокий",
}

create_case_error = {
  "detail": [
    {
      "loc": [
        "string",
        0
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}

check_id= {
    "id": 100,
    "name": "Имя",
    "description": "Описание",
    "steps": ["Шаг 1", "Шаг 2", "Шаг 3"],
    "expected_result": "Ожидаемый результат",
    "priority": "высокий",
}

check_name= {
    "id": 100,
    "name": "Tim",
    "description": "Описание",
    "steps": ["Шаг 1", "Шаг 2", "Шаг 3"],
    "expected_result": "Ожидаемый результат",
    "priority": "высокий",
}