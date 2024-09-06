# Question 1: Write a Python code that prints numbers from 1 to 10 on the screen.
# Ekrana 1'den 10'a kadar sayıları yazdıran bir Python kodu yazın.

for i in range(1,10):  #sayi araligi vermek icin range kullanilmali, bu sayidan bu sayiya kadar gibi
    print(i)

# Question 2: Take a number input from the user and write a Python program that prints even numbers 
# up to this number on the screen. Do this first with 'for' and then with 'while' loops.
# Kullanıcıdan bir sayı girişi alın ve ekrana bu sayıya kadar çift sayıları yazdıran 
# bir Python programı yazın. Bunu önce 'for' ile sonra da 'while' döngüleriyle yapın.

# 1.OPSIYON:
x=int(input("bir rakam girin:"))
for i in range(x):
    if i % 2 == 0:
        print(i)
# 2.OPSIYON:
i= int(0)
x= int(input("bir rakam girin:"))
while i<x :
    if i%2==0:
        print(i)
    i+=1

# Question 3: Write a Python code that receives a start and end value from 
# the user and prints all the numbers between these values ​​(including the end value) on the screen.
# Kullanıcıdan başlangıç ​​ve bitiş değerini alan ve bu değerler arasındaki tüm sayıları 
# (bitiş değeri dahil) ekrana yazdıran bir Python kodu yazınız.

# 1.OPSIYON:
x=int(input("bir baslangic degeri girin: "))
y=int(input("bir bitis degeri girin: "))

for i in range(x,y):
    print(i)

# 2.OPSIYON:
x=int(input("bir baslangic degeri girin: "))
y=int(input("bir bitis degeri girin: "))
while x<=y :
   print(x)
   x+=1


# Question 4: Get a number from the user and write a Python code that prints whether this number is odd or even.
# Kullanıcıdan bir sayı alın ve bu sayının tek mi yoksa çift mi olduğunu yazdıran bir Python kodu yazın

x=int(input("bir sayi girin: "))
if x %2==0:
    print("bu sayi cifttir.")
else:
    print("bu sayi tektir.")

# Question 5: Write a Python program that takes a positive integer input from the user and calculates its factorial.
# Factorial is the product of all positive integers between a number itself and 1. For example: if the user entered 5, 
# the program should give the following output: Enter a number from the user: 5 Factorial: 120
# Kullanıcıdan pozitif bir tam sayı girişi alan ve faktöriyelini hesaplayan bir Python programı yazın. Faktöriyel, 
# bir sayının kendisi ile 1 arasındaki tüm pozitif tam sayıların çarpımıdır. Örneğin: kullanıcı 5 girdiyse,
# program aşağıdaki çıktıyı vermelidir: Kullanıcıdan bir sayı girin: 5 Faktöriyel: 120

# 1.OPSIYON:
x= int(input("bir pozitif sayi giriniz: "))
y=1
while x>1 :
    y*=x
    x-=1
print(y)

# 2.OPSIYON:
x= int(input("bir pozitif sayi giriniz: "))
y=1
a =1
for y in range(y,x+1):
    a *= y
    print(a)


# Question 6: Write a Python code that receives a number from the user and checks whether this number is prime.
# Kullanıcıdan bir sayı alan ve bu sayının asal olup olmadığını kontrol eden bir Python kodu yazın.

x=int(input("bir sayi girin: "))
if x>2 and x!=3 and x!=5 and x!=7:
    if x%2==0 or x%3==0 or x%5==0 or x%7==0:
        print(x," asal sayi degildir")
    else:
        print(x," asal sayidir")
else:
        if x==1:
             print(x,"asal sayi degildir")
        else:
             print(x," asal sayidir")

# Question 7: How to create a loop that calculates the Fibonacci sequence and returns the result as a list containing numbers 
# up to a certain limit?
# Fibonacci dizisini hesaplayan ve sonucu belirli bir sınıra kadar sayı içeren bir liste olarak döndüren bir döngü nasıl oluşturulur?

fibonacci_list = []
a, b = 0, 1
    
while a <= 100:
    fibonacci_list.append(a)
    a, b = b, a + b  
