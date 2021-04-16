x="Donkey"
ev3.set_speech_options(language=None, Voice=F1, Speed=None, Pitch=None)
ev3.set_volume(100, Which='_all_')
while True:
  ev3.speaker.say(x)
