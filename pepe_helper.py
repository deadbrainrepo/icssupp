import subprocess
import requests
import time

def green(text):
    print("\033[32m{}".format(text))
def get_random_joke():
    url = 'https://v2.jokeapi.dev/joke/Any'
    response = requests.get(url)

    if response.status_code == 200:
        joke_data = response.json()
        if joke_data['type'] == 'single':
            joke = joke_data['joke']
        else:
            joke = f"{joke_data['setup']} {joke_data['delivery']}"
        return joke
    else:
        return "Обойдёшься без шутки."

def print_pepe_ascii_art_end():
    pepe_ascii = """⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣠⡶⠛⠉⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⢦⡀⠀⢀⣴⠞⠋⠉⠉⠉⠉⠙⠛⠶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣶⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⠀⠸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠘⠀⠀⠀⠀⠀⠀⢀⣴⠖⠛⠋⠉⠉⠉⠉⠉⠉⠙⠛⠻⢦⣄⠀⠀⣀⣠⣤⣤⣤⣤⣤⣄⣀⠈⢷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢻⣏⠉⠀⠀⠀⠀⠀⠀⠈⠉⠙⠲⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣀⣀⣀⣀⣤⣄⣤⣤⣄⣀⣀⣤⣀⡈⢷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⡈⢻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡴⠟⠉⣉⣉⣩⣭⣽⠥⠦⣤⣌⣉⠛⠿⢦⣄⠈⠛⢶⣗⠀⠀⠀⠀⠀⢰⣞⣻⣽⣽⣭⣭⣭⣽⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡴⢋⣠⠾⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢦⣄⡙⢷⣄⠀⠹⣧⡀⠀⢀⡶⠟⣫⣭⢿⡿⠿⠿⠷⣦⡉⢻⣿⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢻⣧⣾⣁⣤⡤⠴⠶⠖⣶⣶⣶⣶⣶⣶⣶⣶⠒⠛⠛⠳⣿⢷⣤⢺⣇⠀⠉⣢⣿⣿⣿⣾⣶⣶⣦⣄⡀⠹⣾⡏⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠙⡳⠶⣄⣼⣿⣷⢾⣿⡟⠋⠛⣿⡇⠀⠀⠀⠈⣷⠘⢷⡟⢀⡾⣿⣿⣩⣿⣿⠿⢿⣧⠈⠙⠳⢾⣇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣦⡈⠻⢿⣿⣼⣿⣷⣦⣾⣿⠇⠀⠀⠀⠀⠘⣧⢸⢣⡟⠀⣿⣿⣟⣿⣿⣤⣾⡿⠀⢀⣴⢿⡟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣦⣀⠀⠉⠉⠛⠿⠿⠿⢤⣤⣤⡴⠖⠛⢉⣿⠈⢹⡓⢿⠿⠿⠿⠿⠿⠿⠷⠞⠋⣡⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠛⠛⠳⠶⠤⠴⠶⢤⣴⠾⠋⠁⠀⠈⠛⠶⣤⡤⠤⠴⠆⢀⡾⢷⣾⢯⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣴⡶⠶⠖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠈⢳⣄⠀⠀⠛⠛⠛⠁⠀⢻⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣀⣠⣴⡶⠾⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⠶⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢧⠀⠀⠀⠀⠀⠀⠀⣿⣦⠀⠀⠀⠀⠀⠀⠀
⠀⣼⢏⣿⠛⠿⠶⢤⣄⣀⡀⠀⠀⠀⠀⠐⠻⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠇⢸⡇⠀⠀⠀⠀⠀⠀
⠀⠈⠘⣿⣄⠘⢷⣄⣀⠉⠙⠛⠒⠲⠶⣤⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠃⣠⡟⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠙⠷⣄⣈⠉⠙⠳⠶⢤⣄⣀⡀⠀⠀⠉⠉⠉⠛⠛⠳⠶⠶⠶⠶⠶⠶⠤⢤⣤⣤⣤⣤⣤⣤⡤⠶⠾⠋⣠⣾⡋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠙⠛⢦⣄⡀⠀⠈⠉⠙⠛⠛⠛⠛⠛⠛⠶⢦⣤⣤⣤⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣤⠾⠋⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠳⢶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⣰⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠶⠦⠤⠤⢤⣄⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣠⣤⣄⣀⣀⣠⡤⠞⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⣉⣭⣉⠁⠀⣠⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡶⠛⠉⠉⠙⢷⣴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠛⠁⠀⠀⠀⠀⠀⠀⠹⠦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡶⠒⠳⣦⠾⠛⢷⡄⠀⠀⣠⡴⢶⣤⣄⠀⣠⡌⠙⠷⣄⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣄⠀⠀⠹⣦⣠⣾⣃⡴⠟⢁⡼⢋⣴⣯⠞⠋⠀⠀⠀⠈⠻⣆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣦⡀⠀⠈⠉⢿⠁⢠⡼⣋⡴⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠙⢷⡄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⡄⠀⠀⢸⣶⢋⣼⠋⠀⠀⠀⠀⣀⡴⠟⠀⠀⠀⠀⠀⠀⢻⣄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠙⠿⣧⡀⠀⠀⠀⣴⠏⠀⠀⠀⢀⣴⠆⠀⢀⠀⠻⣆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣇⠀⠀⠀⠀⠀⠈⠻⣦⣤⣼⠃⠀⠀⢀⣠⠞⠁⠀⣠⡾⠀⠀⠻⡆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⠃⠹⠗⠀⠀⠀⠀⠀⠀⠀⠀⠙⠓⠀⠀⠾⠃⠀⠀⠸⠋⠀⠀⠀⠀⠿"""
    print(pepe_ascii)

