from stats import word_count, char_count, sort_dict
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  
def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
        #print(text)
        return text
        
def main():
    book_content = get_book_text(f"{sys.argv[1]}")
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    num_words = word_count(book_content)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    num_chars = char_count(book_content)
    char_sort_list = sort_dict(num_chars)
    for item in char_sort_list:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")
    #print(f"{char_sort_list}")
    print("============= END ===============")
    
    
main()
