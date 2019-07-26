import re
randStr = "14125551212 4125551212 (412)5551212 412 555 1212 412-555-1212 1-412-555-1212" 
regex = re.compile(r"((1?)(-| ?)(\()?(\d{3})(\)|-| |\)-|\) )?(\d{3})(-| )?(\d{4}|\d{4}))")
matches = re.findall(regex, randStr)
print(len(matches))
for i in matches:
    print(i[0].lstrip())