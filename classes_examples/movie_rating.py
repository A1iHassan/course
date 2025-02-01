class Movie:
    
    # Constructor
    def __init__(self, title):
        self.title = title
        self.ratings = []

    # Instance Methods
    def add_rating(self, rating):
        if self.is_valid_rating(rating):
            self.ratings.append(rating)
        else:
            print("Invalid rating.")

    def average_rating(self):
        return sum(self.ratings) / len(self.ratings)

    @staticmethod
    def is_valid_rating(rating):
        return (isinstance(rating, int) or isinstance(rating, float)) and 0 <= rating <= 5

    @staticmethod
    def is_valid_title(title):
        not_allowed = ["bad_word", "another_bad_word", "yet_another_bad_word"]
        for i in not_allowed:
            if i == title:
                print("naughty naughty, not allowed")
                return
        if isinstance(title, str) and len(title) > 0:
            print("good title")
        else:
            print("invalid title, make sure it is a string and it has at least 1 character")

# Example Usage:
movie = Movie("Inception")
movie.add_rating(5)
movie.add_rating(4)
print(movie.average_rating())  # Output: 4.5
Movie.is_valid_title("")