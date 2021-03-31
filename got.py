import praw
import random

lists = [
    'göt at',
    'göt',
    'göööt at',
    'gött'
]


"""ID ve client secret için:
    https://www.reddit.com/prefs/apps
    yeni uygulama oluştur
    redirect https://www.example.com/
    type script
    ismini de salla kimse bakmıcak zaten
    prefs apps bölümüne tekrar girdiğinde """
reddit = praw.Reddit(
    user_agent='got at bot',
    username='[buraya ismini koy]',
    password='[buraya şifreni koy]',
    client_id='[buraya client id]',
    client_secret='[buraya client secret]'
) 
user = reddit.redditor('RecepTayyipErdoganX')
for comment in user.stream.comments(skip_existing=True):
    comment.reply(random.choice(lists))
    print(comment.body,'DONE')
    pass
