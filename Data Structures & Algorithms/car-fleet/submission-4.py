class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        end_times = []
        cars = list(zip(position, speed))
        cars.sort(key=lambda x: x[0], reverse = True)
        for pos, spd in cars:
            end_times.append((target-pos)/spd)
            if len(end_times) >=2 and end_times[-1]<=end_times[-2]:
                end_times.pop()
        return len(end_times)



        
        
        