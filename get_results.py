# s206534 WONG CHI KEUNG senior project
import joblib
import sys
import six
from functionaries.youtube import get_youtube_trending_inofrmation
from top2vec import Top2Vec

# a function to get topic keywords from a trained model
def get_topic_keywords(model_path):
    
    # loading model
    model = joblib.load(model_path)
    # getting info about the top trending videos of youtube
    titles, videos_info = get_youtube_trending_inofrmation()
    
    topics_keywords = []
# selecting maximum of 50 videos
    for k in range( min(50, len(videos_info) )):
        keywords = []
        # take top 5/10 words of a topic of each word
        top = 10 if len(videos_info) == 0 else 5
        # appending topic of each word into a single list
        for word in videos_info[k]:
            try:
                res = model.search_topics([word], num_topics=1)[0][0][:top]
                keywords.extend(res)
            except:
                pass

        topics_keywords.append(keywords)
    return titles, topics_keywords
# print(res)
