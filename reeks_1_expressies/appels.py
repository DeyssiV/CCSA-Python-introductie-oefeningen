aantal_appels = int(input())

aantal_kisten = aantal_appels//20
aantal_palletten = aantal_kisten // 35
overgebleven_kisten = aantal_kisten % 35
overgebleven_appels = aantal_appels % 20

print(aantal_palletten)
print(overgebleven_kisten)
print(overgebleven_appels)