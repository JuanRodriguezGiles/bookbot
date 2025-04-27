def get_num_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

def get_num_chars(text):
    words_lower = text.lower()
    chars_dic = {}
    for c in words_lower:
        if c in chars_dic:
            chars_dic[c] = chars_dic[c] + 1
        else:
            chars_dic[c] = 1
    return chars_dic

def sort_on(dict):
    return dict["num"]

def get_report(chars_dic):
    new_list = []
    for key in chars_dic:
        num = chars_dic[key]
        new_list.append({"char": key, "num": num})
    new_list.sort(reverse=True, key=sort_on)
    return new_list