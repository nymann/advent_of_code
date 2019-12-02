from project import Solution


class Day(Solution):
    def __init__(self, day, year):
        super().__init__(day, year)
        self.input = [int(x) for x in self.puzzle_input.split('\n')]

    def part_1(self):
        return sum([self.fuel_requirement(m) for m in self.input])

    def part_2(self):
        return sum([self.recursive_fuel_requirement(mass=m) for m in self.input])

    @staticmethod
    def fuel_requirement(mass: int) -> int:
        return mass // 3 - 2

    def recursive_fuel_requirement(self, mass: int, result_sum: int = 0):
        result = self.fuel_requirement(mass=mass)
        if result <= 0:
            return result_sum
        return self.recursive_fuel_requirement(mass=result, result_sum=result_sum + result)
