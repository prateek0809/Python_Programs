def count_substring(string, sub_string):
    m = len(string)
    n = len(sub_string)
    c = 0

    for i in range(m - n + 1):

        j = 0
        while(j < n):
            if(string[i+j] != sub_string[j]):
                break
            j += 1
        if(j == n):
            c += 1
            j = 0
    return c        

if __name__ == '__main__':
    string = input("Enetr the string:").strip()
    sub_string = input("Enter the sub-string:").strip()
    
    count = count_substring(string, sub_string)
    print(count)