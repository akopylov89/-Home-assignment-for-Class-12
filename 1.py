def autocomplete(string, list_of_words):
    string_formatted = ''
    output_list = []
    for letter in string:
        if letter.isalpha():
            string_formatted+=letter
    for word in list_of_words:
        word_of_list_formatted = ''
        for letter in word:
            if letter.isalpha():
                word_of_list_formatted += letter
        if len(output_list) < 5:
            if word_of_list_formatted.lower().startswith(string_formatted.lower()):
                output_list.append(word)
        else:
            break
    return output_list

if __name__ == '__main__':
    string = '///1A6743bc'
    list_of_words = ['6347456998;;;;;Abccdg', '324264545ab///C','aBc123', 'rabc', '1abc','abc1234567890','abcabNNNc','/nabc//n','abc567','abc345','abc999']
    print(autocomplete(string,list_of_words))