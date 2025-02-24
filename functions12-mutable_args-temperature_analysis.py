# Zadanie: Napisz program, który analizuje wprowadzone temperatury i wykrywa ich średnią, najniższą oraz najwyższą wartość. Program powinien prosić użytkownika o wprowadzanie temperatur jedna po drugiej, a następnie zwracać raport z analizy. Komentarze w kodzie będą po polsku, a nazwy zmiennych i funkcji po angielsku.
# 
# Kroki do wykonania:
# 1) Poproś użytkownika o wprowadzenie serii temperatur, gdzie każda temperatura wprowadzana jest oddzielnie, a zakończenie wprowadzania sygnalizowane jest przez wpisanie "koniec"
# 2) Dla każdej wprowadzonej temperatury, dodaj ją do listy temperatur po konwersji na typ float
# 3) Po zakończeniu wprowadzania danych, wywołaj funkcję analizującą temperatury, która zwraca krotkę zawierającą średnią, maksymalną i minimalną temperaturę z listy. 
#    Uwaga - aby pobrać wartość minimalną z listy, wykorzystaj funkcję "min()", do której przekażesz listę wartości liczbowych, tak samo "max()" oraz "sum()"
# 4) Wyświetl wyniki analizy użytkownikowi

temperatureList = []

while True:
    temperature = input("Wprowadź temperaturę lub wpisz \"koniec\", by zakończyć: ")
    if temperature.lower() == "koniec": break
    else:
        temperatureList.append(float(temperature))

def temperatureAnalysis(temperatureList):
    if len(temperatureList) > 0:
        average = sum(temperatureList) / len(temperatureList)
        minimalTemperature = min(temperatureList)
        maxTemperature = max(temperatureList)
        analysisResult = (average, minimalTemperature, maxTemperature)
        return analysisResult

data = temperatureAnalysis(temperatureList)
avgTemp, minTemp, maxTemp = data    # rozbicie krotki

print("Średnia z podanych temperatur:", avgTemp)
print("Minimalna z podanych temperatur:", minTemp)
print("Maksymalna z podanych temperatur:", maxTemp)

