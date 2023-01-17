def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd digits.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    ans=0
    while i<=len(s)-1:
        if int(s[i])%2!=0:
         ans+=int(s[i])
        i+=1
        
    return ans
print(main('98421'))