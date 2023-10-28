def check_palindrome(word):
    start = 0
    end = len(word) - 1
    while start != end:
        if word[start] == word[end]:
            start += 1
            end -= 1
        else:
            print("not a palindrome")
            return
    print("palindrome")


check_palindrome("rotoor")
