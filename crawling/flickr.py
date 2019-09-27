import flickrapi
import urllib.request
import time

keywords = [
    # "background", "cock", "ostrich", "brambling", "vulture",
    'cheetah', "lion", "window", "food", "hobby", "country",
    "mountain", "snow", "war", "human", "school",
    # "wind", 'street', 'dance', 'travel', 'world',
    # 'movie', 'people', 'person', 'man', 'woman',
]

SAVE_PATH = '/Volumes/SD/deeplearning/data/mosaic/flickr/'

# Flickr api access key
flickr=flickrapi.FlickrAPI('c6a2c45591d4973ff525042472446ca2', '202ffe6f387ce29b', cache=True)

current_milli_time = lambda: int(round(time.time() * 1000))

for keyword in keywords:
    photos = flickr.walk(text=keyword,
                         tag_mode='all',
                         tags=keyword,
                         extras='url_c',
                         per_page=100,           # may be you can try different numbers..
                         sort='relevance')

    urls = []
    for i, photo in enumerate(photos):
        url = photo.get('url_c')
        if url is None:
            continue

        urls.append(url)
        print(keyword + ' url : ' + str(i))
        # get 50 urls
        if i > 500:
            break

    print(keyword + 'total Size : ' + str(len(urls)))

    # Download image from the url and save it to '00001.jpg'

    for i, url in enumerate(urls):
        print(keyword + ' save : ' + str(i))
        try:
            urllib.request.urlretrieve(url, SAVE_PATH + str(current_milli_time()) + str(i) + '.jpg')
        except:
            continue
