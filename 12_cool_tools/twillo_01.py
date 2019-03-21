# date: 2019/03/21 8:09 PM
# author: fanchuang
# github: https://github.com/buxuele/
# email: baogebuxuele@163.com
"""about:
1. send SMS 现在不能用了。有空查查看原因。

"""

from twilio.rest import Client

account_sid = 'ACa1757e977193a93e492e59a180dbf990'
token = '3dac2cc1f4347724600c2e63b7940144'

client = Client(account_sid, token)
# text = 'yooh'

msg = client.messages.create(
    to='+8615026758603',
    from_ ='(765) 379-8980',
    body = 'yes amd!'
)

print(msg.sid)



