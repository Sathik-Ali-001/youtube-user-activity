import os
import json
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build


SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']


def get_authenticated_service():
    creds = None


    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)


    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(r"Client_secrets.json", SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token_file:
            token_file.write(creds.to_json())

    return build('youtube', 'v3', credentials=creds)


def fetch_liked_videos():
    youtube = get_authenticated_service()

    request = youtube.videos().list(
        part='snippet,contentDetails,statistics',
        myRating='like'
    )
    response = request.execute()

    print("\nLiked Videos:\n")
    for item in response.get('items', []):
        title = item['snippet']['title']
        video_id = item['id']
        print(f"{title} - https://www.youtube.com/watch?v={video_id}")


fetch_liked_videos()