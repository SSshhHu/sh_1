def reverse(x:int)->int:
    if x>0:
        a = str(x)
    else:
        a = str(-x)+'-'
    a = int(a[::-1])

    return a if a <=2**31-1 and a >=-2**31-1 else 0##整数溢出就返回0

if __name__ == '__main__':
    b = int(input("请输入一个数字，我们将返回这个数字的反转值："))
    
    print(reverse(b))
## 这里也可以定义一个类，class solution。
## 类的使用方法：