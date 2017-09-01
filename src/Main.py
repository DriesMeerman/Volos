from FileEncryption import FileCryptor


print ("Start Encryption")
crypt = FileCryptor('password')
crypt.encryptToFile("../example_files/ayy_lmao.jpg", "../encrypted_files/ayy_lmao.crypt.txt", True)
crypt.decryptFromFile("../encrypted_files/ayy_lmao.crypt.txt", "../decrypt_files/ayy_lmao.jpg", True)

crypt.encryptToFile("../example_files/textFile.txt", "../encrypted_files/textFile.txt")
crypt.decryptFromFile("../encrypted_files/textFile.txt", "../decrypt_files/textFile.txt");

print ("done")