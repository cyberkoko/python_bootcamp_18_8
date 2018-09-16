import re

post_code_pattern = re.compile('\d(2)-\d(3)')
email_pattern = re.compile('\w.-1+@r\.w+')
datas_pattern = re.compile('\d(1,2) \w(3) \d(4)')


with open("input.txt") as f:
    tekst = f.read()
    kody = post_code_pattern.findall(tekst)
    emails = email_pattern.findall(tekst)
    dates = datas_pattern.findall(tekst)
    print(kody)
    print(emails)
    print(dates)

