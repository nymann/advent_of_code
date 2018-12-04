from project import Solution


class Day(Solution):
    def __init__(self, day, year):
        super().__init__(day, year)
        self.test_input = [
            "#1 @ 1,3: 4x4",
            "#2 @ 3,1: 4x4",
            "#3 @ 5,5: 2x2"
        ]
        self.input = self.puzzle_input.split('\n')
        rows = 1000
        cols = 1000
        self.claims = [[0] * cols for _ in range(rows)]
        self.cutoffs = {0}

    def part_1(self):
        for line in self.input:
            # 1 @ 509,796: 18x15
            # id @ distance_from_fabric_left_edge, distance_from_fabric_top_edge: widthxheight

            id = int(line[1:line.find('@') - 1].strip())
            distance_from_fabric_left_edge = int(line[line.find('@') + 2: line.find(',')])
            distance_from_fabric_top_edge = int(line[line.find(',') + 1: line.find(':')])
            width = int(line[line.find(':') + 2: line.find('x')])
            height = int(line[line.find('x') + 1:])

            for i in range(width):
                for j in range(height):
                    col = i + distance_from_fabric_left_edge
                    row = j + distance_from_fabric_top_edge
                    value = self.claims[col][row]
                    if value == 0:
                        self.claims[col][row] = id
                    else:
                        if value not in self.cutoffs:
                            self.cutoffs.add(value)
                        if id not in self.cutoffs:
                            self.cutoffs.add(id)
                        self.claims[col][row] = -1

        return sum(x.count(-1) for x in self.claims)

    def part_2(self):
        for i in range(len(self.input) + 1):
            if i not in self.cutoffs:
                return i
        return "NO ANSWER"
