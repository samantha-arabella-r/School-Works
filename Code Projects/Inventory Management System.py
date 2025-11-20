'''#NOTES
NOTES/HOW-TO-USE:
**In login module, please enter "admin" as username and "0000" as password to access the inventory system dashboard.**
**This inventory management system is case-sensitive.**

Some of the code existing here are not yet discussed in class lessons, with the group's drive to make our project better 
we searched online how to do things like the nested list, fstrings, and more that helped the system look more 
presentable. Along the codes here, you will stumble upon comments that contains "reference" and links, those are the things 
that the group used as guides.

***Arriving in dashboard, you will have to choose an option stating what you want to access in the inventory system.***
[1] Product List - choosing this will let you see the products that are in the inventory together with its price.
[2] Inventory - choosing this will let you see the products' quantity(ilan lahat), remaining quantity(quantity minus sales, ilan yung natirang qty), and sales(ilan nabenta).
                You can add, remove, and update (price, quantity, sales, capital) products here.
[3] Sales - it is similar to the [2] Inventory but things like capital and income are added. Also, you can't modify
            anything with the data presented in this page.
[4] Purchase - this page is only used when a customer wants to buy from you. This makes the inventory a multi-purpose thing
                since it can act similar to a POS System. 
[5] Search Product - this page searches if the product you entered is existing in the inventory or not. 

by:Samantha A.R.
'''

#DATA-AREA-ONLY
#DASHBOARD DATA
    #Learning Reference for table (nestedlist) and fstrings: https://youtu.be/fsBslGyCeYI
gap=' '*3
data_list=[
    # 0          1                2           3         4        5          6               7            8           9          10
    ['id', 'Product Name', 'Retail Price', 'Unit',    'Qty.', 'Sales', 'Captl.perpc',  'Rem.Qty', 'totlCaptl', 'totlAmnt', 'Income'],
    ['1',     'Monitor',         7500,       'pcs',     30,       2,        6500, ],
    ['2',     'Keyboard',        299,       'pcs',     77,       24,       187, ],
    ['3',     'Mouse',           100,        'pcs',     64,       39,       54,  ],
    ['4',     'Headset',         385,       'pcs',     60,       24,        289,  ],
    ['5',     'Webcam',          289,       'pcs',     54,       13,       175,  ],
    ['6',    'Flash Drive',      245,        'pcs',    100,       40,       110,  ],
    ['7',    'Mouse Pad',        100,        'pcs',     87,       13,       65, ],
    ['8',    'Microphone',       2500,       'pcs',    70,       27,       2100,  ],
    ['9',    'USB Port Hub',     265,        'pcs',     67,       11,      125,  ],
    ['10','External hard drive',   1750,        'pcs',   59,     43,      1431, ],
    ['11','Anti-static wrist strap', 50,     'pcs',     98,        45,      37, ],
    ['12',  'Anti-static mat',    420,        'pcs',     95,        67,      317, ]]


