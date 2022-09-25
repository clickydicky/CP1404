import random

import wikipedia

try:
    search = input('Enter subject to wikipedia: ')
    print(wikipedia.search(search))
    print(wikipedia.summary(search))
    print(wikipedia.page(search))

except wikipedia.DisambiguationError as e:
    # get a random page
    random_search = random.choice(e.options)
    print(wikipedia.search(random_search))
    print(wikipedia.summary(random_search))
    print(wikipedia.page(random_search))