pepe_ascii2 = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠶⠛⠉⠀⠀⠀⠀⠉⠙⠶⠦⣀⡀⠀⠀⠀⣀⣠⠴⠶⠞⠛⠛⠶⠤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠲⣞⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠞⠁⠀⠀⠀⠀⠀⣀⣠⡤⠤⠤⠤⣤⣄⡀⠀⠀⠹⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣴⠃⠀⠀⠀⠀⢠⠶⠛⠉⠁⠀⠀⠀⠀⠀⠈⠙⠓⠦⢤⣿⠤⠖⠒⠒⠒⠒⠒⠚⠒⠓⠲⠾⢧⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⡤⠤⠤⠤⠤⣭⣳⣤⡀⠀⠀⠀⢀⣀⣀⣠⣤⣤⣤⣬⣙⣳⣦⣄⠀⠀
⠀⠀⠀⠀⢀⣀⣿⣷⣦⣤⣄⣀⡀⠀⣀⣀⣤⣤⣤⣶⣯⣭⣥⣶⣶⣯⣭⣽⣶⣶⣬⣭⣙⣴⢖⣫⣭⣿⣿⣶⣶⣶⣶⣶⣾⣿⣿⣿⣷⣤
⠀⠀⠀⣤⠛⢹⡇⠈⠉⠙⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⡿⣿⣿⣿⣿
⠀⢀⡞⠁⠀⠸⠇⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡣⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿
⢀⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⡿⠛⠉⠉⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⣀⠀⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⣉⣩⡭⠿⠛⠉⠁⠀⠀⠀⠀⠀⠙⠛⢿⡒⠛⠛⠛⠋⠻⡭⡉⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠹⣦⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡾⠛⠉⠉⠉⠳⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⢀⣀⠀⠀⠀⠉⠙⠳⠦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣇⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⡄⠀⠈⠉⠛⠢⢤⣤⣀⠀⠀⠈⠉⠉⠑⠒⠒⠒⠢⠤⢤⣤⣤⣤⣤⣄⣠⣤⣤⡤⠔⠚⠋⠁⢀⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⢦⣄⡀⠀⠀⠀⠈⠉⠙⠓⠒⠦⢦⣤⣤⣄⣀⣀⣀⣀⣀⣀⠀⠀⠈⠁⠀⢀⣀⣀⣠⣤⠖⠉⠀⠀
⠛⣻⣶⣦⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠲⢤⣤⣀⣀⠀⠀⠀⠀⠀⠀⠁⠀⠈⠀⠉⠀⠉⠉⠉⠉⠉⣉⣉⣤⣥⣷⠾⠓⢲⣚⡟
⠈⣞⣷⣴⣌⣽⣫⣿⠷⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠛⠛⠛⠷⠶⠶⠶⠶⢶⢦⣤⣤⣴⢿⣯⡉⠉⣁⣞⠗⢂⠹⡝⠅
⠀⣻⣿⣷⢪⣿⣋⠀⠀⢀⡈⣽⡛⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡟⣛⣍⣿⢷⡆⣈⣻⣮⠀⣻⣧⢿⣷⣶⠾
⠿⣿⣿⠾⠿⣿⡿⣵⣿⡏⣿⠹⣿⣞⢷⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣴⠟⡾⣿⣹⣿⣿⢷⡽⣏⠛⠓⠒⠛⠛⠛⠛⠛
⡼⢭⠥⣴⠬⣿⠿⢯⡿⢥⡿⢧⡿⢿⡿⢯⠭⢭⡿⢿⡿⢿⡿⢶⡶⢶⡾⢾⡿⢿⡭⢿⣿⠼⣧⠍⣭⠭⣥⠬⣷⢻⣆⣀⣦⣀⣴⣀⣀⠀
⢱⡿⠶⠿⠶⠾⠶⠾⠶⠾⠷⠾⠶⠾⠷⠾⠶⠾⠷⠾⠷⠾⠷⠾⠷⠾⠟⠛⠻⠞⠛⠛⠛⠛⠛⠛⠛⠋⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⢹"""

req = """curl -X POST -H "Content-Type: application/json" -d '{"command":"python wiza.py"}' http://kunteynir.ru:8080/execute"""
bye = 'Бывай, начальник!\n'
run = '......\n'
hi = '----------------------------------\nЗдравствуйте!\nВас приветствует диагностическая утилита ICSSUPP.\nЧем могу помочь?\n----------------------------------'
green("yap")
subprocess.call("clear")
for i in pepe_ascii2:
    time.sleep(0.001)
    print(i, end='', flush=True)
