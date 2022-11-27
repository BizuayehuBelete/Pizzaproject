import random

tri1 = random.randint(1, 9)
tri2 = random.randint(1, 9)
def diigame(p,y):
    diegame = input("Do you want to play a diegame? y/n ")
    if diegame == 'y':
         product=tri2*tri1
         return product
product=tri1*tri2
    # if diegame == 'y':
    #     print(player1)
    #     print(player2)
    #     product = player1 * player2
    #     print(product)
    #     print(product / 100)
    # else:
    #     print("thank you")
def main():
    list=[40,50,60,75]
    list1=["S","M","L","XL"]
    sum=0
    age=int(input("Enter age: "))
    residentPriceinBsh=20
    residentPriceObSh=60
    while age>=18:
        diigame(tri1, tri2)
        for tr in list1:
            sum+=list[list1.index(tr)]
        tyap = input("Enter size: ")
        extraslice = input("do you want to extra slices y/n")
        if extraslice == "y":
            amountExtra = int(input("how many extra do yo want to add? "))
            sum += amountExtra * 2

        destnation = input("enter your destnatuion: ")
        if destnation == "beersheba":
            sum += list[list1.index(tr)] + residentPriceinBsh
        else:
            sum += list[list1.index(tr)] + residentPriceObSh

        print(sum)
    #print(sum-(product/100))
        print(sum*(1-(product/100)))
    else:
        print(" Soory you canot order!!")
main()
def chose():
    customer = input("do you want to contnue? y/n ")
    if customer == 'n':
        exit()
    return customer
chose()