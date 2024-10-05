#file_contents = ""
def main():
    with open("books/frankenstein.txt") as f:
        print(f"--- Begin report of books/frankenstein.txt ---")
        file_contents = f.read()
        words = file_contents.split()
        numbers = count_words(words)
        print(f"This book contains: {numbers}")
        print("")
        count_characters(file_contents)
        print(f"--- End Report ---")
        
        
def count_words(words):
    counter = 0
    for i in words:
        counter += 1
    return counter

def count_characters(text):
    dict_character = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0,"ß":0,}
    text = text.lower()

    """value = dict_character["a"]
    value += 1"""
    for i in text:
        if i in dict_character:
            value = dict_character[f"{i}"]
            value += 1
            dict_character[f"{i}"] = value
        else:
            pass

    for i in dict_character:
        print(f"the character {i} was found {dict_character[i]} times.")


main()