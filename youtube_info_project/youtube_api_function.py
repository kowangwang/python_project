import argparse
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def get_video_description(video_url):
    DEVELOPER_KEY = '_____'   # 要隱藏
    youtube = build('youtube', 'v3', developerKey=DEVELOPER_KEY)

    video_id = video_url.split('v=')[-1].split('&')[0]

    try:
        request = youtube.videos().list(
            part='snippet',
            id=video_id
        )
        response = request.execute()
        return response['items'][0]['snippet']['description']
    except:
        return '請確認網址是否正確!'

if __name__ == '__main__':
    _input = {
        'video_url':'https://www.youtube.com/watch?v=GblWSnr0-N4&list=RDGblWSnr0-N4&index=1'
    }

    _output = get_video_description(**_input)
    # print(_output)