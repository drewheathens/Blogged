
import urllib.request,json
from .models import quotes
Quotes = quotes.Quotes

# API_KEY = app.config['QUOTES_API_KEY']

# base_url = app.config["QUOTES_API_BASE_URL"]
def configure_request(app)
    global api_key, base_url

def get_quotes(category):
    '''
    Function that gets the json response to our url request
    '''
    get_quotes_url = base_url.format(category,API_KEY)

    with urllib.request.urlopen(get_quotes_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)

        quotes_results = None

        if get_quotes_response['results']:
            quotes_results_list = get_quotes_response['results']
            quotes_results = process_results(quote_results_list)


    return quotes_results

    def process_results(quote_list):
    quotes_results = []
    for quotes_item in quotes_list:
        id = quotes_item.get('id')
        author = quotes_item.get('author')
        comment = quotes_item.get('comment')
        source = quotes_item.get('source')
        quote=quotes_item.get('quote')
        

        if poster:
            quotes_object = Quotes(id,title,overview,poster,vote_average,vote_count)
            quotes_results.append(quotes_object)

    return quotes_results

