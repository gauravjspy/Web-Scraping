import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import datetime
import sqlite3

conn = sqlite3.connect('Women_palazzo.db')
c = conn.cursor()

#c.execute('''CREATE TABLE palazzo(product_link TEXT, product_name TEXT, product_brand TEXT, product_price TEXT, product_mrp TEXT)''')
#print("Table created successfully")

def getSrcapdata(url):
    #headers = {'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0'}
    #r = requests.get(url, headers=headers)
    
    uClient = uReq(url)
    soup = BeautifulSoup(uClient.read(), 'html.parser')
    uClient.close()
    #title = soup.findAll("").text.strip().replace('\n','')
    #print(title)
    xyz = soup.findAll("div",{"class":"_1xHGtK _373qXS"})
    c_date = datetime.datetime.now()
    y = len(xyz)
    #title = soup.find('h1').text.strip().replace('\n','')
    #print(BeautifulSoup.prettify(xyz[0]))

    while (y < 41):
        #print(y)
        y = y + 1
        if (y == 1):
            break
        for s in xyz:
            p_link = (s.a["href"])
            #print(s.a["href"],"\n")
            #print(p_link)

            p_name = s.findAll("a",{"class":"IRpwTa"})
            p_name = p_name[0].text.strip()
            #print(p_name)

            p_brand = s.findAll("div",{"class":"_2WkVRV"})
            p_brand = p_brand[0].text.strip()
            #print(p_brand)

            c_price = s.findAll("div",{"class":"_30jeq3"})
            c_price = c_price[0].text.strip()
            #print(c_price)

            c_MRP = s.findAll("div",{"class":"_3I9_wc"})
            c_MRP = c_MRP[0].text.strip()
            #print(c_MRP)

            img_link = s.findAll("img",{"class":"_2r_T1I"})
            img_link = img_link[0]
            #print(img_link)

            c.execute('INSERT INTO palazzo VALUES(?,?,?,?,?)',(p_link, p_name, p_brand, c_price, c_MRP))
            conn.commit()
    #print(c_date, p_link, p_name, p_brand, c_price, c_MRP)

    #c.execute('SELECT * FROM palazzo')
    #results = c.fetchall()
    #print(results)

getSrcapdata('https://www.flipkart.com/palazzos/pr?sid=clo%2Ccfv%2Cmn6&otracker[]=categorytree&otracker[]=nmenu_sub_Women_0_Palazzos')
print("Page 1 Completed")

def getSrcapdata_1(url):
    uClient = uReq(url)
    soup = BeautifulSoup(uClient.read(), 'html.parser')
    uClient.close()
    abc = soup.findAll("div",{"class":"_1xHGtK _373qXS"})
    c_date = datetime.datetime.now()
    y = len(abc)
   #print(BeautifulSoup.prettify(abc[0]))

    while (y < 41):
        #print(y)
        y = y + 1
        if (y == 1):
            break
        for s in abc:
            p_link = (s.a["href"])

            p_name = s.findAll("a",{"class":"IRpwTa"})
            p_name = p_name[0].text.strip()

            p_brand = s.findAll("div",{"class":"_2WkVRV"})
            p_brand = p_brand[0].text.strip()

            c_price = s.findAll("div",{"class":"_30jeq3"})
            c_price = c_price[0].text.strip()

            c_MRP = s.findAll("div",{"class":"_3I9_wc"})
            c_MRP = c_MRP[0].text.strip()

            img_link = s.findAll("img",{"class":"_2r_T1I"})
            img_link = img_link[0]

            c.execute('INSERT INTO palazzo VALUES(?,?,?,?,?)',(p_link, p_name, p_brand, c_price, c_MRP))
            conn.commit()

    #c.execute('SELECT * FROM palazzo')
    #results = c.fetchall()
    #print(results)

        

getSrcapdata_1('https://www.flipkart.com/palazzos/pr?sid=clo%2Ccfv%2Cmn6&otracker%5B%5D=categorytree&otracker%5B%5D=nmenu_sub_Women_0_Palazzos&page=2')
print("Page 2 Completed")

def getSrcapdata_2(url):
    uClient = uReq(url)
    soup = BeautifulSoup(uClient.read(), 'html.parser')
    uClient.close()
    abc = soup.findAll("div",{"class":"_1xHGtK _373qXS"})
    c_date = datetime.datetime.now()
    y = len(abc)
   #print(BeautifulSoup.prettify(abc[0]))

    while (y < 41):
        #print(y)
        y = y + 1
        if (y == 1):
            break
        for s in abc:
            p_link = (s.a["href"])

            p_name = s.findAll("a",{"class":"IRpwTa"})
            p_name = p_name[0].text.strip()

            p_brand = s.findAll("div",{"class":"_2WkVRV"})
            p_brand = p_brand[0].text.strip()

            c_price = s.findAll("div",{"class":"_30jeq3"})
            c_price = c_price[0].text.strip()

            c_MRP = s.findAll("div",{"class":"_3I9_wc"})
            c_MRP = c_MRP[0].text.strip()

            img_link = s.findAll("img",{"class":"_2r_T1I"})
            img_link = img_link[0]

            c.execute('INSERT INTO palazzo VALUES(?,?,?,?,?)',(p_link, p_name, p_brand, c_price, c_MRP))
            conn.commit()

    #c.execute('SELECT * FROM palazzo')
    #results = c.fetchall()
    #print(results)

        

