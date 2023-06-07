import urllib
import yt_dlp as youtube_dl # client to many multimedia portals
import re
from pygame import mixer
import pygame
import multiprocessing
from playsound import playsound
from moviepy.editor import AudioFileClip
import time
import json
mixer.init() #Initialzing pygame mixer

def init(filePath):
    with open('guts.json', 'w') as target69balls:
        a = filePath.split('\\')
        a.pop()
        str69 = ''
        for elm in a:
            str69 += elm + '\\'
        dict = {"filename": str69}
        json.dump(dict, target69balls)
        print('done')
        return

def download(songname, format, filename):
    if format == "video": #song generator/player 
        search_keyword = songname.replace(" ", "+") + "+lyrics"
        html = urllib.request.urlopen("http://youtube.com/results?search_query=" + search_keyword)
        videos_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        link = "http://youtube.com/watch?v=" + videos_ids[0]
        with open('guts.json') as target:
            e = json.load(target)['filename']
            print(str(e) + filename)
            ydl_opts = {
                'outtmpl': str(e) + filename,
            }
            video_title = ''
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
                info_dict = ydl.extract_info(link, download=False)
                video_title = info_dict.get('title', None)
                print(video_title)
            return
    elif format == "audio":
        search_keyword = songname.replace(" ", "+") + "+lyrics"
        html = urllib.request.urlopen("http://youtube.com/results?search_query=" + search_keyword)
        videos_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        link = "http://youtube.com/watch?v=" + videos_ids[0]
        with open('guts.json') as target:
            e = json.load(target)['filename']
            print(str(e) + filename)
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': str(e) + 'preconvert.mp4',
            }
            video_title = ''
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
                info_dict = ydl.extract_info(link, download=False)
                video_title = info_dict.get('title', None)
                print(video_title)
                def MP4ToMP3(mp4, mp3):
                    FILETOCONVERT = AudioFileClip(mp4)
                    FILETOCONVERT.write_audiofile(mp3)
                    FILETOCONVERT.close()
                VIDEO_FILE_PATH = str(e) + 'preconvert.mp4'
                AUDIO_FILE_PATH = str(e) + filename
                MP4ToMP3(VIDEO_FILE_PATH, AUDIO_FILE_PATH)
                import os
                os.remove(VIDEO_FILE_PATH)
            return

def player(prompt, duration):
    download(prompt, "audio", "antidisestablishmenterianism.mp3")
    mixer.music.load('antidisestablishmenterianism.mp3') #Loading Music File
    mixer.music.play() #Playing Music with Pygame
    time.sleep(duration)
    

def abort():
    mixer.music.stop()
    try:
        import os
        os.remove("C:\\Users\\nikhi\\Downloads\\Codes\\ScienceFairProject\\thatfile.mp3")
    except:
        return

def restart():
    """
    mixer.music.stop()
    mixer.music.load('antidisestablishmenterianism.mp3') #Loading Music File
    mixer.music.play() #Playing Music with Pygame
    """
    playsound('antidisestablishmenterianism.mp3', block=True)

def pause():
    mixer.music.pause()

def unpause():
    mixer.music.unpause()


init("C:\\Users\\nikhi\\Downloads\\Codes\\Libraries\\NikClip\\main.py")
player("pars chainsmokers", 69)
print('ok')
