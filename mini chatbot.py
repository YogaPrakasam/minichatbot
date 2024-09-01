import pyttsx3
import wikipedia

# Initialize the text-to-speech engine
voice = pyttsx3.init()

# Get input from the user
query = input("Searching Wikipedia: ")

try:
    # Fetch summary from Wikipedia
    result = wikipedia.summary(query, sentences=3)
    print(result)
    
    # Use text-to-speech to say the result
    voice.say(result)
    voice.runAndWait()  # Corrected the method name

except wikipedia.exceptions.DisambiguationError as e:
    print("There are multiple entries for this term. Please specify more clearly.")
    print(e.options)

except wikipedia.exceptions.PageError:
    print("The page does not exist on Wikipedia.")

except Exception as e:
    print(f"An error occurred: {e}")