getSrcapdata_2('https://www.flipkart.com/palazzos/pr?sid=clo%2Ccfv%2Cmn6&otracker%5B%5D=categorytree&otracker%5B%5D=nmenu_sub_Women_0_Palazzos&page=3')
print("Page 3 Completed")

def getSrcapdata_3(url):
    uClient = uReq(url)
    soup = BeautifulSoup(uClient.read(), 'html.parser')
    uClient.close()
    abc = soup.findAll("div",{"class":"_1xHGtK _373qXS"})
    c_date = datetime.datetime.now()
    y = len(abc)
   #print(BeautifulSoup.prettify(abc[0]))

    while (y < 41):
        #print(y)
        y = y + 1
        if (y == 1):
            break
        for s in abc:
            p_link = (s.a["href"])

            p_name = s.findAll("a",{"class":"IRpwTa"})
            p_name = p_name[0].text.strip()

            p_brand = s.findAll("div",{"class":"_2WkVRV"})
            p_brand = p_brand[0].text.strip()

            c_price = s.findAll("div",{"class":"_30jeq3"})
            c_price = c_price[0].text.strip()

            c_MRP = s.findAll("div",{"class":"_3I9_wc"})
            c_MRP = c_MRP[0].text.strip()

            img_link = s.findAll("img",{"class":"_2r_T1I"})
            img_link = img_link[0]

            c.execute('INSERT INTO palazzo VALUES(?,?,?,?,?)',(p_link, p_name, p_brand, c_price, c_MRP))
            conn.commit()

    #c.execute('SELECT * FROM palazzo')
    #results = c.fetchall()
    #print(results)

        

getSrcapdata_3('https://www.flipkart.com/palazzos/pr?sid=clo%2Ccfv%2Cmn6&otracker%5B%5D=categorytree&otracker%5B%5D=nmenu_sub_Women_0_Palazzos&page=4')
print("Page 4 Completed")

def getSrcapdata_4(url):
    uClient = uReq(url)
    soup = BeautifulSoup(uClient.read(), 'html.parser')
    uClient.close()
    abc = soup.findAll("div",{"class":"_1xHGtK _373qXS"})
    c_date = datetime.datetime.now()
    y = len(abc)
   #print(BeautifulSoup.prettify(abc[0]))

    while (y < 41):
        #print(y)
        y = y + 1
        if (y == 1):
            break
        for s in abc:
            p_link = (s.a["href"])

            p_name = s.findAll("a",{"class":"IRpwTa"})
            p_name = p_name[0].text.strip()

            p_brand = s.findAll("div",{"class":"_2WkVRV"})
            p_brand = p_brand[0].text.strip()

            c_price = s.findAll("div",{"class":"_30jeq3"})
            c_price = c_price[0].text.strip()

            c_MRP = s.findAll("div",{"class":"_3I9_wc"})
            c_MRP = c_MRP[0].text.strip()

            img_link = s.findAll("img",{"class":"_2r_T1I"})
            img_link = img_link[0]

            c.execute('INSERT INTO palazzo VALUES(?,?,?,?,?)',(p_link, p_name, p_brand, c_price, c_MRP))
            conn.commit()

    #c.execute('SELECT * FROM palazzo')
    #results = c.fetchall()
    #print(results)

        

getSrcapdata_4('https://www.flipkart.com/palazzos/pr?sid=clo%2Ccfv%2Cmn6&otracker%5B%5D=categorytree&otracker%5B%5D=nmenu_sub_Women_0_Palazzos&page=5')
print("Page 5 Completed")

def getSrcapdata_5(url):
    uClient = uReq(url)
    soup = BeautifulSoup(uClient.read(), 'html.parser')
    uClient.close()
    abc = soup.findAll("div",{"class":"_1xHGtK _373qXS"})
    c_date = datetime.datetime.now()
    y = len(abc)
   #print(BeautifulSoup.prettify(abc[0]))

    while (y < 41):
        #print(y)
        y = y + 1
        if (y == 1):
            break
        for s in abc:
            p_link = (s.a["href"])

            p_name = s.findAll("a",{"class":"IRpwTa"})
            p_name = p_name[0].text.strip()

            p_brand = s.findAll("div",{"class":"_2WkVRV"})
            p_brand = p_brand[0].text.strip()

            c_price = s.findAll("div",{"class":"_30jeq3"})
            c_price = c_price[0].text.strip()

            c_MRP = s.findAll("div",{"class":"_3I9_wc"})
            c_MRP = c_MRP[0].text.strip()

            img_link = s.findAll("img",{"class":"_2r_T1I"})
            img_link = img_link[0]

            c.execute('INSERT INTO palazzo VALUES(?,?,?,?,?)',(p_link, p_name, p_brand, c_price, c_MRP))
            conn.commit()

    #c.execute('SELECT * FROM palazzo')
    #results = c.fetchall()
    #print(results)

        

