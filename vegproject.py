#list of vegitables...
veg=['bringal','onions','beans','potato','tamato']
#quantity of veg
quantity=[10,20,8,20,30]
#selling prices....
sel_price=[25,19,40,43,20]
#cost prices.....
c_price=[20,14,25,28,15]
#owner id number list
owner_list=['nani','mouni','kalyani','srinvas']
#shopkeeper acces pasword list...
password_list=['nani@123','mouni@123','kalyani@123','srinivas@123']
username_list=[]
phno_list=[]
k=[]
u1=[]
c=[]

while True:
    j=[]
    t=[]
    sum_sellingprice=0
    t1=[]
    y=[]
    cart=[]
    u_qua=[]
    print('select your role ')
    print('1.OWNER')
    print('2.user')
    ch=input('choose one option:')
    if ch.isalpha ():
        print('Error: option must contain only digits!')
    elif ch=='1':
        username=input('enter user name :')  
        if username in owner_list:
            password=input('enter the password:')
            if password in password_list:
                while True:
                    print('1.ADD Iteams To inventry')
                    print('2.Remove Item')
                    print('3.Update Item')
                    print('4.View Inventry')
                    print('5.View User Details')
                    print('6.View Report')
                    print('7.total revenue')
                    print('8.Itemized profit')
                    print('9.exit')
                    selection=input('choose one option :')
                    if  selection.isalpha():
                        print('Error: option must contain only digits!')
                    elif selection=='1':
                        print('*'*20,'ADD ITEMS','*'*20)
                        a_veg=input('enter the vegitable adding to the Inventry:')
                        a_quantity=int(input('enter the quantitity of adding the vegitable:'))
                        a_price=int(input('enter the selling price of adding vegitable:'))
                        a_cprice=int(input('enter the cost price of the  adding vegitable:')) 
                        veg.append(a_veg)
                        quantity.append(a_quantity)
                        sel_price.append(a_price)
                        c_price.append(a_cprice)                     
                        print('successfully adding the vegitables to inventry')
                        print('-'*50)
                    elif selection=='2':
                        print('*'*15,'REMOVE ITEM','*'*15)
                        item=input('which vegitable do you want to remove:')
                        if item in veg:
                            id1=veg.index(item)
                            veg.pop(id1)
                            quantity.pop(id1)
                            sel_price.pop(id1)
                            c_price.pop(id1)
                        else:
                            print('error: item not in list')
                        print('successfully removing the iems in  inventry')                        
                        print('-'*40)
                        
                    elif selection=='3':
                        print('*'*15,'UPDATE ITEMS','*'*15)
                        item12=input('which vegitable prices do you want to modify:')
                        if item12 in veg:
                            id2=veg.index(item12)
                            m_quan=int(input('enter the modified quantity of vegitables :'))
                            m_selprice=int(input('enter the modified selling price  of vegitables :'))
                            m_cprice=int(input('enter the modified cost price of vegitables :'))
                            quantity[id2]=m_quan
                            sel_price[id2]=m_selprice
                            c_price[id2]=m_cprice
                        else:
                            print('error :item is not in list')
                        print('successfully Updating the iems in inventry')                        
                        print('-'*40)
                    elif selection=='4':
                        print('*'*10,'View Inventry','*'*10)                             
                        print('Vegetables  Quantity')
                        for i, j in zip(veg, quantity):
                            print(f"{i}  {j}")
                        print('-'*26)
                        pass
                    elif selection=='5':
                        print('*'*13,'View User Details','*'*12)
                        li=len(username_list)
                        print('username'+'    '+'phno')
                        for i in range(li):                      
                            print(str(username_list[i])+' :   '+str(phno_list[i]))
                        print('-'*26)
                        
                    elif selection=='6':
                        print('*'*10,'report','*'*10)                             
                        print('Vegetables | Quantity  | sel_price  |  c_price')
                        for i, j,q,v in zip(veg, quantity,sel_price,c_price):
                            print(f"{i} | {j}  |  {q}  |  {v}")
                        print('-'*26)
                    elif selection=='7':
                        print('*'*13,'total revenue','*'*13)
                        print('total revenue of the vegitables',revenue,'/-')
                        print('-'*40)
                        print('*'*13,'Total profit','*'*13)
                        totalprofit=revenue-sum_costprice                         
                        print('selling price',revenue,'-','cost price',sum_costprice,'=',totalprofit)                           
                        print('The total profit of whole day :',totalprofit,'/-')                         
                        print('-'*40) 
                        
                    elif selection=='8':
                        print('*'*13,'Itemized profit','*'*13)
                        profits = [sel_price - c_price for sel_price, c_price in zip(sel_price,c_price)]  
                        total_profit = sum(profits)
                        for veg, profits in zip(veg, profits):
                            print(f"{veg}:{profits}")
                        print("Total Profit:", total_profit)
                        print('-'*40)
                        
                    elif selection=='9':
                        break
                        
                    else:
                        print('choose correct option')
            else:
                print('error :incorrect password!')
        else:
            print('error : username didnot match') 
                    
           
                
        
    elif ch=='2':
        print('*'*15,'Welcome to srinivas vegitables shop','*'*15)
        while True:
            print('1.ADD Items to cart')
            print('2.Remove Item from cart')
            print('3.modify cart')
            print('4.View cart')
            print('5.Billing')
            print('6.exiting')
            selection1=input('choose one option :')
            if  selection1.isalpha():
                print('Error: option must contain only digits!')
            elif selection1=='1':
                
                while True:
                     item=input('what do you want sir/mam:')
                     if  item not  in veg:
                            print('enterd item is not available')
                     elif item in veg:
                        kg=int(input('how many kg do you want sir/mam:'))
                        idx=veg.index(item)
                        if kg<=quantity[idx]:
                            cart.append(item)
                            u_qua.append(kg)
                            m=kg*sel_price[idx]
                            u=kg*c_price[idx]
                            k+=[m]
                            c+=[m]
                           # print("c:",c)
                            revenue=sum(c)
                            #print("revenue:",revenue)
                            u1+=[u]
                            j+=[veg[idx]]
                            t+=[sel_price[idx]]
                            t1+=[c_price[idx]]                    
                            y+=[kg]
                            sum_sellingprice=sum_sellingprice+sum(k)
                            sum_costprice=sum(u1)
                            
                            quantity[idx]=quantity[idx]-kg
                            k1=input('Do you want continue shoping(yes/no):')                              
                            if k1=='no':
                                print('items should be added to cart')
                                break
                            elif k1=='yes':
                                print('continue your shopping')
                            else:
                                pass
                     else:
                        print('out of stock...')
                        continue
                            
                
            elif selection1=='2':
                for veg,quantity in zip(cart,u_qua):
                    print(f"{veg}:{quantity}")
                item1=input('enter a vegitable you should want to remove :')
                if item1 in cart:
                    idx=cart.index(item1)
                    cart.pop(idx)
                    u_qua.pop(idx)
                else:
                    print('item is not in cart')
                print('item should be removed from cart')
                
            elif selection1=='3':
                for veg,quantity in zip(cart,u_qua):
                    print(f"{veg}:{quantity}")
                mod=input('enter the modified item/quantity:')
                if mod in cart:
                    idx1=cart.index(mod)
                    user=int(input('enter the quantity you should modify:'))
                    u_qua[idx1]=user
                else:
                    print('enter item not in your card')
                print('items should be modified of your card')
            elif selection1=='4':
                print('*'*15,'view cart','*'*15)
                le=len(cart)
                for i in range(le):
                    total=y[i]*t[i]
                    print(j[i]+' '+str(y[i])+'*'+str(t[i])+' '+':'+str(total))                        
                print('-'*42)
                pass
            elif selection1=='5':
                print('*'*20,'billing','*'*20)
                
                username=input('enter your good name plase sir/madam:')
                if  username.isdigit():
                    print('Error: Username must contain only letters!')
                else:
                    pass
                while True:
                    s = 10
                    phno = input("Enter your phone number: ")
                    if not phno.isdigit():
                        print("Error: Please enter a valid numeric phone number.")
                        
                    elif len(phno) < s:
                        print("Error: Mobile number is too short.")
                        
                    elif len(phno) > s:
                        print("Error: Mobile number is too long.")
                    elif phno[0] in {'1','2','3','4','5'}:
                        print('Error: Phone numbers cannot start with 1, 2, 3, 4,5')                       
                    else:
                        
                       username_list+=[username]
                       phno_list+=[phno]
                       sum_sellingprice=0
                       for i in range(len(y)):
                           
                           total=y[i]*t[i]
                           sum_sellingprice += total
                           print(j[i]+'  '+str(y[i])+'*'+str(t[i])+'  '+':'+str(total))                        
                       print('-'*46)
                       break
                        
                print('total ammount:',sum_sellingprice,'/-')
                        
                print('Thank you sir visit again')
                
                k=[]
                pass
            elif selection1=='6':
                break
            else:
                print('choose the option correctly')
    else:
        print('choose the option correctly')
