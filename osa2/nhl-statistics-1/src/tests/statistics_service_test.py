import unittest
from player import Player
from statistics_service import StatisticsService


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89),
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_finds_player_by_full_name(self):
        self.assertEqual(self.stats.search("Kurri").name, "Kurri")

    def test_search_finds_player_by_partial_name(self):
        self.assertEqual(self.stats.search("Gret").name, "Gretzky")

    def test_search_returns_none_when_not_found(self):
        self.assertIsNone(self.stats.search("Tuntematon"))

    def test_team_contains_only_matching_players(self):
        self.assertEqual(
            [p.name for p in self.stats.team("EDM")],
            ["Semenko", "Kurri", "Gretzky"],
        )

    def test_unknown_team_is_empty(self):
        self.assertEqual(self.stats.team("XXX"), [])

    def test_top_sorts_by_points(self):
        # Pohjan top(n) palauttaa sijat 0..n eli n+1 pelaajaa.
        self.assertEqual(
            [p.name for p in self.stats.top(2)],
            ["Gretzky", "Lemieux", "Yzerman"],
        )

    def test_top_zero_returns_best_player(self):
        self.assertEqual(self.stats.top(0)[0].name, "Gretzky")

    def test_top_negative_is_empty(self):
        self.assertEqual(self.stats.top(-1), [])
