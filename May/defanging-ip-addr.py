class Solution:
    def defangIPaddr(self, address: str) -> str:
        x = address.replace('.','[.]')
        return x