import sys
'''s='sawatiti'
n=len(s)
d={}

for x in s:
    if x not in d:
        d[x]=1
    else:
        d[x]=d[x]+1

#print(d,end="")
for k,v in d.items():
    print(k,">>>>",v)'''

# s="durga software"
# n=len(s)
# a=s.split()
# b=[]
# for x in a:
#     b.append(x[::-1])
#
# print(b)


# s="durga soft"
# n=len(s)
# i=-1
# while(i>=-n):
#     print(s[i],end="")
#     i=i-1

#
# s="durga soft slutions"
# a=s.split()
# b=[]
# n=len(a)-1
# while(n>=0):
#     b.append(a[n])
#     n=n-1
# print(b,end="")

# s="misshhiipplliioo"
# n=len(s)
# a={}
# for x in s:
#     if x not in a:
#         a[x]=1
#         #a.append(x)
#     else:
#         a[x]=a[x]+1
#
# print(a,end="")

# s="swati"
# i=1
# while(i<len(s)):
#     print(s[i],end="")
#     i=i+2

# s="s6v22p34"
# output=""
# output2=""
# for x in s:
#     if(x.isalpha()):
#         output=output+x
#     else:
#         output2=output2+x
#
# for x in sorted(output):
#     print(x,end="")
# for y in sorted(output2):
#     print(y,end="")

# s="a44b10c2"
# output=""
# for x in s:
#     if x.isalpha():
#         output=output+x
#         previous=x
#     else:
#         output=output+previous*(int(x)-1)
#
# print(output,end="")

# s="a4b3c5"
# output=""
# for x in s:
#     if x.isalpha():
#         output=output+x
#         previous=x
#     else:
#         output=output+chr(ord(previous)+int(x))
#
# print(output)
# s="swati"
# p="vishal"
# output=""
# i=j=0
# while (i<len(s) or (j<len(p))):
#     if(i<len(s)):
#         output=output+s[i]
#         i=i+1
#     if(j<len(p)):
#       output=output+p[j]
#       j=j+1
#
# print(output)


# while (i<len(s) or (j<len(p))):
#     output=output+s[i]+p[j]
#
#     i=i+1
#     j=j+1
#
# print(output)


# s="GLOBANT"
# n=len(s)
# i=0
# #print(s,end="")
# for x in s:
#     if(i<=len(s)):
#         print(s[i::1])
#         i=i-1
# n=6
# for i in range(1,n): #rows
#     for j in range(1,i+1): #stars
#         print("f ",end="")
#     # n=n-1
#     print()
#
#
# i=0
# s="FLEXTRADE"
# n = len(s)
# for x in s:
#     while(i<=len(s)):
#         print(s[:i:1])
#         i=i-1


#
# s="swati"
# i=0
# for x in s:
#     print("character at positive{} and negative{} is {}".format(i,-(len(s)-i),x))
#     i=i+1
#
# s="mississippi"
# a=[]
# d={}
# for x in s:
#     if x not in a:
#         a.append(x)
#         d[x]=1
#     else:
#         d[x]=d[x]+1
#
# print(a)
# for k,v in d.items():
#     print(k,">>>>>>>>",v)
#

# s=input("enter a string")
# sub=input("enter a substring")
#
# if sub in s:
#     print("present")
#
# else:
#     print("not present")
# s=input("enter a string")
# sub=input("enter a substring")
#
# if (s==sub):
#     print("equal")
# elif (s>sub):
#     print(" s greater")
# else:
#     print("sub is greater")

#
# s=input("enter a string")
# sub=input("enter a substring")
# pos=-1
# n=len(s)
# while True:
#     pos=s.rfind(sub,pos+1,n)
#     if (pos==-1):
#          break
#     print("found at ",pos)
#
#
# s=input("enter a string")
# sub=input("enter a substring")
# print(s.rindex(sub))
# #


# s= input("enter a alphanumeric string")
# n=len(s)
# i=0
#
# for x in s:
#         if s[0:5:1].isalpha() and s[6:9:1].isdigit() and s[9::1].isalpha():
#             print("it passes the cosing standards")
#             break
#         else:
#             print("invalid")
#             break
#
# s = input("enter a alphanumeric")
# n = len(s)
# i = 0
#
# if(len(s)==10):
#     print("valid input")
#
# for x in s:
#         if (i in range(0,3)):
#             if( (ord(s[i])) >= 97 and (ord(s[i])) <= 122):
#                 print(s[i],end="")
#             else:
#                 break
#             i=i+1
#         elif(i in range(3,5)):
#             if( (ord(s[i])) >= 48 and (ord(s[i])) <= 57):
#                 print(s[i],end="")
#             else:
#                 break
#             i=i+1
#         elif (i in range(5,7)):
#             if( (ord(s[i])) >= 97 and (ord(s[i])) <= 122):
#                 print(s[i],end="")
#
#             i=i+1
#         continue
#         # print("unsuccessfull")
#         # #sys.exit(0)
# else:
#     print("successfull")

[-]



























