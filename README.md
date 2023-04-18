# Telegram Channel Message Delete Duplicates Bot

This is a bot that listens to new messages in a Telegram channel and deletes the message from the chat if it is the same as the previous message. This is useful for channels that post the same message multiple times.

## Setup

To use this bot, you will need to do the following:

1. Create a Telegram bot and get its token.
2. Add the bot to your Telegram channel.
3. Get the ID of the channel (either the @channelname or the -100id).
4. Clone this repository.
5. Install the required dependencies using pip (telepot).

## Usage

To use the bot, simply run the `main.py` file. 
The bot will automatically start listening for new messages in the channel and deleting duplicate messages.

## Heroku Deployment
1. Create a heroku python app
2. Create a Procfile containing:
    worker: python main.py
3. Push your app using git to heroku
3. heroku ps:scale worker=1


## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. All contributions are welcome!

