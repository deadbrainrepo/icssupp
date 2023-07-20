import subprocess

print("Здравствуйте!")
print("Вас приветствует диагностическая утилита ICSSUPP.")
print("Чем могу помочь?")
print("1) Проверить состояние служб\n2) Послать нахуй\n")
cypher = input()
if cypher == "1":
    print("Запускаю...")
    subprocess.call("/usr/local/ics/support/bin/status")
else: print("Иди нахуй")