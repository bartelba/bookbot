def get_num_words(text):
    num_of_words_found = 0
    words_found = text.split(' ', -1)
    for word in words_found:
        if str.isspace(word):
            None
        else:
            num_of_words_found += 1
    return num_of_words_found

def num_of_each_character(text):
    char_dict = {}
    charaters = list(text)
    for char in charaters:
        if char.isalpha():
            lower_char = char.lower()
            char_dict[lower_char] = char_dict.get(lower_char, 0) + 1    
    sorted_dict = {}
    for key in sorted(char_dict, key=char_dict.get, reverse=True):
        sorted_dict[key] = char_dict[key]
    return sorted_dict