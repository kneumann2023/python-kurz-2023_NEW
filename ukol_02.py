# Firma eviduje informace o počtu součástek na skladě ve slovníku. 
# Klíč slovníku je kód součástky, hodnota klíče je počet součástek na skladě.
# Následně naprogramuj následující varianty:
# a)
# Pokud zadaný kód není ve slovníku, není součástka skladem. 
# Vypiš tedy zprávu, že součástka není skladem.
# b)
# Pokud zadaná součástka na skladě je, ale je jí méně, než požaduje zákazník, vypiš text o tom, 
# že lze prodat pouze omezené množství kusů.
# Následně součástku odeber ze slovníku, protože je vyprodaná.
# c) 
# Pokud zadaná součástka na skladě je a je jí dostatek, vypiš informaci, že poptávku lze 
# uspokojit v plné výši, a sniž počet součástek na skladě o množství požadované zákazníkem

sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

soucastka = input("Uveďte kód požadované součástky: ")
mnozstvi = int(input("Uveďte požadované množství: "))

if soucastka not in sklad:  
    print("Součástka není skladem.")
else:
    pocet_skladem = 0
    for kod, kusy in sklad.items():
        pocet_skladem += kusy
        if kod == soucastka and mnozstvi > kusy:  
            print("Lze prodat pouze omezené množství kusů.")
            pocet_skladem = sklad.pop(kod)                                                     
        if kod == soucastka and mnozstvi < kusy:                  
            print("Skladem je dostatečné množství kusů.")
            pocet_skladem_novy = (sklad[kod] - mnozstvi)
            sklad[kod] = pocet_skladem_novy   
            print(f"Skladem zbývá {pocet_skladem_novy} kusů.")
            print(sklad)