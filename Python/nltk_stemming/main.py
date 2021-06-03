from  nltk.stem import  PorterStemmer
from nltk.stem import  LancasterStemmer

porter = PorterStemmer()
lancaster = LancasterStemmer()

print("Porter Stemmer")
print((porter.stem("cats")))
print((porter.stem("troubling")))
print("----------")
print("Lancaster Stemmer")
print((lancaster.stem("cats")))
print((lancaster.stem("troubling")))