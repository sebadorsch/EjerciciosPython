def generate_hashtag(s):
    if not s:
        return False
    words = s.split(" ")
    resultado = "#"
    for x in words:
        resultado = resultado + x.capitalize()
    if len(resultado) < 141:
        return resultado
    else:
        return False


if __name__ == '__main__':

    print(generate_hashtag('codewars is nice'), '#CodewarsIsNice', 'Should capitalize first letters of words.')

    print(generate_hashtag(''), False, 'Expected an empty string to return False')    
    print(generate_hashtag('Do We have A Hashtag')[0], '#', 'Expeted a Hashtag (#) at the beginning.')
    print(generate_hashtag('Codewars'), '#Codewars', 'Should handle a single word.')
    print(generate_hashtag('Codewars      '), '#Codewars', 'Should handle trailing whitespace.')
    print(generate_hashtag('Codewars Is Nice'), '#CodewarsIsNice', 'Should remove spaces.')
    
    print(generate_hashtag('CodeWars is nice'), '#CodewarsIsNice', 'Should capitalize all letters of words - all lower case but the first.')
    print(generate_hashtag('c i n'), '#CIN', 'Should capitalize first letters of words even when single letters.')
    print(generate_hashtag('codewars  is  nice'), '#CodewarsIsNice', 'Should deal with unnecessary middle spaces.')
    print(generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'), False, 'Should return False if the final word is longer than 140 chars.')
