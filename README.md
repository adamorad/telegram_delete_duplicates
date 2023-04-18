# telegram_delete_duplicates
A simple script that deletes duplicate messages (text or caption) in a channel using Telepot and and telegram bot.

## Heroku Deployment
1. Create a heroku python app
2. Create a Procfile containing:
    worker: python main.py
3. Push your app using git to heroku
3. heroku ps:scale worker=1
