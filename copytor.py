''''Homework 1-copytor.py:
Write a function called copy, which takes in a file name and a new file name and copies the contents of the first file into the second file.
Note: we've provided you with the first chapter of Alice's Adventures in Wonderland to give you some sample text to work with. This is also the text used in the tests.
copy('story.txt', 'story_copy.txt) # None
expect the contents of story.txt and story_copy.txt to be the same'''

# First, create the source file with the content
with open("story.txt", 'w') as file:
    file.write('Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: \n')
    file.write('once or twice she had peeped into the book her sister was reading,\n')
    file.write('but it had no pictures or conversations in it,\n')
    file.write('and what is the use of a book,thought Alice, without pictures or conversations \n')
    file.write('continue next week')
    print("source file:", file)

# Then use the copy function 
def copy(source_filename, target_filename):
    with open(source_filename, 'r') as source:
        content = source.read()
        with open(target_filename, 'w') as target:
            target.write(content)

# Test the copy function
copy('story.txt', 'story_copy.txt')

# Verify the contents
with open('story.txt', 'r') as file:
    print("\nOriginal file content:")
    print(file.read())
    
with open('story_copy.txt', 'r') as file:
    print("\nCopied file content:")
    print(file.read())
