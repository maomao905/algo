"""
map longURL to shortURL
we have to hash longURL
use incremental number as unique ID and hash(ID)
possible characters 62 chars (lowecase + uppercase + digits)
62^7 = 3521 billion urls assuming 7 length for short urls
"""
class Codec:
    def __init__(self):
        self.chars = string.ascii_letters + string.digits
        self.map = {c: i for i, c in enumerate(self.chars)}
        self.longURLs = {}
        self.N = len(self.chars)
        self.id = 0
        self.url = 'https://tinyurl.com/'

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        res = []
        self.id += 1
        n = self.id
        while n > 0:
            n, mod = divmod(n, self.N)
            res.append(self.chars[mod])
        self.longURLs[self.id] = longUrl
        
        res.reverse()
        return self.url + ''.join(res)
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        url = shortUrl[len(self.url):]
        
        _id = 0
        base = 1
        for c in reversed(url):
            _id += self.map[c] * base
            base *= self.N
        return self.longURLs[_id]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
