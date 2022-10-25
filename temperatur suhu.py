#konversi satuan temperatur

print("\nPROGRAM KONVERSI TEMPERATUR\n")

#celcius
celcius = int(input("masukkan suhu dalam celcius:"))
print("suhu adalah", celcius, "celcius")

#reamur
reamur = (4/5*celcius)
print("hasil konversi dari suhu", celcius, "C ke reamur adalah", reamur, "reamur")

#farhenheit
farhenheit = ((9/5)*celcius+32)
print("hasil konversi dari suhu",  celcius, " C ke farhenheit adalah", farhenheit, "farhenheit")

#reamur
kelvin = celcius+273
print("hasil konversi dari suhu", celcius,  " C ke kelvin adalah", kelvin, "kelvin")

