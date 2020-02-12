from subprocess import call
import youtube_dl as ud
import os
import colorama
from colorama import Fore, Back, Style
colorama.init()
while True:

    manue_prog = int(input(
        "Free Youtube Download\n1. Скачати відео \n 2. Скачати плейлист \n3. Показати \n 4. Скачати музику \n0. Вихід \n"))

    def downl_vid(call):
        print(Fore.GREEN)
        enter_adres = input("Enter URL -----> ")
        command = "youtube-dl " + enter_adres + " -c"
        os.chdir("Downloads_videos")
        call(command.split(), shell=True)
        print(Style.RESET_ALL)

    def downl_format(call):
        print(Fore.YELLOW)
        enter_adres2 = input("Enter URL -----> ")
        command_1 = "youtube-dl -F " + enter_adres2
        call(command_1.split(), shell=True)
        enter_format = input("Enter format |-----> :")
        command_2 = "youtube-dl -f " + enter_format + " " + enter_adres2 + " -c"
        call(command_2.split(), shell=True)
        print(Style.RESET_ALL)

    def downl_mus(call):
        print(Fore.BLUE)
        enter_adres_mus = input("Enter URL -----> ")
        command_3 = "youtube-dl -x --audio-format mp3  " + enter_adres_mus
        os.chdir("Downloads_musik")
        call(command_3.split(), shell=True)
        print(Style.RESET_ALL)

    if manue_prog == 1:
        print(Fore.BLUE + " ")
        downl_vid(call)
        print(Style.RESET_ALL)
    elif manue_prog == 2:
        downl_vid(call)

    elif manue_prog == 3:
        print(Fore.GREEN + " ")
        downl_format(call)
        print(Style.RESET_ALL)

    elif manue_prog == 4:
        print(Fore.BLUE + " ")
        downl_mus(call)
        print(Style.RESET_ALL)
    elif manue_prog == 0:
        break

    else:
        print(Fore.BLUE + "Print 1 / 2 / 3...")
