import facebook
import json
import test
print
print 
print 'Please copy and paste "https://www.facebook.com/login.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fexplorer%2F145634995501895%2F" into your browser, and log into Facebook.'
print
access_token=raw_input('Then, please select "Get Access Token">"Extended Permissions">"read_stream","publish_actions">"Get Access Token". Once you have done this, please copy and paste the Access Token here:    ')
print
print
print "Please wait while the program gets to know you a little better. This could take some time..."

def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

graph = facebook.GraphAPI(access_token)
feed = graph.get_object("me/feed", limit = 300)
next= int((str(feed["paging"]["next"]))[-10:])
feed2= graph.get_object("me/feed", limit = 300, until=next)
third= int((str(feed2["paging"]["next"]))[-10:])
feed3= graph.get_object("me/feed", limit = 300, until=third)



class Post():
    """object representing status update"""
    def __init__(self, UserData):
        if 'message' in UserData:
            self.message = UserData["message"]
        else:
            self.message = ""
        
        

list_instance=[]

def initiate_training(source, dest):
    for each in source:
        p=Post(each)
        dest.append(p)
        
initiate_training(feed['data'], list_instance)
initiate_training(feed2['data'], list_instance)
initiate_training(feed3['data'], list_instance)



           
def concat_all(L):
    res = ""
    for s in L:
        res = res + " " + s
    return res
    
#test.TestEqual(concat_all(['I','had','a','pretty','pony.'], 'I had a pretty pony.')
           
train_txt=[] 
for each in list_instance:
    train_txt.append(each.message)
    if each == '" "':
        train_txt.remove(each)



concatonated=concat_all(train_txt)
     
#print concatonated

def next_letter_frequencies(txt):
    r = {}
    for i in range(len(txt)-1): 
        if txt[i] not in r:
            r[txt[i]] = {}
        next_letter_freqs = r[txt[i]] 
        next_letter = txt[i+1]
        if next_letter not in next_letter_freqs:
            next_letter_freqs[next_letter] = 1
        else: 
            next_letter_freqs[next_letter] = next_letter_freqs[next_letter] + 1
    return r
    
#test.testEqual(type(next_letter_frequencies("Hello, my name is Chello"), type({}))
    
PersDict=next_letter_frequencies(concatonated)

#print pretty(PersDict)

def sorted_letters(counts):
    p=counts.items()
    y=sorted(p, key=lambda x: x[1], reverse= True)
    z=[(tup[0]) for tup in y] 
    return z
    
#test.testEqual(sorted_letters({'a':3,'r':6,'d':5}), ['r','d','a'])

SortedPersDict={}

for char in PersDict:
    v=sorted_letters(PersDict[char])
    SortedPersDict[char]=v
    
#print pretty(SortedPersDict)

print
print
print "This is a 'Next Letter Generator' that will try to guess the next character of your status after every letter you type." 
print
print "To accept the character offered to you, type 'y'."
print "To get another suggestion, simply hit enter."
print "To type the next character manually, type 'm'"
print "To erase a character, type 'DEL'."
print "When you're finished, type 'END'"
print
print

ultimate=''

user_input=raw_input("Type the letter you wish to begin your status with:   ")

ultimate=ultimate+user_input

while user_input != "end".upper():
    options=SortedPersDict[user_input]
    for char in options:
        print ultimate
        print
        current=raw_input("Would you like '"+str(char)+"' to be your next character?   ")
        if current == 'y':
            user_input=str(char)
            ultimate=ultimate+user_input
            break
        elif current == 'm':
            user_input=raw_input("Type the next letter of your post here:   ")
            ultimate=ultimate+user_input
            break
        elif current == 'del'.upper():
            ultimate=ultimate[:-1]
            user_input=ultimate[-1]
            break
        elif current == 'end'.upper:
            user_input='end'.upper
            break
print
print
print
print ultimate
print

post_status=raw_input("Thank you for using the 'Next Letter Generator'. If you would like to post your results to Facebook, please type 'Post'. If you would like to terminate the program, please hit enter.    ")

if post_status == 'Post':
    graph.put_object("me", "feed", message=ultimate+"""
    Posted via King Hufflepuff's kickass program""")
print
print 'TERMINATE PROGRAM'
print 
print '~*wu wuz hurr*~'
