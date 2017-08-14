class Movie():
    # the __init__ function is a constructor to the class
    # it is called at the moment an object of the class is crated
    # it takes one arguement to be self
    # movie_title,movie_storyline,movie_poster,movie_trailer are the arguements here
    
    def __init__ (self,movie_title,movie_storyline,movie_poster,movie_trailer):
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=movie_poster
        self.trailer_youtube_url=movie_trailer
