## Python chatbot documentation

**Description**
- Simple chatbot using Python 3.8 and Python modules. Chatbot analyse input from microphone and waiting for waking up word/s ("báro", "hej báro") then comes command mode where chatbos is waiting for commands. 
- Chatbot is in Czech language.

**Requirements**
- Python 3.8
- Python modules (some modules need to be installed manually, not with pip):
  - speech_recognition - Speech recognition
    - "pip install SpeechRecognition"
  - pygame - for work with audio
    - "pip install pygame"
  - gtts - Google text to speech
    - "pip install gTTS"
  - io - bytes audio
    - no need to install
  - time - always handly
    - no need to install
- Microphone

 **How to run**
 - "python chatbot.py"

 **commands**
 waking up with "báro" or "hej báro". 
 - "Kolik je hodin" -> Chatbot gonna answer what time is it.
 - "Vyhledej (argument)"  -> Chatbot gonna searching on google (argument) with default browser.
 - "Otevři (argument)"  -> Chatbot gonna open something from (argument) where argument is {"facebook", "twitter", "instagram", "zing"}.
 - "Řekni (argument)" -> Simple echo command.
 - "zapni (+ random (+ vypni se))"  -> there are 3 options:
   - "...zapni..."  -> Open youtube.
   - "...zapni...random..." -> Open random playlist on youtube.
   - "...zapni...random...vypni se..."  -> Open random playlist on youtube and turn off.
 - "vypni se" or "konec"  -> Closing app.
