def is_palindrome(str):
    if len(str) in (0,1):
        return True
    
    iters = len(str)//2

    for i in range(iters):
        if str[i] != str[-i-1]:
            return False
    return True

def builtin(str):
    if str == str[::-1]:
        return True
    else:
        return False
    
if __name__ == "__main__":
    test_strings = ["", "a", "aa", "abc", "abcba"]
    for str in test_strings:
        print(str, end=" ")
        print(f"is_palindrom says: {is_palindrome(str)} builtin says:{builtin(str)}")