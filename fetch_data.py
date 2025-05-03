import requests

def fetch_pubmed_abstract(query, max_results=1):
    url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
    params = {
        "query": query,
        "resultType": "core",
        "format": "json",
        "pageSize": max_results
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        abstracts = [result.get("abstractText", "") for result in data.get("resultList", {}).get("result", [])]
        return abstracts
    return []