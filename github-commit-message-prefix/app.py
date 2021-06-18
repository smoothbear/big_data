from regex.regex import Regex
import requests
import regex

baseURL = 'https://api.github.com/repos/{owner}/{repo}/commits?per_page=100'
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

class App:
    def __init__(self) -> None:
        self.repositories = {
            "vue": {
                "owner": "vuejs",
                "repo": "vue",
                "messages": []
            },
            "linux": {
                "owner": "torvalds",
                "repo": "linux",
                "messages": []
            },
            "react": {
                "owner": "facebook",
                "repo": "react",
                "messages": []
            },
            "flutter": {
                "owner": "flutter",
                "repo": "flutter",
                "messages": []
            },
            "tensorflow": {
                "owner": "tensorflow",
                "repo": "tensorflow",
                "messages": []
            },
            "bootstrap": {
                "owner": "twbs",
                "repo": "bootstrap",
                "messages": []
            }
        }
        self.get_commits_by_url()
        regex = Regex(self.repositories)
        regex.pa

    def get_commits_by_url(self):
        for key, value in self.repositories:
            changedOwner = baseURL.replace("{owner}", value.get("owner"))
            URL = changedOwner.replace("{repo}", value.get("repo"))

            for page in range(1, 5):
                response = requests.get(URL + "&page=" + str(page), headers=headers)
                if response.status_code != 200:
                    break

                for commit in response.json():
                    value.get("messages").append((commit.get('commit').get('message')))

        return