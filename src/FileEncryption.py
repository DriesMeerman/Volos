import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES

class AESCipher(object):

    def __init__(self, key):
        self.bs = 32
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:]))

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    def encryptB64(self, raw):
        return base64.b64encode(self.encrypt(raw))

    def decryptB64(self, enc):
        return self.decrypt(base64.b64decode(enc))


    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]


class FileCryptor(object):

    def __init__(self, key):
        self.aes = AESCipher(key)

    def encryptToFile(self, inPath, outPath, b64=False):
        with open (inPath, "rb") as fp:
            data = fp.read()

        with open(outPath, "wb") as fp:
            if b64:
                fp.write(self.aes.encryptB64(data))
            else:
                fp.write(self.aes.encrypt(data))

    def decryptFromFile(self, inPath, outPath, b64=False):
        with open(inPath, "rb") as fp:
            data = fp.read()

        with open(outPath, "wb") as fw:
            if b64:
                fw.write(self.aes.decryptB64(data))
            else:
                fw.write(self.aes.decrypt(data))
