import sys
reader = sys.stdin.readline
writer = sys.stdout.write

class P1700:
    n_outlet = None
    n_use = None
    use = None
    unplug_counter = None
    current_state = None

    @staticmethod
    def stdin_processor():
        P1700.n_outlet, P1700.n_use = map(int, reader().split())
        P1700.use = list(map(int, reader().split()))
        return

    @staticmethod
    def reusability_checker(upcoming_opening_range, target):
        if upcoming_opening_range >= P1700.n_use:
            return False
        for index in range(upcoming_opening_range, upcoming_opening_range + P1700.n_outlet):
            if index >= P1700.n_use:
                break
            elif P1700.use[index] == target:
                return True
        return False

    @staticmethod
    def necessity_checker(current_opening_range, target):
        current_closing_range = P1700.n_use if P1700.n_use < current_opening_range + P1700.n_outlet else current_opening_range + P1700.n_outlet
        if target in set(P1700.use[current_opening_range:current_closing_range]):
            return True
        return False

    @staticmethod
    def unplugger(current_opening_range):
        P1700.unplug_counter += 1
        for target in P1700.current_state:
            if P1700.necessity_checker(current_opening_range, target):
                continue
            elif not P1700.reusability_checker(current_opening_range + P1700.n_outlet, target):
                P1700.current_state.remove(target)
                return
        for target in P1700.current_state:
            if not P1700.necessity_checker(current_opening_range, target):
                P1700.current_state.remove(target)
                return
        return

    @staticmethod
    def compute():
        P1700.current_state = set(P1700.use[0:P1700.n_outlet])
        P1700.unplug_counter = 0
        for opening_range in range(P1700.n_outlet, P1700.n_use, P1700.n_outlet):
            for use_index in range(opening_range, opening_range + P1700.n_outlet):
                if use_index >= P1700.n_use:
                    break
                elif P1700.use[use_index] not in P1700.current_state:
                    P1700.unplugger(opening_range)
                    P1700.current_state.add(P1700.use[use_index])
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