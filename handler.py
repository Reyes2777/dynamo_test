import json

from models_dynamo import calcdesempeno


def main(event, context):
    lista = calcdesempeno()
    body = {
        "message": "Estos son los estudiantes en riesgo",
        "lista": lista
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
