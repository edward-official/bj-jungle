import sys
reader = sys.stdin.readline
writer = sys.stdout.write

class P2110:
    answer = 0

    @staticmethod
    def is_distance_possible(houses, required_distance, target_count):
        count = 1
        previous_house = houses[0]
        for house in houses[1:]:
            if house - previous_house >= required_distance:
                count += 1
                previous_house = house
        if count < target_count:
            # writer(f"distance {required_distance} failed\n")
            return False
        else:
            # writer(f"distance {required_distance} succeed\n")
            if P2110.answer < required_distance:
                P2110.answer = required_distance
            return True

    @staticmethod
    def find_distance(houses, target_count, opening_distance, closing_distance):
        if opening_distance >= closing_distance:
            return
        center_distance = (opening_distance + closing_distance) // 2
        if P2110.is_distance_possible(houses, center_distance, target_count):
            P2110.find_distance(houses, target_count, center_distance + 1, closing_distance)
        else:
            P2110.find_distance(houses, target_count, opening_distance, center_distance)
        return

    @staticmethod
    def execute():
        quantity_house, quantitiy_modem = map(int, reader().rstrip().split())
        houses = [int(reader().rstrip()) for _ in range(quantity_house)]
        houses.sort()
        # writer(f"{houses}\n")
        P2110.find_distance(houses, quantitiy_modem, 1, houses[-1])
        writer(f"{P2110.answer}\n")
        return

P2110.execute()