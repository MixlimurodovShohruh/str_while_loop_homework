def main(s):
    """
    A string of numbers is given. Find how many even digits there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    ans=0
    while i<=len(s)-1:
        if int(s[i])%2==0:
            ans+=1
        i+=1
    return ans

print(main('56786543250'))