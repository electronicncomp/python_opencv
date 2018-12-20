import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
variable = input()
speak.Speak(variable)