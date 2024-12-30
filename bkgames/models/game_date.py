from functools import total_ordering


@total_ordering
class GameDate:
    """
    This class is used to store information about date when game was played.

    In the input data, there's no information about year.
    But in the application games have to be sorted in order in a way that
    games played e.g. in month=10 are earlier than games played in month=2.

    Which exact year this is not exactly important, as it would be only for sorting purposes.
    So, this missing piece of data can be just simulated with another piece of information
    that could be used for sorting purposes. In this class it's called _sort_value.
    """

    # TODO: in the client of this code, season_start_month should be provided based on the config.json file
    # TODO: but do we need season_start_month at all?
    def __init__(self, month: int, day: int, season_start_month: int):
        if month < 1 or month > 12:
            raise ValueError("Month must be between 1 and 12")

        # Simplification, as it doesn't matter in the context of sorting by days and months.
        # Month can have up to 31 days. Even if in real life months can have smaller number of days.
        if day < 1 or day > 31:
            raise ValueError("Day must be between 1 and 31")

        if season_start_month < 1 or season_start_month > 12:
            raise ValueError("Season start month must be between 1 and 12")

        self._month = month
        self._day = day
        self._sort_value: int = self.__determine_sort_value__(month, season_start_month)
        # a trick to reliably sort both month and day as ints
        self._monthday = self._month * 100 + self._day  # e.g. dec 23 is 1223

    def __determine_sort_value__(self, month: int, season_start_month: int) -> int:
        if month < season_start_month:
            return 1  # next year
        return 0  # current year

    def __lt__(self, other: "GameDate") -> bool:
        if self._sort_value == other._sort_value:
            return self._monthday < other._monthday
        return self._sort_value < other._sort_value

    def __gt__(self, other: "GameDate") -> bool:
        return other < self

    def __eq__(self, other: "GameDate") -> bool:
        return self._month == other._month and self._day == other._day

    def __repr__(self):
        return f"{self._day}.{self._month}"
