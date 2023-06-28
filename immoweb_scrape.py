import requests


buy_url = "https://www.immoweb.be/nl/zoekertje/gebouw-gemengd-gebruik/te-koop/gent/9000/10655537"
search_results_url = "https://www.immoweb.be/nl/zoeken/huis/te-koop/gent/9000?countries=BE&page=1&orderBy=relevance"

url = buy_url

def requestURL(conn, url):
    # Request page from url
    try:
        response = conn.get(url)
        
        # If the response was succesful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occured : {http_err}')
    except Exception as err:
        print(f'Other error occured : {err}')
    
    return response

requestURL()