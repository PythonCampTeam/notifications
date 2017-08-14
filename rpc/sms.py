from twilio.rest import Client
from nameko.rpc import rpc
from keys import accaunt_sid, auth_token


@rpc
def buy():

    client = Client(accaunt_sid, auth_token)

    client.messages.create(
        to='+77017335394',
        from_='+16195866444',
        body='Na potolke nosok!'
        )