getSrcapdata_5('https://www.flipkart.com/palazzos/pr?sid=clo%2Ccfv%2Cmn6&otracker%5B%5D=categorytree&otracker%5B%5D=nmenu_sub_Women_0_Palazzos&page=6')
print("Page 6 Completed")

def getSrcapdata_6(url):
    uClient = uReq(url)
    soup = BeautifulSoup(uClient.read(), 'html.parser')
    uClient.close()
    abc = soup.findAll("div",{"class":"_1xHGtK _373qXS"})
    c_date = datetime.datetime.now()
    y = len(abc)
   #print(BeautifulSoup.prettify(abc[0]))

    while (y < 41):
        #print(y)
        y = y + 1
        if (y == 1):
            break
        for s in abc:
            p_link = (s.a["href"])

            p_name = s.findAll("a",{"class":"IRpwTa"})
            p_name = p_name[0].text.strip()

            p_brand = s.findAll("div",{"class":"_2WkVRV"})
            p_brand = p_brand[0].text.strip()

            c_price = s.findAll("div",{"class":"_30jeq3"})
            c_price = c_price[0].text.strip()

            c_MRP = s.findAll("div",{"class":"_3I9_wc"})
            c_MRP = c_MRP[0].text.strip()

            img_link = s.findAll("img",{"class":"_2r_T1I"})
            img_link = img_link[0]

            c.execute('INSERT INTO palazzo VALUES(?,?,?,?,?)',(p_link, p_name, p_brand, c_price, c_MRP))
            conn.commit()

    #c.execute('SELECT * FROM palazzo')
    #results = c.fetchall()
    #print(results)

        

getSrcapdata_6('https://www.flipkart.com/palazzos/pr?sid=clo%2Ccfv%2Cmn6&otracker%5B%5D=categorytree&otracker%5B%5D=nmenu_sub_Women_0_Palazzos&page=7')
print("Page 7 Completed")

def getSrcapdata_7(url):
    uClient = uReq(url)
    soup = BeautifulSoup(uClient.read(), 'html.parser')
    uClient.close()
    abc = soup.findAll("div",{"class":"_1xHGtK _373qXS"})
    c_date = datetime.datetime.now()
    y = len(abc)
   #print(BeautifulSoup.prettify(abc[0]))

    while (y < 41):
        #print(y)
        y = y + 1
        if (y == 1):
            break
        for s in abc:
            p_link = (s.a["href"])

            p_name = s.findAll("a",{"class":"IRpwTa"})
            p_name = p_name[0].text.strip()

            p_brand = s.findAll("div",{"class":"_2WkVRV"})
            p_brand = p_brand[0].text.strip()

            c_price = s.findAll("div",{"class":"_30jeq3"})
            c_price = c_price[0].text.strip()

            c_MRP = s.findAll("div",{"class":"_3I9_wc"})
            c_MRP = c_MRP[0].text.strip()

            img_link = s.findAll("img",{"class":"_2r_T1I"})
            img_link = img_link[0]

            c.execute('INSERT INTO palazzo VALUES(?,?,?,?,?)',(p_link, p_name, p_brand, c_price, c_MRP))
            conn.commit()

    #c.execute('SELECT * FROM palazzo')
    #results = c.fetchall()
    #print(results)

        

getSrcapdata_7('https://www.flipkart.com/palazzos/pr?sid=clo%2Ccfv%2Cmn6&otracker%5B%5D=categorytree&otracker%5B%5D=nmenu_sub_Women_0_Palazzos&page=8')
print("Page 8 Completed")

def getSrcapdata_8(url):
    uClient = uReq(url)
    soup = BeautifulSoup(uClient.read(), 'html.parser')
    uClient.close()
    abc = soup.findAll("div",{"class":"_1xHGtK _373qXS"})
    c_date = datetime.datetime.now()
    y = len(abc)
   #print(BeautifulSoup.prettify(abc[0]))

    while (y < 41):
        #print(y)
        y = y + 1
        if (y == 1):
            break
        for s in abc:
            p_link = (s.a["href"])

            p_name = s.findAll("a",{"class":"IRpwTa"})
            p_name = p_name[0].text.strip()

            p_brand = s.findAll("div",{"class":"_2WkVRV"})
            p_brand = p_brand[0].text.strip()

            c_price = s.findAll("div",{"class":"_30jeq3"})
            c_price = c_price[0].text.strip()

            c_MRP = s.findAll("div",{"class":"_3I9_wc"})
            c_MRP = c_MRP[0].text.strip()

            img_link = s.findAll("img",{"class":"_2r_T1I"})
            img_link = img_link[0]

            c.execute('INSERT INTO palazzo VALUES(?,?,?,?,?)',(p_link, p_name, p_brand, c_price, c_MRP))
            conn.commit()

    #c.execute('SELECT * FROM palazzo')
    #results = c.fetchall()
    #print(results)

        

getSrcapdata_8('https://www.flipkart.com/palazzos/pr?sid=clo%2Ccfv%2Cmn6&otracker%5B%5D=categorytree&otracker%5B%5D=nmenu_sub_Women_0_Palazzos&page=9')
print("Page 9 Completed")

