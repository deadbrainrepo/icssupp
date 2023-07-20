import requests


def get_random_joke():
    url = 'https://v2.jokeapi.dev/joke/Any'
    response = requests.get(url)

    if response.status_code == 200:
        joke_data = response.json()
        if joke_data['type'] == 'single':
            joke = joke_data['joke']
        else:
            joke = f"{joke_data['setup']} {joke_data['delivery']}"
        return joke
    else:
        return "Failed to fetch joke. Please try again later."


if __name__ == "__main__":
    joke = get_random_joke()
    print(joke)