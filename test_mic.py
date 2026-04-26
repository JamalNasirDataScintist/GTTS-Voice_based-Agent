import speech_recognition as sr 
print("Available input devices ")

devices=sr.Microphone.list_microphone_names()

if not devices:
    print("No devices found")
else:
    for index, name in enumerate(devices):
        print(f"{index}: {name}")