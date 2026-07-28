class Solution:
    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "nishanth"
        return "nishanth".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "nishanth":
            return []
        return s.split("nishanth")