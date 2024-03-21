import os
from multiprocessing import current_process, Process


def square_numbers():
    for i in range(100):
        i * i
        print(f'Process id is {os.getpid()}')
        print(f'Task Repr is {current_process().__repr__()}')


if __name__ == '__main__':
    processes = []

    num_processes_os = os.cpu_count()  # the number of cores on your machine
    print(num_processes_os)
    # create process

    for i in range(num_processes_os):
        p = Process(target=square_numbers())
        processes.append(p)

    # start

    for p in processes:
        print(f"name of process is {p.name}")
        p.start()

    #join
    for p in processes:
        p.join()