class Solution:
    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "emnishpty"
        return "nishanth".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "emnishpty":
            return []
        return s.split("nishanth")