def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_count = dict()
    for ch in text:
        ch = ch.lower()
        if ch in char_count:
            char_count[ch] += 1
        else:
            char_count[ch] = 1
    return char_count

def sorted_chars(char_dict):
    char_list = []
    for key, value in char_dict.items():
        char_list.append(dict(char=key,num=value))
    def sort_on(items):
        return items["num"]
    char_list.sort(reverse=True,key=sort_on)
    return char_list