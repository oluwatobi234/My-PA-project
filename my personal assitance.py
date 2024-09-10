import time
import datetime as dt
import requests
import speech_recognition as sr
import pyttsx3



import pyttsx3

def ask_speack(text):
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()

    # Get the list of available voices
    voices = engine.getProperty('voices')

    # Set the desired voice (0 for the first voice, 1 for the second, etc.)
    engine.setProperty('voice', voices[0].id)  # 0 for the first voice, change to voices[1].id for a different voice

    # Set the speech rate (speed)
    the_rate = 100
    engine.setProperty('rate', the_rate + 40)

    # Pass the text to the speech engine
    engine.say(text)

    # Run the speech engine to say the text
    engine.runAndWait()

    name = input('What is your name: ')
    greet = input(f'Hello {name}, what can i do for you? ')
    command =  ['add task', 'check weather', 'set reminder, ']

    while True:
        if greet == 'add task' :
            add_task(task)
            greet = input('what else can i do for you? ')
            if greet.lower() == 'nothing':
               break
        elif greet == 'check weather':
            check_weather()
            greet = input("What else can do for you? ")
            if greet.lower() == 'nothing':
               break
        elif greet == 'set reminder':
            set_reminder()
            greet = input('what else can i do for you? ')
            if greet.lower() == 'nothing':
               break
        else:
            greet= input(f'enter valid input {command}')
            
            


def add_task(task_list):
  task = input ('Enter the task that you want to add: ')
  task_list.append(task)
  ask_speack(f'task{task} as been added')

task = []

# Function to check weather in a specified city
def check_weather():
  # Base URL for the OpenWeatherMap API
  Base_url = "http://api.openweathermap.org/data/2.5/weather?"
  
  # Your unique API key to authenticate and access OpenWeatherMap API data
  my_API_Key = "5713eec70cdfec7a2b97db89b874629d"
  
  # The city for which you want to check the weather, currently set to Doncaster
  City = "Doncaster"  

  # Function to convert temperature from Kelvin (default) to Celsius and Fahrenheit
  def kelvin_to_celsuis_fahrenheit(kelvin):
     # Convert Kelvin to Celsius
     celsuis = kelvin - 273.15
     # Convert Celsius to Fahrenheit
     fahrenheit = celsuis * (9/5) + 32
     return celsuis, fahrenheit

  # Construct the full API URL with the base URL, API key, and city name
  url =  Base_url + "appid=" + my_API_Key + "&q=" + City
  
  # Send a request to the API and get the weather data in JSON format
  weather = requests.get(url).json() 

  # Extract the current temperature in Kelvin from the API response
  temp_kelvin =  weather['main']['temp']
  
  # Convert temperature to Celsius and Fahrenheit
  temp_celsuis, temp_fahreheit = kelvin_to_celsuis_fahrenheit(temp_kelvin)
  
  # Extract the 'feels like' temperature in Kelvin and convert it
  what_theweather_like_K = weather['main']['feels_like']
  what_theweather_like_C, what_theweather_like_F = kelvin_to_celsuis_fahrenheit(what_theweather_like_K) 
  
  # Extract wind speed from the API response
  wind_speed = weather['wind']['speed']
  
  # Extract humidity, represented as a percentage, from the API response
  humidity = weather['main']['humidity']
  
  # Extract a general description of the weather (e.g., "clear sky", "cloudy")
  description =  weather['weather'][0]['description'] 
  
  # Convert Unix timestamp for sunrise and sunset to local time using the city's timezone
  sunrise_time = dt.datetime.utcfromtimestamp(weather['sys']['sunrise'] + weather['timezone'])
  sunset_time = dt.datetime.utcfromtimestamp(weather['sys']['sunset'] + weather['timezone'])

  # Print out all the weather information in a readable format
  print(f"Temperature in {City}: {temp_celsuis: .2f}°C or {temp_fahreheit: .2f}°F")
  print(f"Temperature in {City} feels like: {what_theweather_like_C: .2f}°C or {what_theweather_like_F: .2f}°F")
  print(f"Humidity in {City}: {humidity}% ")
  print(f"Wind Speed in {City}: {wind_speed} m/s ")
  print(f"General weather in {City}: {description}")
  print(f"Sun rises in {City} at {sunrise_time} local time")
  print(f"Sun sets in {City} at {sunset_time} local time")

#Function for the set reminder:+
def set_reminder():
    # A list of dictionaries containing default reminders with 'text' and 'time' in minutes
    reminders = [{'text': 'Meeting', 'time': 300}, 
                 {'text': 'gym', 'time': 60}, 
                 {'text': 'reading', 'time': 200}]

    # Asking the user for a new reminder description (the task)
    new_reminder = input('What is the reminder for? ')

    # Asking the user for the time (in minutes) for the new reminder
    new_time = input('In how many minutes? ')

    # Convert the user's input time (string) to a float to handle decimal time inputs
    my_time = float(new_time)

    # Add the new reminder (with text and time) to the reminders list
    reminders.append({'text': new_reminder, 'time': new_time})

    # Convert the time to seconds for the time.sleep() function (since time.sleep() works in seconds)
    my_time = my_time * 60

    # Loop through the list of reminders and print each one
    for reminder in reminders:
        # Access the 'text' and 'time' of each reminder and display them
        print(f"Reminder set for {reminder['text']} in {reminder['time']} minutes")
    
    # Pause the program for the set time in seconds (my_time), simulating a wait for the reminder
    time.sleep(my_time)

    # After the sleep period ends, display the reminder text to the user
    print(f"Reminder: {new_reminder}")

  
result = ask_speack("hello , deborah, your 8 years old and you like your brother laptop but he wont give you hahaha  ")
print(result)       






