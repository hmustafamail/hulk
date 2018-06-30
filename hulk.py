# nltk demo
# Reduce input text to function words.
#
# Mustafa Hussain
# also Daren Thomas and Stephen Falk:
# https://stackoverflow.com/questions/5486337/how-to-remove-stop-words-using-nltk-or-python
#

# Must download stopwords first. Run in Python shell:
# nltk.download("stopwords")

from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer

# example: hulk would like to smash the house please
#     becomes "hulk would like smash house please"
#
# example: "to be or not to be that is the question" becomes "question"

tkzr = TweetTokenizer()

while True:
    in1 = input("hulk) ")
    word_list = tkzr.tokenize(in1) #in1.split(" ")
    
    filtered_words = [word for word in word_list if word not in stopwords.words('english')]
    print(" ".join(filtered_words).upper())
