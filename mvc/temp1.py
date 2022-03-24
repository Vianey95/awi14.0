import json
texto1 = '''{
  "error": {
    "code": 400,
    "messagee": "EMAIL_EXISTS",
    "errors": [
      {
        "messagee": "EMAIL_EXISTS",
        "domain": "global",
        "reason": "invalid"
      }
    ]
  }
} '''
formato = json.loads(texto1)
error = formato['error']
print(error['messagee'])