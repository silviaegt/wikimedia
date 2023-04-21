

continued = session.get(
    formatversion=2,
    action='query',
    list='exturlusage',
    euquery='*.uy',
    gcmlimit=100,  # 100 results per request
    continuation=True)
urls = []
pageids = []
titles = []
try:
    for portion in continued:
        if 'query' in portion:
            for url in portion['query']['exturlusage']:
                print(url['url'])
                urls.append(url['url'])
                pageids.append(url['pageid'])
                titles.append(url['title'])
        else:
            print("MediaWiki returned empty result batch.")
except APIError as error:
    raise ValueError(
        "MediaWiki returned an error:", str(error)
    )

print("Fetched {} pages".format(len(urls)))
