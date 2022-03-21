# External imports
from dotenv import dotenv_values
from slack_bolt import App # type: ignore
from slack_bolt.adapter.socket_mode import SocketModeHandler # type: ignore




# Internal imports
# from services.databaseService import getPerson as person


# Initialise the app
config = dotenv_values('./development.env')

# Initializes your app with your bot token and socket mode handler
app = App(token=config.get('SLACK_BOT_TOKEN'))

# Listens to incoming messages that contain "hello"
# To learn available listener arguments,
# visit https://slack.dev/bolt-python/api-docs/slack_bolt/kwargs_injection/args.html
@app.message("hello") # type: ignore
def message_hello(message: str, say): # type: ignore
    print('Method triggered')
    # say() sends a message to the channel where the event was triggered
    say("Hey there user!")

@app.command('/play')
def play(ack, say):
    print('ack')
    print(ack)
    ack()
    say('hallo')

# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, config.get('SLACK_APP_TOKEN')).start()
