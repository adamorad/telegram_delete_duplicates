import time
import telepot

bot_token = 'telegram bot token'
channel_id = '@channel_name or -100id'
error_count = 0
# A program that listens to new messages in a telegram channel
# and deletes the message from the chat if it is the same as the previous message
# This is useful for channels that post the same message multiple times


bot = telepot.Bot(bot_token)

# use bot to get the last 100 messages in the channel
response = bot.getUpdates(offset=-100)



def delete_message(i):
    print('deleting message')
    print('message id: ' + str(response[i]['channel_post']['message_id']))
    # try:
    #     print('text: ' + response[i]['channel_post']['text'])
    # except:
    #     print('no text')
    # try:
    #     print('caption: ' + response[i]['channel_post']['caption'])
    # except:
    #     print('no caption')
    m_id = telepot.message_identifier(response[i]['channel_post'])
    try:
        bot.deleteMessage(m_id)
        print('deleted message: ' + str(response[i]['channel_post']['message_id']))
    except Exception as e:
        # print(e.args[0])
        return


def check_for_dups(response):
    for i in range(len(response)):
        for j in range(len(response)):
            # print(i, j)
            if i != j:
                try:
                    if response[i]['channel_post']['text'] == response[j]['channel_post']['text']:
                        # print(i, j)
                        delete_message(i)
                        response.pop(i)
                        return response
                except:
                    try:
                        if response[i]['channel_post']['caption'] == response[j]['channel_post']['caption']:
                            # print(i, j)
                            # print(response[i]['channel_post']['caption'])
                            delete_message(i)
                            response.pop(i)
                            return response
                    except:
                        continue
    print('done looping through messages')
    time.sleep(10)
    return bot.getUpdates()


while True:
    if response:
        # sort the messages by message id
        response = sorted(response, key=lambda k: k['channel_post']['message_id'])
        response = check_for_dups(response)
    else:
        time.sleep(10)
        print('no more messages, waiting for new messages')
