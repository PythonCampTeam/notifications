body_type = "text/html"
body_mail = "<html><body>Hello, {}!. Your order is ready. See your label {}</body></html>"

schema_body = {'to_email': {'type': 'string', 'empty': False,
               'required': True},
               'from_email': {'type': 'string'},
               'subject': {'type': 'string'},
               'name': {'type': 'string'},
               'label': {'type': 'string'}}

schema_sms = {"to_phone": {'type': 'string'},
              "content": {'type': 'string'}}

content = "Your order is ready"
