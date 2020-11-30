
class Movie:
    def __init__(self, title: str, release_year: str, type: str, watch_amount: str):
        self.title = title
        self.release_year = release_year
        self.type = type
        self.watch_amount = watch_amount


class Series(Movie):
    def __init__(self,
                 title: str,
                 release_year: str,
                 type: str,
                 watch_amount: str,
                 season_number: str,
                 episode_number: str
                 ):
        super().__init__(title, release_year, type, watch_amount)
        self.season_number = season_number
        self.episode_number = episode_number
