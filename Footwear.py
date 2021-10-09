from bs4 import BeautifulSoup as soup # HTML data structure
from urllib.request import urlopen as uReq # Web client
import sqlite3

# Create connection
conn = sqlite3.connect('footwear.db')
c = conn.cursor()

#c.execute('''CREATE TABLE footwear(product_link TEXT, product_name TEXT, product_brand TEXT, product_price TEXT, product_mrp TEXT)''')
#print("create table successfully")

#print('''▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ Welcome to Webscraping ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒''')

'''
•	Website: String
•	Product Link: String
•	Product Name: String
•	Product Brand: String
•	Product Category: String
•	Sizes Available: Array
•	Price: Integer
•	MRP Integer
•	Gender: String
•	Description: String
•	Primary Image Link: String
•	Secondary Image Links: Array

'''
# URL for web scrap from in this example we web scrap products from flipkart.com
page_url = "https://www.flipkart.com/mens-footwear/pr?sid=osp,cil&otracker=nmenu_sub_Men_0_Footwear&fm=neo%2Fmerchandising&iid=M_4ab2896f-9a5d-41ec-8ee7-bfd0ead15843_1_372UD5BXDFYS_MC.PR9Y9GHWCY6G&otracker=hp_rich_navigation_5_1.navigationCard.RICH_NAVIGATION_Fashion~Men%2BFootwear_PR9Y9GHWCY6G&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_5_L1_view-all&cid=PR9Y9GHWCY6G"

# opens the connection and downloads html page from url
uClient = uReq(page_url)

#parses html into a soup data structure to travverse html as if it were a json data type
page_soup = soup(uClient.read(), 'html.parser')
uClient.close()


xyz = page_soup.findAll("div",{"class":"_1xHGtK _373qXS"})
pqr = page_soup.findAll("div",{"class":"rcweVK"})
#mno = page_soup.findAll("div",{"class":"_2c7YLP UtUXW0 _6t1WkM _3HqJxg"})
y = len(xyz)
#print(y)
#print(soup.prettify(xyz[0]))

#a = 2

while (y < 41):
    #print(y)
    y = y+1
    if (y == 1):
        break
    #print("Loop terminated")
    for abc in xyz:
        p_link = (abc.a["href"])
        #print(abc.a["href"])
        
        p_name = abc.findAll("a",{"class":"IRpwTa"})
        p_name = p_name[0].text.strip()
        #p_name = str(p_name.encode('utf-8', 'replace'))
        #print(p_name) #Working

        p_brand = abc.findAll("div",{"class":"_2WkVRV"})
        p_brand = p_brand[0].text.strip()
        #p_brand = str(p_brand.encode('utf-8', 'replace'))
        #print(p_brand) # Working

        c_price = abc.findAll("div",{"class":"_30jeq3"})
        c_price = c_price[0].text
        #c_price = str(c_price.encode('utf-8','replace'))
        #c_price = c_price[14:] # Remove first fourteen character from converted
        #print(c_price) # Working

        c_mrp = abc.findAll("div",{"class":"_3I9_wc"})
        c_mrp = c_mrp[0].text
        #c_mrp = str(c_mrp.encode('utf-8','replace'))
        #c_mrp = c_price.translate(None, '[]') # Extract brackets and place none
        #c_mrp = c_mrp[1:]
        #print(c_mrp) # Working

        #p_img_link = abc.findAll("img",{"class":"_2r_T1I"})
        #p_img_link = p_img_link[0]
        #print(p_img_link)

        #for abc in mno:
         #       p_disc = abd.findAll("div",{"class":"row _1v8OXw"})
          #      p_disc = p_disc[0]
           #     print(p_disc)

    
        
        
                

        #try:
        #    p_size = p_size[0].text
        #    print(p_size)
        #except:
        #   print("Error")

        c.execute('''INSERT INTO footwear VALUES(?,?,?,?,?)''',(p_link, p_name, p_brand, c_price, c_price))
        conn.commit()

        #c.execute("SELECT * FROM footwear")
        #results = c.fetchall()
        #print(results)
        #print("Product URL:",abc.a["href"],"\n")
        #print("Product Name: ",p_name,"\n")
        #print("Product Brand: ",p_brand,"\n")
        #print("Current Price: ",c_price,"\n")
        #print("Current MRP: ",c_mrp,"\n")
        #print(abc.img["src"]) # Not working
    #conn.commit()

 #select all data from table
    c.execute('''SELECT * FROM footwear''')
    results = c.fetchall()
    print(results)
        

        #for ac in pqr:
         #   p_size = str(ac.span["class"])
          #  homepage = "https://www.flipkart.com/"
           # p_size = homepage + p_size
            #data3 = p_link + "\n"
'''
        if a == 100:
            page_url = str(page_url[0:-2]) + str(a)
        elif a > 100:
            page_url = str(page_url[0:-3]) + str(a)
        elif a <= 10:
            page_url = str(page_url[0:-1]) + str(a)
        elif 10 < a <= 99:
            page_url = str(page_url[0:-2]) + str(a)

        a = int(a)
        a = a+1
        print(a)'''
'''
        uClient = uReq(page_url)
        page_soup = soup(uClient.read(), 'html.parser')
        uClient.close()

        #print(page_url)
        xyz = page_soup.findAll("div",{"class":"_1xHGtK _373qXS"})
        pqr = page_soup.findAll("div",{"class":"rcweVK"})
        y = len(xyz)
        #print(y)
     '''

     
        
            
            
'''

#finds each product from the store page
containers = page_soup.findAll("div", {"class":"_1xHGtK _373qXS"})
#containers = page_soup.findAll("div", {"class":"_25b18c"})

print(len(containers))
#print(soup.prettify(containers[0]))

# Name of the output file to write to local disk
#filename = "Product.csv"

# Headers of csv file to be weitten
#headers = ""

# Loop over each product and grab attributes about each product
container = containers[0]
print(container.a["href"])

p_name = container.findAll("a",{"class":"IRpwTa"})
print(p_name[0].text)

p_brand = container.findAll("div",{"class":"_2WkVRV"})
print(p_brand[0].text)

#p_price = container.findAll("div",{"class":"_30jeq3"})
p_price = container.findAll("div",{"class":"_25b18c"})
print(p_price[0].text)

#p_mrp = container.findAll("div",{"calss":"_3I9_wc"})
#print(p_mrp[0].text)

#p_size = container.findALl("div",{"class":"Lia2vD"})
#print(p_size[0].text)

#p_gender = container.findAll("span",{"class":"_2I9KP_"})
#print(p_gender[0].text)
'''















