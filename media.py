import webbrowser


class Movie():

    # static variable for available rating
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # setting variables for movie definitions
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # opening webbrowser for specified movie
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
