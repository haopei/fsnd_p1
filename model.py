class Movie():
    """Movie Class"""
    def __init__(self, title, story, poster, trailer, duration, genre, year):
        self.title = title
        self.story = story
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer
        self.duration = duration
        self.genre = genre
        self.year = year
