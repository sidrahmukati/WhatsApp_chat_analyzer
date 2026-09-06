from urlextract import URLExtract
from wordcloud import WordCloud
from collections import Counter
import pandas as pd
import emoji

extract = URLExtract()

def fetch_stats(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    #fetch number of message
    num_messages = df.shape[0]

    #fetch number of words
    words = []
    for message in df['message']:
        words.extend(message.split())

    #fetch number of media shared
    num_media = df[df['message'].astype(str).str.contains(r'(Media|image|video|album|sticker|GIF|Document) omitted>', case=False, na=False)].shape[0]
    
    #fetch numbers of links
    links = []
    for message in df['message']:
        links.extend(extract.find_urls(message))

    return num_messages, len(words), num_media, len(links)

def most_busy_person(df):
    x = df['user'].value_counts().head()
    df = round((df['user'].value_counts().head() / df.shape[0]) * 100, 2).reset_index().rename(
        columns={'index':'user', 'user':'percent'})
    return x, df

def create_wordcloud(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    wc = WordCloud(width=500, height=500, min_font_size=10, background_color="white")
    df_wc = wc.generate(df['message'].str.cat(sep=' '))
    return df_wc

def emoji_helper(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    emojis = []
    for message in df['message']:
        emojis.extend([c for c in emoji.EMOJI_DATA.keys() if c in message])
    emoji_df = pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))), columns=['emoji', 'count'])

    return emoji_df

def timeline(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    monthly_timeline = df.groupby(['year', 'month_num', 'month']).count()['message'].reset_index()
    time = []
    for i in range(monthly_timeline.shape[0]):
        time.append(monthly_timeline['month'][i] + "-" + str(monthly_timeline['year'][i]))
    monthly_timeline['time'] = time

    daily_timeline = df.groupby('only_date')['message'].count().reset_index()
    daily_timeline['only_date'] = pd.to_datetime(daily_timeline['only_date'])

    return monthly_timeline, daily_timeline

def week_activity(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    busy_day = df['day_name'].value_counts()
    busy_month = df['month'].value_counts()

    return busy_day, busy_month

def activity_heatmap(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    period_order = [
        '0-1', '1-2', '2-3', '3-4', '4-5', '5-6',
        '6-7', '7-8', '8-9', '9-10', '10-11', '11-12',
        '12-13', '13-14', '14-15', '15-16', '16-17',
        '17-18', '18-19', '19-20', '20-21', '21-22',
        '22-23', '23-00'
    ]

    df['period'] = pd.Categorical(df['period'], categories=period_order, ordered=True)
    user_heatmap = df.pivot_table(index='day_name', columns='period', values='message', aggfunc='count').fillna(0)

    return user_heatmap
