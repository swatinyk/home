# import pytest
# import pytest_html
# import pytest_ordering
# #import pytest-xdist
# import selenium
# import fileinput
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.action_chains import ActionChains
# driver=webdriver.Chrome()
# @pytest.fixture()
# @pytest.mark.run(order=1)
# def test_browser_search():
#     driver.maximize_window()
#     driver.get("https://testautomationpractice.blogspot.com/")
#
#
# @pytest.mark.run(order=2)
# def test_draganddrop(test_browser_search):
#     source=driver.find_element_by_xpath("//*[contains(text(),'Drag me to my target')]")
#     target=driver.find_element_by_xpath("//*[contains(text(),'Drop here')]")
#     actions=ActionChains(driver)
#     actions.drag_and_drop(source,target).perform()
#
# @pytest.mark.run(order=3)
# def test_slider(test_browser_search):
#     slider=driver.find_element_by_id("slider")
#     slidersize=slider.size
#     print(slidersize)
#     p=slidersize['width']
#     action=ActionChains(driver)
#     action.drag_and_drop_by_offset(slider,0,600000).perform()
#
# @pytest.mark.run(order=4)
# def test_scroll(test_browser_search):
#     #driver.switch_to.frame("frame-one1434677811")
#     # d=driver.find_element_by_xpath("//*[@id='post-body-1307673142697428135']/div[1]/select/option[3]")
#     # driver.execute_script("arguments[0].scrollIntoView();",d)
#     driver.execute_script("window.scrollBy(0,1500)","")
#
#     #driver.switch_to.frame("frame-one1434677811")
#     d=driver.find_element_by_css_selector("select.contains('CSS')")
#     d.click()
#     # driver.execute_script("arguments[0].scrollIntoView();",d)
#
# @pytest.mark.run(order=5)
# def test_booktable(test_browser_search):
#     d=driver.find_element_by_xpath("//table[@name='BookTable']")
#     rows=driver.find_elements_by_xpath("//table[@name='BookTable']/tbody/tr")
#     print(len(rows))
#     r=len(rows)
#     col =driver.find_elements_by_xpath("//table[@name='BookTable']/tbody/tr[1]/th")
#     print(len(col))
#     c=len(col)
#     before="//table[@name='BookTable']/tbody/tr["
#     after="]/td["
#     againafter="]"
#     for i in range(2,r+1):
#         for j in range(1,c+1):
#             p=driver.find_element_by_xpath(before+str(i)+after+str(j)+againafter).text
#             print(p,end=" ")
#             f=open("webdata.txt","a")
#             f.write(p)
#             # if p=="Master In Java":
#             #     ele=driver.find_element_by_xpath(before+str(i)+after+str(4)+againafter).text
#             #     print(ele)
#             #     break
#         print()
#     f.close()
#




# s='selenieiem'
# n=len(s)
# d={}
# for i in s[::1]:
#     if i=='e':
#         d[i]=d.get(i,0)+1
#         s=d[i]
#         print("@"*s,end="")
#     else:
#         print(i,end="")

# s='selenieiem'
# n=len(s)
# d={}
#
# for i in s[::1]:
#     if i not in d:
#         d[i]=d.get(i,0)+1
#     else:
#         d[i]=d[i]+1
#
# print(d)




# for i in range(1,9):
#     if s[i]&s[i+1] not in d:
#         d[i]=d.get(i,0)+1
#     else:
#         d[i]+d[2]=1
#


# print(s[0],end='')
#
# for i in range(1,8):
#     if i>1 and i%2==0:
#         print(" ",s[i],end="")
#         print(s[i])
#
#     else:
#         print(s[i],end="")



# import sys
# class Student:
#     count = 0
#     def __init__(self):
#         self.count = self.count + 1
#         print(self.count)
# s1=Student()
# s4=s1
# s2=Student()
# s3=Student()
# print(sys.getrefcount(s1))
# # print("The number of students:",Student.count)
#


# Months = {"January","February", "March", "April", "May", "June"}
# print("\nprinting the original set ... ")
# print(Months)
# print("\nAdding other months to the set...");
# Months.add("July");
# Months.add("August");
# print("\nPrinting the modified set...");
# print(Months)
# print("\nlooping through the set elements ... ")
# for i in Months:
#     print(i)
#
# s=(10,[1,2,3,4])
# t=s
# print(t)
# print(s)
# p=t[0]
# p.append("g")
# print(t)
# print(s)

# Days1 = {"Monday",  "Tuesday", "Wednesday", "Thursday"}
# Days2 = {"Monday", "Tuesday", "Sunday"}
# print(Days1.difference_update(Days2)) #{"Wednesday", "Thursday" will be printed}
# print(Days1)
# print(Days2)

# l={1,2,3}
# l.add(6)
#
# print(l)
#
# s='26/05/2019'
# s1=s.split("/",2)
# print(s1)

#s="HCL electronic city banglore"
# s1=s.split(" ")
# for i in s1:
#     print(i,end="")
#
# for i in s:
#     if i.isspace():
#         pass
#     else:
#         print(i,end="")




#####swatiii
####pawar
p=[1,3,5,7,9]
q=[2,4,6,8,0,0]
t=[1,1,1,1,1,1]
x=[2222,3333]
s=[10,15,20,30,40,50,45]
max=min=s[0]
first=second=0
for i in s:
    if i>max:
        max=i

    if i<min:
        min=i
Max=max
Min=min
print("maximum",max,"minimum",min)
for j in s:
    if j<max:
        if(j==min):
            continue
        max=j

print("second min",max)
for j in s:
        if j>Min:

            if(j==Max):
                continue
            Min=j
print("second max",Min)


S='VISHAL'
n=len(S)
i=n-1
while -i <=0:
    print(S[i])
    i=i-9















































