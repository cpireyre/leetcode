# better than no-op but strictly speaking still wrong
# because it doesn't return a real URL, only a hash, but whatever
CHARSET = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
def keyBang():
    return ''.join(choices(CHARSET, k=3))
    
class Codec:

    def __init__(self):
        self.mem = {}

    def encode(self, longUrl: str) -> str:
        key = keyBang()
        self.mem.update({key: longUrl})
        return key


    def decode(self, shortUrl: str) -> str:
        return self.mem[shortUrl]
# Runtime: 34 ms, faster than 87.68% of Python3 online submissions for Encode and Decode TinyURL.
# Memory Usage: 13.8 MB, less than 97.67% of Python3 online submissions for Encode and Decode TinyURL.
