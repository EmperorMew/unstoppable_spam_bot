import plivo
import time
from config import api_key, api_secret
client = plivo.RestClient(api_key, api_secret)

callers = [11234567891, 13219879874]


victim = input("Enter victim number with country code: ")
messages = input("Enter messages to send: ").split()
rest = input("Enter rest time: ")


def spam(index):
    response = client.messages.create(
        src= callers[index],
        dst= victim,
        text= messages[index%len(messages)])
    print (response)
    time.sleep(int(rest))


count = len(callers)

i = 0
while i < count:
    print(i)
    print(spam(i))
    if i == count-1:
        i = -1
    i += 1
