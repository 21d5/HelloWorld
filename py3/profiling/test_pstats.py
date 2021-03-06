import cProfile
import pstats


def slowest_replace(orignal_str):
    replace_list = []
    for i, char in enumerate(orignal_str):
        c = char if char != " " else "-"
        replace_list.append(c)
    return "".join(replace_list)


def slow_replace(orignal_str):
    replace_str = ""
    for i, char in enumerate(orignal_str):
        c = char if char != " " else "-"
        replace_str += c
    return replace_str


def fast_replace(orignal_str):
    return "-".join(orignal_str.split())


def fastest_replace(orignal_str):
    return orignal_str.replace(" ", "-")


def main():
    orignal_str = '  41 414- 34(#$&*@#&$  f)'
    for _ in range(10000):
        slowest_replace(orignal_str=orignal_str)
        slow_replace(orignal_str=orignal_str)
        fast_replace(orignal_str=orignal_str)
        fastest_replace(orignal_str=orignal_str)


if __name__ == '__main__':
    cProfile.run("main()", 'timeit')
    p = pstats.Stats('timeit')
    p.sort_stats('tottime')
    p.print_stats()
