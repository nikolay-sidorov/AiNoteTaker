#this module transcribes audios to text using Faster-Whisper
from faster_whisper import WhisperModel
import glob
import os

model_size = "base" #use "base". There are aso "large" and "medium" sizes
model = WhisperModel(model_size, device="auto", compute_type="float32") #loads model you can use compute_type="auto" instead

def log(result_text, result_file_name:str): #writes transcripted text into a file
    with open(f"{result_file_name}", "a") as file:
        file.write(f"{result_text}\n") 

def transcribe(audio:str, result_file_name:str, language:str): #transcribes audio to text 'audio' is path to .mp3 audio file
    task = "transcribe"
    segments, _ = model.transcribe(audio=audio, task=task, language=language) #add **options to define language
    for segment in segments:
        print(segment.text)
        log(segment.text, result_file_name)
        
def buildList(temp:str): #builds a list of file names in a folder 'temp' is path to this folder
    files = []
    for i in range(os.listdir(temp).__len__()):
        file = glob.glob(f"{temp}/*-{i}.mp3")
        files.append(file)
    return files

def transcribe_folder(temp:str, result_file_name:str): #applies transcribe function to every file in a folder (temp) and writes result to a file 'result.txt'. Previous version proceeded file NOT one after another
    files = buildList(temp)
    for file in files:
        file = ''.join(file)
        print(f"{file}\n")
        if os.path.exists(file) and file.lower().endswith(".mp3"):
            transcribe(file, result_file_name)

transcribe('/Users/nikolaysidorov/allProjects/autoNotes/audios/openai.mp3', "test.txt", 'de')