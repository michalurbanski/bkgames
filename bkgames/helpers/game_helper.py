def calculate_game_year(season_start_year, season_start_month, month):
    return season_start_year if int(month) >= season_start_month else (season_start_year + 1)
