import pytube
from pytube.cli import on_progress
import random
import re
import os
import pydub
branco='\033[0m'
branco2='\033[7;37m'
verde='\033[32m'
vermelho='\033[31m'
vermelho2='\033[7;31m'
amarelo='\033[33m'

class download:
    def __init__(self, link):
        self.num = str(random.randint(10000000, 9999999999))
        self.link = link
        self.arquivo = pytube.YouTube(self.link, on_progress_callback=on_progress)

    def audio(self):
        try:
            print(f'{verde}Baixando Audio{branco}')
            audio = self.arquivo.streams.filter(only_audio=True).first()
            audioname = f'Mirror_Audio({self.num}).mp4'
            diretorio = 'Download/Audio'
            mp4 = audio.download(
                output_path=diretorio,
                filename=audioname
            )
            musica = pydub.AudioSegment.from_file(mp4, format='mp4')
            caminho_mp3 = mp4[:-4]+'.mp3'
            musica.export(caminho_mp3, format='mp3')
            os.remove(os.path.join(diretorio,audioname))
            print(' ')
            return f'{verde}Download Concluido!{branco}'
        except:
            return f'{vermelho}Erro ao Baixar Audio{amarelo}!{branco}'

    def video(self):
        try:
            print(f'{verde}Baixando Video{branco}')
            video = self.arquivo.streams.filter(
                progressive=True,
                file_extension='mp4'
            ).first()
            video.download(
                output_path='Download/Video',
                filename=f'Mirror_Video({self.num}).mp4'
            )
            
            print(' ')
            return f'{verde}Download Concluido!{branco}'
        except:
            return f'{vermelho}Erro ao Baixar Video{amarelo}!{branco}'

class playlist:
    def __init__(self, link):
        self.num = None
        self.link = link
        self.list = []
        self.playlist = pytube.Playlist(self.link)

    def audio(self):
        self.playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
        audioNum = 1
        for audio in self.playlist.videos:
            self.num = random.randint(10000000, 9999999999)
            try:
                print(f'{verde}baixando audio {amarelo}({audioNum})\n{verde}Nome{amarelo}: {verde}{audio.title}{branco}')
                download = audio.streams.filter(only_audio=True).first()
                nameaudio = f'Mirror_Audio({self.num}).mp4'
                diretorio = "Download/Audio"
                mp4 = download.download(
                    output_path=diretorio,
                    filename=nameaudio
                )
                musica = pydub.AudioSegment.from_file(mp4, format='mp4')
                caminho_mp3 = mp4[:-4]+'.mp3'
                musica.export(caminho_mp3, format='mp3')
                os.remove(os.path.join(diretorio,nameaudio))
                

                audioNum += +1
            except:
                print(f'{vermelho}Falha Ao Baixar audio {amarelo}({audioNum})\n{vermelho}Nome{amarelo}: {vermelho}Falha ao Buscar Nome!{branco}')
                iteration = str(input(f'{amarelo}Quer Continuar Baixando? (S) Para Sim ou (N) Para Não\n{verde}>>>>{branco}'))
                if iteration == 'n' or iteration == 'N':
                    break

        return 'Download Da Playlist Esta Concluido!'

    def video(self):
        self.playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
        videoNum = 1
        for video in self.playlist.videos:
            self.num = random.randint(10000000, 9999999999)
            try:
                print(f'{verde}baixando video {amarelo}({videoNum})\n{verde}Nome{amarelo}: {verde}{video.title}{branco}')
                video = video.streams.filter(
                    type='video',
                    progressive=True,
                    file_extension='mp4'
                ).first()
                video.download(
                    output_path='Download/Video',
                    filename=f'Mirror_Video({self.num}).mp4'
                )
                videoNum += +1

            except:
                print(f'{vermelho}Falha Ao Baixar video {amarelo}({videoNum})\n{vermelho}Nome{amarelo}: {vermelho}Falha ao Buscar Nome!{branco}')
                iteration = str(input(f'{amarelo}Quer Continuar Baixando? (S) Para Sim ou (N) Para Não\n{verde}>>>>{branco}'))
                if iteration == 'n' or iteration == 'N':
                    break

        return 'Download Da Playlist Esta Concluido!'


if __name__ == '__main__':
  print ('Modulo Para Importaçoes')
