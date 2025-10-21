import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="pkg_resources")


import os
import eel
from backend.auth import recognize
from backend.auth.recognize import AuthenticateFace
from backend.feature import *
from backend.command import *



def start():
    
    eel.init("frontend") 
    
    play_assistant_sound()
    @eel.expose
    def init():
        eel.hideLoader() # type: ignore

        speak("Welcome to Jarvis")
        speak("Ready for Face Authentication")
        flag = recognize.AuthenticateFace()
        if flag ==1:
            speak("Face recognized successfully")
            eel.hideFaceAuth() # type: ignore
            eel.hideFaceAuthSuccess() # type: ignore
            speak("Welcome to Your Assistant")
            eel.hideStart() # type: ignore
            play_assistant_sound()
        else:
            speak("Face not recognized. Please try again")
        
    os.system('start msedge.exe --app="http://127.0.0.1:8000/index.html"')
    
    
    
    eel.start("index.html", mode=None, host="localhost", block=True) 
