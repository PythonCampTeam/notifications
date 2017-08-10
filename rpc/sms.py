from twilio.rest import Client
from nameko.rpc import rpc

accaunt_sid = 'AC3adbfe0e72f9d7dc7197fefd2cab7aca'
auth_token = 'f3ab11d8839c7752d07db9854b93bc8f'


@rpc
def buy():

    client = Client(accaunt_sid, auth_token)

    client.messages.create(
        to='+77017335394',
        from_='+16195866444',
        body='Na potolke nosok!'
        )
