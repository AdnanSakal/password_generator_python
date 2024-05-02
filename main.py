import random
import string
password = []
alphabet = string.ascii_letters
digits = string.digits
punctuation = string.punctuation
a = random.sample(list(alphabet),5)
b = random.sample(list(digits),3)
c = random.sample(list(punctuation),2)
aa = "".join(a)
bb = "".join(b)
cc = "".join(c)
password.append(aa)
password.append(bb)
password.append(cc)
var = "".join(password)
print(f"your strong password is (☞ﾟヮﾟ)☞ {var}")


    
