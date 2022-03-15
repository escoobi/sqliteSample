from gtts import gTTS


from playsound import playsound


audio = "audio.mp3"
idioma = "pt"
sp = gTTS(text="vamos sair daqui, agora!", lang=idioma, slow=True)
sp.save(audio)
playsound(audio)
