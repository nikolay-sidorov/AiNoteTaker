#This module create a OpenAI langchain chain and receives note from OpenAI
from langchain.chains import ConversationChain, LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationSummaryBufferMemory
from langchain.prompts import PromptTemplate, Prompt, ChatPromptTemplate
#import openai

class WriteWithOpenAI:
    def __init__(self, key:str, memory_tokens:int, template_str:str, path_to_note_file:str): #needs openAI API Key, limit for memory tokens, templeate for a prompt and path to note file form user
        self.key = key
        llm = ChatOpenAI(openai_api_key=key, model="gpt-3.5-turbo")
        self.memory_tokens=memory_tokens
        memory = ConversationSummaryBufferMemory(llm=llm, max_token_limit=memory_tokens)
        self.template_str = template_str
        prompt=PromptTemplate(template=template_str, input_variables=['text'])
        self.chain = LLMChain(llm=llm, memory=memory, prompt=prompt)
        self.path_to_note_file=path_to_note_file
    
    def writeNoteMacOS(self, response:str, path_to_note_file:str): #generates note file
        with open(path_to_note_file, 'a') as file:
            file.write(response)
    
    def generateNotes(self, chunks:list): #sends request to OpenAI
        for c in chunks:
            result = self.chain.predict(text=c)
            print(result)
            self.writeNoteMacOS(response=result, path_to_note_file=self.path_to_note_file)



### USE CASE FOR THIS MODULE!
"""
key = ''
template_str = """
#you have to make the notes in bullet points on the following text. You'll be writing the notes for the Markfown file, so use headers, lists, tables, <html> and other tools Markdown has to create readable and informative notes. Try to pack as much important information into your note as possible. The text: {text}
"""

model = WriteWithOpenAI(key=key, template_str=template_str, memory_tokens=77, path_to_note_file='markdown.md')

chunks = Chunkenize('result.txt', 3500)
model.generateNotes(chunks, 'note.md')
"""




##OLD VERSION OF MODULE. DON'T DELETE!! MIGHT BE USEFUL!
'''

key = ''

llm = ChatOpenAI(openai_api_key=key, model="gpt-3.5-turbo")
memory_tokens=77 #token limit for emory
memory = ConversationSummaryBufferMemory(llm=llm, max_token_limit=memory_tokens)
template_str = """
you have to make the notes in bullet points on the following text. You'll be writing the notes for the Markfown file, so use headers, lists, tables, <html> and other tools Markdown has to create readable and informative notes. Try to pack as much important information into your note as possible. The text: {text}
"""
template_str_html = """
you have to make the notes in bullet points on the following text. You'll be writing the notes for the html file, so use headers, lists, tables, <html> and other tools HTML has to create readable and informative notes. Try to pack as much important information into your note as possible. The text: {text}
"""

prompt=PromptTemplate(template=template_str_html, input_variables=['text'])
chain = LLMChain(llm=llm, memory=memory, prompt=prompt)
chunk_tokens=4096-memory_tokens-len(template_str) #token limit for chunks => rest after memory and prompt tokens

def writeNoteMacOS(response:str, path_to_note_file:str):
    with open(path_to_note_file, 'a') as file:
        file.write(response)


#chunks = Chunkenize('result.txt', chunk_tokens)

def generateNotes(chunks:list):
    for c in chunks:
        result = chain.predict(text=c)
        print(result)
        writeNoteMacOS(result, 'note.html')

'''