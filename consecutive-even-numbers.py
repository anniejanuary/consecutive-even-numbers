#niech wypisze liczby 1-20 ale parzyste

a=2
while a<=20:
    print(a)
    a+=2 #zwiększanie wartości zmiennej a o 2. #to samo co a=a+2
    
    
#   OR

for x in range(2,21,2):#od 2 do 21(bo 1 jest nieparzyste) i przeskok co 2
    print (x)

    
#   OR
    
a=0

while a<=20:
    a+=1
    if a%2!=0:
        continue
    #print w 1 linii:
    print(a,end=" ") 
    
    
