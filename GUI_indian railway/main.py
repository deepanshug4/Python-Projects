import os
import pandas as pd
from pydub import AudioSegment 
from gtts import gTTS

def textToSpeech(text, filename):
    '''
    make a audio file from the given text
    '''
    mytext = str(text)
    if "hindi" in filename:
        language = 'hi'
    else:
        language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filename)

def mergeAudios(audios):
    '''
    This function returns pydub audio segment
    '''
    combined = AudioSegment.empty()
    for audio in audios:
        combined+= AudioSegment.from_mp3(audio)
    return combined


def generateSkeleton_hi():
    '''
    Get the audio segments!!
    '''
    audio = AudioSegment.from_mp3('railway.mp3')
    # 1st One
    start = 88000
    finish = 90200 #in miliseconds
    audioProcessed = audio[start:finish]
    audioProcessed.export('1_hindi.mp3', format='mp3') 
    # 2nd part (City from)
    # 3rd part (Se chal kar)
    start = 91000
    finish = 92200 #in miliseconds
    audioProcessed = audio[start:finish]
    audioProcessed.export('3_hindi.mp3', format='mp3') 
    # 4th part (Via city)
    # 5th part (Ke Raste)
    start = 94000
    finish = 95000 #in miliseconds
    audioProcessed = audio[start:finish]
    audioProcessed.export('5_hindi.mp3', format='mp3') 
    # 6th part (Destination City)
    # 7th part (ko jane wali gaadi)
    start = 96000
    finish = 98900 #in miliseconds
    audioProcessed = audio[start:finish]
    audioProcessed.export('7_hindi.mp3', format='mp3') 
    # 8th part (Train number and name)
    # 9th part (kuch hee samai mein platform sankaya)
    start = 105000
    finish = 108200 #in miliseconds
    audioProcessed = audio[start:finish]
    audioProcessed.export('9_hindi.mp3', format='mp3') 
    # 10th part (platform number)
    # 11th part (Pr aa rhi h)
    start = 109000
    finish = 112250 #in miliseconds
    audioProcessed = audio[start:finish]
    audioProcessed.export('11_hindi.mp3', format='mp3') 


def generateSkeleton_eng():
    '''
    Get the audio segments!!
    '''
    audio = AudioSegment.from_mp3('railway.mp3')
    # 1st One (May I have your attention please train number)
    start = 64280
    finish = 70010 #in miliseconds
    audioProcessed = audio[start:finish]
    audioProcessed.export('1_english.mp3', format='mp3') 
    # 2nd part (Train number and Train Name)
    # 3rd part (from)
    start = 76150
    finish = 77020 #in miliseconds
    audioProcessed = audio[start:finish]
    audioProcessed.export('3_english.mp3', format='mp3') 
    # 4th part (Source city)
    # 5th part (To)
    start = 78030
    finish = 79030 #in miliseconds
    audioProcessed = audio[start:finish]
    audioProcessed.export('5_english.mp3', format='mp3') 
    # 6th part (Destination City)
    # 7th part (Via)
    start = 80010
    finish = 80800 #in miliseconds
    audioProcessed = audio[start:finish]
    audioProcessed.export('7_english.mp3', format='mp3') 
    # 8th part (Via City)
    # 9th part (is arriving on platform number)
    start = 82200
    finish = 87000 #in miliseconds
    audioProcessed = audio[start:finish]
    audioProcessed.export('9_english.mp3', format='mp3') 
    # 10th part (platform number)


def generateAnnouncement(filename):
    '''
    '''
    df = pd.read_excel(filename)
    for index, item in df.iterrows():
        # Hindi Items
        textToSpeech(item['from'], '2_hindi.mp3')
        textToSpeech(item['via'], '4_hindi.mp3')
        textToSpeech(item['to'], '6_hindi.mp3')
        textToSpeech(item['train_no'] + " " + item['train_name'], '8_hindi.mp3')
        textToSpeech(item['platform'], '10_hindi.mp3')
        # English Items
        textToSpeech(item['train_no'] + " " + item['train_name'], '2_english.mp3')
        textToSpeech(item['from'], '4_english.mp3')
        textToSpeech(item['to'], '6_english.mp3')
        textToSpeech(item['via'], '8_english.mp3')
        textToSpeech(item['platform'], '10_english.mp3')

        audios_hi=[f'{i}_hindi.mp3' for i in range(1,12)]
        audios_eng= [f'{i}_english.mp3' for i in range(1,11)]
        announcement_hi = mergeAudios(audios_hi)
        announcement_eng = mergeAudios(audios_eng)
        announcement_hi.export(f"announcement_hindi_{item['train_no']}_{index+1}.mp3", format='mp3')
        announcement_eng.export(f"announcement_english_{item['train_no']}_{index+1}.mp3", format='mp3')

if __name__ == "__main__":
    print("Generating Hindi Skeleton")
    generateSkeleton_hi()
    print("Generating English Skeleton")
    generateSkeleton_eng()
    print("Now generating announcements")
    generateAnnouncement("announce.xls")
