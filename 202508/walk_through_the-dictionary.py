favourite_languages={
    'sam': 'C',
    'alice': 'Python',
    'bob': 'Java',
    'david':'C++'
}
a=favourite_languages.items()
print(a)
for k,v in favourite_languages.items():
    print('\nkey:'+k)
    print('value:'+v)
print('**************************************')
for k in favourite_languages.keys():
    print('\nkey:'+k)
    print('value:'+favourite_languages[k])
print('**************************************')
for k in favourite_languages:
    print('\n'+k)
print('**************************************')
a=list(favourite_languages.keys())
print(a[0])
