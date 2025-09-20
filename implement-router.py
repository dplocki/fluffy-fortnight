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
        return sum(1
            for s, d, t in self.memory
            if d == destination and startTime <= t and endTime >= t)

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
