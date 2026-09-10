# Write a program to detech whether a comment is spam or not. A comment should be treated a spam if it contains any of the keywords:"Make a lot of money", "buy now","subscribe this", or "click this"
c=input("Enter ur comment: ")
if "Make a lot of money" in c or "buy now"in c or "subscribe this"  in c or "click this" in c:
    print("spam")
else:
    print("Not spam")    
