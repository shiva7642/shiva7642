from datetime import datetime
name = input("Enter Your Name: ")
#List of Items
lists='''
Rice    Rs 20/kg
Sugar   Rs 30/kg
Salt    Rs 20/kg
Oil     Rs 80/kg
Paneer  Rs 110/kg
Maggi   Rs 50/kg
Boost   Rs 90/each
Colgate Rs 90/each
'''
#print(lists)
#Declaration
price=0
pricelist=[]
totalprice=0
Finalfinalprice=0
ilist=[]
qlist=[]
plist=[]
#Rates for items
items={'rice':20,'sugar':30,'salt':20,'oil':80,'paneer':110,'maggi':50,'boost':90,'colgate':85}
option=int(input("For List of Items Press 1 : "))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("If you want to buy Press 1 or 2 for exit :"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items :")
        quantity=int(input("Enter Quantity :"))
        if item in items.keys():    
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)    
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("Sorry you entered item is no available")
    else:
        print("You entered wrong number")
    inp=input("Can i bill the items yes or no :")
    if inp=='y':
        pass
        if finalamount !=0:
            print(25*"=","Shiva Supermarket",25*'=')
            print(25*'','Hyderabad')
            print('Name :',name,30*' ','Date :',datetime.now())
            print(75*'-')
            print('Sno',15*' ','items',13*" ",'Quantity',15*' ','Price')   
            for i in range(len(pricelist)):
                print(i,8*' ',9*' ',ilist[i],15*' ',qlist[i],20*' ',plist[i])
            print(75*'-')
            print(50*' ','TotalAmount:','Rs',totalprice)
            print(75*'-')
            print(52*' ','GstAmount:','Rs',gst)            
            print(75*'-')
            print(50*' ','finalAmount:','Rs',finalamount)
            print(75*'-')
            print(20*' ','Thanks for visiting')
            print(75*'-')
    if inp=='n':
        print('Thank you visiting and Welcom')
                    
        