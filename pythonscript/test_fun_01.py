
##   encoding:utf-8

def swap(a,b):
    return (b,a)

##默认参数
def fun_arg(x=1,y='YY'):
    return "x:"+str(x)+","+"y:"+y

#a,b=('kara','yuch')
#a,b=swap(a,b)

#print a+"  "+b

#print fun_arg(2)
#print fun_arg(y='ZZ')
print fun_arg()