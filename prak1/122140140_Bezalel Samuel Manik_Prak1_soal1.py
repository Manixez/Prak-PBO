num1=int(input("Masukkkan batas Bawah : "))
num2=int(input("Masukkkan batas Atas : "))
if(num1<0 or num2<0):
    print("Batas bawah dan batas atas tidak boleh dibawah nol")
elif(num1%2==1):
    for i in range (num1,num2,2):
        print (i)
else:
    num1+=1
    for i in range (num1,num2,2):
        print (i)
