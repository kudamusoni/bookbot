def get_word_count(text):
    word_arr = text.split()
    return len(word_arr)

def get_count_of_characters(text):
    arr = {}
    for char in list(text):
        if char.lower() in arr:
            arr[char.lower()] += 1
        else:
            arr[char.lower()] = 1
    return arr

def get_num(dictionary):
    return dictionary["num"]

def character_report(chars):
    arr = []
    for char in chars:
        arr.append({
            "char": char,
            "num": chars[char]
        })
    arr.sort(key=get_num, reverse=True)
    return arr
    