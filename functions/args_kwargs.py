def demo(*args,**kwargs):
    print(args)
    print(kwargs)


demo(10,True,"ok",name="java",price=1000)

# key value pairs go to kwargs, others go to args
# args is a tuple, kwargs is a dictionary