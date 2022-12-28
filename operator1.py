number1 = 5
number2 = 10

#operator perbandingan
if (number1 != number2):
    print("Nomor berbeda!")
else:
    print("Nomor sama!")

#operator logika
if number1 > 99 and number1 < 1000:
    print("Bilangan ratusan!")
else:
    print("Bukan Bilangan ratusan!")

#operator aritmatika
while number1< 10:
    number3 = int(input("masukan angka : "))

    if number3 == 00:
        break

    if number3 % 2 == 0:
        print("Bilangan Genap")
    else:
        print("Bilangan Ganjil")
#~modulus % : sisa bagi
#~karena bernilai true maka akan menjadi infinite loop 
# yang bisa diberhentikan dengan adanya break yaitu '00'
#~cara berhentiin inputnya dengan '00'
