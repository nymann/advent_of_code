from collections import defaultdict
from itertools import cycle

from project import Solution


class Day(Solution):
    def __init__(self, day, year):
        super().__init__(day, year)
        self.input = self.puzzle_input.split('\n')

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

        return two_times_counter * three_times_counter

    def part_2(self):
        box_ids = []
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
                box_ids.append(line)

        for box_id in box_ids:
            copy_ids = box_ids
            for compare in copy_ids[1:]:
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
        return two_times_counter * three_times_counter