subprocess.call("clear")

for i in run:
    time.sleep(0.2)
    print(i, end='', flush=True)
subprocess.call("clear")

for i in hi:
    time.sleep(0.01)
    print(i, end='', flush=True)



while True:
    print("----------------------------------\n1) Проверить состояние служб\n2) Сделать ребилд\n3) Починить ClamAV\n4) Проверить "
          "стейты\n5) Продлить тестовый период\n6) Пошутить\n7) Дать root'a\n0) Выход\n----------------------------------")

    cypher = input('Введите число: ')

    if cypher == "0":
        subprocess.call("clear")
        for i in bye:
            time.sleep(0.05)
            print(i, end='', flush=True)
        print_pepe_ascii_art_end()
        break
    elif cypher == "1":
        subprocess.call("clear")
        subprocess.call("/usr/local/ics/support/bin/status")

    elif cypher == "2":
        subprocess.call("/usr/local/ics/backup/bin/rebuild")
        subprocess.call("clear")
        print("Ребилд прошёл успешно!")
    elif cypher == "3":
        subprocess.call("xs clamav disable", shell=True)
        subprocess.call("rm -rf /var/db/clamav/*", shell=True)
        subprocess.call("freshclam", shell=True)
        subprocess.call("xs clamav enable", shell=True)
        subprocess.call("clear")
        print("ClamAV в порядке!")
    elif cypher == "4":
        subprocess.call("clear")
        print("Стейты\n----------------------------------")
        subprocess.call("pfctl -ss | sed 's/\:/ /g' | awk '{print $(NF-3)}' | sort -f | uniq -c | sort -k 1nr -k 2f | head", shell=True)
        print("----------------------------------")
    elif cypher == "5":
        subprocess.call("sh -c 'BASE_PARTITION=\"'$(zfs list -d 0 -H | cut -f 1 | grep zp)'\" && zfs set zfs:trial=839 $BASE_PARTITION@ok' && xs execworker restart && xs jojoba restart", shell=True)
        subprocess.call("clear")
        print("Тестовый период успешно продлён.")
    elif cypher == "6":
        subprocess.call("clear")
        print("----------------------------------")
        print(get_random_joke())
        print("----------------------------------")
    elif cypher == "7":
        subprocess.call("passwd root && echo R! >> /etc/motd.template", shell=True)
        subprocess.call("service motd restart", shell=True)
        subprocess.call("clear")
        print("Пароль успешно изменён")
    elif cypher == "8":
        subprocess.call(req, shell=True)

    else:
        print("----------------------------------\nНет такой буквы\n----------------------------------")