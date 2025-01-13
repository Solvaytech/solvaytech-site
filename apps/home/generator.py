import random
import string
class KeyGenerator:
    def __init__(self, length = 1000,
                pool =  string.ascii_letters 
                            + string.digits 
                            # + string.punctuation
                ):

        self.length = length
        self.pool = pool
        self.token = ""

    def randomGenerateKey(self):
        return ''.join(random.choices(self.pool, k=self.length))