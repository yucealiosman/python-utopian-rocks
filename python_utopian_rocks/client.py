import requests
import urllib.parse
from collections import defaultdict
class Client:
    def __init__(self):
        self.base_url = "https://utopian.rocks/api/"

    def get_posts(self, *args, **kwargs):
        return self.request(path="posts", params=kwargs)

    def get_moderators(self):
        return self.request('moderators')

    def is_moderator(self, user_name):
        if user_name in self.get_moderators():
            return True
        return False

    def get_moderators_by_category(self, category):
        mod_dict = {}
        for post in self.request("posts", {"category": category}):
            if not mod_dict.get(post['moderator']):
                mod_dict[post['moderator']] = {}
            if not mod_dict.get(post['moderator'], {}).get(post['status']):
                mod_dict[post['moderator']][post['status']] = []
            mod_dict[post['moderator']][post['status']].append(post)
        return mod_dict


    def get_moderators_stats_by_category(self, category):
        mod_dict = defaultdict(dict)
        for post in self.request("posts", {"category": category}):
            if not mod_dict.get(post['moderator'], {}).get(post['status']):
                mod_dict[post['moderator']][post['status']] = 0
            mod_dict[post['moderator']][post['status']] += 1
        return mod_dict

    def get_projects_stats_by_category(self, category):
        project_dict = defaultdict(dict)

        for post in self.request("posts", {"category": category}):
            if not project_dict.get(post['repository'], {}).get("contributions"):
                project_dict[post['repository']]['contributions'] = 0
            project_dict[post['repository']]['contributions'] += 1

            if not project_dict.get(post['repository'], {}).get('total_utopian_rewards'):
                project_dict[post['repository']]['total_utopian_rewards'] = 0
            project_dict[post['repository']]['total_utopian_rewards'] += float(post['utopian_vote'])
        return project_dict

    def get_contributors(self, **kwargs):
        result = self.request("posts", params=kwargs)

        author_dict = defaultdict(dict)

        for post in result:
            if not author_dict.get(post['author'], {}).get(
                    "contributions"):
                author_dict[post['author']]['contributions'] = 0
            author_dict[post['author']]['contributions'] += 1

            if not author_dict.get(post['author'], {}).get(
                    'total_utopian_rewards'):
                author_dict[post['author']]['total_utopian_rewards'] = 0
            author_dict[post['author']]['total_utopian_rewards'] += float(
                post['utopian_vote'])
            if not author_dict.get(post['author'], {}).get(
                    "total_staff_picked"):
                author_dict[post['author']]['total_staff_picked'] = 0
            author_dict[post['author']]['total_staff_picked'] += 1 if post['staff_picked'] else 0

        return author_dict

    def get_statistics_by_date(self, date):
        return self.request(f"statistics/{date}", )

    def get_moderators_by_date(self, date):
        return self.get_statistics_by_date(date)[0]["moderators"]

    def get_categories_by_date(self, date):
        return self.get_statistics_by_date(date)[1]["categories"]

    def get_projects_by_date(self, date):
        return self.get_statistics_by_date(date)[2]["projects"]

    def get_staff_picks_by_date(self, date):
        return self.get_statistics_by_date(date)[3]["staff_picks"]

    def get_tasks_requests_by_date(self, date):
        return self.get_statistics_by_date(date)[4]["task_requests"]




    def request(self, path, params=None):
        if not params:
            params = {}
        url = urllib.parse.urljoin(self.base_url, path)
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
