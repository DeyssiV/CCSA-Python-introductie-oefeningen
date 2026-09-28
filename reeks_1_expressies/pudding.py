aantal_stuks = int(input())
kostprijs_stuk = float(input())
aantal_barcodes = int(input())
aantal_mijlen = int(input())
totaal_kostprijs = aantal_stuks * kostprijs_stuk
flyer_mijlen = (aantal_stuks//aantal_barcodes)*aantal_mijlen
print(f"Phillips spendeerde ${totaal_kostprijs} voor {flyer_mijlen} frequent flyer mijlen.")