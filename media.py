import webbrowser
class Movie():
    ''' This class provides a to store movie related information'''
    def __init__(self, movie_title,movie_storyline,poster_image,trailer_youtube,movie_rating,movie_desc,movie_director):
        '''This is a constructor of movie class and it gets called when memory for the object allocated
        The self parameter refers to the instance of the object
        title is an instance variable to store the title of the movie
        '''
        self.title = movie_title
        ''' storyline is an instance variable to store the story line of the movie'''
        self.storyline = movie_storyline
        ''' poster_image_url is an instance variable to store the URL of the movie poster image'''
        self.poster_image_url = poster_image
        ''' trailer_youtube_url is an instance variable to store the youtube URL of the movie trailer'''
        self.trailer_youtube_url = trailer_youtube
        ''' movie_rating is an instance variable to store the movie rating'''
        self.movie_rating=movie_rating
        ''' movie_desc is an instance variable to store the deacription of the movie'''
        self.movie_desc=movie_desc
        ''' movie_director is an instance variable to store the movie director name'''
        self.movie_director = movie_director
        
        ''' show_trailer is an instance method to run the youutube movie trailer'''
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
