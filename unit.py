from diagram import *

def main1():
    list=[40,50,60,75]
    list1=["S","M","L","XL"]
    sum=0
    age=int(input("Enter age: "))
    residentPriceinBsh=20
    residentPriceObSh=60
    while age>=18:
        diagrame(tri1, tri2)
        for tr in list1:
            sum+=list[list1.index(tr)]
        tyap= input("Enter size: ")
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
main1()
def chose():
    customer = input("do you want to contnue? y/n ")
    if customer == 'n':
        exit()
    return customer
chose()

