import webbrowser


class media():
    """ 
        Defines media class.
        Media class is parent class of Movie and TvShow class and can be extended with 
        other media classes when need there is a need.
        
        Class attribute:
            The media class contains 7 attibutes and should be initiated will all 7.
            title (str) -> the title of the TvShow or Movie.
            storyline (str) -> the storyline of the TvShow or Movie
            trailer_youtube_url (str) -> URL to youtube trailer
            actors (list of strings) -> List of Actors that are in TvShow or Movie
            imdb_rating (float) -> IMDB rating from IMDB.com
            genre (List of strings) -> List of genres that apply for TvShow or Movie
            poster_image_url (str) -> URL to a poster img
            
                
    """
    def __init__(self, title, storyline, trailer_youtube_url, actors, imdb_rating, genre, poster_image_url):
        self.title = title
        self.storyline = storyline
        self.trailer_youtube_url = trailer_youtube_url
        self.actors = actors
        self.imdb_rating = imdb_rating
        self.genre = genre
        self.poster_image_url = poster_image_url


class Movie(media):
    """Extension of media Class, contains data about Movies.
    
        Movies is a child class to Media.
    
        Class attribute:
            The Movie class contains 10 attibutes and should be initiated with 9 below. 
            The last attribute is set automatically 
            title (str) -> the title of the Movie.
            storyline (str) -> the storyline of the Movie
            trailer_youtube_url (str) -> URL to youtube trailer
            actors (list of strings) -> List of Actors that are in Movie
            imdb_rating (float) -> IMDB rating from IMDB.com
            genre (List of strings) -> List of genres that apply for Movie
            poster_image_url (str) -> URL to a poster img
            year (int) -> Year the movie was released
            director (str) -> Director name
            
            Automatically set attributes:
            type (str) -> 'Movie', all movies are of type Movie, this is set to be able
            to distiguise between different media types in UI
    
    """
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
    """Extension of media Class, contains data about TvShow.
    
        TvShow is a child class to Media.
    
        Class attribute:
            The Movie class contains 11 attibutes where one is set automatically and one is optional.
            title (str) -> the title of the TvShow.
            storyline (str) -> the storyline of the TvShow.
            trailer_youtube_url (str) -> URL to youtube trailer
            actors (list of strings) -> List of Actors that are in TvShow
            imdb_rating (float) -> IMDB rating from IMDB.com
            genre (List of strings) -> List of genres that apply for TvShow
            poster_image_url (str) -> URL to a poster img
            start_year (int) -> Year the of the first season
            seasons (int) -> Number of seasons

            Optional attributes
            end_year (int) -> Year of the last season, if not set (ie, TvShow still on air) end_year = None
            
            Automatically set attributes:
            type (str) -> 'Movie', all movies are of type Movie, this is set to be able
            to distiguise between different media types in UI
    
    """
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
