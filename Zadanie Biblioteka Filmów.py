import faker

fake = faker.Faker()


class Movie:
    def __init__(self, title: str, release_year: str, genre: str, watch_amount: int):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.watch_amount = watch_amount

    def movie_str(self):
        return f"{self.title} {self.release_year}"

    def play(self):
        self.watch_amount += 1


class Series(Movie):
    def __init__(self,
                 title: str,
                 release_year: str,
                 genre: str,
                 watch_amount: int,
                 season_number: str,
                 episode_number: str
                 ):
        super().__init__(title, release_year, genre, watch_amount)
        self.season_number = season_number
        self.episode_number = episode_number

    def series_str(self):
        return f"{self.title} {self.season_number}{self.episode_number}"

    def play(self):
        self.watch_amount += 1


library = [
    Movie(title="Mad Max 2", release_year="1981", genre="action", watch_amount=0),
    Movie(title="Die Hard", release_year="1988", genre="action", watch_amount=0),
    Movie(title="Castle in the Sky", release_year="1984", genre="animation", watch_amount=0),
    Movie(title="Blade Runner", release_year="1981", genre="action", watch_amount=0),
    Series(title="The Office", release_year="1982", genre="sitcom", episode_number="E01", season_number="S01", watch_amount=0),
    Series(title="Lucyfer", release_year="2013", genre="Comedy", episode_number="E03", season_number="S05", watch_amount=0),
    Series(title="South Park", release_year="2004", genre="animation", episode_number="E15", season_number="S02", watch_amount=0),
    Series(title="Teen Wolf", release_year="2016", genre="horror", episode_number="E01", season_number="S03", watch_amount=0),
    Series(title="Rick and Morty", release_year="2014", genre="animation", episode_number="E06", season_number="S06", watch_amount=0)
    ]


def get_movies():
    movie_library = library
    return movie_library


def get_series():
    series_library = library

