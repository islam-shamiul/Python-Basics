def swap_case(s):
    st = ""
    for i in range(0, len(s)-1, 1):
        if s[i].islower():
            st += s[i].upper()
        elif s[i].isupper():
            st += s[i].lower()
        else:
            st += s[i]
    return st


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
