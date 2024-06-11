"""
Use the user_template string's .format() method to include the user's message into the user template, and print the result.
Call the respond() function with the message passed in and save the result as response.
Log the bot's response using the bot_template string's .format() method.
Send the message "hello" to the bot.
"""

# Create templates
bot_template = "BOT : {0}"
user_template = "USER : {0}"

def send_message(message):
    print(user_template.format(message))
    response = respond(message)
    print(bot_template.format(response))

def respond(message):
   bot_message = "I can hear you! You said: " + message
   return bot_message



send_message("This is the message")