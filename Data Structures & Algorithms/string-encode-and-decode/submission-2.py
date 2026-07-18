class Solution:
    def __init__(self):
        self.delim = '\x1E' #record seperator

    def encode(self, strs: List[str]) -> str:
        return self.delim.join(strs) if strs else 'None'

    def decode(self, s: str) -> List[str]:
        if s == 'None':
            return []
        return s.split(self.delim)
        