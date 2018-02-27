
import requests, random, time, json
from time import sleep
from faker import Faker
from random import getrandbits


print ("################################################")
print ("             DEVELOPED BY @IAMKISHANN ©.        ")
print ("################################################")

def main():

    faker = Faker()
    s = requests.Session()
    s.headers = {
            'Origin':'https://www.excelsiormilano.com',
            'Referer':'https://www.excelsiormilano.com/content/45-nike-air-jordan-1-x-off-white',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }
    s.headers.update()
    url = "https://www.excelsiormilano.com/module/antcontactcustom/sendmail"



########edit  this###########
    bdate = "1998-09-11"
    phone = "7022798025"
    size = ['8','8,5','9','9,5','10','10,5','11','11,5','12','12,5','13']
    instagram = "fuckjamzi" 
    country = "United States"
    city = "new york"
    zipcode = "90701"
    street = "12345 bob ave"

    #if your email 1234lab@gmail.com replase xxx with 1234lab
    email = "xxx+{}@gmail.com".format(getrandbits(40)) 
#####################

    fname = faker.first_name()
    lname = faker.last_name()

    data = {
        'first_name':fname,
        'last_name':lname,
        'birth':bdate,
        'mail':email,
        'number':phone,
        'size':random.choice(size),
        'state':instagram,
        'country':country,
        'city':city,
        'zip':zipcode,
        'street':street
    }
    re = s.post(url, data=data)
    print (re.text)
    
    if re.status_code == 200:
        print("Entry Successful with ", email, "success")
    else:
        print("Error submitting entry", "error")
        

while True:
    main()
    #time.sleep(2)
