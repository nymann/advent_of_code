import operator
from datetime import datetime

from project import Solution


class Guard:
    def __init__(self, id):
        self.id = id
        self.total_time_slept = 0
        self.naps = []

    def add_nap(self, wake_up_time, sleep_time):
        time_slept = (wake_up_time - sleep_time).total_seconds()
        self.naps.append((sleep_time, wake_up_time))
        self.total_time_slept += time_slept

    def __repr__(self):
        return "\n\tid: %s, sleep_time: %s\n" % (self.id, self.total_time_slept)


class Day(Solution):
    def __init__(self, day, year):
        super().__init__(day, year)
        self.test_input = [
            "[1518-11-01 00:00] Guard #10 begins shift",
            "[1518-11-01 00:05] falls asleep",
            "[1518-11-01 00:25] wakes up",
            "[1518-11-01 00:30] falls asleep",
            "[1518-11-01 00:55] wakes up",
            "[1518-11-01 23:58] Guard #99 begins shift",
            "[1518-11-02 00:40] falls asleep",
            "[1518-11-02 00:50] wakes up",
            "[1518-11-03 00:05] Guard #10 begins shift",
            "[1518-11-03 00:24] falls asleep",
            "[1518-11-03 00:29] wakes up",
            "[1518-11-04 00:02] Guard #99 begins shift",
            "[1518-11-04 00:36] falls asleep",
            "[1518-11-04 00:46] wakes up",
            "[1518-11-05 00:03] Guard #99 begins shift",
            "[1518-11-05 00:45] falls asleep",
            "[1518-11-05 00:55] wakes up"
        ]
        self.input = self.puzzle_input.split('\n')

    def part_1(self):
        guards = []
        current_guard_id = None
        sleep_time = None
        for line in self.input:
            if "#" in line:
                current_guard_id = int(line[line.find('#') + 1:line.find("begins") - 1].strip())
                # if there's any guard with this id, append him
                if len([x for x in guards if x.id == current_guard_id]) == 0:
                    guards.append(Guard(current_guard_id))
            elif "falls asleep" in line and current_guard_id is not None and sleep_time is None:
                sleep_time = datetime.strptime(line[1:line.find(']')], "%Y-%m-%d %H:%M")
            elif "wakes up" in line and sleep_time is not None and current_guard_id is not None:
                for guard in guards:
                    if guard.id == current_guard_id:
                        wake_up_time = datetime.strptime(line[1:line.find(']')], "%Y-%m-%d %H:%M")
                        guard.add_nap(wake_up_time=wake_up_time, sleep_time=sleep_time)
                        sleep_time = None
                        current_guard_id = None
                        break
        guards.sort(key=lambda g: g.total_time_slept, reverse=True)

        mode = dict()
        for x in guards[0].naps:
            asleep = x[0]
            wake_up = x[1]
            nap_length = (wake_up - asleep).total_seconds() / 60
            stop = asleep.minute + nap_length
            start = asleep.minute
            while start < stop:
                actual_minute = start % 60
                if actual_minute in mode:
                    mode[actual_minute] += 1
                else:
                    mode[actual_minute] = 1
                start += 1

        # print("000000000011111111112222222222333333333344444444445555555555")
        # print("012345678901234567890123456789012345678901234567890123456789")
        # output = ""
        # for i in range(60):
        #     if i in mode:
        #         output += str(mode[i])
        #     else:
        #         output += "."
        # print(output)
        mode = max(mode.items(), key=operator.itemgetter(1))[0]

        id = guards[0].id
        print("mode: %s, id: %s" % (mode, id))
        return mode * id

    def part_2(self):
        return "NO ANSWER"
