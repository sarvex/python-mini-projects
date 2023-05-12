from textblob import TextBlob    # importing textblob library

t = 1
while t:
    a = input("Enter the word to be checked:- ")	 # incorrect spelling
    print(f"original text: {str(a)}")

    b = TextBlob(a)  #correcting the text

    # prints the corrected spelling
    print(f"corrected text: {str(b.correct())}")
    t = int(input("Try Again? 1 : 0 "))
