CardNumberStr = input()
cardNumber = list(map(int, CardNumberStr))
flag=0
size = len(cardNumber)
end = -1 if size % 2 == 0 else 0

for i in range(len(cardNumber) - 2, end, -2):

    if cardNumber[i] * 2 > 9:
        cardNumber[i] = 1 + cardNumber[i] * 2 % 10
    else:
        cardNumber[i] =cardNumber[i] * 2
checksum=0
for i in range(size):
    checksum += cardNumber[i]


#print(checksum)
if checksum % 10 == 0:
    flag=1
else:
    flag=0
if(flag==1):
    start=int(CardNumberStr[0]) * 10 +int(CardNumberStr[1])

    if(start==34 or start==37):
        print("American Express")
    elif(start>=51 and start<=55):
        print("MasterCard")
    elif(int(CardNumberStr[0])):
        print("Visa")
else:
    print("Invalid")
