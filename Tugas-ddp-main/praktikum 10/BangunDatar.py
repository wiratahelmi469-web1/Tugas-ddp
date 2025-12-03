import math

def persegi(sisi):
    hasil = math.pow(sisi, 2)
    return hasil

def persegi_panjang(panjang, lebar):
    hasil = panjang * lebar
    return hasil

def segitiga(alas, tinggi):
    hasil = 0.5 * alas * tinggi
    return hasil

def lingkaran(jari_jari):
    hasil = math.pi * math.pow(jari_jari, 2)
    return hasil

def jajargenjang(alas, tinggi):
    return alas*tinggi

print(jajargenjang(5,4))