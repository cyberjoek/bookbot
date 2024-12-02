def getbook(book_name):
    book_url = "books/" + book_name + ".txt"
    file_contents = ""
    with open(book_url) as f:
        file_contents = f.read()
    return file_contents

def sort_on(dict):
    return dict["num"]

def wordcount(text_to_check):
    words = text_to_check.split()
    return len(words)

def lettercount(text_to_check):
    lowered_text = text_to_check.lower()
    letter_counts = dict()
    letter_list = []
    for l in lowered_text:
        if l.isalpha():
            if l in letter_counts:
                letter_counts[l] += 1
            else:
                letter_counts[l] = 1
    for letter in letter_counts:
        temp = dict()
        temp["name"] = letter
        temp["num"] = letter_counts[letter]
        letter_list.append(temp)
    letter_list.sort(reverse=True, key=sort_on)
    return letter_list
    

def main():
    whichbook = "frankenstein"
    book1 = getbook(whichbook)
    word_count = wordcount(book1)
    letter_counts = lettercount(book1)
    print(f"--- Begin report of Books/{whichbook}.txt ---")
    print(f"{word_count} words found in the document")
    print("")
    for letter in letter_counts:
#        print(letter)
        cnt = letter["num"]
        ltr = letter["name"]
        print(f"The character '{ltr}' was found {cnt} times")
    print("--- End report ---")
#    print(letter_counts)

main()