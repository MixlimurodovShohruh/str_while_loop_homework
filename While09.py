def main(s):
    """
    A string of numbers is given. Find the sum of all the digits and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
i=0
s=0
while i<len(s):
    x=s[i]
    s = s+s[i]
    i=i+1
    print(main('222525253'))