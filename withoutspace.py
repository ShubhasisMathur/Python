def smallest(s):
 
    l = len(s)
    ans = ""
 
    # iterate the string
    for i in range (l-1):
 
        # first point where s[i]>s[i+1]
        if (s[i] > s[i + 1]):
 
            # append the string without
            # i-th character in it
            for j in range (l):
                if (i != j):
                    ans += s[j]
             
            return ans
 
    # leave the last character
    ans = s[0: l - 1]
    return ans
 
# Driver Code
if __name__ == "__main__":
 
    s = "abcdd"
 
    print (smallest(s))