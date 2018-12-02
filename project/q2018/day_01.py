from itertools import cycle
from project import Solution


class Day(Solution):
    def __init__(self, day, year):
        super().__init__(day, year)
        self.input = self.puzzle_input.split('\n')

    def part_1(self):
        return sum(map(int, self.input))

    def part_2(self):
        frequency = 0
        seen_frequencies = {0}
        for line in cycle(self.input):
            change = int(line)
            frequency += change
            if frequency in seen_frequencies:
                return frequency
            seen_frequencies.add(frequency)
