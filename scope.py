#local and global variable
#global variable
balance=3000

def buy_things(item,price):
    #local scope variable
    #you can access glopal variable without using the global keyword
    print('previous balance value',balance)
    balance=600 #akhna dila local hit korba
    #balance=balance
    #if u want to modify a global bariable ,u have to use the global keyword
    gloabal balance
    balance=500
    dream_phone ='xphone'
    #balance=balance-price
   # print('balance inside the function' balance)
    print(f'balance after buying {item}',balance)

#print(dream_phone)
buy_things('sunglass',1000)