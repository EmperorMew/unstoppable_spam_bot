import time
import plivo
from config import api_key, api_secret
client = plivo.RestClient(api_key, api_secret)

callers = [11234567891, 13219879874]

victim = input("Enter victim number with country code: ")
rest = input("Enter rest time: ")


def spam(index):
    response = client.calls.create(
        from_=callers[index],
        to_= victim,
        answer_url='https://s3.amazonaws.com/static.plivo.com/answer.xml',
        answer_method='GET', )
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
