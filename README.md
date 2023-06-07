# NikClip - v1

Introducing NikClip, a versatile Python module tailored to provide a seamless music playback and download experience. With NikClip, you can harness the power of Python to effortlessly play and download your favorite tunes. This robust module leverages the capabilities of popular libraries like PyDub and youtube-dl to offer a wide range of features. NikClip enables you to play music files in various formats, including MP3, WAV, and FLAC, allowing for an immersive listening experience. Additionally, it empowers you to search, stream, and download music from platforms such as YouTube, SoundCloud, and Bandcamp, expanding your music collection effortlessly. Whether you are building a music player application or simply seeking a tool to enhance your music exploration, NikClip is your go-to module, designed to harmonize your Python projects with the world of music.


# About

NikClip is still in a development mode. It is in the second version. Updates monthly!

## How to use NikClip

Using your package installer (pip, anaconda, etc.) download the library.
Ex:
```pip install NikClip```

First initialize the library by using the `init` function. It takes 1 parameter: the file path of the script that is calling this function. 
example: `init("C:\\Users\\bob\\Codes\\main.py")`

To download a video or song (from youtube) just use the `download()`  method. It takes one parameter: the query of what you want to search up, the format of the media (audio or video), and the filename that you want the media to have.
example: `download("Shake it off Lyrical", "audio", "randomfile.mp3")`

To play a song use the `play()` function. It takes 2 parameters: the prompt for the media (on youtube), and th play duration (in seconds).
example: `play("Shake it off Lyrical", 100)`

## Upcoming Features
- Duration replaced with limitless 
- `restart()`, `pause()`, `resume()`, and `abort()` functions added
- `playfile()` function that plays files with one parameter: the file location.
- Faster Speeeeeeeeeeeeeeeds (lol)