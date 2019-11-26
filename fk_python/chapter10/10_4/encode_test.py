import json


s = json.dumps(['yeeku',{'favorite':('coding',None, 'game',25)}])

print(s)

s2 = json.dumps("\"foo\bar")
print(s2)

s3 = json.dumps('\\')
print(s3)

s4 = json.dumps({"c":0, "b": 0, "a": 0}, sort_keys=True)
print(s4)

s5 = json.dumps([1,2,3, {'x':5,'y':7}], separators=(',', ':'))
print(s5)

s6 = json.dumps({'Python':5, 'Kotlin': 7}, sort_keys=True, indent=4)
print(s6)

s7 =json.JSONEncoder().encode({"names": ("孙悟空", "齐天大圣")})
print(s7)
f = open('a.json', 'w' )
json.dump(['Kotlin',{'Python':'excellent'}],f)
