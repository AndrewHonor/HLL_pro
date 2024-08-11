import requests
from bs4 import BeautifulSoup
from flask import Flask, request
from faker import Faker

app = Flask(__name__)
fake = Faker()


response = requests.get("https://en.wikipedia.org/wiki/List_of_music_genres_and_styles")
soup = BeautifulSoup(response.content, 'html.parser')
genres = [li.text for li in soup.select("div.div-col li")]
print(genres)

music_stats = {genre: fake.city() for genre in genres}
print(music_stats)
@app.route('/stats_by_city')
def stats_by_city():
    genre = request.args.get('genre')
    if not genre:
        return "Genre is a required parameter", 400

    city = music_stats.get(genre)
    if city:
        return city
    else:
        return "Genre not found", 404

if __name__ == '__main__':
    app.run(debug=True)
