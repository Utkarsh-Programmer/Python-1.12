# Problem 7
# write a program to find out whether a given post is talking about “Harry” or not.

post = "Welcome to the World of Python Harry!"

if "Harry".lower() in post.lower():
    print("This post is talking about Harry.")
else:
    print("This post is about something else.")


# NOTE: `lower` method converts the string to lowercase.
