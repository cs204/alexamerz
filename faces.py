def main ():
    s = input()
    s= convert(s)
    print (s)

def convert (s):
    s2 = s.replace (":)", "\N{Slightly smiling Face}")
    s3 = s2.replace (":(", "\N{Slightly frowning Face}")
    return s3


main()