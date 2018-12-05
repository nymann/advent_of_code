import operator
from datetime import datetime


# from project import Solution
from project import Solution


class Guard:
    def __init__(self, id):
        self.id = id
        self.total_time_slept = 0
        self.naps = []
        self.favorite_minute = None

    def add_nap(self, wake_up_time, sleep_time):
        time_slept = (wake_up_time - sleep_time).total_seconds()
        self.naps.append((sleep_time, wake_up_time))
        self.total_time_slept += time_slept

    def get_modes(self):
        mode = {}
        for nap in self.naps:
            asleep = nap[0]
            wake_up = nap[1]
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
        return mode

    def get_favorite_minute(self):
        mode = self.get_modes()
        if not mode or len(mode) == 0:
            return 0, 0
        maximum = max(mode, key=mode.get, default=0)  # Just use 'min' instead of 'max' for minimum.
        return maximum, mode[maximum]

    def __repr__(self):
        return "\n\tid: %s, sleep_time: %s\n" % (self.id, self.total_time_slept)


class Day(Solution):
    def __init__(self, day, year):
        print("hey")
        super().__init__(day, year)
        self.input = self.puzzle_input.split('\n')
        self.input.sort()
        self.guards = []

    def part_1(self):
        current_guard_id = None
        sleep_time = None
        for line in self.input:
            if "#" in line:
                current_guard_id = int(line[line.find('#') + 1:line.find("begins") - 1].strip())

                # if there's any guard with this id, append him
                if len([x for x in self.guards if x.id == current_guard_id]) == 0:
                    self.guards.append(Guard(current_guard_id))
            elif "falls asleep" in line:
                sleep_time = datetime.strptime(line[1:line.find(']')], "%Y-%m-%d %H:%M")
            elif "wakes up" in line:
                for guard in self.guards:
                    if guard.id == current_guard_id:
                        wake_up_time = datetime.strptime(line[1:line.find(']')], "%Y-%m-%d %H:%M")
                        guard.add_nap(wake_up_time=wake_up_time, sleep_time=sleep_time)
                        break
        self.guards.sort(key=lambda g: g.total_time_slept, reverse=True)

        mode = dict()
        for x in self.guards[0].naps:
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
        mode = max(mode.items(), key=operator.itemgetter(1))[0]

        id = self.guards[0].id
        return mode * id

    def part_2(self):
        mode = 0
        highest_guard_seen = None  # LUL
        minute = 0
        for guard in self.guards:
            maximum = guard.get_favorite_minute()
            if maximum[1] > mode:
                mode = maximum[1]
                minute = maximum[0]
                highest_guard_seen = guard
        print("%s * %s (the actual minute was (%s)" % (highest_guard_seen.id, mode, minute))
        return highest_guard_seen.id * minute

