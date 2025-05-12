from gtts import gTTS
import os

text = "Нарешті наступила весна. Дуже прикольна погода. 👍"

tts = gTTS(text=text, lang='uk')
tts.save("spring.mp3")
os.system('start spring.mp3')

