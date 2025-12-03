def celcius_ke_fahrenheit(celcius):
    """Konversi suhu dari Celcius ke Fahrenheit."""
    return celcius * 9/5 + 32

print(celcius_ke_fahrenheit(0))    
print(celcius_ke_fahrenheit(100)) 

def is_genap(n):
    """Mengembalikan True jika n genap, False jika ganjil."""
    return n % 2 == 0

print(is_genap(4))  
print(is_genap(7))  


def nilai(score):
    """Mengembalikan 'lulus' jika score >= 75, selainnya 'gagal'."""
    return "lulus" if score >= 75 else "gagal"

print(nilai(80))  
print(nilai(60))  

def bilangan(n):
    i = 1
    while i < n:
        if i % 2 == 1:
            print(i)
        i = i + 1

print(bilangan(20)) 