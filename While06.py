def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    i=0
    ans=0
    s=s.upper()
    while i<len(s):
    
        if s[i]!="a" and s[i]!="e" and s[i]!="i" and s[i]!="o" and s[i]!="u" and s[i].isalpha():
            ans+=1
        i+=1
    return ans
    
print(main("asdf852ghujk54445h4545l"))