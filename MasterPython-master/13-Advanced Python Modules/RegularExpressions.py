# regular expressions are used for text pattern matching
import re

patterns = ['term1', 'term2']

text = 'This is the string with term1, but not with other term'

for pattern in patterns:
    print('searching for "%s" in : \n"%s"' % (pattern, text))
    # check for match
    if re.search(pattern, text):
        print('\n')
        print('match was found. \n')

    else:
        print('\n')
        print('match was not found. \n')
# lets use regular expression to split
split_term = '@'
phrase = 'What is your email, is it hello@gmail.com?'

print(re.split(split_term, phrase))  # list of two items before and after @ symbol
# find the matches ina string
print(re.findall('match', 'this is one match and this is the second match'))


# lets create a function that gives all the matches to a pttern

def match_re_find(patterns, phrase):
    '''
    Takes a list of regular expression patterns
    Prints list of all matches
    '''
    for pattern in patterns:
        print('searching the phrase using the re check:%s' % pattern)
        print(re.findall(pattern, phrase))
        print('\n')


test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'
test_patterns = ['sd*',  # s followed by zero or more d's\n",
                 'sd+',  # s followed by one or more d's\n",
                 'sd?',  # s followed by zero or one d's\n",
                 'sd{3}',  # s followed by three d's\n",
                 'sd{2,3}',  # s followed by two to three d's\n",
                 ]

match_re_find(test_patterns, test_phrase)
# lets take one more example
test_phrase = 'This is an example sentence. Lets see if we can find some letters.'
test_patterns = ['[a-z]+',  # sequences of lower case letters
                 '[A-Z]+',  # sequences of upper case letters
                 '[a-zA-Z]+',  # sequences of lower or upper case letters
                 '[A-Z][a-z]+'  # one upper case letter followed by lower case letters
                 ]
match_re_find(test_patterns, test_phrase)

# lets take an example with escape sequence
test_phrase = 'This is a string with some numbers 1233 and a symbol #hashtag'
test_patterns = [r'\d+',  # sequence of digits\n"
                 r'\D+',  # sequence of non-digits
                 r'\s+',  # sequence of whitespace
                 r'\S+',  # sequence of non-whitespace
                 r'\w+',  # alphanumeric characters
                 r'\W+',  # non-alphanumeric
                 ]
match_re_find(test_patterns, test_phrase)