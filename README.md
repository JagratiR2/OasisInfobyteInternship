import pyttsx3
import wikipedia

voice = pyttsx3.init()

while True:
  In = input("Search Wikipedia for: ")
  if In:  
    break
  else:
    print("Please enter a search term.")

try:
  result = wikipedia.summary(In, sentences=3)
  print(result)
  voice.say(result)
  voice.runAndWait()
except wikipedia.exceptions.PageError:
  print("Sorry, couldn't find a Wikipedia page titled", In)

