from tkinter import *
from tkinter import filedialog
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from processF import wholeProcess
from processF import cache_dir

def noteDir():
    dir = filedialog.askdirectory()
    global noteDirectory
    noteDirectory = dir
    ndir = tb.Label(root, text=f'directory: {dir}')
    ndir.pack()

def browse():
    file = filedialog.askopenfile(title='choose file', filetypes=[('audio files', ("*.mp3", ".m4a"))])
    global audio_file_name
    audio_file_name = file.name
    audio = tb.Label(root, text=f'audio: {file.name}')
    audio.pack()

def click():
    global audio_file_name
    audio_file_name = audio_file_name
    api_key = entry_size.get() 
    global noteDirectory
    noteDirectory = noteDirectory
    noteName = f'{noteDirectory}/{entryNoteName.get()}.md'
    cache_l = tb.Label(root, text=f'cache: {cache_dir}')
    cache_l.pack() 
    if  api_key!='' and audio_file_name!='':
        try:
            wholeProcess(api_key, audio_file_name, noteName)
        except Exception as e:
            exc = tb.Label(root, text=f'exception: {e}')
            exc.pack()

if __name__=="__main__":

    root = tb.Window(themename='vapor')
    root.title('autoNote')
    root.geometry('500x500')

    audio_file_name = str()
    noteDirectory = str()

    entry_file = tb.Button(root, width=30, text='choose audio file', command=browse) 
    entry_file.pack(pady=30)


    entry_size_label = tb.Label(root, width=30, text='enter your OpenAI API Key', bootstyle='secondary') #gets openai key
    entry_size_label.pack()
    entry_size = tb.Entry(root, width=30)
    entry_size.pack()

    entryNoteName_label = tb.Label(root, width=30, text='Note Name', bootstyle='secondary')
    entryNoteName_label.pack()
    entryNoteName = tb.Entry(root, width=30)
    entryNoteName.pack()

    button = tb.Button(root, width=30, text='choose note directory', command=noteDir)
    button.pack(pady=30)


    button = tb.Button(root, text='generate note', bootstyle='outline', command=click)
    button.pack(pady=20, padx=50)

    root.mainloop()

    ##IMPORTANT!!!

    #app keeps opening itself in a loop. Probably, something in ctranslate2 causes it

    """
    add

    datas=[('myenv/lib/python3.11/site-packages/whisper/assets/mel_filters.npz', 'myenv/lib/python3.11/site-packages/whisper/assets'), 
        ('myenv/lib/python3.11/site-packages/whisper/assets', './whisper/assets'),
        ('myenv/lib/python3.11/site-packages/ffprobe', './ffprobe'),
        ('myenv/lib/python3.11/site-packages/ffmpeg', './ffmpeg')],

    to package with pyinstaller usccessfully!!!
    """
    #use pyinstaller --windowed to create .app