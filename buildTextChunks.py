#This module builds optimal text chunks that perceive complete sentences
#maximal size of gpt-3.5-turbo input is 4096 tokens! => chunk size = 4096
#import nltk

def Tokenize(text_path:str):
    #nltk.download('punkt') #NECESSARY
    with open(text_path, "+tr") as file:
        text = file.read()

    text_tokenized = {} #dictionary {'sentense':'size'}

    """for sentence in (nltk.tokenize.sent_tokenize(text)):
        text_tokenized.update({sentence:len(sentence)})"""

    sentences = text.split('.')
    for sentence in sentences:
        text_tokenized.update({sentence:len(sentence)})
    print(text_tokenized)
    return text_tokenized

def WholeSize(text_tokenized:dict): #whole size of dictionary (in Tokens). This function isn't actually used,but I still leave it here
    whole_size = 0
    for i in text_tokenized.values():
        whole_size+=i
    return whole_size

def Chunkenize(text_path:str, chunk_size:int):
    text_tokenized = Tokenize(text_path)
    curs = 0 #current size
    i = 0 #iterator
    cs = chunk_size #max size of a chunk
    points = [] #the points
    tt_list = list(text_tokenized.items()) #turns dictionary into list of tuples which elements are keys and values of same dict elements. Reason: dictionaries can not be accesed by index
    while i<len(tt_list): #sets points where chunk size achieves the possible maximum. Special thanks to my ADS teacher cause jump-search algorithm inspired me to do it this way
        curs += (tt_list[i])[1]
        if curs>cs:
            curs = 0
            i-=1
            points.append(i)
        i+=1
    points.append(len(tt_list)-1) #sets point to the end of lists
    #points.insert(0, 0) #SETS point to the beginning of the list. NOT needed, but I will leave it there as a comment
    chunk:str=''#chunk
    chunks=[]
    for i in range(len(tt_list)): #builds chunks of maximum possible size
        add = (tt_list[i])[0]
        chunk=chunk+add #idk why but 'chunk.join(add)' doesn't work
        if i in points:
            chunks.append(chunk)
            chunk=''
    return chunks

