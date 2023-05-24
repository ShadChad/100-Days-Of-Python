import win32com.client as wincl

# speaker_number = 1
# spk = wincl.Dispatch("SAPI.SpVoice")
# vcs = spk.GetVoices()
# SVSFlag = 11
# print(vcs.Item (speaker_number) .GetAttribute ("Name")) # speaker name
# spk.Voice
# spk.SetVoice(vcs.Item(speaker_number)) # set voice (see Windows Text-to-Speech settings)
# spk.Speak("Hello, it works!")

# names = ['kushal','hari','shyam']
while True:
    names = []
    name = (input("Enter your Name: "))
    name.replace(" ","")
    
    names.append(name)
    print(names[0])
    
    # if not name.isalpha():
    #     speaker = wincl.Dispatch("SAPI.SpVoice")
    #     speaker.Speak("Please enter a valid name")
    #     continue

    def speak():
        i = 0
        for name in names:
            
            speaker = wincl.Dispatch("SAPI.SpVoice")
            speaker.Speak(f"ShoutOut to You {names[i]}")
            i = i+1

    speak()
