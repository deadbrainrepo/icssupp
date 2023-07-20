import subprocess
cypher = (1)
print("Здравствуйте!")
print("Вас приветствует диагностическая утилита ICSSUPP.")
print("Чем могу помочь?")
while cypher != 0:
    print("1) Проверить состояние служб\n2) Послать нахуй\n")
    cypher = input()

    if cypher == "1":
        subprocess.call("/usr/local/ics/support/bin/status")
    if cypher == "2":
        print("Иди нахуй")
    if cypher == "3":
        subprocess.call("/usr/local/ics/backup/bin/rebuild")