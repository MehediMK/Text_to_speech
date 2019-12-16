from gtts import gTTS
import os

to = open('my.txt', 'r')
mytext=to.read().replace('\n',' ')
langu='en'
meout=gTTS(text=mytext, lang=langu, slow=False)
meout.save("output.mp3")
to.close()
os.system("start output.mp3")
