# -*- coding: utf-8 -*-

import webbrowser

#definindo uma classe, o qual pode conter dados e métodos
class Movie():
    """This class provides a way to store movie related information"""

    #Class Variables
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    #no Construtor os dados são inicializados assim que uma instância é criada
    #"self" é a instância em questão, no caso pode ser "toy_story" ou  "coracao_valente"
    #Todas as variáveis associadas a uma instância específica são chamadas de Variáveis de Instância. Por exemplo: "self.title"
      
    #Construtor
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        #Instance Variables
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #Todos os métodos ou funções que são associados a uma instância tem o "self" como primeiro argumento.
    #São chamados de Métodos de Instância

    #Instance Methods
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url) 