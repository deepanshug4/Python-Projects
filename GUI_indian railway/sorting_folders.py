import os
import shutil

def makeDir(lang, p):
    try:
        os.mkdir(os.path.join(p, lang))
    except Exception as e:
        return

def fileMove(audios, lang, p):
    for audio in audios:
        try:
            shutil.move(os.path.join(p, audio), os.path.join(p, lang))
        except Exception as e:
            os.remove(os.path.join(p, lang, audio))
            shutil.move(os.path.join(p, audio), os.path.join(p, lang))


def findAudios(p, lang):
    ls = os.listdir()
    finalLs = []
    for l in ls:
        if lang.lower() in l and '.mp3' in l:
            finalLs.append(l)
    return finalLs

if __name__ == "__main__":
    currentPath = os.getcwd()
    langs = ['Hindi', 'English']
    for lang in langs:
        makeDir(lang, currentPath)
        audio = findAudios(currentPath, lang)
        fileMove(audio, lang, currentPath)