from include import LKGMirror, colors
from sys import argv
import os

if __name__ == '__main__':
    os.system('clear')
    print(f'{colors.logo}\n{colors.verde}Mirror LKG {colors.vermelho}YouTube{colors.amarelo}!{colors.branco}')
    try:
        if len(argv[1]) <= 1:
            print(f'{colors.vermelho}Use{colors.amarelo}: {colors.vermelho}python3 app.py -h{colors.branco}')
        else:
            if argv[1] == '-h' or argv[1] == '-H':
                print(f'''{colors.vermelho}use{colors.amarelo}:{colors.verde} python3 app.py [opcoes] 
                {colors.vermelho}opcoes{colors.amarelo}:{colors.verde}
                -v ou -V Baixar Video
                -a ou -A Baixar Audio
                -pv ou -PV Baixar Playlist De Videos
                -pa ou -PA Baixar Playlist De Musicas
                -h ou -H ajuda\n
                {colors.amarelo}({colors.vermelho}COMANDO PARA FAZER DOWNLOAD DE VIDEOS DO YOUTUBE{colors.amarelo})\n
                {colors.amarelo}[{colors.verde}Author{colors.amarelo}:{colors.verde}Loock{colors.amarelo}]
                [{colors.verde}Github{colors.amarelo}:{colors.verde}https://github.com/SenhorLoock{colors.amarelo}]{colors.branco}
            ''')
            else:
                link = str(input(f'{colors.verde}Digite o Link{colors.amarelo}:{colors.branco} '))
                if argv[1] == '-v' or argv[1] == '-V':
                    msg = LKGMirror.download(link).video()
                    print(msg)
                elif argv[1] == '-a' or argv[1] == '-A':
                    msg = LKGMirror.download(link).audio()
                    print(msg)
                elif argv[1] == '-pa' or argv[1] == '-PA':
                    msg = LKGMirror.playlist(link).audio()
                    print(msg)
                elif argv[1] == '-pv' or argv[1] == '-PV':
                    msg = LKGMirror.playlist(link).video()
                    print(msg)
    except:
        print(f'''{colors.vermelho}use{colors.amarelo}:{colors.verde} python3 app.py [opcoes]
                {colors.vermelho}opcoes{colors.amarelo}:{colors.verde}
                -v ou -V Baixar Video
                -a ou -A Baixar Audio
                -pv ou -PV Baixar Playlist De Videos
                -pa ou -PA Baixar Playlist De Musicas
                -h ou -H ajuda\n
                {colors.amarelo}({colors.vermelho}COMANDO PARA FAZER DOWNLOAD DE VIDEOS DO YOUTUBE{colors.amarelo})\n
                {colors.amarelo}[{colors.verde}Author{colors.amarelo}:{colors.verde}Loock{colors.amarelo}]
                [{colors.verde}Github{colors.amarelo}:{colors.verde}https://github.com/SenhorLoock{colors.amarelo}]{colors.branco}
            ''')
            

    # Remova os comentários para executar o bloco try-except
    # try:
    #     ...
    # except:
    #     ...

