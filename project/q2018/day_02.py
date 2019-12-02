from collections import defaultdict

from project import Solution


class Day(Solution):
    def __init__(self, day, year):
        super().__init__(day, year)
        self.input = self.puzzle_input.split('\n')
        self.box_ids = []

    def part_1(self):
        two_times_counter = 0
        three_times_counter = 0
        for line in self.input:
            chars = defaultdict(int)
            twice = False
            three = False
            for char in line:
                chars[char] += 1
            for key, val in chars.items():
                if val == 2:
                    twice = True
                if val == 3:
                    three = True
            if twice:
                two_times_counter += 1
            if three:
                three_times_counter += 1
            if twice or three:
                self.box_ids.append(line)
        return two_times_counter * three_times_counter

    def part_2(self):
        for box_id in self.box_ids:
            for compare in self.box_ids:
                difference = 0
                common_letters = ""
                for c1, c2 in zip(box_id, compare):
                    if difference > 1:
                        break
                    if c1 != c2:
                        difference += 1
                    else:
                        common_letters += c1
                if difference == 1:
                    return common_letters
        return "ERROR, NO SOLUTION FOUND"
