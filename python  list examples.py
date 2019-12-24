# l=['10','20','30','40','50']
# n=len(l)
# print(n)
# i=0
# for x in l:
#     print("index at positive index {} and negative index {} is {}".format(i,-(n-i),x))
#     i=i+1

# # l1=[x for x in p if x%2==0]
# # print(l1)
#
# l=[x for x in range(1,101) if x%10==0]
# print(l)
# p=[10,20,30,40,50]
# y=[10,20,30,40,50]
# print(id(p))
# print(id(y))


# x=[[10,20,30],[40,50,60],[70,80,90]]
# for i in range(len(x)):
#     for j in range(len(x[i])):
#         print("|",x[i][j],"|",end=" ")
#     print()

#
# a=['worddddd','apple','boyyyyy ','cat']
# b=['word','appe','boyyyyy ','cat']
# print([[w.upper() ,len(w)] for w in a if w in b])

# print([w for w in a if len(w)>6])
# print ([ w[0] for w in a ])
#
# v=['a','e','i','o','u']
# word=input("enter a word")
# found={}
# for x in word:
#     if x in v:
#         if x not in found:
#            found[x]=1
#         else:
#             found[x]=found[x]+1
# print(found)

# t="swati"
# s=list(t)
# print(s)

#
# t=eval(input("enter a tuple"))
# sum=0
# avg=0
# for x in t:
#     sum=sum+x
#     avg=sum/len(t)
#
# print(sum,avg)
#
# s="the name is durga software"
# s2="durga software"
# p=set(s)
# p2=set(s2)
#
# print(p|p2)
# print(p&p2)
# print(p.difference(p2))
# print(p.symmetric_difference(p2))
# print(p.symmetric_difference_update(p2))
# s="the name s durga software"
# v={'a','e','i','o','u'}
#
# d=v.intersection(set(s))
# print(d)
#
# d={}
# i=0
# sum=0
# no=int(input("enter no of students"))
# while (i<=no):
#     name=input("enter name")
#     marks=int(input("enter marks"))
#     d[name]=marks
#     i=i+1
#
# for k,v in d.items():
#     print("names",k,">>>>  marks",v)
# for k in d.keys():
#     print(k)
# for v in d.values():
#     sum=sum+v
# print(sum)

#
# s="mississipppiim"
# d={}
#
# for x in s:
#     if x in d:
#         d[x]=d[x]+1
#     else:
#         d[x]=d.get(x,0)+1

#
# v={'a','e','i','o','u'}
# s="umbrella"
# d={}
# for x in s:
#      if x in v:
#          d[x]=d.get(x,0)+1
# for k,v in d.items():
#     print(k,">>>",v)
#
#
# print({x:x**x for x in range(1,11)})
# print([x for x in range(1,15) if x%2==1
#        ])

#
# t=(100,600,900,500)
# print(min(t))
# print(max(t))
# a=[]
# l=[100,200,300,400,900,100,300,]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#             if l[i] < l[j]:
#                 l[i], l[j] = l[j], l[i]
#
# print (l)

# fact=6
#
# sum=1
# while(fact>0):
#     sum=sum*fact
#     fact=fact-1
# print(sum)

#
#
# s="123456"
# b=list(s)
# print(b)
# n=len(b)-1
# while(n>0):
#     print(b[n],end="")
#     n=n-1
#
#
# a=1235621
# s=str(a)
# a=list(s)
# b=[]
# n=len(a)-1
# while(n>=0):
#     b.append(a[n])
#     n=n-1
# print(a,">>>>",b)
# if a==b:
#     print("palindrome")
# else:
#     print("not an pallindrome")

#
# fib=5
# i=0
# a=0
# b=1
# while (i<=fib):
#     temp=a
#     a=b
#     b=temp+b
#     print(b)
#     i=i-1

# l=[0,1]
# c=int(input("enter the length of teh series"))
#
# l.extend((l[x-1]+l[x-2])  for x in range(2,c))
#
# print(l[0:c])
#
#
# l=[1,4,7,1,2,10,2,10]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if(l[i]>l[j]):
#             temp=l[i]
#             l[i]=l[j]
#             l[j]=temp
#
# print(l)
# k=[]
# for x in l:
#     if x not in k:
#         k.append(x)
# print(k)

class toooldexception(Exception):
    def __init__(self,args):
        self.arg=args


class tooyoungexception(Exception):
    def __init__(self,args):
        self.arg=args


n=int(input("enter the age"))
if n >60:
    raise ValueError("too old")
else:
    raise ValueError("too young")

























