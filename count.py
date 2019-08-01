
# from string import punctuation
# from operator import itemgetter

# N = 10
# words = {}

# words_gen = (word.strip(punctuation).lower() for line in open("test1.txt") 
#                                              for word in line.split())
                                          
# for word in words_gen:
#     words[word] = words.get(word, 0) + 1

# top_words = sorted(words.iteritems(), key=itemgetter(1), reverse=True)[:N]

# for word, frequency in top_words:
#     print "%s: %d" % (word, frequency)


# from string import punctuation

# def sort_items(x, y):
#     """Sort by value first, and by key (reverted) second."""
#     return cmp(x[1], y[1]) or cmp(y[0], x[0])

# N = 10
# words = {}

# words_gen = (word.strip(punctuation).lower() for line in open("test1.txt") 
#                                              for word in line.split())
                                          
# for word in words_gen:
#     words[word] = words.get(word, 0) + 1

# top_words = sorted(words.iteritems(), cmp=sort_items, reverse=True)[:N]

# for word, frequency in top_words:
#     print "%s: %d" % (word, frequency)
# from string import punctuation

# N = 10
# words = {}

# words_gen = (word.strip(punctuation).lower() for line in open("test1.txt") 
#                                              for word in line.split())
                                          
# for word in words_gen:
#     words[word] = words.get(word, 0) + 1

# top_words = sorted(words.iteritems(), 
#                    cmp=lambda x, y: cmp(x[1], y[1]) or cmp(y[0], x[0]), 
#                    reverse=True)[:N]

# for word, frequency in top_words:
#     print "%s: %d" % (word, frequency)

from string import punctuation

N = 10
words = {}

words_gen = (word.strip(punctuation).lower() for line in open("test1.txt")
                                             for word in line.split())

for word in words_gen:
    words[word] = words.get(word, 0) + 1

top_words = sorted(words.iteritems(), 
                   key=lambda(word, count): (-count, word))[:N] 

for word, frequency in top_words:
    print "%s: %d" % (word, frequency)

# import urllib
# import operator
# txtFile = urllib.urlopen("test1.txt").readlines()
# txtFile = " ".join(txtFile) # this with .readlines() replaces new lines with spaces
# txtFile = "".join(char for char in txtFile if char.isalnum() or char.isspace()) # removes everything that's not alphanumeric or spaces.

# word_counter = {}
# for word in txtFile.split(" "): # split in every space.
#     if len(word) > 0 and word != '\r\n':
#         if word not in word_counter: # if 'word' not in word_counter, add it, and set value to 1
#             word_counter[word] = 1
#         else:
#             word_counter[word] += 1 # if 'word' already in word_counter, increment it by 1

# for i,word in enumerate(sorted(word_counter,key=word_counter.get,reverse=True)[:10]):
#     # sorts the dict by the values, from top to botton, takes the 10 top items,
#     print "%s: %s - %s"%(i+1,word,word_counter[word])

