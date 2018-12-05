import glob
import importlib.util
from datetime import datetime


def load_day(py_file, day, year):
    print(py_file)
    spec = importlib.util.spec_from_file_location("project", py_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    solution = module.Day(day=day, year=year)
    return solution.part_1, solution.part_2


def time_function(f):
    start = datetime.now()
    r = f()
    t = (datetime.now() - start).total_seconds()
    return r, t


def run_day(py_file, day, year):
    f = load_day(py_file, day=day, year=year)
    p1 = time_function(f[0])
    p2 = time_function(f[1])

    return p1, p2


def main(day="*", year="*"):
    print("\u001b[32;1mAdvent \u001b[34;1mof \u001b[31;1mCode \u001b[0m2018")
    py_files = glob.glob(f"./project/q{year}/day_{day}")
    for py_file in py_files:
        day = int(py_file[py_file.rfind("day_") + 4:-3])
        year = int(year) if year != "*" else datetime.now().year
        p1, p2 = run_day(py_file, day=day, year=year)

        print("\u001b[33;1mDay", day)
        print("\u001b[36;1m  Part 1")
        print("\u001b[32m   ", p1[0])
        print("\u001b[0m   ", p1[1])
        print("\u001b[36;1m  Part 2")
        print("\u001b[32m   ", p2[0])
        print("\u001b[0m   ", p2[1])
        print("")


if __name__ == "__main__":
    # if you wanna run a specific day
    main(day="05.py", year="2018")

    # or if you wanna run all:
    # main()
