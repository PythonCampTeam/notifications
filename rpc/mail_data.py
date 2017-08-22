# import cerberus
#
#
# import sendgrid
# from sendgrid.helpers.mail import (ASM, Category, Content, CustomArg, Email,
#                                    Header, Mail, Section)

body_type = "text/html"
body_mail = "<html><body>{}</body></html>"

schema_body = {'to_email': {'type': 'string'},
               'from_email': {'type': 'string'},
               'subject': {'type': 'string'},
               'content': {'type': 'string'}}


# SENDGRID_API_KEY = ''
# sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)
# from_email = Email("test@example.com")
# to_email = Email("tamara.malysheva@saritasa.com")
# subject = "Sending mail"
# content = Content("text/plain", "Hello from Russia")
# mail = Mail(from_email, subject, to_email, content)
# response = sg.client.mail.send.post(request_body=mail.get())
# print(response.status_code)
# #print(response.body)
# #print(response.headers)
#
#
# def send_templated_email(template_id='3e593b00-d9c9-447a-a0d6-561b65ea0cbb',
#                          to_email="tamara.malysheva@saritasa.com",
#                          from_email="test@example.com",
#                          subject="Sending mail",
#                          body='blablabla'
#                          ):
#
#     sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)
#     from_email = Email(from_email)
#     to_email = Email(to_email)
#     content = Content("text/html",
#                       "<html><body>{body}</body></html>".format(body=body))
#     sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)
#     mail = Mail(from_email, subject, to_email, content)
#     mail.template_id = template_id
#     response = sg.client.mail.send.post(request_body=mail.get())
#     print(response.status_code)
#     print(response.body)
#     print(response.headers)
#     #mail.template_id = '3e593b00-d9c9-447a-a0d6-561b65ea0cbb'
#
#
# def build_kitchen_sink():
#     """All settings set"""
#
#     mail = Mail()
#
#     mail.from_email = Email("test@example.com", "Example User")
#
#     mail.subject = "Hello World from the SendGrid Python Library"
#     mail.to_email = Email("tamara.malysheva@saritasa.com")
#
#     mail.add_content(Content("text/plain", "some text here"))
#     mail.add_content(Content("text/html", "<html><body>some text here</body></html>"))
#
#     mail.template_id = "3e593b00-d9c9-447a-a0d6-561b65ea0cbb"
#
#     mail.add_section(Section("%section1%", "Substitution Text for Section 1"))
#     mail.add_section(Section("%section2%", "Substitution Text for Section 2"))
#
#     mail.add_header(Header("X-Test1", "test1"))
#     mail.add_header(Header("X-Test3", "test2"))
#
#     mail.add_category(Category("May"))
#     mail.add_category(Category("2016"))
#
#     mail.add_custom_arg(CustomArg("campaign", "welcome"))
#     mail.add_custom_arg(CustomArg("weekday", "morning"))
#
#     mail.reply_to = Email("test@example.com")
#
#     return mail.get()
#
#
# def send_kitchen_sink():
#
#     # Assumes you set your environment variable:
#     # https://github.com/sendgrid/sendgrid-python/blob/master/TROUBLESHOOTING.md#environment-variables-and-your-sendgrid-api-key
#     sg = sendgrid.SendGridAPIClient()
#     data = build_kitchen_sink()
#     response = sg.client.mail.send.post(request_body=data)
#     print(response.status_code)
#     print(response.headers)
#     print(response.body)
