class Router:

    def __init__(self, memoryLimit: int):
        self.memory = deque(maxlen=memoryLimit)
        self.ids = set()

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        if packet in self.ids:
            return False
        
        self.ids.add(packet)
        self.memory.append(packet)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.memory:
            return []

        packet = self.memory.popleft()
        self.ids.remove(packet)
        return packet

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        size = len(self.memory)
        low = 0
        high = size

        while low < high:
            mid = (low + high) // 2
            if self.memory[mid][2] < startTime:
                low = mid + 1
            else:
                high = mid

        result = 0
        for index in range(low, size):
            if self.memory[index][2] > endTime:
                break

            if self.memory[index][1] == destination:
                result += 1

        return result

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
