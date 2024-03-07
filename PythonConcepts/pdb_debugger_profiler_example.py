import cProfile
import pdb


def cal_sum(a, b):
    pdb.set_trace()
    return a + b


profiler = cProfile.Profile()
profiler.enable()

cal_sum(1, 3)

profiler.disable()
profiler.print_stats()