def getSrcapdata_9(url):
    uClient = uReq(url)
    soup = BeautifulSoup(uClient.read(), 'html.parser')
    uClient.close()
    abc = soup.findAll("div",{"class":"_1xHGtK _373qXS"})
    c_date = datetime.datetime.now()
    y = len(abc)
   #print(BeautifulSoup.prettify(abc[0]))

    while (y < 41):
        #print(y)
        y = y + 1
        if (y == 1):
            break
        for s in abc:
            p_link = (s.a["href"])

            p_name = s.findAll("a",{"class":"IRpwTa"})
            p_name = p_name[0].text.strip()

            p_brand = s.findAll("div",{"class":"_2WkVRV"})
            p_brand = p_brand[0].text.strip()

            c_price = s.findAll("div",{"class":"_30jeq3"})
            c_price = c_price[0].text.strip()

            c_MRP = s.findAll("div",{"class":"_3I9_wc"})
            c_MRP = c_MRP[0].text.strip()

            img_link = s.findAll("img",{"class":"_2r_T1I"})
            img_link = img_link[0]

            c.execute('INSERT INTO palazzo VALUES(?,?,?,?,?)',(p_link, p_name, p_brand, c_price, c_MRP))
            conn.commit()

    #c.execute('SELECT * FROM palazzo')
    #results = c.fetchall()
    #print(results)

        

getSrcapdata_9('https://www.flipkart.com/palazzos/pr?sid=clo%2Ccfv%2Cmn6&otracker%5B%5D=categorytree&otracker%5B%5D=nmenu_sub_Women_0_Palazzos&page=10')
print("Page 10 Completed")

def getSrcapdata_10(url):
    uClient = uReq(url)
    soup = BeautifulSoup(uClient.read(), 'html.parser')
    uClient.close()
    abc = soup.findAll("div",{"class":"_1xHGtK _373qXS"})
    c_date = datetime.datetime.now()
    y = len(abc)
   #print(BeautifulSoup.prettify(abc[0]))

    while (y < 41):
        #print(y)
        y = y + 1
        if (y == 1):
            break
        for s in abc:
            p_link = (s.a["href"])

            p_name = s.findAll("a",{"class":"IRpwTa"})
            p_name = p_name[0].text.strip()

            p_brand = s.findAll("div",{"class":"_2WkVRV"})
            p_brand = p_brand[0].text.strip()

            c_price = s.findAll("div",{"class":"_30jeq3"})
            c_price = c_price[0].text.strip()

            c_MRP = s.findAll("div",{"class":"_3I9_wc"})
            c_MRP = c_MRP[0].text.strip()

            img_link = s.findAll("img",{"class":"_2r_T1I"})
            img_link = img_link[0]

            c.execute('INSERT INTO palazzo VALUES(?,?,?,?,?)',(p_link, p_name, p_brand, c_price, c_MRP))
            conn.commit()

    #c.execute('SELECT * FROM palazzo')
    #results = c.fetchall()
    #print(results)

        

getSrcapdata_10('https://www.flipkart.com/palazzos/pr?sid=clo%2Ccfv%2Cmn6&otracker%5B%5D=categorytree&otracker%5B%5D=nmenu_sub_Women_0_Palazzos&page=11')
print("Page 11 Completed")

def getSrcapdata_11(url):
    uClient = uReq(url)
    soup = BeautifulSoup(uClient.read(), 'html.parser')
    uClient.close()
    abc = soup.findAll("div",{"class":"_1xHGtK _373qXS"})
    c_date = datetime.datetime.now()
    y = len(abc)
   #print(BeautifulSoup.prettify(abc[0]))

    while (y < 41):
        #print(y)
        y = y + 1
        if (y == 1):
            break
        for s in abc:
            p_link = (s.a["href"])

            p_name = s.findAll("a",{"class":"IRpwTa"})
            p_name = p_name[0].text.strip()

            p_brand = s.findAll("div",{"class":"_2WkVRV"})
            p_brand = p_brand[0].text.strip()

            c_price = s.findAll("div",{"class":"_30jeq3"})
            c_price = c_price[0].text.strip()

            c_MRP = s.findAll("div",{"class":"_3I9_wc"})
            c_MRP = c_MRP[0].text.strip()

            img_link = s.findAll("img",{"class":"_2r_T1I"})
            img_link = img_link[0]

            c.execute('INSERT INTO palazzo VALUES(?,?,?,?,?)',(p_link, p_name, p_brand, c_price, c_MRP))
            conn.commit()

    #c.execute('SELECT * FROM palazzo')
    #results = c.fetchall()
    #print(results)

        

getSrcapdata_11('https://www.flipkart.com/palazzos/pr?sid=clo%2Ccfv%2Cmn6&otracker%5B%5D=categorytree&otracker%5B%5D=nmenu_sub_Women_0_Palazzos&page=12')
print("Page 12 Completed")

