class Game:
    def __init__(self, levels):
        self.levels = levels
        self.current_level_index = 0
        self.current_level_len = len(levels[0])

    def set_level_index(self, level_index):
        self.current_level_index = level_index
        self.current_level_len = len(self.levels[level_index])

    def get_score(self, actions):
        current_level = self.levels[self.current_level_index]
        max_steps = 0
        steps = 0
        for i in range(self.current_level_len - 1):
            if (current_level[i] == '0'):
                steps += 1
            elif (current_level[i] == '1' and actions[i - 1] == '1'):
                steps += 1
            elif (current_level[i] == '2' and actions[i - 1] == '2'):
                steps += 1
            else:
                if steps > max_steps:
                    max_steps = steps
                    steps = 1
        if steps > max_steps:
            max_steps = steps
            steps = 0
        return max_steps == self.current_level_len - 1, max_steps