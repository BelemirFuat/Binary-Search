import math

dizi =[1,5,3,2,7,8,9,2,56,24,55,78,90]

print("diziniz sıralanıyor...")    

dizi= sorted(dizi)

print("diziniz sıralandı...")

uzunluk = len(dizi)

print(dizi[0:uzunluk+1])

aranan = int(input("Aranacak sayıyı giriniz:"))

uzunluk = len(dizi)

max = uzunluk-1
min = 0
orta = math.floor((max+min)/2)

while(True):
    if(aranan==dizi[orta]):
        print("Bulundu. index ={}".format(orta))
        break
    
    elif(aranan>dizi[orta]):
        min=orta
        orta = math.floor((max+min)/2)

    elif(aranan<dizi[orta]):
        max = orta
        orta = math.floor((max+min)/2)

    if(math.fabs(max-min)==1 ):
        print("Bulunamadı.")
        break


    