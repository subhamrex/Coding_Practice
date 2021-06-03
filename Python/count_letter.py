import pprint # for preety print
messege='''A newly initialized Chatterbot instance starts off with no knowledge of how to communicate. To allow it to properly respond to user inputs, the instance needs to be trained to understand how conversations flow. Since Chatterbot relies on machine learning at its backend, it can very easily be taught conversations by providing it with datasets of conversations.'''
count={}
for chr in messege:
    count.setdefault(chr,0)
    count[chr] = count[chr] + 1
# x=pprint.pformat(count)    #use pprint.pformat to get output as string value
# print(x)
pprint.pprint(count)