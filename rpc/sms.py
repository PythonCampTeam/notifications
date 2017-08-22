# from nameko.rpc import rpc
#
# from keys import accaunt_sid, auth_token
# from twilio.rest import Client

schema_sms = {"to_phone": {'type': 'string'},
              "content": {'type': 'string'}}

# @rpc
def buy():

    client = Client(accaunt_sid, auth_token)

    client.messages.create(
        to='+79994413746',
        from_='+16195866444',
        body='Na potolke nosok!'
        )
