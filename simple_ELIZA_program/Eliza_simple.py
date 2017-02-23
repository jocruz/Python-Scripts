
import random

def longestWord (sentence):
    words = sentence.split()

    longest = 0
    i = 1

    while i < len(words):
        if len(words[i]) > len(words[longest]):
            longest = i
        i = i + 1

    return words[longest]

def nextResponse (word):
   
    # one based on the user input
    replies = ["OMG ", "LOL ", "You don't say. ", "Is that so? ", "I see. "]
    replyType = random.randint(1, 10)

    if replyType <= 3: # 30% of the time, reply randomly
        rep = random.randint(1, 5) # choose a random element from 'replies'
        return replies[rep]

    # Otherwise, reply normally...
    if len(word) == 4:
        return "Tell me more about " + word + " "
    elif len(word) == 5:
        return "Why do you think " + word + " is important? "
    elif len(word) >= 6:
        return "Now we are getting somewhere. How does " + word + " affect you the most? "
    else:
        return "Maybe we should move on. Is there something else you would like to talk about? "

def main():
    prompt = "What would you like to talk about? "
    answer = input(prompt)

    while answer != "Goodbye":
        if "you" in answer:
            prompt = "I'm not important. Let's talk about you instead. "
        else:
            topic = longestWord(answer)
            prompt = nextResponse(topic)
        answer = input(prompt)

    print("Thank you for chatting with me.")

main()
