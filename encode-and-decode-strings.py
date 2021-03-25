"""
use non-ASCII delimiter
"""

class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return chr(257).join(strs) if strs else None
        

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        return s.split(chr(257)) if s is not None else []


"""
data size(4 bytes) + data
string size = string length in ASCII

divide the size into 1byte each

0xff = 255 = 0b11111111
"""
class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        def get_bytes(size):
            return reversed([chr((size >> i * 8) & 0xff) for i in range(4)])
        
        res = []
        for s in strs:
            res.extend(get_bytes(len(s)))
            res.append(s)
        return ''.join(res)
        

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        i = 0
        res = []
        while i < len(s):
            size = 0
            # take 4 bytes to get size of string
            for c in s[i:i+4]:
                size = (size << 8) + ord(c)
            i += 4
            res.append(s[i:i+size])
            i += size
        return res
        

# Your Codec object will be instantiated and called as such:
codec = Codec()
print(codec.decode(codec.encode(['aaa','bbb'])))
print(codec.decode(codec.encode([',',','])))
print(codec.decode(codec.encode([])))
print(codec.decode(codec.encode([''])))
print(codec.decode(codec.encode(['',''])))
