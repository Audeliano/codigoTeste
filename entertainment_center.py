# -*- coding: utf-8 -*-

import media
import fresh_tomatoes

#criando a instância (o objeto) "toy_story" da classe "Movie"
#uma vez criado, o construtor da classe "Movie" é chamado. Ele é basicamente o método "init" da classe
#Instance
toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to live", "https://lumiere-a.akamaihd.net/v1/images/c3c2b4a3323c4a71929cd5fc76bcda4df7157175.jpeg?region=0%2C0%2C1024%2C320", "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toy_story.storyline)
#toy_story.show_trailer()

#Instance
coracao_valente = media.Movie("Coracao Valente", "O filme retrata a figura historica de William Wallace, guerreiro, patriota escoces e heroi medieval.", "https://upload.wikimedia.org/wikipedia/pt/0/0e/Braveheart_poster.jpg", "https://www.youtube.com/watch?v=pvLaJ-tPbYQ")
#coracao_valente.show_trailer()

movies = [toy_story, coracao_valente]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)

print(media.Movie.__doc__, media.Movie.__name__, media.Movie.__module__)
