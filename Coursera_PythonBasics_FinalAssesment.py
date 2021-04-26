#1) Below are a set of scores that students have received in the past semester.
# Write code to determine how many are 90 or above and assign that result to the value a_scores

scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
scores_split = scores.split(" ")
a_scores = 0

for score in scores_split:
    score = float(score)
    if score >= 90:
        a_scores += 1

print(a_scores)

# 2) Write code that uses the string stored in org and creates an acronym which is assigned to the variable acro.
# Only the first letter of each word should be used, each letter in the acronym should be a capital letter,
# and there should be nothing to separate the letters of the acronym.
# Words that should not be included in the acronym are stored in the list stopwords.
# For example, if org was assigned the string “hello to world” then the resulting acronym should be “HW”.

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"
acro = ""
lst1 = org.split()

for org_stopword in lst1:
    if org_stopword in stopwords:
        lst1.remove(org_stopword)

for acronym in lst1:
    acro += acronym[0].upper()

print(acro)


#3) Write code that uses the string stored in sent and creates an acronym which is assigned to the variable acro.
# The first two letters of each word should be used, each letter in the acronym should be a capital letter,
# and each element of the acronym should be separated by a “. ” (dot and space).
# Words that should not be included in the acronym are stored in the list stopwords.
# For example, if sent was assigned the string “height and ewok wonder” then the resulting acronym should be “HE. EW. WO”.


stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"
acro = ""
sent_split = sent.split()

for stopword in sent_split:
    if stopword in stopwords:
        sent_split.remove(stopword)

for acronym in sent_split:
    acro = acro + acronym[0] + acronym[1]
    if acronym != sent_split[-1]:
        acro += ". "
acro = acro.upper()
print(acro)


#4) A palindrome is a phrase that, if reversed, would read the exact same.
# Write code that checks if p_phrase is a palindrome by reversing it and then checking if the reversed
# version is equal to the original. Assign the reversed version of p_phrase to the variable r_phrase
# so that we can check your work.


p_phrase = "was it a car or a cat I saw"
r_phrase = p_phrase[::-1]
print(r_phrase)


#5) Provided is a list of data about a store’s inventory where each item in the list represents the name of an item,
# how much is in stock, and how much it costs. Print out each item in the list with the same formatting,
# using the .format method (not string concatenation).
# For example, the first print statment should read The store has 12 shoes, each for 29.99 USD.

inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]

for inv in inventory:
    item, stock, price = inv.split(", ")
    print("The store has {} {}, each for {} USD.".format(stock, item, price))
