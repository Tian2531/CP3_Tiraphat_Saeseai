# CP3_Tiraphat_Saeseai_Exercise 8 : ปฏิบัติการสร้างโปรแกรมจริงบนเงื่อนไขเขียนโปรแกรมร้านขายของโดยดัดแปลงจากโปรแกรมใน Lecture 40
Username = input("Username : ")
Password = input("Password : ")
if Username == "Tian" and Password == "1234":
    print("Welcome to Tian Restaurants")
    print("This is Menu you can Eat")
    print("1.Prakraphongtodnampra 300 THB")
    print("2.Pizza 250 THB")
    print("3.Ramen 150 THB")
    print("4.Kapao-wagyu 120 THB")
    Userselected = int(input("Pls select menu : "))
    if Userselected == 1:
        Order = int(input("How many do you want : "))
        print("Price",Order*300,"THB")
        print("Vat 7 %")
        Price = Order*300
        Vat = Price*7/100
        print("Total",Price+Vat,"THB")
    if Userselected == 2:
        Order = int(input("How many do you want : "))
        print("Price", Order*250, "THB")
        print("Vat 7 %")
        Price = Order*250
        Vat = Price * 7 / 100
        print("Total", Price + Vat, "THB")
    if Userselected == 3:
        Order = int(input("How many do you want : "))
        print("Price", Order*150, "THB")
        print("Vat 7 %")
        Price = Order * 150
        Vat = Price * 7 / 100
        print("Total", Price + Vat, "THB")
    if Userselected == 4:
        Order = int(input("How many do you want : "))
        print("Price", Order * 120, "THB")
        print("Vat 7 %")
        Price = Order * 120
        Vat = Price * 7 / 100
        print("Total", Price + Vat, "THB")
else:
    print("Invaild Username or Password")
