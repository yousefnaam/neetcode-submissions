from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join("🫣" + s for s in strs)

    def decode(self, s: str) -> List[str]:
        parts = s.split("🫣")
        return parts[1:]  