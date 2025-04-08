#this module assembles the whole process of note generation in a single function
#this module is successor of process.py that is more adapted for using faster-whisper
from audioToTextF import transcribe
from buildTextChunks import Chunkenize
from generateNotes import WriteWithOpenAI
import shutil
import os
import appdirs

cache_dir = appdirs.user_cache_dir(appname='autoNotes')

def is_empty(dir): #checks if a directory is empty
    dir_empty = bool()
    if os.listdir(dir) == 0:
        dir_empty = 1
    else:
        dir_empty = 0
    return dir_empty

def wholeProcess(api_key:str, audio_path:str, note_file_path:str):

    #cache_dir = appdirs.user_cache_dir(appname='autoNotes')
    #cache_dir = cache_dir
    #DECIDED to use cach_dir variable as global

    if not os.path.exists(cache_dir): #creates cache directory for the programm if it doesn't exist yet
        os.mkdir(cache_dir)
    
    cache_dir_empty = is_empty(cache_dir)

    if cache_dir_empty == False: #clears cache directory before starting process if it isn't empty
        for i in os.listdir(cache_dir):
            if os.path.isfile(f"{cache_dir}/{i}"):
                os.remove(f"{cache_dir}/{i}")
            else:
                shutil.rmtree(f"{cache_dir}/{i}")
    
    key = api_key 
    template_str = """
    you have to make the notes in bullet points on the following text. You'll be writing the notes for the Markfown file, so use headers, lists, tables, <html> and other tools Markdown has to create readable and informative notes. Try to pack as much important information into your note as possible. The text: {text}
    """
    #template_str_html = """
    #you have to make the notes in bullet points on the following text. You'll be writing the notes for the html file, so use headers, lists, tables, <html> and other tools HTML has to create readable and informative notes. Try to pack as much important information into your note as possible. The text: {text}
    #"""
    memory_size=96

    audio = audio_path 
    temporary_audio=f'{cache_dir}/temp_audio'
    transcript_file_name=f'{cache_dir}/text.txt'
    language="de"

    transcribe(audio, transcript_file_name, language)
    chunk_size=int(4096-memory_size-(len(template_str)/4)) #defines optimal size of a chunk. One Open AI token is +-4 Eng signs. Max gpt-3.5-turbo input is 4096 tokens
    chunks = Chunkenize(transcript_file_name, chunk_size)
    note_file=note_file_path
    model = WriteWithOpenAI(key, memory_size, template_str, note_file)
    model.generateNotes(chunks)
    
    if os.path.exists(temporary_audio): 
        shutil.rmtree(temporary_audio)
    if os.path.exists(transcript_file_name):
        os.remove(transcript_file_name)

#wholeProcess('openay key', 'audio path', 'note path with extension')
