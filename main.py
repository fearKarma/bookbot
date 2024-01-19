def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    knew = get_chars_dict(text)
    report = generate_report(knew)


    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for i in report:
        if not i[0].isalpha():
            continue
        print(f"the {i[0]} character was found {i[1]} times")
    
    print()
    print("--- End report ---")

    
    
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
    for x in dictionary:
        t = x,dictionary[x]
        new_list.append(t)
    new_list.sort(key = lambda tup: tup[1], reverse=True )

    return new_list


          
             

main()
