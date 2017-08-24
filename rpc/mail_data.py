# import cerberus
import base64
#
import sendgrid
from sendgrid.helpers.mail import Content, Email,  Mail,  Attachment

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
#     SENDGRID_API_KEY = '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'
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
#     #print(response.body)
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

# body = {
# "to_email": "tamara.malysheva@saritasa.com",
# "from_email": "test@example.com",
# "subject" : "blabla",
# "content" : "content"
# }
SENDGRID_API_KEY = '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'
sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)

from_email = Email("from@example.com")
subject = "subject"
to_email = Email("tamara.malysheva@saritasa.com")
content = Content("text/html", "<html><body>blabla</body></html>")

#pdf = open("/home/developer/test.pdf", "rb").read()
with open("/home/developer/test.pdf", 'rb') as f:
    pdf = f.read()
    f.close()
encoded = base64.b64encode(pdf).decode()
attachment = Attachment()
attachment.content = encoded
attachment.type = "application/pdf"
attachment.filename = "test.pdf"
attachment.disposition = "attachment"
attachment.content_id = '1236'

mail = Mail(from_email, subject, to_email, content)
mail.template_id = '3e593b00-d9c9-447a-a0d6-561b65ea0cbb'

mail.add_attachment(attachment)

response = sg.client.mail.send.post(request_body=mail.get())

print(response.status_code)
print(response.body)
print(response.headers)