#CODE-STARTS-HERE
while True: #loop for back to login module
    print("\n\n---------- LOGIN ----------")
    print("INVENTORY MANAGEMENT SYSTEM")
    
    #loginModule
    username=str(input("Enter username:"))
    password=str(input("Enter password:"))
    

    while True: #loop back to dashboard page
        if (username=="admin" and password=="0000"):
            print("\n\n\n---------- INVENTORY MANAGEMENT SYSTEM ----------")
            print("*** DASHBOARD ***")        
            print("[1] Product List")         
            print("[2] Inventory")            
            print("[3] Sales")                
            print("[4] Purchase")             
            print("[5] Search product")       
            print("[6] View inventory report") 
            print("[7] Logout")               
            dashOP=str(input("Enter option:"))


            if dashOP == "1" or dashOP=="one" or dashOP=="ONE" or dashOP=="One": #[1]ProductList-StartLine-Done-Debugged
                print("\n\n\n***** PRODUCT LIST *****")
                    #product list table heading
                pl_tableHeading=f"{'id':^5s}{gap}{'Product Name':^25s}{gap}{'Price':^5s}"
                print("-"*45)
                print(pl_tableHeading)
                print("-"*45)
                    #tableproductlist
                for data in data_list[1:]: 
                    rec=f"{data[0]:^5s}{gap}{data[1]:^25s}{gap}{data[2]:^5d}"
                    print(rec)
                print("-"*45)
                print("\n[1] Back to dashboard")
                print("[2] Log out")
                stop2=str(input("Enter option:"))
                if stop2=="1" or stop2=="one" or stop2=="ONE" or stop2=="One":
                    continue
                elif stop2=="2" or stop2=="two" or stop2=="TWO" or stop2=="Two":
                    print("\nLogged out.")
                    break
                else:
                    print("\nThe option you entered is invalid.")
                    print("You will be directed back to dashboard.")
                    continue
            #ProductList-EndLine


            elif dashOP == "2" or dashOP=="two" or dashOP=="TWO" or dashOP=="Two": #[2]Inventory-StartLine-Done-Debugged
                print("\n\n\n***** INVENTORY *****")
                    #inventory table heading
                inv_tableHeading=f"{'id':^5s}{gap}{'Product Name':^25s}{gap}{'Retail Price':^12s}{gap}{'Unit':^5s}{gap}{'Qty.':^5s}{gap}{'Sales':^6s}{gap}{'Rem.Qty.':^8s}"
                print("-"*90)
                print(inv_tableHeading)
                print("-"*90)
                    #tableinventory
                for data in data_list[1:]:
                    d_Seven=data[4]-data[5]
                    d_eight=data[6]*data[4] 
                    d_nine=data[2]*data[5] 
                    rec1=f"{data[0]:^5s}{gap}{data[1]:^25s}{gap}{data[2]:^12d}{gap}{data[3]:^5s}{gap}{data[4]:^5d}{gap}{data[5]:^6d}{gap}{d_Seven:^8d}"
                    print(rec1)
                print("-"*90)

                print("\n[1] Add Product")
                print("[2] Remove Product")
                print("[3] Update Product")
                print("[4] Back to dashboard")
                print("[5] Log out")
                stop2=str(input("Enter option:"))
                if stop2=="1" or stop2=="One" or stop2=="one" or stop2=="ONE": #[1]AddProduct-Inventory Reference: https://pynative.com/python-accept-list-input-from-user/
                    print("\n")
                    print("="*15)
                    print("Adding Product")
                    print("="*15)
                    addprod=[]
                    howmany_product=(input("\nHow many product/s do you want to add? "))
                    if howmany_product.isdigit():
                        change=int(howmany_product)
                        for i in range (0, change):
                            print("\n")
                            id=str(input("Enter product id: "))
                            prodname=input("Enter product name: ")
                            price=str(input("Enter product price: "))
                            if price.isdigit():
                                price1=int(price)
                            else:
                                print("\nFAILED TO ADD PRODUCT/S!")
                                print("Please enter integers only. Try again.")
                                break
                            unit=str(input("Enter product unit: "))
                            qty=input("Enter product quantity: ")
                            if qty.isdigit():
                                qty1=int(qty)
                            else:
                                print("\nFAILED TO ADD PRODUCT!/S")
                                print("Please enter integers only. Try again.")
                                break
                            sales=input("Enter product sales: ")
                            if sales.isdigit():
                                sales1=int(sales)
                                if sales1<=qty1:
                                    pass
                                else:
                                    print("\nFAILED TO ADD PRODUCT/S!")
                                    print("The product sales you entered exceeds the product quantity you inputted.")
                                    print("Product sales must not exceed the product quantity.")
                                    break
                            else:
                                print("\nFAILED TO ADD PRODUCT/S!")
                                print("Please enter integers only. Try again.")
                                break
                            capperpc=input("Enter product capital (per product): ")
                            if capperpc.isdigit():
                                capperpc1=int(capperpc)
                                if capperpc1<price1:
                                    pass
                                else:
                                    print("\nFAILED TO ADD PRODUCT/S!")
                                    print("The product capital you entered exceeds the product price you inputted.")
                                    print("Product capital must not be higher than the product price.")
                                    break
                            else:
                                print("\nFAILED TO ADD PRODUCT/S!")
                                print("Please enter integers only. Try again.")
                                break
                            addprod=[id,prodname,price1,unit,qty1,sales1,capperpc1]
                            data_list.append(addprod)
                            print("\nThe product you entered is added to inventory.")
                        print("\n[1] View Inventory")
                        print("[2] Back to dashboard")
                        stop3=(input("Enter option:"))
                        if stop3=="1" or stop3=="ONE" or stop3=="one" or stop3=="One": #copypasted from the above code- VIEW UPDATED INVENTORY
                            print("\n\n***** INVENTORY *****")
                            #inventory table heading
                            inv_tableHeading=f"{'id':^5s}{gap}{'Product Name':^25s}{gap}{'Retail Price':^12s}{gap}{'Unit':^5s}{gap}{'Qty.':^5s}{gap}{'Sales':^6s}{gap}{'Rem.Qty.':^8s}"
                            print("-"*90)
                            print(inv_tableHeading)
                            print("-"*90)
                                    #tableinventory
                            for data in data_list[1:]:
                                d_Seven=data[4]-data[5]
                                d_eight=data[6]*data[4] 
                                d_nine=data[2]*data[5] 
                                rec1=f"{data[0]:^5s}{gap}{data[1]:^25s}{gap}{data[2]:^12d}{gap}{data[3]:^5s}{gap}{data[4]:^5d}{gap}{data[5]:^6d}{gap}{d_Seven:^8d}"
                                print(rec1)
                            print("-"*90)
                        elif stop3=="2" or stop3=="TWO" or stop3=="two" or stop3=="Two":
                            continue
                        else:
                            print("\nThe option you entered is invalid.")
                            print("You will be directed back to dashboard")
                            continue
                    else:
                        print("\nFAILED!")
                        print("Please enter integers only. Try again.")
                        print("\nYou will be directed back to dashboard.")
                        continue
                elif stop2=="2" or stop2=="two" or stop2=="TWO" or stop2=="Two": #[2] RemoveProduct-Inventory
                    print("\n")
                    print("="*18)
                    print("Removing Product")
                    print("="*18)
                    remove_product= input("\nEnter product name you want to remove from inventory: ")
                    if any(remove_product in x for x in data_list):
                        for sublist in data_list:
                            if remove_product in sublist:
                                list_index=data_list.index(sublist)
                                del data_list[list_index]
                                print("\nThe product you entered is successfully removed.")
                                print("\nYou will be directed back to dashboard.")
                                break
                    else: 
                        print("\nFAILED TO REMOVE PRODUCT!")
                        print("The product you entered is not existing.")
                        print("\nYou will be directed back to dashboard.")
                        continue
                elif stop2=="3" or stop2=="THREE" or stop2=="three" or stop2=="Three": #[3] Update Product
                    print("\n")
                    print("="*18)
                    print("Updating Product")
                    print("="*18)
                    up_product= str(input("\nEnter product name of the item you want to update: "))
                    if any(up_product in x for x in data_list):
                        for sublist in data_list:
                            if up_product in sublist:
                                print("\n What do you want to update from the product ", up_product, "?")
                                print("\n[1] Product Price")
                                print("[2] Product Quantity")
                                print("[3] Product Sales")
                                print("[4] Product Capital (per one item)")
                                op_up_product=(input("\nEnter option: "))
                                if op_up_product =="1" or op_up_product=="ONE" or op_up_product=="one" or op_up_product=="One":
                                    up_price=(input("\nEnter product price:"))
                                    if up_price.isdigit():
                                        up_price1=int(up_price)
                                        updateprod_index=data_list.index(sublist)
                                        for data in data_list[updateprod_index:]:
                                            d_Seven=data[4]-data[5]
                                            d_eight=data[6]*data[4] 
                                            d_nine=data[2]*data[5] 
                                            if up_price1>(data[6]):
                                                data_list[updateprod_index][2]=up_price1
                                                print("\nThe price of", up_product, "is successfully updated.")
                                                print("You will be directed back to dashboard.")
                                                break
                                            else:
                                                print("\nFAILED TO UPDATE PRODUCT!")
                                                print("Retail price must be higher than capital.")
                                                print("\nYou will be directed back to dashboard")
                                                break
                                    else:
                                        print("\nFAILED TO UPDATE PRODUCT!")
                                        print("Please enter integers only. Try again.")
                                        print("\nYou will be directed back to dashboard.")
                                        break
                                elif op_up_product=="2" or op_up_product=="TWO" or op_up_product=="two" or op_up_product=="Two":
                                    up_qty=(input("\nEnter product quantity: "))
                                    if up_qty.isdigit():
                                        up_qty1=int(up_qty)
                                        updateprod_index=data_list.index(sublist)
                                        data_list[updateprod_index][4]=up_qty1
                                        print("\nThe product quantity of", up_product, "is successfully updated.")
                                        print("You will be directed back to dashboard.")
                                        continue
                                    else:
                                        print("\nFAILED TO UPDATE PRODUCT!")
                                        print("Please enter integers only. Try again.")
                                        print("\nYou will be directed back to dashboard.")
                                        break
                                elif op_up_product=="3" or op_up_product=="THREE" or op_up_product=="three" or op_up_product=="Three":
                                    up_sales=(input("\nEnter product sales: "))
                                    updateprod_index=data_list.index(sublist)
                                    if up_sales.isdigit():
                                        up_sales1=int(up_sales)
                                        updateprod_index=data_list.index(sublist)
                                        for data in data_list[updateprod_index:]:
                                            d_Seven=data[4]-data[5]
                                            d_eight=data[6]*data[4] 
                                            d_nine=data[2]*data[5] 
                                            if up_sales1<=d_Seven:
                                                updateprod_index=data_list.index(sublist)
                                                data_list[updateprod_index][5]=up_sales1
                                                print("\nThe product sales of", up_product, "is successfully updated.")
                                                print("You will be directed back to dashboard.")
                                                break
                                            else:
                                                print("\nFAILED TO UPDATE PRODUCT!")
                                                print("The product sales you entered exceeds the total quantity")
                                                print("of the product",up_product, "you entered.")
                                                print("\nYou will be directed back to dashboard.")
                                                break
                                    else:
                                        print("\nFAILED TO UPDATE PRODUCT!")
                                        print("Please enter integers only. Try again.")
                                        print("\nYou will be directed back to dashboard.")
                                        break
                                elif op_up_product=="4" or op_up_product=="FOUR" or op_up_product=="four" or op_up_product=="Four":
                                    up_cptlperpc=(input("\nEnter product capital (per pc./quantity): "))
                                    updateprod_index=data_list.index(sublist)
                                    if up_cptlperpc.isdigit():
                                        up_cptlperpc1=int(up_cptlperpc)
                                        updateprod_index=data_list.index(sublist)
                                        for data in data_list[updateprod_index:]:
                                            d_Seven=data[4]-data[5]
                                            d_eight=data[6]*data[4] 
                                            d_nine=data[2]*data[5] 
                                            if up_cptlperpc1<(data[2]):
                                                updateprod_index=data_list.index(sublist)
                                                data_list[updateprod_index][6]=up_cptlperpc1
                                                print("\nThe product capital of", up_product, "is successfully updated.")
                                                print("You will be directed back to dashboard.")
                                                break
                                            else:
                                                print("\nFAILED TO UPDATE PRODUCT!")
                                                print("The capital you entered exceeds the retail price.")
                                                print("Capital must not be higher than the retail price.")
                                                print("\nYou will be directed back to dashboard.")
                                                break
                                    else:
                                        print("\nFAILED TO UPDATE PRODUCT!")
                                        print("Please enter integers only. Try again.")
                                        print("\nYou will be directed back to dashboard.")
                                        break
                                else:
                                    print("\nFAILED TO UPDATE PRODUCT!")
                                    print("The option you entered in invalid.")
                                    print("\nYou will be directed back to dashboard.")
                                    continue
                    else:
                        print("\nFAILED TO UPDATE PRODUCT!")
                        print("The product you entered is not existing.")
                        print("\nYou will be directed back to dashboard.")
                        continue
                elif stop2=="4" or stop2=="FOUR" or stop2=="four" or stop2=="Four": #[4]Inventory-Back to dashboard
                    continue
                elif stop2=="5" or stop2=="FIVE" or stop2=="five" or stop2=="Five": #[5] Log out- inventory
                    print("\nLogged out.")
                    break
                else:
                    print("\nThe option you entered is invalid.")
                    print("You will be directed back to dashboard.")
                    continue
            #Inventory-EndLine


            elif dashOP == "3" or dashOP=="THREE" or dashOP=="three" or dashOP=="Three": #[3] Sales-Startline-Done-Debugged
                print("\n\n\n***** SALES *****")
                inv_tableHeading=f"{'id':^5s}{gap}{'Product Name':^25s}{gap}{'Retail Price':^12s}{gap}{'Unit':^5s}{gap}{'Qty.':^5s}{gap}{'Sales':^6s}{gap}{'Rem.Qty.':^8s}{gap}{'Capital':^7s}{gap}{'Total Capital':^13s}{gap}{'Total Amount':^12s}{gap}{'Income':^8s}"
                print("-"*138)
                print(inv_tableHeading)
                print("-"*138)
                #table
                for data in data_list[1:]:
                    d_Seven=data[4]-data[5] #remqty
                    d_eight=data[6]*data[4] #totalcapital
                    d_nine=data[2]*data[5]  #totalamount
                    d_ten=d_nine-d_eight
                    rec1=f"{data[0]:^5s}{gap}{data[1]:^25s}{gap}{data[2]:^12d}{gap}{data[3]:^5s}{gap}{data[4]:^5d}{gap}{data[5]:^6d}{gap}{d_Seven:^8d}{gap}{data[6]:^7d}{gap}{d_eight:^13d}{gap}{d_nine:^12d}{gap}{d_ten:^8d}"
                    print(rec1)
                print("-"*138)
            #Sales-Endline


            elif dashOP =="4" or dashOP=="FOUR" or dashOP=="four" or dashOP=="Four": #[4] Purchase-StartLine-Done-Debugged
                print("\n\n\n***** PURCHASE *****")
                buy_product=str(input("\nEnter product name that you want to buy: "))
                if any(buy_product in x for x in data_list):
                    for sublist in data_list:
                        buyprod_index=data_list.index(sublist)
                        if buy_product in sublist:
                            ask_qty=(input("\nEnter quantity of the product you will buy: "))
                            if ask_qty.isdigit():
                                ask_qty1=int(ask_qty)
                                buyprod_index=data_list.index(sublist)
                                for data in data_list[buyprod_index:]:
                                    d_Seven=data[4]-data[5]
                                    d_eight=data[6]*data[4] 
                                    d_nine=data[2]*data[5] 
                                    if ask_qty1<=d_Seven:
                                        data_list[buyprod_index][5]=data_list[buyprod_index][5]+ask_qty1
                                        print("\n\nYou successfully purchased", ask_qty1, buy_product,"!")
                                        print("Thank you for purchasing!")
                                        print("\nYou will be directed back to dashboard.")
                                        break
                                    else:
                                        print("\nFAILED TO PURCHASE PRODUCT!")
                                        print("The product quantity you entered is insufficient from what the")
                                        print("inventory can provide or is out of stock.")
                                        print("\nYou will be directed back to dashboard.")
                                        break
                            else:
                                print("\nFAILED TO PURCHASE PRODUCT!")
                                print("Please enter integers only. Try again.")
                                print("\nYou will be directed back to dashboard.")
                                break
                else:
                    print("\nThe product you entered is not existing in inventory.")
                    print("\nYou will be directed back to dashboard.")
                    continue
            #Purchase-EndLine
            

            elif dashOP=="5" or dashOP=="FIVE" or dashOP=="five" or dashOP=="Five": #[5]Search product-StartLine-Done-Debugged
                print("\n\n\n***** SEARCH PRODUCT *****")
                print("\n>>> NOTE: YOU WILL BE DIRECTED BACK TO DASHBOARD IF THE PRODUCT YOU ENTERED IS NOT EXISTING. <<<")
                find_product=str(input("\nEnter product name: "))
                if any(find_product in x for x in data_list):
                    print("The product",find_product, "is existing in inventory.")
                    print("\nYou will be directed back to dashboard.")
                else:
                    print("The product", find_product, "is not existing in inventory.")
                    print("\nYou will be directed back to dashboard.")
            #SearchProduct-Endline-Done


            elif dashOP=="6" or dashOP=="six" or dashOP=="SIX" or dashOP=="Six": #[6] View Full Inventory Report-Done-Debugged
                print("\n\n\n*****************")
                print("INVENTORY REPORT")
                print("*****************")
                import datetime #Reference:w3schools
                x = datetime.datetime.now()
                print("\nDate:",x.strftime("%a"),",",x.strftime("%x"))
                print("Time:",x.strftime("%I"),":",x.strftime("%M"),x.strftime("%p"))
                inv_tableHeading=f"{'id':^5s}{gap}{'Product Name':^25s}{gap}{'Retail Price':^12s}{gap}{'Unit':^5s}{gap}{'Qty.':^5s}{gap}{'Sales':^6s}{gap}{'Rem.Qty.':^8s}{gap}{'Capital':^7s}{gap}{'Total Capital':^13s}{gap}{'Total Amount':^12s}{gap}{'Income':^8s}"
                print("-"*138)
                print(inv_tableHeading)
                print("-"*138)
                #table
                for data in data_list[1:]:
                    d_Seven=data[4]-data[5] #remqty
                    d_eight=data[6]*data[4] #totalcapital
                    d_nine=data[2]*data[5]  #totalamount
                    d_ten=d_nine-d_eight
                    rec1=f"{data[0]:^5s}{gap}{data[1]:^25s}{gap}{data[2]:^12d}{gap}{data[3]:^5s}{gap}{data[4]:^5d}{gap}{data[5]:^6d}{gap}{d_Seven:^8d}{gap}{data[6]:^7d}{gap}{d_eight:^13d}{gap}{d_nine:^12d}{gap}{d_ten:^8d}"
                    print(rec1)
                print("-"*138)  
            elif dashOP=="7": #[7]Logout
                print("\nLogged out.")
                break 
            else: 
                print("\nThe option you entered is invalid. Try again.")
        else: #if username and password incorrect
            print("\nInvalid username/password.")
            print("Please try again.")
            break