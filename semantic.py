import spacy

#nlp = spacy.load('en_core_web_md')
nlp = spacy.load('en_core_web_sm')

# first code extract from notes 
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word2.similarity(word3))
print(word1.similarity(word3))

# second code extract from notes 

def word_comparison(tokens): 
    for token1 in tokens:
        for token2 in tokens:
            similarity = round(token1.similarity(token2) * 100, 1)
            print(f"{token1.text}, {token2.text}, {similarity}%")

token_example = nlp('cat apple monkey banana')
word_comparison(token_example)

# For the above comparison, it is interesting that cat and monkey are closely associated, 
# them being more closely associated than monkey and banana, which are two things that 
# are closely associated as when monkeys are portrayed on tv, in documentaries and cartoons 
# it would not be uncommon to see a monkey eating a banana. 
# It is understandable that cat and banana are not too closely associated as cats don't 
# eat bananas (as far as I'm aware), and cats are animals and bananas are fruits.  

# my own word comparison
token_my_example = nlp('house skyscraper shack')
word_comparison(token_my_example)

# the model judges a house to be as similar to a skyscaper as a shack, which to me seems 
# quite different.

# third code extract from notes - comparing sentences 

sentence_to_compare = "Why is my cat on the car"

sentences = ["Where did my dog go", 
"Hello, there is my car", 
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    similarity = round(similarity * 100, 0) 
    print(f"{sentence} - {similarity}%")


# en_core_web_md vs en_core_web_sm 
#
# When I run the above code using en_core_web_sm, I get a user warning which tells me that the 
# sm model has no word vectors loaded, which means that it may not give useful similarity judgements 
# I notice this when I look at the similarity percentages. For example, cat and apple are much more 
# closely associated in the sm model, and cat is more closely associated to apple than to 
# monkey or than moneky is to banana. Which is not the case in the md model. 
