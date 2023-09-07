s1=(input("enter the first string: ")).lower()
s2=(input("enter the second string: ")).lower()
if(len(s1)>len(s2) or len(s1)<len(s2) ):
    print("Not Anagram")
else:
    list1 = list(s1)
    list2= list(s2)
    list1.sort()
    list2.sort()
    if(list1==list2):
        print("Anagram")
    else:
        print("Not Anagram")
