import re

class Regex:
    def __init__(self, repositories) -> None:
        self.patterns = {
            "vue": {
                "pattern_1": [],
                "pattern_2": [],
                "pattern_3": [],
                "pattern_4": [],
                "other_pattern": []
            },
            "linux": {
                "pattern_1": [],
                "pattern_2": [],
                "pattern_3": [],
                "pattern_4": [],
                "other_pattern": []
            },
            "react": {
                "pattern_1": [],
                "pattern_2": [],
                "pattern_3": [],
                "pattern_4": [],
                "other_pattern": []
            },
            "flutter": {
                "pattern_1": [],
                "pattern_2": [],
                "pattern_3": [],
                "pattern_4": [],
                "other_pattern": []
            },
            "tensorflow": {
                "pattern_1": [],
                "pattern_2": [],
                "pattern_3": [],
                "pattern_4": [],
                "other_pattern": []
            },
            "bootstrap": {
                "pattern_1": [],
                "pattern_2": [],
                "pattern_3": [],
                "pattern_4": [],
                "other_pattern": []
            },
            "all": {
                "pattern_1": [],
                "pattern_2": [],
                "pattern_3": [],
                "pattern_4": [],
                "other_pattern": []
            }
        }

        self.pattern_1_regex = re.compile('(?i)([+[A-Z])+\w+]')
        self.pattern_2_regex = re.compile('(?i)([A-Z])\w+:')
        self.pattern_3_regex = re.compile('(?i)([+[A-Z])+\w+\([^)]*\):')
        self.pattern_4_regex = re.compile('(?i)([A-Z])\w')

        self.extract(repositories)

    def extract(self, repositories):
        for key, value in repositories.items():
            for message in value.get("messages"):
                commitTitle = message.split("\n")[0]

                if commitTitle.startswith("Merge"):
                    continue

                if self.pattern_1_regex.match(commitTitle):
                    self.patterns.get(key).get("pattern_1").append(commitTitle)
                    self.patterns.get("all").get("pattern_1").append(commitTitle)

                elif self.pattern_2_regex.match(commitTitle):
                    self.patterns.get("all").get("pattern_2").append(commitTitle)
                
                elif self.pattern_3_regex.match(commitTitle):
                    self.patterns.get("all").get("pattern_3").append(commitTitle)

                elif self.pattern_4_regex.match(commitTitle):
                    self.patterns.get("all").get("pattern_4").append(commitTitle)

                else:
                    self.patterns.get("all").get("other_pattern").append(commitTitle)

        print("-------------------------------------------------------------------------\n\n결과: ")
        print("flutter")
        print("pattern 1 : ", str(len(patterns.get("flutter").get("pattern_1"))))
        print("pattern 2 : ", str(len(patterns.get("flutter").get("pattern_2"))))
        print("pattern 3 : ", str(len(patterns.get("flutter").get("pattern_3"))))
        print("pattern 4 : ", str(len(patterns.get("flutter").get("pattern_4"))))
        print("other_pattern : ", str(len(patterns.get("flutter").get("other_pattern"))))