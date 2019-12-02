from typing import Optional

from project import Solution


class Day(Solution):
    def __init__(self, day, year):
        super().__init__(day, year)
        self.input = self.puzzle_input.split(',')

    def part_1(self) -> int:
        return self.solver(noun=12, verb=2)

    def part_2(self) -> Optional[int]:
        for verb in range(100):
            for noun in range(100):
                output = self.solver(noun=noun, verb=verb)
                if output == 19690720:
                    return 100 * noun + verb
        return None

    def solver(self, noun: int, verb: int) -> int:
        p_input = [int(l) for l in self.input]
        p_input[1] = noun
        p_input[2] = verb

        for x in range(0, len(p_input), 4):
            opcode = p_input[x]
            start_pos = p_input[x + 1]
            end_pos = p_input[x + 2]
            output_pos = p_input[x + 3]

            if opcode == 1:
                # add
                p_input[output_pos] = p_input[start_pos] + p_input[end_pos]
            elif opcode == 2:
                # multiply
                p_input[output_pos] = p_input[start_pos] * p_input[end_pos]
            elif opcode == 99:
                break
        return p_input[0]
