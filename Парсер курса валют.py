import json
import matplotlib.pyplot as plt
from datetime import datetime

# Считать историю
with open("history.json", "r", encoding="utf-8") as f:
    история = json.load(f)

# Сортировать по дате (на всякий случай)
история.sort(key=lambda x: x["date"])

# Даты и курсы
даты = [datetime.strptime(x["date"], "%Y-%m-%d") for x in история]
usd = [x["usd"] for x in история]
eur = [x["eur"] for x in история]

# Строим график
plt.plot(даты, usd, label="USD")
plt.plot(даты, eur, label="EUR")
plt.xlabel("Дата")
plt.ylabel("Курс")
plt.title("Динамика курса валют")
plt.legend()
plt.grid()
plt.show()
