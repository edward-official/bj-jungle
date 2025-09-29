import sys
reader = sys.stdin.readline
writer = sys.stdout.write

class P1946:
    n_testcase = None
    n_applicants = None
    applicants = None
    admission_limit = None

    @staticmethod
    def stdin_processor():
        P1946.n_applicants = int(reader())
        P1946.applicants = []
        for _ in range(P1946.n_applicants):
            rank1, rank2 = map(int, reader().split())
            P1946.applicants.append((rank1, rank2))
        return

    @staticmethod
    def applicants_sorter():
        P1946.applicants.sort(key = lambda element: element[0])
        return

    @staticmethod
    def testcase_processor():
        P1946.admission_limit = 1
        best_rank2 = P1946.applicants[0][1]
        for rank1, rank2 in P1946.applicants[1:]:
            if rank2 < best_rank2:
                P1946.admission_limit += 1
                best_rank2 = rank2
        return

    @staticmethod
    def stdout_processor():
        writer(f"{P1946.admission_limit}\n")
        return

    @staticmethod
    def compute():
        for _ in range(P1946.n_testcase):
            P1946.stdin_processor()
            P1946.applicants_sorter()
            P1946.testcase_processor()
            P1946.stdout_processor()
        return

    @staticmethod
    def execute():
        P1946.n_testcase = int(reader())
        P1946.compute()
        return

P1946.execute()