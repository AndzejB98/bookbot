def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def get_num_words(filepath):
    dict_result = {}
    dict_list = []

    result = get_book_text(filepath)
    words = result.split()
    words_count = len(result.split())
    for char in result:
        has_character = char.lower() in dict_result
        if has_character == False:
            dict_result[char.lower()] = 1
        else:
            dict_result[char.lower()] += 1
    
    for key, value in dict_result.items():
        dict_list.append({"char": key, "num": value})
    dict_list.sort(key=lambda item: item["num"], reverse=True)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at", {filepath})
    print("----------- Word Count ----------")
    print(f"Found", words_count, "total words")
    print("--------- Character Count -------")
    for item in dict_list:
        key = item["char"]
        value = item["num"]
        key_is_alpha = key.isalpha()
        if key_is_alpha == True:
            print(f"{key}: {value}")
    print("============= END ===============")