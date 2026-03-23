from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

MENSAJES_ERROR = {
    "multiplicar1_1_10":{
        "num1":{
            "less_than_equal":"El primer parámetro debe ser menor o igual a 10",
            "greater_than_equal": "El primer parámetro debe ser mayor o igual a 1",
            "int_parsing": "El primer parámetro debe ser un número",
            "missing": "El primer parámetro es obligatorio"
        },
        "num2":{
            "less_than_equal":"El segundo parámetro debe ser menor o igual a 10",
            "greater_than_equal":"El segundo parámetro debe ser mayor o igual a 1",
            "int_parsing":"El segundo parámetro debe ser un número",
            "missing":"El segundo parámetro es obligatorio"
        }
    }
}