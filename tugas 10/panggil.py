import BangunRuang as br
import BangunDatar as bd

print(f"----- BANGUN RUANG -----")
print(f"volume kubus dengan sisi 4 adalah : ",{br.kubus(4)})
print(f"volume balok dengan panjang 4, lebar 3, tinggi 2 adalah :")
print(br.balok(4,3,2))
print(f"volume prisma segitiga dengan alas 3, tinggi 4, panjang 5 adalah : ")
print(br.prisma_segitiga(3,4,5))
print(f"volume tabung adalah")
print(br.tabung(0.5, 5))
print(f"volume kerucut adalah")
print(br.kerucut(5,5))

print("----- BANGUN DATAR -----")
print(f"luas persegi adalah")
print(bd.persegi(4))
print(f"luas persegi panjang adalah")
print(bd.persegi_panjang(8,4))
print(f"luas segitiga adalah")
print(bd.segitiga(6,4))
print(f"luas lingkaran adalah")
print(bd.lingkaran(4))
print(f"luas jajaargenjang adalah {bd.jajargenjang(4,7)}")