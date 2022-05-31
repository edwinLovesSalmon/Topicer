# s206534 WONG CHI KEUNG EDWINn senior project
from typing import Any, Dict, List
import requests
from requests.exceptions import RequestException
import re, os
from nltk.corpus import stopwords 

stop_words = stopwords.words('english')

class YouTube:
    def __init__(self, url, api_key):
        self.url =  url
        self.api_key = api_key

    def get_response(self, payload: Dict[str, Any]):
        try:
            res = requests.get(self.url, params=payload)
            res.raise_for_status()
        except RequestException:

                print("Error while retrieving based on payload: {}".format(payload) )
            # )
        else:
            return res.json()

    def get_trendings(self, region_code: str = "ID",
                      result_per_page: int = 50):
        payload = {
            "key": self.api_key,
            "chart": "mostPopular",
            "part": "snippet, topicDetails",
            # "regionCode": region_code,
            "maxResults": result_per_page,
            'defaultAudioLanguage': 'en',
            'defaultLanguage': 'en'
        }

        response = self.get_response(payload)
        videos = response.get("items")
        # _LOGGER.debug("Got %d videos from youtube", len(videos))

        cursor = response.get("nextPageToken")
        count = 0
        while cursor:
            payload["pageToken"] = cursor
            response = self.get_response(payload)

            cursor = response.get("nextPageToken")
            videos.extend(response.get("items"))

            if count == result_per_page:
                return videos
            count += 1
        return videos


def processing(text):

    processed = []
    for tex in text:
        tex= tex.replace('_', ' ').replace('-', ' ').replace('(', '').replace(')', '')
        words = tex.split(' ')
        processed.extend(words)

    processed = [word for word in processed if not word in stop_words]
    return processed


def get_youtube_trending_inofrmation():

    url = f'https://www.googleapis.com/youtube/v3/videos'
    API_key = 'AIzaSyCrpF3-ZgMWv-tXvNfXnRqyiDfKztzhvXI'

    youtube = YouTube(url=url, api_key=API_key)
    videos = youtube.get_trendings()
    count = 0

    # filter the relevant data from the returned information of a youtube video 
    titles, videos_info = [], []
    for video in videos:
        
        try:
            # title of a video
            title =  video['snippet']['title']
            # categories of a video
            cate = video['topicDetails']['topicCategories']
            cates = []
            for cat in cate:
                # each category is present using a wikepedia link 
                cates.append(os.path.split(cat)[-1])
            videos_info.append( processing(cates) )
            titles.append(title)
        except:
            # print('passed')
            pass
            
    return titles, videos_info
