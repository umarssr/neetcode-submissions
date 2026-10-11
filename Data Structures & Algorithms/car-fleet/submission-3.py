class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ttf = [0]*len(speed)
        cars = list(zip(position, speed))
        cars.sort(reverse = True)
        for i in range(len(speed)):
            ttf[i] = (target-cars[i][0])/cars[i][1]
        fleets = 0
        j = 0
        while j < len(ttf):
            if j == 0:
                j+=1
                fleets +=1
            else:
                if ttf[j]>ttf[j-1]:
                    fleets +=1
                else:
                    ttf[j] = ttf[j-1]
                j+=1
        return fleets
        