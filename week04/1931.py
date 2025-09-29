import sys
reader = sys.stdin.readline
writer = sys.stdout.write

class P1931:
    n_meeting = None
    meeting = None
    meeting_counter = None

    @staticmethod
    def stdin_processor():
        P1931.n_meeting = int(reader().strip())
        P1931.meeting = []
        for _ in range(P1931.n_meeting):
            t1, t2 = map(int, reader().split())
            P1931.meeting.append((t1, t2))
        return

    @staticmethod
    def meeting_sorter():
        P1931.meeting.sort(key = lambda element: (element[1], element[0]))
        return

    @staticmethod
    def compute():
        recent_closing = -1
        P1931.meeting_counter = 0
        for opening_time, closing_time in P1931.meeting:
            if recent_closing <= opening_time:
                recent_closing = closing_time
                P1931.meeting_counter += 1
        return

    @staticmethod
    def stdout_processor():
        writer(f"{P1931.meeting_counter}\n")
        return

    @staticmethod
    def execute():
        P1931.stdin_processor()
        P1931.meeting_sorter()
        P1931.compute()
        P1931.stdout_processor()
        return

P1931.execute()