class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        #  "4#Hello5#World"
        res = []
        i = 0
        while i < len(s):
            # Find where the length ends and the string begins
            j = s.find('#', i)
            length = int(s[i:j])
            
            # Extract the exact substring using the length
            start_of_str = j + 1
            end_of_str = start_of_str + length
            res.append(s[start_of_str:end_of_str])
            
            # Move index to the start of the next encoded block
            i = end_of_str
        return res
