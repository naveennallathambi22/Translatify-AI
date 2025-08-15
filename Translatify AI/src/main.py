import pygame
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os
flag = 0

language_tuples = [
    ('afrikaans', 'af'), ('albanian', 'sq'), ('amharic', 'am'), ('arabic', 'ar'),
    ('armenian', 'hy'), ('azerbaijani', 'az'), ('basque', 'eu'), ('belarusian', 'be'),
    ('bengali', 'bn'), ('bosnian', 'bs'), ('bulgarian', 'bg'), ('catalan', 'ca'),
    ('cebuano', 'ceb'), ('chichewa', 'ny'), ('chinese (simplified)', 'zh-cn'),
    ('chinese (traditional)', 'zh-tw'), ('corsican', 'co'), ('croatian', 'hr'),
    ('czech', 'cs'), ('danish', 'da'), ('dutch', 'nl'), ('english', 'en'),
    ('esperanto', 'eo'), ('estonian', 'et'), ('filipino', 'tl'), ('finnish', 'fi'),
    ('french', 'fr'), ('frisian', 'fy'), ('galician', 'gl'), ('georgian', 'ka'),
    ('german', 'de'), ('greek', 'el'), ('gujarati', 'gu'), ('haitian creole', 'ht'),
    ('hausa', 'ha'), ('hawaiian', 'haw'), ('hebrew', 'he'), ('hindi', 'hi'),
    ('hmong', 'hmn'), ('hungarian', 'hu'), ('icelandic', 'is'), ('igbo', 'ig'),
    ('indonesian', 'id'), ('irish', 'ga'), ('italian', 'it'), ('japanese', 'ja'),
    ('javanese', 'jw'), ('kannada', 'kn'), ('kazakh', 'kk'), ('khmer', 'km'),
    ('korean', 'ko'), ('kurdish (kurmanji)', 'ku'), ('kyrgyz', 'ky'), ('lao', 'lo'),
    ('latin', 'la'), ('latvian', 'lv'), ('lithuanian', 'lt'), ('luxembourgish', 'lb'),
    ('macedonian', 'mk'), ('malagasy', 'mg'), ('malay', 'ms'), ('malayalam', 'ml'),
    ('maltese', 'mt'), ('maori', 'mi'), ('marathi', 'mr'), ('mongolian', 'mn'),
    ('myanmar (burmese)', 'my'), ('nepali', 'ne'), ('norwegian', 'no'), ('odia', 'or'),
    ('pashto', 'ps'), ('persian', 'fa'), ('polish', 'pl'), ('portuguese', 'pt'),
    ('punjabi', 'pa'), ('romanian', 'ro'), ('russian', 'ru'), ('samoan', 'sm'),
    ('scots gaelic', 'gd'), ('serbian', 'sr'), ('sesotho', 'st'), ('shona', 'sn'),
    ('sindhi', 'sd'), ('sinhala', 'si'), ('slovak', 'sk'), ('slovenian', 'sl'),
    ('somali', 'so'), ('spanish', 'es'), ('sundanese', 'su'), ('swahili', 'sw'),
    ('swedish', 'sv'), ('tajik', 'tg'), ('tamil', 'ta'), ('telugu', 'te'),
    ('thai', 'th'), ('turkish', 'tr'), ('ukrainian', 'uk'), ('urdu', 'ur'),
    ('uyghur', 'ug'), ('uzbek', 'uz'), ('vietnamese', 'vi'), ('welsh', 'cy'),
    ('xhosa', 'xh'), ('yiddish', 'yi'), ('yoruba', 'yo'), ('zulu', 'zu')
]
language_dict = {name.lower(): code for name, code in language_tuples}


def takecommand():
    """Capture voice input and return recognized text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"The User said {query}\n")
    except Exception:
        print("say that again please.....")
        return "None"
    return query

query = takecommand()
while (query == "None"):
    query = takecommand()


def destination_language():
    """Prompt user for target language and return its code."""
    print("Enter the language in which you want to convert: Ex. Hindi, English, etc.")
    print()
    while True:
        to_lang = takecommand()
        if to_lang == "None":
            continue
        to_lang = to_lang.lower()
        if to_lang in language_dict:
            return language_dict[to_lang]
        print("Language not available. Please input another language.")

to_lang = destination_language()




try:
    translator = Translator()
    translated = translator.translate(query, dest=to_lang)
    text = translated.text
except Exception as e:
    print(f"Translation failed: {e}")
    text = ""

if text:
    try:
        speak = gTTS(text=text, lang=to_lang, slow=False)
        speak.save("captured_voice.mp3")
        pygame.mixer.init()
        pygame.mixer.music.load("captured_voice.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
        pygame.mixer.music.stop()
        os.remove('captured_voice.mp3')
    except Exception as e:
        print(f"Speech synthesis or playback failed: {e}")
    print(text)
else:
    print("No text to speak.")