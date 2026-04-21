class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return "" 
        
        data = self.store[key]

        #less than first value
        if timestamp < data[0][0]:
            return ''

        #first value
        if timestamp == data[0][0]:
            return data[0][1]

        #last value
        if timestamp >= data[-1][0]:
            return data[-1][1]

        l, r = 0, len(data)
        ans = ''
        while l <= r:
            m = (l+r)//2
            if data[m][0] <= timestamp:
                ans = data[m][1]
                l = m+1
            else:
                r = m-1
        return ans

# alice -> [(1, 'happy'), (2, 'sad'), (4, 'yey')]
