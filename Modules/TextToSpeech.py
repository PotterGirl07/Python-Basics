from gtts import gTTS
sample = "Hello, my name is Aashra."
TTS = gTTS(text = sample, lang="en")
TTS.save("audio1.mp3")
