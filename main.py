import playsound
import os
import random
import datetime
import pywhatkit
import speech_recognition as sr
import subprocess


def openFile(argument):
    try:
        os.startfile(argument)

    except:
        pass

def closeFile(argument):
    try:
       subprocess.call(["taskkill","/F","/IM",argument])
    except:
        pass

def take_command():
    try:
        with sr.Microphone() as source:
            print('Jarvis is now listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
            else:
                pass
    except:
        pass
    return(command)

def jarvisListening():
    rn = random.randint(1, 11)
    switcher = {
        1: 'caged_listening_on_1.wav',
        2: 'caged_listening_on_2.wav',
        3: 'caged_listening_on_3.wav',
        4: 'caged_listening_on_4.wav',
        5: 'caged_listening_on_5.wav',
        6: 'caged_listening_on_6.wav',
        7: 'caged_listening_on_7.wav',
        8: 'caged_listening_on_8.wav',
        9: 'caged_listening_on_0_s.wav',
        10: 'caged_listening_on_10.wav',
        11: 'caged_listening_on_11.wav',

    }
    return switcher.get(rn, '')

def jarvisSuggestion():
    rn = random.randint(1, 6)
    switcher = {
        1: 'worth.mp3',
        2: 'caged_insult_0.wav',
        3: 'caged_jarvis_humor_0.wav',
        4: 'caged_jarvis_humor_2_s.wav',
        5: 'caged_jarvis_humor_3.wav',
        6: 'caged_jarvis_humor_4',

    }
    return switcher.get(rn, '')

def jarvisConfirm():
    rn = random.randint(0, 11)
    switcher = {
        0: 'caged_confirm_0_s.wav',
        1: 'caged_confirm_1.wav',
        2: 'caged_confirm_2.wav',
        3: 'caged_confirm_3.wav',
        4: 'caged_confirm_4.wav',
        5: 'caged_confirm_5.wav',
        6: 'caged_confirm_6.wav',
        7: 'caged_confirm_7.wav',
        8: 'caged_confirm_8.wav',
        9: 'caged_confirm_9.wav',
        10: 'caged_confirm_10.wav',
        11: 'caged_confirm_11.wav',

    }
    return switcher.get(rn, '')

def jarvisConfused():
    rn = random.randint(0, 4)
    switcher = {
        0: 'caged_repeat_0.wav',
        1: 'caged_repeat_1.wav',
        2: 'caged_repeat_2.wav',
        3: 'caged_repeat_3.wav',
        4: 'caged_repeat_4_s.wav',
    }
    return switcher.get(rn, '')

def hour():
    hour = datetime.datetime.now().strftime('%H')
    inthour = int(datetime.datetime.now().strftime('%H'))
    if inthour < 13:
        return 'caged_num_'+ hour +'.wav'
    else:
        switcher = {
            13: 'caged_num_1.wav',
            14: 'caged_num_2.wav',
            15: 'caged_num_3.wav',
            16: 'caged_num_4.wav',
            17: 'caged_num_5.wav',
            18: 'caged_num_6.wav',
            19: 'caged_num_7.wav',
            20: 'caged_num_8.wav',
            21: 'caged_num_9.wav',
            22: 'caged_num_10.wav',
            23: 'caged_num_11.wav',
            0: 'caged_num_12.wav',
        }
        return switcher.get(inthour, '')
def minute():
    minute = datetime.datetime.now().strftime('%M')
    intmin = int(datetime.datetime.now().strftime('%M'))
    if intmin == 0:
        return 'caged_clock_oclock.wav'
    elif intmin < 10 & intmin > 0:
        return 'caged_num_0'+ minute +'.wav'
    else:
        return 'caged_num_'+ minute +'.wav'
def ampm():
    inthour = int(datetime.datetime.now().strftime('%H'))
    if inthour > 12:
        return 'caged_clock_pm.wav'
    else:
        return 'caged_clock_am.wav'
def late():
    rn = random.randint(0, 2)
    switcher = {
        0: 'caged_clock_late_0.wav',
        1: 'caged_clock_late_1.wav',
        2: 'caged_clock_late_2_s.wav',

    }
    return switcher.get(rn, '')

playsound.playsound('caged_welcome.wav')
inthour = int(datetime.datetime.now().strftime('%H'))
playsound.playsound(jarvisListening())
if inthour > 20 or inthour < 6:
    playsound.playsound(late())
listener = sr.Recognizer()

exitvariable: int = 0

def run_jarvis():
    try:
        end = True
        command = take_command()
        if 'hello' in command:
            playsound.playsound('caged_listening_on_0_s.wav')
        elif 'morning' in command:
            playsound.playsound('caged_listening_on_morning.wav')
        elif 'evening' in command:
            playsound.playsound('caged_listening_on_evening.wav')
        elif 'afternoon' in command:
            playsound.playsound('caged_listening_on_afternoon.wav')
        elif 'open up' in command:
            playsound.playsound(jarvisConfirm())
            if 'chrome' in command:
                openFile(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
            elif 'steam' in command:
                openFile(r'C:\Program Files (x86)\Steam\Steam.exe')
            elif 'discord' in command:
                openFile(r"'C:\Users\Kenji Sanehira\AppData\Local\Discord\Update.exe' --processStart Discord.exe")
            elif 'cura' in command:
                playsound.playsound('caged_loading_1.wav')
                playsound.playsound('caged_loading_2.wav')
                openFile(r'C:\Program Files\Ultimaker Cura 4.8.0\Cura.exe')
            elif 'spotify' in command:
                openFile(r'C:\Users\Kenji Sanehira\AppData\Local\Microsoft\WindowsApps\Spotify')
            else:
                playsound.playsound(jarvisConfused())
        elif 'i think' in command:
            playsound.playsound('caged_complement.wav')
        elif 'shutdown' in command:
            playsound.playsound('caged_closing.wav')
            end = False
        elif 'good night' in command:
            playsound.playsound('caged_goodnight.wav')
            playsound.playsound('caged_evening.wav')
        elif 'goodnight' in command:
            playsound.playsound('caged_goodnight.wav')
            playsound.playsound('caged_evening.wav')
        elif 'hype me up' in command:
            playsound.playsound('caged_seize_s.wav')
        elif 'siri' in command:
            playsound.playsound('caged_cc_16.wav')
        elif 'alexa' in command:
            playsound.playsound('caged_cc_16.wav')
        elif 'among us' in command:
            playsound.playsound('caged_cc_20.wav')
        elif 'did you like that' in command:
            playsound.playsound('caged_cc_21_s.wav')
        elif 'damn' in command:
            playsound.playsound('caged_cc_22.wav')
        elif 'who asked' in command:
            playsound.playsound('caged_cc_27.wav')
        elif 'what is under there' in command:
            playsound.playsound('caged_cc_26.wav')
        elif 'spencer miller' in command:
            playsound.playsound('caged_cc_28.wav')
        elif 'where is stark tower' in command:
            playsound.playsound('caged_cc_30.wav')
        elif 'who created you' in command:
            playsound.playsound('caged_cc_31.wav')
        elif 'what time is it' in command:
            rn = random.randint(0, 1)
            switcher = {
                0: 'caged_clock_time_0.wav',
                1: 'caged_clock_time_1.wav',
            }
            playsound.playsound(switcher.get(rn, ''))
            playsound.playsound(hour())
            playsound.playsound(minute())
            playsound.playsound(ampm())
        elif 'turn on my lights' in command:
            playsound.playsound(jarvisConfirm())
        elif 'time to show off' in command:
            playsound.playsound(jarvisConfirm())
        elif 'turn my led lights on' in command:
            playsound.playsound(jarvisConfirm())
        elif 'turn off dummy' in command:
            playsound.playsound(jarvisConfirm())
        elif 'is it that time' in command:
            playsound.playsound('house_party_protocol.mp3')
        elif 'do you think' in command:
            playsound.playsound(jarvisSuggestion())
        elif 'should i' in command:
            playsound.playsound(jarvisSuggestion())
        elif 'play' in command:
            playsound.playsound('caged_media_play.wav')
            song = command.replace('play', '')
            pywhatkit.playonyt(song)
        elif "let's get to work" in command:
            playsound.playsound('caged_confirm_3.wav')
            pywhatkit.playonyt("tony stark's workshop")
        elif 'homework protocol' in command:
            playsound.playsound('caged_music_playback.wav')
            pywhatkit.playonyt("lofi hip hop radio - beats to relax/study to")
        elif 'startup mark 46' in command:
            playsound.playsound('caged_intro_a.wav')
            playsound.playsound(hour())
            playsound.playsound(minute())
            playsound.playsound(ampm())
            playsound.playsound('caged_listening_on_6.wav')
            #turn led lights on
        elif 'flight test' in command:
            playsound.playsound('caged_unavailable_3.wav')
            playsound.playsound('caged_loading_0.wav')
            #flicker led lights
        elif 'flitetest' in command:
            playsound.playsound('caged_unavailable_3.wav')
            playsound.playsound('caged_loading_0.wav')
        elif 'open faceplate' in command:
            playsound.playsound(jarvisConfirm())
            #open faceplate
        elif 'close faceplate' in command:
            #close faceplate
            playsound.playsound(jarvisConfirm())
        elif 'suit lights on' in command:
            playsound.playsound(jarvisConfirm())
        elif 'suit lights off' in command:
            playsound.playsound(jarvisConfirm())
        elif 'turn on arc reactor' in command:
            playsound.playsound(jarvisConfirm())
        elif 'turn off arc reactor' in command:
            playsound.playsound(jarvisConfirm())
        elif 'blow mark 46' in command:
            playsound.playsound('caged_self_destruct_0.wav')
            playsound.playsound('caged_')
        else:
            pass
        return end
    except:
        pass

while run_jarvis():
    run_jarvis()