print(fibonacci_list)

# Question 8: Write a Python code that takes a word from the user and prints the reverse of this word on the screen.
# Kullanıcıdan bir kelime alan ve bu kelimenin tersini ekrana yazdıran bir Python kodu yazın.

x=input("bir kelime girin: ")
print(x[::-1])


# Question 9: How to create a combination of loop and conditional statement that takes a word input from the user and
# checks whether that word is a palindrome (the same when read backwards)?
# Kullanıcıdan bir kelime girişi alan ve bu kelimenin bir palindrom olup olmadığını (geriye doğru okunduğunda da aynı) 
# kontrol eden bir döngü ve koşullu ifade kombinasyonu nasıl oluşturulur?

x=input("bir kelime girin: ")
y= x[::-1]
if x==y :
    print("bu kelime bir polindromdur.")
else:
    print("bu kelime bir polindrom degildir.")

# Question 10: Write the code that calculates the person's weight index and returns the result as underweight, 
# overweight or overweight according to the index value. (You can look on the internet for the weight index calculation) 
# To do this, ask the user for their weight and height measurements. weight index If it is below 25, it is weak, 
# Between 25-30 is normal, If you are over 30-40, you are overweight. If you are over 40, you are overweight.
# Kişinin kilo endeksini hesaplayan ve endeks değerine göre zayıf, kilolu veya fazla kilolu sonucunu döndüren kodu yazın. 
# (Kilo endeksi hesaplaması için internete bakabilirsiniz) Bunun için kullanıcıdan kilo ve boy ölçülerini isteyin.
# Kilo endeksi 25'in altındaysa zayıf, 25-30 arasıysa normal, 30-40'ın üzerindeyse kilolusunuz. 40'ın üzerindeyse kilolusunuz.

kilo=int(input("kilonuzu giriniz: "))
boy=float(input("boyunuzu metre cinsinden giriniz: "))
kilo_endeksi=kilo/boy**2
if kilo_endeksi<25:
    print("zayifsiniz.")
elif 25<kilo_endeksi<30:
    print("normalsiniz.")
else:
    print("kilolusunuz.")


# Question 11: How to write a Python program that finds the largest of three numbers entered by a user?
# Kullanıcının girdiği üç sayıdan en büyüğünü bulan bir Python programı nasıl yazılır?

birinci_sayi=int(input("1.sayiyi girin:"))
ikinci_sayi=int(input("2.sayiyi girin:"))
ucuncu_sayi=int(input("3.sayiyi girin:"))
if birinci_sayi>ikinci_sayi and birinci_sayi>ucuncu_sayi:
    print("en buyuk sayi:",birinci_sayi)
if birinci_sayi>ikinci_sayi and birinci_sayi<ucuncu_sayi:
    print("en buyuk sayi:",ucuncu_sayi)
if birinci_sayi<ikinci_sayi and ikinci_sayi>ucuncu_sayi:
    print("en buyuk sayi:",ikinci_sayi)


# Question 12: Get Midterm and Final grades from a student for any course. The sum of 40% of the midterm exam grade and 60% of
# the final grade will give the year-end average. If the average is below 50, "FAILED" will appear on the screen, and if it is
# 50 or above, "SUCCESSFUL" will be displayed on the screen. This printing process is 4 lessons. and the lessons will be 
# written one after the other.
# Herhangi bir ders için bir öğrenciden Vize ve Final notlarını alın. Vize sınav notunun %40'ı ile Final notunun %60'ının toplamı
# yıl sonu ortalamasını verecektir. Ortalama 50'nin altındaysa ekranda "FAILED" (BAŞARISIZ) yazısı, 50 veya üzeriyse ekranda 
# "SUCCESSFUL" (BAŞARILI) yazısı görünecektir. Bu yazdırma işlemi 4 derstir ve dersler birbiri ardına yazılacaktır.

vize_notu=int(input("vize notunuzu giriniz: "))
final_notu=int(input("final notunuzu giriniz: "))
ortalama=(vize_notu*40)/100+(final_notu*60)/100
if ortalama<50:
    print("FAILED")
else:
    print("SUCCESFUL")
