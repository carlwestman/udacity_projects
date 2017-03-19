import webbrowser


class media():
    def __init__(self, title, storyline, trailer_youtube_url, actors, imdb_rating, genre, poster_image_url):
        self.title = title
        self.storyline = storyline
        self.trailer_youtube_url = trailer_youtube_url
        self.actors = actors
        self.imdb_rating = imdb_rating
        self.genre = genre
        self.poster_image_url = poster_image_url


class Movie(media):
    """Extension of MotionPicture Class, contains data about Movies."""
    def __init__(self, title, trailer_youtube_url, storyline,
                 poster_image_url, actors, imdb_rating, genre, year, director):

        media.__init__(self,
                       title=title,
                       storyline=storyline,
                       trailer_youtube_url=trailer_youtube_url,
                       actors=actors,
                       imdb_rating=imdb_rating,
                       genre=genre,
                       poster_image_url=poster_image_url)

        self.type = "Movie"
        self.title = title
        self.trailer_youtube_url = trailer_youtube_url
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.actors = actors
        self.imdb_rating = imdb_rating
        self.genre = genre
        self.year = year
        self.director = director
        self.__name__ = 'Movie'


class TvShow(media):
    """Extension of MotionPicture Class, contains data about TV Show."""
    def __init__(self, title, storyline, trailer_youtube_url, poster_image_url, actors, imdb_rating, genre, start_year, seasons, end_year=None):

        media.__init__(self,
                       title=title,
                       storyline=storyline,
                       trailer_youtube_url=trailer_youtube_url,
                       actors=actors,
                       imdb_rating=imdb_rating,
                       genre=genre,
                       poster_image_url=poster_image_url)

        self.type = "Tv Show"
        self.title = title
        self.storyline = storyline
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url
        self.actors = actors
        self.imdb_rating = imdb_rating
        self.genre = genre
        self.start_year = start_year
        self.end_year = end_year
        self.seasons = seasons