def getSrcapdata_12(url):
    uClient = uReq(url)
    soup = BeautifulSoup(uClient.read(), 'html.parser')
    uClient.close()
    abc = soup.findAll("div",{"class":"_1xHGtK _373qXS"})
    c_date = datetime.datetime.now()
    y = len(abc)
   #print(BeautifulSoup.prettify(abc[0]))

    while (y < 41):
        #print(y)
        y = y + 1
        if (y == 1):
            break
        for s in abc:
            p_link = (s.a["href"])

            p_name = s.findAll("a",{"class":"IRpwTa"})
            p_name = p_name[0].text.strip()

            p_brand = s.findAll("div",{"class":"_2WkVRV"})
            p_brand = p_brand[0].text.strip()

            c_price = s.findAll("div",{"class":"_30jeq3"})
            c_price = c_price[0].text.strip()

            c_MRP = s.findAll("div",{"class":"_3I9_wc"})
            c_MRP = c_MRP[0].text.strip()

            img_link = s.findAll("img",{"class":"_2r_T1I"})
            img_link = img_link[0]

            c.execute('INSERT INTO palazzo VALUES(?,?,?,?,?)',(p_link, p_name, p_brand, c_price, c_MRP))
            conn.commit()

    #c.execute('SELECT * FROM palazzo')
    #results = c.fetchall()
    #print(results)

        

getSrcapdata_12('https://www.flipkart.com/palazzos/pr?sid=clo%2Ccfv%2Cmn6&otracker%5B%5D=categorytree&otracker%5B%5D=nmenu_sub_Women_0_Palazzos&page=13')
print("Page 13 Completed")

def getSrcapdata_13(url):
    uClient = uReq(url)
    soup = BeautifulSoup(uClient.read(), 'html.parser')
    uClient.close()
    abc = soup.findAll("div",{"class":"_1xHGtK _373qXS"})
    c_date = datetime.datetime.now()
    y = len(abc)
   #print(BeautifulSoup.prettify(abc[0]))

    while (y < 41):
        #print(y)
        y = y + 1
        if (y == 1):
            break
        for s in abc:
            p_link = (s.a["href"])

            p_name = s.findAll("a",{"class":"IRpwTa"})
            p_name = p_name[0].text.strip()

            p_brand = s.findAll("div",{"class":"_2WkVRV"})
            p_brand = p_brand[0].text.strip()

            c_price = s.findAll("div",{"class":"_30jeq3"})
            c_price = c_price[0].text.strip()

            c_MRP = s.findAll("div",{"class":"_3I9_wc"})
            c_MRP = c_MRP[0].text.strip()

            img_link = s.findAll("img",{"class":"_2r_T1I"})
            img_link = img_link[0]

            c.execute('INSERT INTO palazzo VALUES(?,?,?,?,?)',(p_link, p_name, p_brand, c_price, c_MRP))
            conn.commit()

    #c.execute('SELECT * FROM palazzo')
    #results = c.fetchall()
    #print(results)

        

getSrcapdata_13('https://www.flipkart.com/palazzos/pr?sid=clo%2Ccfv%2Cmn6&otracker%5B%5D=categorytree&otracker%5B%5D=nmenu_sub_Women_0_Palazzos&page=14')
print("Page 14 Completed")

def getSrcapdata_14(url):
    uClient = uReq(url)
    soup = BeautifulSoup(uClient.read(), 'html.parser')
    uClient.close()
    abc = soup.findAll("div",{"class":"_1xHGtK _373qXS"})
    c_date = datetime.datetime.now()
    y = len(abc)
   #print(BeautifulSoup.prettify(abc[0]))

    while (y < 41):
        #print(y)
        y = y + 1
        if (y == 1):
            break
        for s in abc:
            p_link = (s.a["href"])

            p_name = s.findAll("a",{"class":"IRpwTa"})
            p_name = p_name[0].text.strip()

            p_brand = s.findAll("div",{"class":"_2WkVRV"})
            p_brand = p_brand[0].text.strip()

            c_price = s.findAll("div",{"class":"_30jeq3"})
            c_price = c_price[0].text.strip()

            c_MRP = s.findAll("div",{"class":"_3I9_wc"})
            c_MRP = c_MRP[0].text.strip()

            img_link = s.findAll("img",{"class":"_2r_T1I"})
            img_link = img_link[0]

            c.execute('INSERT INTO palazzo VALUES(?,?,?,?,?)',(p_link, p_name, p_brand, c_price, c_MRP))
            conn.commit()

    #c.execute('SELECT * FROM palazzo')
    #results = c.fetchall()
    #print(results)

        

getSrcapdata_14('https://www.flipkart.com/palazzos/pr?sid=clo%2Ccfv%2Cmn6&otracker%5B%5D=categorytree&otracker%5B%5D=nmenu_sub_Women_0_Palazzos&page=15')
print("Page 15 Completed")

def getSrcapdata_15(url):
    uClient = uReq(url)
    soup = BeautifulSoup(uClient.read(), 'html.parser')
    uClient.close()
    abc = soup.findAll("div",{"class":"_1xHGtK _373qXS"})
    c_date = datetime.datetime.now()
    y = len(abc)
   #print(BeautifulSoup.prettify(abc[0]))

    while (y < 41):
        #print(y)
        y = y + 1
        if (y == 1):
            break
        for s in abc:
            p_link = (s.a["href"])

            p_name = s.findAll("a",{"class":"IRpwTa"})
            p_name = p_name[0].text.strip()

            p_brand = s.findAll("div",{"class":"_2WkVRV"})
            p_brand = p_brand[0].text.strip()

            c_price = s.findAll("div",{"class":"_30jeq3"})
            c_price = c_price[0].text.strip()

            c_MRP = s.findAll("div",{"class":"_3I9_wc"})
            c_MRP = c_MRP[0].text.strip()

            img_link = s.findAll("img",{"class":"_2r_T1I"})
            img_link = img_link[0]

            c.execute('INSERT INTO palazzo VALUES(?,?,?,?,?)',(p_link, p_name, p_brand, c_price, c_MRP))
            conn.commit()

    #c.execute('SELECT * FROM palazzo')
    #results = c.fetchall()
    #print(results)

        

