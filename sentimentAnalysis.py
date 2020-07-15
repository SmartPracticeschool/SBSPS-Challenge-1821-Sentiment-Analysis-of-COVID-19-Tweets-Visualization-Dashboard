import tweepy
from textblob import TextBlob
import  numpy as np
import pandas as pd
import re
import pandas as pd

Positive=0
Negative=0
Neutral=0
def cleanText(text):
    global Positive,Negative,Neutral
    text=re.sub(r'RT @[\w]*:',"",text)
    text = re.sub('#', '', text)
    text=re.sub(r'@[\w]*',"",text)
    text=re.sub(r'https?://[A-Za-z0-9./]*','',text)
    text=re.sub('\n','',text)
    tb= TextBlob(text)
    if(tb.sentiment.polarity>0):
        Positive+=1
    elif(tb.sentiment.polarity<0):
        Negative+=1
    else:
        Neutral+=1

    #print(str(i) + ". " + text)
    return text

consumer_key='Jxm97G9XLjso76EesqMjO98MO'
consumer_secret='xMlZQgZYJQUII28h7ce4HEuJP0BmTdp2nDqUVHi9P626EppAw4'

access_token='1101020537663426561-Nu3GBN3lED8lZoLEBGLZDOXrAWu3iu'
access_token_secret='ulU94cQ4FfH3foUgynjgHmd7qkG1Yr4kYMhqbdtpadFNr'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

search_word='#LockDown1' #Search topic

api=tweepy.API(auth,wait_on_rate_limit=True)
#date_since='2020-7-15'  # date
public_tweets=tweepy.Cursor(api.search,q=search_word,lang='en',WOEID_LOOKUP_URL=2282863).items(100000)
tweet_details=[[tweet.text,tweet.user.location,tweet.created_at] for tweet in public_tweets]
df=pd.DataFrame(data=tweet_details,columns=['Tweets','Location','Time'])
df['Tweets']=df['Tweets'].apply(cleanText)
l=len(df.index)
print(df.head(l-1))
Agree=(Positive/l)*100
Disagree=(Negative/l)*100
Neutral=(Neutral/l)*100
print('Agree:',round(Agree,2),"%")
print('Disagree:',round(Disagree,2),"%")
print('Neutral:',round(Neutral,2),"%")
print(df['Time'][1])
