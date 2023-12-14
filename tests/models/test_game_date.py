import pytest
from bkgames.models.game_date import GameDate


@pytest.fixture
def season_start_month():
    return 9


class TestGameDate:
    def test_december_later_than_november(self, season_start_month):
        november = GameDate(month=11, day=1, season_start_month=season_start_month)
        december = GameDate(month=12, day=1, season_start_month=season_start_month)
        assert december > november

    def test_january_later_than_december(self, season_start_month):
        december = GameDate(month=12, day=1, season_start_month=season_start_month)
        january = GameDate(month=1, day=1, season_start_month=season_start_month)
        assert january > december

    def test_day_in_the_month_greater(self, season_start_month):
        first_day_of_december = GameDate(
            month=12, day=1, season_start_month=season_start_month
        )
        second_day_of_december = GameDate(
            month=12, day=2, season_start_month=season_start_month
        )
        assert second_day_of_december > first_day_of_december

    def test_the_same_date_is_equal(self, season_start_month):
        first_date = GameDate(month=12, day=1, season_start_month=season_start_month)
        the_same_date = GameDate(month=12, day=1, season_start_month=season_start_month)

        assert first_date == the_same_date
        assert the_same_date == first_date
        assert first_date >= the_same_date
        assert first_date <= the_same_date

    def test_the_same_month_different_days(self, season_start_month):
        first = GameDate(month=3, day=3, season_start_month=season_start_month)
        second = GameDate(month=3, day=7, season_start_month=season_start_month)

        third = GameDate(month=3, day=7, season_start_month=season_start_month)
        fourth = GameDate(month=3, day=3, season_start_month=season_start_month)

        assert second > first
        assert third > fourth

    @pytest.mark.parametrize(
        "month,day",
        [
            (13, 1),
            (-1, 1),
            (1, 32),
            (1, -1),
        ],
    )
    def test_incorrect_dates_raise_exception(self, season_start_month, month, day):
        with pytest.raises(ValueError):
            GameDate(month=month, day=day, season_start_month=season_start_month)

    def test_incorrect_start_month_raises_exception(self):
        with pytest.raises(ValueError):
            GameDate(month=1, day=1, season_start_month=13)
        with pytest.raises(ValueError):
            GameDate(month=1, day=1, season_start_month=-1)
        with pytest.raises(ValueError):
            GameDate(month=1, day=1, season_start_month=0)
