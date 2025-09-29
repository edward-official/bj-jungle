import sys

reader = sys.stdin.readline
writer = sys.stdout.write

class P1700:
    n_outlet = None
    n_sequence = None
    sequence = None
    current_state = None
    unplug_counter = None

    @staticmethod
    def stdin_processor():
        P1700.n_outlet, P1700.n_sequence = map(int, reader().split())
        P1700.sequence = list(map(int, reader().split()))
        return

    @staticmethod
    def outlet_manager(index):
        if len(P1700.current_state) < P1700.n_outlet:
            P1700.current_state.append(P1700.sequence[index])
            return
        current_maximum_index = -1
        target_device = None
        for plugged_device in P1700.current_state:
            try:
                next_index = P1700.sequence.index(plugged_device, index + 1)
            except ValueError:
                target_device = plugged_device
                break
            if next_index > current_maximum_index:
                current_maximum_index = next_index
                target_device = plugged_device
        P1700.current_state.remove(target_device)
        P1700.unplug_counter += 1
        P1700.current_state.append(P1700.sequence[index])
        return

    @staticmethod
    def compute():
        P1700.current_state = []
        P1700.unplug_counter = 0
        for index, device in enumerate(P1700.sequence):
            if device in P1700.current_state:
                continue
            P1700.outlet_manager(index)
        return

    @staticmethod
    def stdout_processor():
        writer(f"{P1700.unplug_counter}\n")
        return

    @staticmethod
    def execute():
        P1700.stdin_processor()
        P1700.compute()
        P1700.stdout_processor()
        return

P1700.execute()