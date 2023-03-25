countries_informtaion = {}
countries_informtaion["Polska"] = ("Warszawa", 37.97)
countries_informtaion["Niemcy"] = ("Berlin", 82.02)
countries_informtaion["Słowacja"] = ("Bratysława", 5.45)

for country in countries_informtaion.keys():
    print(country)

country = input("Informacje o jakim kraju chcesz wiedzieć ")

country_information = countries_informtaion.get(country)

print()
print(country)
print("----------")
print("Stolica: " + country_information[0])   
print("Liczba mieszkańców (mln): " + str(country_information[1]))

input()
