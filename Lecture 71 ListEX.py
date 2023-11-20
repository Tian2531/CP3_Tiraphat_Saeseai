# CP3_Tiraphat_Saeseai
MenuList = []
PriceList = []

def showBill():
    total = 0
    print("----- My Foods -----")
    for x in range(len(MenuList)):
        print(MenuList[x],PriceList[x])
        total = total + int(PriceList[x])
    print("Total :", total)

while True:
    MenuName = input("Pls Enter Your Menu : ")
    if (MenuName.lower() == "exit"):
        break
    else:
        MenuPrice = input("Price : ")
        MenuList.append(MenuName)
        PriceList.append(MenuPrice)

showBill()
