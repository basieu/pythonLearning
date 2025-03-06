# Zadanie: Użyj modułów "time" i "datetime" do symulacji prostego systemu śledzenia czasu pracy nad projektem. Nauczysz się używać różnych funkcji związanych z czasem i datą.
# 
# 1) Użyj modułu "datetime", aby zapisać czas rozpoczęcia pracy nad projektem jako zmienną "start_time"
# 2) Symuluj pracę nad projektem przez wywołanie "time.sleep()" z losowo wybranym krótkim czasem (np. od 1 do 5 sekund)
# 3) Użyj modułu "datetime" ponownie, aby zapisać czas zakończenia pracy nad projektem jako zmienną "end_time"
# 4) Oblicz łączny czas pracy nad projektem i wyświetl wynik
# 5) Jeśli łączny czas pracy przekracza 3 sekundy, wyświetl komunikat o dużej ilości włożonego czasu, w przeciwnym razie poinformuj o krótkim czasie pracy

import datetime
import time
import random

start_time = datetime.datetime.now()
print("Czas rozpoczęcia zadania:", start_time.strftime("%d.%m.%Y %H:%M:%S"))

sleepTime = random.randint(1, 5)
time.sleep(sleepTime)

end_time = datetime.datetime.now()
print("Czas zakończenia zadania:", end_time.strftime("%d.%m.%Y %H:%M:%S"))

totalTime = end_time - start_time
print("Czas pracy:", totalTime)

if totalTime.total_seconds() > 3:
    print("Duża ilość włożonego czasu:", totalTime.total_seconds(), "sekund")
else:
    print("Krótki czas pracy:", totalTime.total_seconds(), "sekund")





"""

start_time = time.perf_counter()

sleepTime = random.randint(1, 5)
time.sleep(sleepTime)

end_time = time.perf_counter()

totalTime = round(end_time - start_time)

if totalTime > 3:
    print("Duża ilość włożonego czasu:", totalTime, "sekund")
else:
    print("Krótki czas pracy:", totalTime, "sekund")

"""