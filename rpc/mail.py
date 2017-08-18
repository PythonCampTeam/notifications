
import sendgrid

from sendgrid.helpers.mail import Mail, Email, Content


SENDGRID_API_KEY = ''
sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)
from_email = Email("test@example.com")
to_email = Email("tamara.malysheva@saritasa.com")
subject = "Sending mail"
content = Content("text/plain", "Hello from Russia")
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
#print(response.body)
#print(response.headers)
