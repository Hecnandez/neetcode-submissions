class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "fff"
        elif strs == [""]:
            return "ttt"
        else:
            return "|||".join(strs)

    def decode(self, s: str) -> List[str]:
        strs = s.split("|||")
        if strs[0] == "ttt":
            return [""]
        elif strs[0] == "fff":
            return []
        else: 
            return strs