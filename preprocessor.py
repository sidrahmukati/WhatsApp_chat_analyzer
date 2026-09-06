import re
import pandas as pd

def preprocessor(data):
    # Regex pattern matching both iOS/Laptop [dd/mm/yy, hh:mm:ss AM/PM] 
    # and Android dd/mm/yyyy, hh:mm -
    pattern = r"(\[\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}(?::\d{2})?\s?(?:[AP]M|[ap]m)?\]|\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s?-\s?)"

    # Split data and extract dates
    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)

    raw_messages = []
    raw_dates = []
    
    for i in range(0, len(dates)):
        raw_dates.append(dates[i])
        raw_messages.append(messages[i*2 + 1] if len(messages) > (i*2 + 1) else messages[i])

    df = pd.DataFrame({'user_message': raw_messages, 'message_date': raw_dates})
    
    df['message_date'] = df['message_date'].str.replace(r'[\[\]\-]', '', regex=True).str.strip()
    df['message_date'] = pd.to_datetime(df['message_date'], format='mixed')

    df.rename(columns={'message_date': 'date'}, inplace=True)

    # separate users and messages
    users = []
    messages = []
    try:
        users.remove('group_notification')
    except ValueError:
        pass
    for message in df['user_message']:
        entry = re.split('([\w\W]+?):\s', message)
        if entry[1:]:
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append('group_notification')
            messages.append(entry[0])

    df['user'] = users
    df['message'] = messages
    df.drop(columns=['user_message'], inplace=True)

    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['only_date'] = pd.to_datetime(df['date']).dt.date
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    period = []
    for hour in df[['day_name', 'hour']]['hour']:
        if hour == '23':
            period.append(str(hour) + "-" + str('00'))
        elif hour == '00':
            period.append(str('00') + "-" + str(int(hour) + 1))
        else:
            period.append(str(hour) + "-" + str(int(hour) + 1))

    df['period'] = period

    return df
