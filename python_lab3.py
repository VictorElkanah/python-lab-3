import random, time
import matplotlib.pyplot as plt

temps = []
for t in range(10):
    temp = 25 + random.uniform(-1, 1)
    temps.append(temp)
    with open("temps.csv", "a") as f:
        f.write(f"{t},{temp}\n")
    time.sleep(0.5)

plt.plot(temps)
plt.xlabel("time (s)")
plt.ylabel("temperature (C)")
plt.title("temperature log")
plt.show()

import random, time
import matplotlib.pyplot as plt

temps = []
hums = []
for t in range(10):
    temp = 25 + random.uniform(-1, 1)
    hum = 50 + random.uniform(-5, 5)
    temps.append(temp)
    hums.append(hum)
    with open("data.txt", "a") as f:
        f.write(f"{t},{temp}\n")
        time.sleep(0.5)

plt.plot(temps)
plt.xlabel("time (s)")
plt.ylabel("temperature (C)")
plt.title("temperature log")
plt.show()

plt.plot(hums)
plt.xlabel("time (s)")
plt.ylabel("humidity (C)")
plt.title("humidity log")
plt.show()