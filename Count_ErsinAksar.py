

fileName = input("Enter file name: ")
#keyWord = input("Enter keyword to be searched:")
countNumber = 0
kelimeler = list()
tumKelimeler = list()
kelimeSozluk = {}
with open(fileName, 'r') as file:
    for line in file:
        words = line.split()
        for word in words:
            tumKelimeler.append(word)
            if word not in kelimeler:
                kelimeler.append(word)
                #if (word == keyWord):
                #   countNumber = countNumber + 1
    countKelime = 0
    for i in kelimeler:
        countKelime = 0
        for j in tumKelimeler:
            if i==j:
                countKelime=countKelime+1


        kelimeSozluk[i] = countKelime

#print("Occurrences of the all words: ", tumKelimeler)
print("Occurrences of the all words: ", kelimeSozluk)






