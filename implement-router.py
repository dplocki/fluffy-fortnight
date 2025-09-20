class Router:

    def __init__(self, memoryLimit: int):
        self.memory_limit = memoryLimit
        self.queue = deque(maxlen=memoryLimit)
        self.memory = defaultdict(deque)
        self.ids = set()

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        if packet in self.ids:
            return False
        
        if len(self.queue) == self.memory_limit:
            old_destination = self.queue[0]
            old_source, old_timestamp = self.memory[old_destination].popleft()
            self.ids.discard((old_source, old_destination, old_timestamp))

        self.queue.append(destination)
        self.ids.add(packet)
        self.memory[destination].append((source, timestamp))
        return True

    def forwardPacket(self) -> List[int]:
        if not self.queue:
            return tuple()

        destination_id = self.queue.popleft()
        paket = self.memory[destination_id].popleft()
        result = (paket[0], destination_id, paket[1])
        self.ids.remove(result)
        return result

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        packets = self.memory[destination]
        n = len(packets)
       
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if packets[mid][1] < startTime:
                left = mid + 1
            else:
                right = mid
        start_index = left
        
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if packets[mid][1] <= endTime:
                left = mid + 1
            else:
                right = mid
        end_index = left
        
        return end_index - start_index

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
