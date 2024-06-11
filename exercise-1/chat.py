"""
Write a function called respond() with a single parameter message which returns the bot's response. To do this, concatenate the strings "I can hear you! You said: " and message.
Store the concatenated strings in bot_message, and return this result.

"""


bot_template = "BOT : {0}"
user_template = "USER : {0}"

def respond(message):
   bot_message = "I can hear you! You said: " + message
   return bot_message


def ____(message):
    bot_message = bot_template.format(respond(message))

    return bot_message


print(respond("hello!"))