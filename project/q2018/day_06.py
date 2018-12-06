from project import Solution


class Day(Solution):
    def __init__(self, day, year):
        super().__init__(day, year)
        self.input = self.puzzle_input.split('\n')
        self.test_input = [
            "1, 1",
            "1, 6",
            "8, 3",
            "3, 4",
            "5, 5",
            "8, 9"
        ]

        self.rows = 360
        self.cols = 360
        self.map = [["#"] * self.cols for _ in range(self.rows)]
        self.x_max = 0
        self.y_max = 0
        self.finite_boys = []
        self.points = []

    def part_1(self):

        input = self.input
        alphabet = "abcdefghijklmnopqrstuvwxyzæøå!@$%^&*()-_=+[]ä¡²³¤€¼½¾‘"
        for row in range(0, len(input)):
            line = input[row]
            point = Point(line, str(alphabet[row]))
            self.map[point.x][point.y] = point.name
            self.points.append(point)

        for point in self.points:
            for row in range(0, self.rows):
                for col in range(0, self.cols):
                    current = self.map[row][col]
                    current_value = int(current[current.find(':') + 1:]) if ':' in current else None
                    new_value = get_taxicab_distance(point, (row, col))
                    if not current_value:
                        if current == "#":
                            self.map[row][col] = f"{point.name.lower()}:{new_value}"
                        continue

                    if new_value < current_value:
                        self.map[row][col] = f"{point.name.lower()}:{new_value}"
                    elif new_value == current_value:
                        self.map[row][col] = f".:{new_value}"

        # Clean up map
        for row in range(0, self.rows):
            for col in range(0, self.cols):
                current = self.map[row][col]
                if len(current) == 1:
                    continue
                self.map[row][col] = current[:current.find(":")]

        # Remove infinites.
        infinite_letters = set()
        for i in range(0, self.rows):
            top_row = self.map[0][i].upper()
            if top_row not in infinite_letters:
                infinite_letters.add(top_row)

            left_edge = self.map[i][0].upper()
            if left_edge not in infinite_letters:
                infinite_letters.add(left_edge)

            bottom_row = self.map[i][self.rows - 1].upper()
            if bottom_row not in infinite_letters:
                infinite_letters.add(bottom_row)

            right_edge = self.map[self.rows - 1][i].upper()
            if right_edge not in infinite_letters:
                infinite_letters.add(right_edge)

        for point in self.points:
            if point.name not in infinite_letters:
                self.finite_boys.append(point)

        highest_found = 0
        for finite_boy in self.finite_boys:
            count = sum(x.count(finite_boy.name.lower()) for x in self.map) + 1
            finite_boy.score = count
            if finite_boy.score > highest_found:
                highest_found = finite_boy.score
        return highest_found

    def part_2(self):
        region_size = 0
        for row in range(0, 1200):
            for col in range(0, 1200):
                sum_of_point = 0
                for point in self.points:
                    sum_of_point += get_taxicab_distance(point, (row, col))
                    if sum_of_point >= 10000:
                        break
                if sum_of_point < 10000:
                    region_size += 1
        return region_size


class Point:
    def __init__(self, line, name=None):
        self.x = int(line[:line.find(',')])
        self.y = int(line[line.find(',') + 1:])
        self.name = name.upper()
        self.score = None

    def __repr__(self):
        return f"{self.name}: ({self.x}, {self.y})"


def get_taxicab_distance(p, q):
    return abs(p.x - q[0]) + abs(p.y - q[1])
