import math

def kubus(sisi):
    hasil = math.pow(sisi, 3)
    return hasil

def balok(panjang, lebar, tinggi):
    hasil = p * l * t
    return hasil

def balok(p, l, t):
    hasil = p * l * t
    return hasil

def prisma_segitiga(alas, tinggi, panjang):
    luas_alas = 0.5 * alas * tinggi
    hasil = luas_alas * panjang
    return hasil

def tabung(jari_jari, tinggi):
    hasil =math.pi * math.pow(jari_jari, 2) * tinggi
    return hasil

def kerucut(jari_jari, tinggi):
    hasil = (1/3) * math.pi * math.pow(jari_jari, 2) * tinggi
    return hasil

def bola(jari_jari):
    hasil = (4/3) * math.pi * math.pow(jari_jari, 3)
    return hasil

print(tabung(0.5, 5))