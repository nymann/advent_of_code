import re

# from project import Solution
from project import Solution


class Day(Solution):
    def __init__(self, day, year):
        super().__init__(day, year)
        self.input = self.puzzle_input
        self.test_input = "dabAcCaCBAcCcaDA"

    def part_1(self):
        return react_polymer(self.input)

    def part_2(self):
        results = []
        d = set()
        line = self.input
        for char in "abcdefghijklmnopqrstuvwxyz":
            if char.upper() in d:
                # We already tested this.
                continue

            p = polymer_to_test(line, char)
            results.append(react_polymer(p))

        results.sort()
        return results[0]


def react_polymer(line):
    index = 0
    manipulated_line = line
    stop_index = len(line)

    while index < stop_index:
        char = manipulated_line[index]
        previous_char = manipulated_line[index - 1] if index > 0 else None
        if previous_char and previous_char.lower() == char.lower() and previous_char != char:
            manipulated_line = manipulated_line[:index - 1] + "" + manipulated_line[index + 1:]
            stop_index -= 2
            index -= 2
        index += 1
    return len(manipulated_line)


def polymer_to_test(line, char_to_remove):
    l = re.compile(re.escape(char_to_remove), re.IGNORECASE)
    return str(l.sub('', line))
