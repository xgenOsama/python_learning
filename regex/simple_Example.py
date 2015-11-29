import re
# \s space character * any number of them ()group them
# print(re.split(r'(\s*)', 'here are some words'))
# \s \S no space \d digits \D not digits
# print(re.split(r'[a-f][a-f]', 'jflkAm,m,xczad;flertwdakFdaslkj', re.I|re.M))
# * = 0 or more | + = 1 or more | ? = 0 or 1 of ... | {5} exact number | {1,60} range of numbers
# . any character but new line

print(re.findall(r'\d{1,5}\s\w+\s\w+\.\w+', 'ocinwe12354 main st.sdfds'))
print(re.split(r'(\s*)', 'here are some words'))
