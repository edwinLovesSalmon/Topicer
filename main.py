# s206534 WONG CHI KEEUNG EDWIN senior project
# Topicer, a trends evaluation topic listener applicaiton
from fastapi import FastAPI
from starlette.requests import Request
from fastapi.templating import Jinja2Templates
from functionaries.get_results import get_topic_keywords


app = FastAPI()


templates = Jinja2Templates(directory="./templates")

# returns the index html page
@app.get('/')
def index(request: Request):
    """Function to return the index page of an app
    """
    return templates.TemplateResponse("index.htm", context={"request": request, "title": "indexer", "keywords": 'Keys' })

@app.post('/trending')
def get_trending_topics(request: Request):

    model_path = './trained_model/top2vec.jl'
    titles, topics_keywords = get_topic_keywords(model_path)
    
    keywords = []

    for k in range( 10 ):
        # titles_display.append( f" <b>({k+1}) => Title:</b> {titles[k]}" )
        keywords.append( f"{topics_keywords[k]}".replace('\'', '').replace('[', '').replace(']', '') )


    return templates.TemplateResponse("index.htm", context={"request": request, "content":  zip(titles,keywords) })



