def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    num_word = get_num_word(text)
    num_letter = get_num_letter(text)
    sorted_num_letter = sort_dict(num_letter)
    generate_report(sorted_num_letter,num_word,book_path)
    return

def generate_report(list,word_count,book_path):
    print(f"-- Begin Report of {book_path} --")
    print(f"-- Total words {word_count} --")
    for item in list:
        print(f"the {item["letter"]} appeared {item["num"]} times")
    print("--End Report--")
    
def sort_on(dict):
    return dict["num"]

def sort_dict(letter_dict : dict[str,int]):
    list_dict = []
    for letter in letter_dict:
        if letter.isalpha():
            item = {"letter": letter, "num" : letter_dict[letter]}
            list_dict.append(item)
    list_dict.sort(reverse = True , key=sort_on)
    return list_dict

def get_num_letter(text: str)->dict[str,int]:
    num_letter = {}
    text = text.lower()
    for letter in text:
        if letter in num_letter:
            num_letter[letter] += 1
        else:
            num_letter[letter] = 1
    return num_letter

def get_num_word(text: str) -> int:
    words = text.split()
    return len(words)

def get_text(file: str) -> str:
    with open(file) as f:
       return f.read()
        
main()