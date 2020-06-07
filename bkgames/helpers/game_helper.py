""" Helpers - simple functions helpful for the program """

# TODO: it's used only here - so it can be moved to proper class as a static method
def calculate_game_year(season_start_year: int, season_start_month: int, month: int) -> int:
    """ Based on available data, calculates year in which games was played.

    Year information is missing in current input data - only month and day
    are available. Year has to be inferred then from available data.

    When season starts in October (10th month), months greater than 10 are
    known to be in the same year. If month has smaller number, it means that
    it's from the next year.

    Parameters:
        season_start_year (int): Year when season has started
            (in current implementation - from config file)
        season_start_month (int): Month starting from which games should be
            processed
        month (int): Month when game was played

    Returns:
        int: Year in which game was played
    """

    if month >= season_start_month:
        return season_start_year

    return season_start_year + 1