getSrcapdata_15('https://www.flipkart.com/palazzos/pr?sid=clo%2Ccfv%2Cmn6&otracker%5B%5D=categorytree&otracker%5B%5D=nmenu_sub_Women_0_Palazzos&page=16')
print("Page 16 Completed")

def getSrcapdata_16(url):
    uClient = uReq(url)
    soup = BeautifulSoup(uClient.read(), 'html.parser')
    uClient.close()
    abc = soup.findAll("div",{"class":"_1xHGtK _373qXS"})
    c_date = datetime.datetime.now()
    y = len(abc)
   #print(BeautifulSoup.prettify(abc[0]))

    while (y < 41):
        #print(y)
        y = y + 1
        if (y == 1):
            break
        for s in abc:
            p_link = (s.a["href"])

            p_name = s.findAll("a",{"class":"IRpwTa"})
            p_name = p_name[0].text.strip()

            p_brand = s.findAll("div",{"class":"_2WkVRV"})
            p_brand = p_brand[0].text.strip()

            c_price = s.findAll("div",{"class":"_30jeq3"})
            c_price = c_price[0].text.strip()

            c_MRP = s.findAll("div",{"class":"_3I9_wc"})
            c_MRP = c_MRP[0].text.strip()

            img_link = s.findAll("img",{"class":"_2r_T1I"})
            img_link = img_link[0]

            c.execute('INSERT INTO palazzo VALUES(?,?,?,?,?)',(p_link, p_name, p_brand, c_price, c_MRP))
            conn.commit()

    #c.execute('SELECT * FROM palazzo')
    #results = c.fetchall()
    #print(results)

        

getSrcapdata_16('https://www.flipkart.com/palazzos/pr?sid=clo%2Ccfv%2Cmn6&otracker%5B%5D=categorytree&otracker%5B%5D=nmenu_sub_Women_0_Palazzos&page=17')
print("Page 17 Completed")

def getSrcapdata_17(url):
    uClient = uReq(url)
    soup = BeautifulSoup(uClient.read(), 'html.parser')
    uClient.close()
    abc = soup.findAll("div",{"class":"_1xHGtK _373qXS"})
    c_date = datetime.datetime.now()
    y = len(abc)
   #print(BeautifulSoup.prettify(abc[0]))

    while (y < 41):
        #print(y)
        y = y + 1
        if (y == 1):
            break
        for s in abc:
            p_link = (s.a["href"])

            p_name = s.findAll("a",{"class":"IRpwTa"})
            p_name = p_name[0].text.strip()

            p_brand = s.findAll("div",{"class":"_2WkVRV"})
            p_brand = p_brand[0].text.strip()

            c_price = s.findAll("div",{"class":"_30jeq3"})
            c_price = c_price[0].text.strip()

            c_MRP = s.findAll("div",{"class":"_3I9_wc"})
            c_MRP = c_MRP[0].text.strip()

            img_link = s.findAll("img",{"class":"_2r_T1I"})
            img_link = img_link[0]

            c.execute('INSERT INTO palazzo VALUES(?,?,?,?,?)',(p_link, p_name, p_brand, c_price, c_MRP))
            conn.commit()

    #c.execute('SELECT * FROM palazzo')
    #results = c.fetchall()
    #print(results)

        

getSrcapdata_17('https://www.flipkart.com/palazzos/pr?sid=clo%2Ccfv%2Cmn6&otracker%5B%5D=categorytree&otracker%5B%5D=nmenu_sub_Women_0_Palazzos&page=18')
print("Page 18 Completed")

def getSrcapdata_18(url):
    uClient = uReq(url)
    soup = BeautifulSoup(uClient.read(), 'html.parser')
    uClient.close()
    abc = soup.findAll("div",{"class":"_1xHGtK _373qXS"})
    c_date = datetime.datetime.now()
    y = len(abc)
   #print(BeautifulSoup.prettify(abc[0]))

    while (y < 41):
        #print(y)
        y = y + 1
        if (y == 1):
            break
        for s in abc:
            p_link = (s.a["href"])

            p_name = s.findAll("a",{"class":"IRpwTa"})
            p_name = p_name[0].text.strip()

            p_brand = s.findAll("div",{"class":"_2WkVRV"})
            p_brand = p_brand[0].text.strip()

            c_price = s.findAll("div",{"class":"_30jeq3"})
            c_price = c_price[0].text.strip()

            c_MRP = s.findAll("div",{"class":"_3I9_wc"})
            c_MRP = c_MRP[0].text.strip()

            img_link = s.findAll("img",{"class":"_2r_T1I"})
            img_link = img_link[0]

            c.execute('INSERT INTO palazzo VALUES(?,?,?,?,?)',(p_link, p_name, p_brand, c_price, c_MRP))
            conn.commit()

    #c.execute('SELECT * FROM palazzo')
    #results = c.fetchall()
    #print(results)

        

