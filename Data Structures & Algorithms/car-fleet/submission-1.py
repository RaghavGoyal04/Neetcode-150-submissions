class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        st = []
        for p, s in sorted(zip(position, speed), key= lambda x: x[0], reverse=True):
            time = (target - p)/s
            # Only add to the stack if it takes LONGER than the fleet ahead of it.
            # If it takes less or equal time, it gets absorbed, so we do nothing.
            if not st or time > st[-1]:
                st.append(time)
        return len(st)