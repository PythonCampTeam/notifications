body_type = "text/html"
body_mail = "<html><body>Hello, {}!. Your order is ready. See your label <a href={}</a></body></html>"

schema_body = {'to_email': {'type': 'string', 'empty': False,
               'required': True},
               'from_email': {'type': 'string'},
               'subject': {'type': 'string'},
               'name': {'type': 'string'},
               'label': {'type': 'string'}}

schema_sms = {"to_phone": {'type': 'string'},
              "content": {'type': 'string'}}

# @rpc
# def buy():
#
#     client = Client(accaunt_sid, auth_token)
#
#     client.messages.create(
#         to='+79994413746',
#         from_='+16195866444',
#         body='Na potolke nosok!'
#         )
#
# {
#     "to_phone": "+79994413746",
#     "content": "OK"
# }
