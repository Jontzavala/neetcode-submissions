class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        sorted_cars = sorted(cars, reverse=True)
        fleets = 0
        prev_fleet_time = 0
        for i in range(len(sorted_cars)):
            time_to_target = (target - sorted_cars[i][0]) / sorted_cars[i][1]
            if time_to_target > prev_fleet_time:
                fleets += 1
                prev_fleet_time = time_to_target
        return fleets
