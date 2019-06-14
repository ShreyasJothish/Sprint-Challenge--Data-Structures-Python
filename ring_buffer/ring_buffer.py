class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        # Insert at current location and increment
        self.storage[self.current] = item
        self.current += 1

        # Handle roll over case
        if self.current == self.capacity:
            self.current = 0

    def get(self):
        output = []
        # Start fetching the items from current location
        for i in range(self.capacity):
            if self.storage[i]:
                output.append(self.storage[i])

        return output