getSrcapdata_18('https://www.flipkart.com/palazzos/pr?sid=clo%2Ccfv%2Cmn6&otracker%5B%5D=categorytree&otracker%5B%5D=nmenu_sub_Women_0_Palazzos&page=19')
print("Page 19 Completed")

def getSrcapdata_19(url):
    uClient = uReq(url)
    soup = BeautifulSoup(uClient.read(), 'html.parser')
    uClient.close()
    abc = soup.findAll("div",{"class":"_1xHGtK _373qXS"})
    c_date = datetime.datetime.now()
    y = len(abc)
   #print(BeautifulSoup.prettify(abc[0]))

    while (y < 41):
        #print(y)
        y = y + 1
        if (y == 1):
            break
        for s in abc:
            p_link = (s.a["href"])

            p_name = s.findAll("a",{"class":"IRpwTa"})
            p_name = p_name[0].text.strip()

            p_brand = s.findAll("div",{"class":"_2WkVRV"})
            p_brand = p_brand[0].text.strip()

            c_price = s.findAll("div",{"class":"_30jeq3"})
            c_price = c_price[0].text.strip()

            c_MRP = s.findAll("div",{"class":"_3I9_wc"})
            c_MRP = c_MRP[0].text.strip()

            img_link = s.findAll("img",{"class":"_2r_T1I"})
            img_link = img_link[0]

            c.execute('INSERT INTO palazzo VALUES(?,?,?,?,?)',(p_link, p_name, p_brand, c_price, c_MRP))
            conn.commit()

    #c.execute('SELECT * FROM palazzo')
    #results = c.fetchall()
    #print(results)

        

getSrcapdata_19('https://www.flipkart.com/palazzos/pr?sid=clo%2Ccfv%2Cmn6&otracker%5B%5D=categorytree&otracker%5B%5D=nmenu_sub_Women_0_Palazzos&page=20')
print("Page 20 Completed")

def getSrcapdata_20(url):
    uClient = uReq(url)
    soup = BeautifulSoup(uClient.read(), 'html.parser')
    uClient.close()
    abc = soup.findAll("div",{"class":"_1xHGtK _373qXS"})
    c_date = datetime.datetime.now()
    y = len(abc)
   #print(BeautifulSoup.prettify(abc[0]))

    while (y < 41):
        #print(y)
        y = y + 1
        if (y == 1):
            break
        for s in abc:
            p_link = (s.a["href"])

            p_name = s.findAll("a",{"class":"IRpwTa"})
            p_name = p_name[0].text.strip()

            p_brand = s.findAll("div",{"class":"_2WkVRV"})
            p_brand = p_brand[0].text.strip()

            c_price = s.findAll("div",{"class":"_30jeq3"})
            c_price = c_price[0].text.strip()

            c_MRP = s.findAll("div",{"class":"_3I9_wc"})
            c_MRP = c_MRP[0].text.strip()

            img_link = s.findAll("img",{"class":"_2r_T1I"})
            img_link = img_link[0]

            c.execute('INSERT INTO palazzo VALUES(?,?,?,?,?)',(p_link, p_name, p_brand, c_price, c_MRP))
            conn.commit()

    #c.execute('SELECT * FROM palazzo')
    #results = c.fetchall()
    #print(results)

        

getSrcapdata_20('https://www.flipkart.com/palazzos/pr?sid=clo%2Ccfv%2Cmn6&otracker%5B%5D=categorytree&otracker%5B%5D=nmenu_sub_Women_0_Palazzos&page=21')
print("Page 21 Completed")

def getSrcapdata_21(url):
    uClient = uReq(url)
    soup = BeautifulSoup(uClient.read(), 'html.parser')
    uClient.close()
    abc = soup.findAll("div",{"class":"_1xHGtK _373qXS"})
    c_date = datetime.datetime.now()
    y = len(abc)
   #print(BeautifulSoup.prettify(abc[0]))

    while (y < 41):
        #print(y)
        y = y + 1
        if (y == 1):
            break
        for s in abc:
            p_link = (s.a["href"])

            p_name = s.findAll("a",{"class":"IRpwTa"})
            p_name = p_name[0].text.strip()

            p_brand = s.findAll("div",{"class":"_2WkVRV"})
            p_brand = p_brand[0].text.strip()

            c_price = s.findAll("div",{"class":"_30jeq3"})
            c_price = c_price[0].text.strip()

            c_MRP = s.findAll("div",{"class":"_3I9_wc"})
            c_MRP = c_MRP[0].text.strip()

            img_link = s.findAll("img",{"class":"_2r_T1I"})
            img_link = img_link[0]

            c.execute('INSERT INTO palazzo VALUES(?,?,?,?,?)',(p_link, p_name, p_brand, c_price, c_MRP))
            conn.commit()

    #c.execute('SELECT * FROM palazzo')
    #results = c.fetchall()
    #print(results)

        

