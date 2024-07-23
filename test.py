import os
import googleapiclient.discovery
import csv

DEVELOPER_KEY = "AIzaSyB5mCuEoYZ3BYhfk_hOdSGejEEXjVhnz8E"
VIDEO_ID = "f7Puiilv5Tw"

# Функция для скачивания корневых комментариев
def youtube(nextPageToken=None):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"    

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        part="id,snippet",
        maxResults=100,
        pageToken=nextPageToken,
        videoId=VIDEO_ID
    )
    response = request.execute()
    return response

# Функция для скачивания реплаев на комментарии
def youtubechild(NextParentId, nextPageToken=None):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.comments().list(
        part="id,snippet",
        maxResults=100,
	pageToken=nextPageToken,
        parentId=NextParentId
    )
    response = request.execute()
    return response


def download_comments():
    print('Downloading comments...')
    
    items = []
    nextPageToken = None
    i = 0
    
    while True:
        response = youtube(nextPageToken)
        new_items = response.get("items", [])
        items.extend(new_items)
        nextPageToken = response.get("nextPageToken")
        
        print(f'Downloading comments {i * 100}-{(i + 1) * 100}...')
        i += 1
        
        if nextPageToken is None:
            break
    
    print(f'Total comments downloaded: {len(items)}')
    return items

# Пример вызова функции
comments = download_comments()

commenttext_list = [
    f'{comment["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"]}: {comment["snippet"]["topLevelComment"]["snippet"]["textOriginal"]}'
    for comment in comments
]


with open('comments.txt', 'w', encoding="utf-8") as f:
    f.write('\n'.join(commenttext_list))