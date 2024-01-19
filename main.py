def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    knew = get_chars_dict(text)
    generate_report(knew)

    
    
def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def generate_report(dictionary):
    new_list = []
    print("--- Begin report of books/frankenstein.txt ---") 
    print("77986 words found in the document")
    print(" ")
    for x in dictionary:
        if x.isalpha():
             t = x,dictionary[x]
             new_list.append(t)
    new_list.sort(key = lambda tup: tup[1], reverse=True )
    for y in new_list:
        print(f"The {y[0]} was found {y[1]} times")
    print(" ")
    print("--- End of report ---")


          
             

main()
