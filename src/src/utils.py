
import json
import random


class Utils():
    JINRO = 1
    KYOUJIN = 2
    MURABITO = 3
    URANAISHI = 4
    KISHI = 5

    def __init__(self):
        self.data = open('../data/data.json', 'r')
        self.data = json.load(self.data)
        self.positions = ['新規', 'ジロリアン', '一般人', '店員', 'かえぽん']

    def decide_positions(self, num_p):
        """
        return: self.data
        """
        self.data[0]["participant"] = num_p
        random.shuffle(self.positions)
        for i in range(num_p):
            self.data[0]["player_{}".format(
                i+1)]['position'] = self.positions[i]
        if '新規' not in self.positions[:num_p]:
            # TODO : player_2　の2をランダムに
            self.data[0]['player_2']['position'] = "新規"
            self.positions[1] = "新規"
        return self.data, self.positions[:num_p]
    