getSrcapdata_21('https://www.flipkart.com/palazzos/pr?sid=clo%2Ccfv%2Cmn6&otracker%5B%5D=categorytree&otracker%5B%5D=nmenu_sub_Women_0_Palazzos&page=22')
print("Page 22 Completed")

def getSrcapdata_22(url):
    uClient = uReq(url)
    soup = BeautifulSoup(uClient.read(), 'html.parser')
    uClient.close()
    abc = soup.findAll("div",{"class":"_1xHGtK _373qXS"})
    c_date = datetime.datetime.now()
    y = len(abc)
   #print(BeautifulSoup.prettify(abc[0]))

    while (y < 41):
        #print(y)
        y = y + 1
        if (y == 1):
            break
        for s in abc:
            p_link = (s.a["href"])

            p_name = s.findAll("a",{"class":"IRpwTa"})
            p_name = p_name[0].text.strip()

            p_brand = s.findAll("div",{"class":"_2WkVRV"})
            p_brand = p_brand[0].text.strip()

            c_price = s.findAll("div",{"class":"_30jeq3"})
            c_price = c_price[0].text.strip()

            c_MRP = s.findAll("div",{"class":"_3I9_wc"})
            c_MRP = c_MRP[0].text.strip()

            img_link = s.findAll("img",{"class":"_2r_T1I"})
            img_link = img_link[0]

            c.execute('INSERT INTO palazzo VALUES(?,?,?,?,?)',(p_link, p_name, p_brand, c_price, c_MRP))
            conn.commit()

    #c.execute('SELECT * FROM palazzo')
    #results = c.fetchall()
    #print(results)

        

getSrcapdata_22('https://www.flipkart.com/palazzos/pr?sid=clo%2Ccfv%2Cmn6&otracker%5B%5D=categorytree&otracker%5B%5D=nmenu_sub_Women_0_Palazzos&page=2')
print("Page 23 Completed")

def getSrcapdata_23(url):
    uClient = uReq(url)
    soup = BeautifulSoup(uClient.read(), 'html.parser')
    uClient.close()
    abc = soup.findAll("div",{"class":"_1xHGtK _373qXS"})
    c_date = datetime.datetime.now()
    y = len(abc)
   #print(BeautifulSoup.prettify(abc[0]))

    while (y < 41):
        #print(y)
        y = y + 1
        if (y == 1):
            break
        for s in abc:
            p_link = (s.a["href"])

            p_name = s.findAll("a",{"class":"IRpwTa"})
            p_name = p_name[0].text.strip()

            p_brand = s.findAll("div",{"class":"_2WkVRV"})
            p_brand = p_brand[0].text.strip()

            c_price = s.findAll("div",{"class":"_30jeq3"})
            c_price = c_price[0].text.strip()

            c_MRP = s.findAll("div",{"class":"_3I9_wc"})
            c_MRP = c_MRP[0].text.strip()

            img_link = s.findAll("img",{"class":"_2r_T1I"})
            img_link = img_link[0]

            c.execute('INSERT INTO palazzo VALUES(?,?,?,?,?)',(p_link, p_name, p_brand, c_price, c_MRP))
            conn.commit()

    #c.execute('SELECT * FROM palazzo')
    #results = c.fetchall()
    #print(results)

        

getSrcapdata_23('https://www.flipkart.com/palazzos/pr?sid=clo%2Ccfv%2Cmn6&otracker%5B%5D=categorytree&otracker%5B%5D=nmenu_sub_Women_0_Palazzos&page=24')
print("Page 24 Completed")

def getSrcapdata_24(url):
    uClient = uReq(url)
    soup = BeautifulSoup(uClient.read(), 'html.parser')
    uClient.close()
    abc = soup.findAll("div",{"class":"_1xHGtK _373qXS"})
    c_date = datetime.datetime.now()
    y = len(abc)
   #print(BeautifulSoup.prettify(abc[0]))

    while (y < 41):
        #print(y)
        y = y + 1
        if (y == 1):
            break
        for s in abc:
            p_link = (s.a["href"])

            p_name = s.findAll("a",{"class":"IRpwTa"})
            p_name = p_name[0].text.strip()

            p_brand = s.findAll("div",{"class":"_2WkVRV"})
            p_brand = p_brand[0].text.strip()

            c_price = s.findAll("div",{"class":"_30jeq3"})
            c_price = c_price[0].text.strip()

            c_MRP = s.findAll("div",{"class":"_3I9_wc"})
            c_MRP = c_MRP[0].text.strip()

            img_link = s.findAll("img",{"class":"_2r_T1I"})
            img_link = img_link[0]

            c.execute('INSERT INTO palazzo VALUES(?,?,?,?,?)',(p_link, p_name, p_brand, c_price, c_MRP))
            conn.commit()

    #c.execute('SELECT * FROM palazzo')
    #results = c.fetchall()
    #print(results)

        

getSrcapdata_24('https://www.flipkart.com/palazzos/pr?sid=clo%2Ccfv%2Cmn6&otracker%5B%5D=categorytree&otracker%5B%5D=nmenu_sub_Women_0_Palazzos&page=25')
print("Page 25 Completed")