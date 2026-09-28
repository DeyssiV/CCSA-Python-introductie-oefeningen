aantal = 60
boek = 24.95
korting = 40
inkoop = boek - (boek * (40/100))
verstuurkost = ((aantal - 1) * 0.75) + 3
totaal = inkoop * aantal + verstuurkost
print(totaal)