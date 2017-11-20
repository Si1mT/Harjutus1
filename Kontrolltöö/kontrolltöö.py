#1
print ("Sisestage 2 numbrit")
number1=int(input())
number2=int(input())
for x in range(number1,number2):
    if(x % 2 == 0):
        print (x)
#2

with open('C:\\Users\\SIIM\\Downloads\\kttekst.txt',"r") as f:
    words1=[]
    words3=[]
    for line in f:
        line.rstrip()
        words2=line.split()
        for word in words2:
            words1.append(word)
            words1.sort()
            sona=(int(len(word)))
            if sona<5:
                words3.append(sona)
    print (len(words1))
    print (len(words3))


#3

list1=[11 ,15 ,6, 13 ,13 ,25, 32 ,11 ,20, 5, 31 ,16 ,32, 29 ,11, 13,3 ,29, 28, 24]
list2=[5 ,19, 16, 4, 12 ,7, 2, 28 ,34 ,29, 29, 36, 6 ,8, 24, 18 ,31, 7,1, 7]

g=set(list1).intersection(list2)
print("Sarnased numbrid listidel on:" ,g)

suurim1=(max(list1))
suurim2=(max(list2))
list5=[suurim1,suurim2]
print("Kahe listi suurim arv on:",(max(list5)))

väikseim1=(min(list1))
väikseim2=(min(list2))
list6=[väikseim1,väikseim2]
print("Kahe listi väikseim arv on:",(min(list5)))

average1=sum(list1)/ len(list1)
print ("Esimese listi keskmine on:",average1)
average2=sum(list2)/ len(list2)
print ("Teise listi keskmine on:",average2)

average3=(average1+average2)/2
print("Mõlema listi kesmine on:",average3)
