# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    x = filename + ".txt"
    z = open(x, "r")
    print(z.read())

    return z


read_file_content("story")

"""this function read the text contained in “story.txt”. 
and  return a dictionary whose keys are unique words, and their values the count of those words in the text"""


def word_count():
    storyfile = open("story.txt", "r")
    one = storyfile.read()

    counts = dict()
    words = one.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    print()
    print()
    print(counts)
    return counts


word_count()


