import matplotlib.pyplot as plt
import numpy as np

class Visualize:
    def __init__(self, patterns) -> None:
        self.visualize(patterns)

    def visualize(patterns):
        x = np.arrange(3)

        plt.ylabel("number")
        plt.bar(x, [len(patterns.get("all").get("pattern_1")), len(patterns.get("all").get("pattern_2")), len(patterns.get("all").get("pattern_3"))])
        plt.xticks(x, ["[ADD] prefix", "pattern 2", "pattern 3", "pattern 4"])
        plt.show()