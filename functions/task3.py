# args-->(100,True,20,20.89,100,"java",90.90)

# ans = {
#     'int':[100,20,100],
#     float:[],
#     str:[]
#     boolean:[True]
# }

def ans(*args):
    return {
        'int': [i for i in args if type(i).__name__ == 'int'],
        'float': [i for i in args if type(i).__name__ == 'float'],
        'str': [i for i in args if type(i).__name__ == 'str'],
        'boolean': [i for i in args if type(i).__name__ == 'bool']
    }

print(ans(100, True, 20, 20.89, 100, "java", 90.90, "C", False, "Python"))
    
