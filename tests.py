import unittest
from python_utopian_rocks.client import Client


class TestClient(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_is_moderator(self):
        self.assertEqual(True, self.client.is_moderator("favcau"))

    def test_get_posts(self):
        self.assertEqual(True, isinstance(self.client.get_posts(category='social'), list))

    def test_get_moderators_by_category(self):
        self.assertEqual(True, isinstance(self.client.get_moderators_by_category("social"), dict))

    def test_get_moderators_stats_by_category(self):
        self.assertEqual(True, isinstance(self.client.get_moderators_stats_by_category("social"), dict))

    def test_get_projects_stats_by_category(self):
        self.assertEqual(True, isinstance(
            self.client.get_projects_stats_by_category("social"), dict))

    def test_get_contributors(self):
        self.assertEqual(True, isinstance(
            self.client.get_contributors(category="social", status="reviewed", staff_picked=False), dict))

    def test_get_moderators_by_date(self):
        self.assertEqual(True, isinstance(
            self.client.get_moderators_by_date("today"), list))

    def test_get_categories_by_date(self):
        self.assertEqual(True, isinstance(
            self.client.get_categories_by_date("today"), list))

    def test_get_projects_by_date(self):
        self.assertEqual(True, isinstance(
            self.client.get_projects_by_date("today"), list))

    def test_get_staff_picks_by_date(self):
        self.assertEqual(True, isinstance(
            self.client.get_staff_picks_by_date("today"), list))

    def test_get_tasks_requests_by_date(self):
        self.assertEqual(True, isinstance(
            self.client.get_tasks_requests_by_date("today"), list))
