# n = int(input())
# x = n + 1
# for i in range(x):
#     for j in range(i):
#         char = ord('A') + x + (j-1)
#         print(chr(char),end="")
#     x -= 1
#     print()

# n = int(input())
# x = n
# for i in range(n):
#     for j in range(1 , x+1):
#         print(j, end="")
#     x -= 1
#     print()


# from sys import stdin
#
#
# def isPermutation(a, b):
#     if len(a)==len(b):
#         s1 = []
#         s2 = []
#         for i in a:
#             s1.append(i)
#         for x in b:
#             s2.append(x)
#         s1.sort()
#         s2.sort()
#         if s1 == s2:
#             return True
#         else:
#             return False
#     else:
#         return False
#
#
# string1 = stdin.readline().strip()
# string2 = stdin.readline().strip()
#
# ans = isPermutation(string1, string2)
#
# if ans:
#     print('true')
# else:
#     print('false')


# from sys import stdin
#
#
# def removeConsecutiveDuplicates(string):
#     list = []
#     x = string[0]
#     list.append(x)
#     for i in string[1:]:
#         if i == x:
#             continue
#         else:
#             list.append(i)
#         x = i
#     y = ""
#     for b in list:
#       y = y + b
#     return y
#
#
# string = stdin.readline().strip()
#
# ans = removeConsecutiveDuplicates(string)
#
# print(ans)

#
# from sys import stdin
#
#
# def highestOccuringChar(string):
#     hchar = string[0]
#     hcount = 0
#     for i in string:
#         v = string.count(i)
#         if v > hcount:
#             hcount = v
#             hchar = i
#     return hchar
#
# string = stdin.readline().strip()
# ans = highestOccuringChar(string)
#
# print(ans)

# n = int(input())
# for i in range(n):
#     print(" "*(n-i-1),end="")
#     for j in range(i+1,i*2+2):
#         print(j, end ="")
#         if j == (i*2+1):
#             for v in range(j,i+1,-1):
#                 print(v-1, end="")
#             break
#     print()

# n = int(input())
# for i in range(1, n+1,2):
#     print(" "*((n-i)//2),end="")
#     for j in range(i):
#         print("*",end="")
#     print()
# for i in range(n-2,0,-2):
#     print(" " * ((n - i) // 2), end="")
#     for j in range(i):
#         print("*",end="")
#     print()


# n = int(input())
# for i in range(n):
#     print(" "*(n-i-1),end="")
#     for j in range(i+1,0,-1):
#         print(j,end="")
#         if j == 1:
#             for v in range(j,i+1):
#                 print(v+1,end="")
#     print()


# from sys import stdin


# def binarySearch(arr, n, x):
#     a = 0
#     for i in range(a, n):
#         middle = int(((n - 1) - a) // 2)
#         if arr[i] == x:
#             return i
#         elif arr[i] > x:
#             a = middle
#         elif arr[i] < x:
#             n = middle
#         else:
#             return -1
#     return -1
#
#
# # Taking Input Using Fast I/O
# def takeInput():
#     n = int(stdin.readline().strip())
#
#     if n == 0:
#         return list(), 0
#
#     arr = list(map(int, stdin.readline().strip().split(" ")))
#     return arr, n
#
#
# # main
# arr, n = takeInput()
# t = int(stdin.readline().strip())
#
# while t > 0:
#     x = int(input().strip())
#     print(binarySearch(arr, n, x))
#
#     t -= 1


# n = int(input())
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j, end="")
#     print(" "*((n-i)*2), end="")
#     for j in range(i,0,-1):
#         print(j, end="")
#     print()


# n = int(input())
# for i in range(n):
#     print(("0" * i) + "*" + ("0"*(n-i-1)) + "*" + ("0"*(n-i-1)) + "*" + ("0"*i), end="")
#     print()


# n = int(input())
# for i in range(1,n+1):
#     print(" "*(i-1),end="")
#     for j in range(i,n+1):
#         print(j, end="")
#     print()
# for i in range(n-1,0,-1):
#     print(" "*(i-1),end="")
#     for j in range(i,n+1):
#         print(j, end="")
#     print()

# n = int(input())
# a = n
# for i in range(a):
#     for j in range(n, a, -1):
#         print(j, end="")
#     for k in range((a*2)-1):
#         print(a, end="")
#     for l in range((n-i+1), n+1):
#         print(l, end="")
#     a -= 1
#     print()
# a = 2
# for i in range(n-1):
#     for j in range(n, a, -1):
#         print(j, end="")
#     for k in range((a*2)-1):
#         print(a, end="")
#     for l in range(a+1, n+1):
#         print(l, end="")
#     a += 1
#     print()


# n = int(input())
# a = 1
# if n == 2:
#     print(1, 2)
#     print(3, 4)
#     exit()
# elif n == 1:
#     print(1)
#     exit()
# if n % 2 == 0:
#     x = 4
# else:
#     x = 3
#
# while a <= (n*n):
#     for j in range(n):
#         print(a, end=" ")
#         if a < (n*n+1):
#             a += 1
#     print()
#     if a == (((n*n)-n)+1):
#         continue
#     else:
#         a += n
# a -= (n*x)
# while a != ((n*2)+1):
#     for j in range(n):
#         print(a, end=" ")
#         a += 1
#     if a != ((n*2)+1):
#         a -= (n*3)
#     print()

# from sys import stdin
#
#
# def pushZerosAtEnd(arr, n):
#     nlist = []
#     count0 = 0
#     for i in range(n):
#         if arr[i] != 0:
#             nlist.append(arr[i])
#     count0 = len(arr) - len(nlist)
#     zlist = []
#     while count0 > 0:
#         zlist.append(0)
#         count0 -= 1
#     flist = nlist + zlist
#     return flist
#
#
# # Taking Input Using Fast I/O
# def takeInput():
#     n = int(stdin.readline().rstrip())
#
#     if n == 0:
#         return list(), 0
#
#     arr = list(map(int, stdin.readline().rstrip().split()))
#     return arr, n
#
#
# # to print the array/list
# def printList(arr, n):
#     for i in range(n):
#         print(arr[i], end=" ")
#
#     print()
#
#
# # main
# t = int(stdin.readline().strip())
#
# while t > 0:
#     arr, n = takeInput()
#
#     pushZerosAtEnd(arr, n)
#     printList(pushZerosAtEnd(arr, n), n)
#
#     t -= 1


"""
    In order to print two or more integers in a line separated by a single
    space then you may consider printing it with the statement,

    print(str(num1) + " " + str(num2))
    Take Minimum value as MIN_VALUE = -2147483648

"""

# from sys import stdin
#
#
# def findLargest(arr, nRows, mCols):
#     csumlist = []
#     for b in range(mCols):
#         a = 0
#         for i in arr:
#             for j in i:
#                 a += i[b]
#                 break
#         csumlist.append(a)
#
#     rsumlist = []
#     for i in arr:
#         a = 0
#         for j in i:
#             a += j
#         rsumlist.append(a)
#
#     bigc = 0
#     ccount = -1
#     for i in csumlist:
#         if i > bigc:
#             bigc = i
#             ccount += 1
#
#     bigr = 0
#     rcount = -1
#     for i in rsumlist:
#         if i > bigr:
#             bigr = i
#             rcount += 1
#
#     if nRows == 0:
#         rcount = 0
#         bigr = -2147483648
#     if mCols == 0:
#         ccount = 0
#         bigc = -2147483648
#     if bigc > bigr:
#         print("column " + str(ccount) + " " + str(bigc))
#     elif bigr >= bigc:
#         print("row " + str(rcount) + " " + str(bigr))
#
#
# # Taking Input Using Fast I/O
# def take2DInput():
#     li = stdin.readline().rstrip().split(" ")
#     nRows = int(li[0])
#     mCols = int(li[1])
#
#     if nRows == 0:
#         return list(), 0, 0
#
#     mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
#     return mat, nRows, mCols
#
#
# # main
# t = int(stdin.readline().rstrip())
#
# while t > 0:
#     mat, nRows, mCols = take2DInput()
#     findLargest(mat, nRows, mCols)
#
#     t -= 1


# '''
#     In order to print two or more integers in a line separated by a single
#     space then you may consider printing it with the statement,
#
#     print(str(num1) + " " + str(num2))
#     Take Minimum value as MIN_VALUE = -2147483648
#
# '''
#
# from sys import stdin
# MIN_VALUE = -2147483648
#
#
# def findLargest(arr, nRows, mCols):
#     isRow = True
#     bigt = MIN_VALUE
#     num = 0
#     for i in range(nRows):
#         bigr = 0
#         for j in range(mCols):
#             bigr += arr[i][j]
#         if bigr > bigt:
#             bigt = bigr
#             num = i
#     for j in range(mCols):
#         bigc = 0
#         for i in range(nRows):
#             bigc += arr[i][j]
#         if bigc > bigt:
#             bigt = bigc
#             num = j
#             isRow = False
#     if isRow:
#         print("row "+str(num)+" "+str(bigt))
#     else:
#         print("column "+str(num)+" "+str(bigt))
#
#
# #Taking Input Using Fast I/O
# def take2DInput():
#     li = stdin.readline().rstrip().split(" ")
#     nRows = int(li[0])
#     mCols = int(li[1])
#
#     if nRows == 0:
#         return list(), 0, 0
#
#     mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
#     return mat, nRows, mCols
#
#
# #main
# t = int(stdin.readline().rstrip())
#
# while t > 0:
#
#     mat, nRows, mCols = take2DInput()
#     findLargest(mat, nRows, mCols)
#
#     t -= 1

# from sys import stdin
#
#
# def sumOfTwoArrays(arr1, n, arr2, m, output):
#     x, y = arr1, arr2
#     if len(x) > len(y):
#         z = len(x) - len(y)
#         for i in range(z):
#             y.insert(0, 0)
#     else:
#         z = len(y) - len(x)
#         for i in range(z):
#             x.insert(0, 0)
#
#     temp = 0
#     sum = []
#     for i in range(len(x) - 1, -1, -1):
#         if x[i] + y[i] + temp >= 10:
#             sum.insert(0, (x[i] + y[i] + temp) - 10)
#             temp = 1
#         else:
#             sum.insert(0, (x[i] + y[i] + temp))
#             temp = 0
#     if temp == 1:
#         sum.insert(0, 1)
#         return sum
#     else:
#         if m == 0 or n == 0:
#             sum.insert(0, 0)
#             return sum
#         sum.insert(0, 0)
#         return sum
#
#
# # Taking Input Using Fast I/O
# def takeInput():
#     n = int(stdin.readline().rstrip())
#     if n == 0:
#         return list(), 0
#
#     arr = list(map(int, stdin.readline().rstrip().split(" ")))
#     return arr, n
#
#
# # main
# t = int(stdin.readline().rstrip())
#
# while t > 0:
#     arr1, n = takeInput()
#     arr2, m = takeInput()
#
#     outputSize = (1 + max(n, m))
#     output = outputSize * [1]
#
#     for i in sumOfTwoArrays(arr1, n, arr2, m, output):
#         print(i, end=" ")
#     print()
#
#     t -= 1

# from sys import stdin
#
#
# def spiralPrint(mat, nRows, mCols):
#     k = 0
#     l = 0
#     while (k < nRows and l < mCols):
#         for i in range(l, mCols):
#             print(mat[k][i], end=" ")
#         k += 1
#         for i in range(k, nRows):
#             print(mat[i][mCols - 1], end=" ")
#         mCols -= 1
#         if (k < nRows):
#             for i in range(mCols - 1, (l - 1), -1):
#                 print(mat[nRows - 1][i], end=" ")
#             nRows -= 1
#         if (l < mCols):
#             for i in range(nRows - 1, k - 1, -1):
#                 print(mat[i][l], end=" ")
#             l += 1
#
# # Taking Input Using Fast I/O
# def take2DInput():
#     li = stdin.readline().rstrip().split(" ")
#     nRows = int(li[0])
#     mCols = int(li[1])
#
#     if nRows == 0:
#         return list(), 0, 0
#
#     mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
#     return mat, nRows, mCols
#
#
# # main
# t = int(stdin.readline().rstrip())
#
# while t > 0:
#     mat, nRows, mCols = take2DInput()
#     spiralPrint(mat, nRows, mCols)
#     print()
#
#     t -= 1


# n=int(input())
# l=input().split()
# b = []
# for i in l:
#     b.append(int(i))
# max=b[-1]
# b=b[::-1]
# k=[b[0]]
# for i in range(1,n):
#     if b[i]>=max:
#         max=b[i]
#         k.append(b[i])
# k=k[::-1]
# print(*k)
#
#
# s=input().split()
# l=[]
# for i in s:
#     l.append(len(i))
# b = min(l)
# out = s[l.index(b)]
# print(out)
#
#
# n = input().split()
# row = int(n[0])
# col = int(n[-1])
# overall = []
# for i in range(row):
#     temp = input().split()
#     rowin = []
#     for j in temp:
#         rowin.append(int(j))
#     overall.append(rowin)
#
# for k in range(row):
#     for l in range(row - k):
#         fin = overall[k]
#         print(*fin)


# i = int(input())
# f = int(input())
#
# for j in range(i,f+1):
#     count = 0
#     for k in range(1,j+1):
#         if j % k == 0:
#             count += 1
#     if count == 2:
#         print(j)


# i = int(input())
# f = int(input())
#
# while i <= f:
#     count = 0
#     v = 1
#     while v <= i:
#         if i % v == 0:
#             count += 1
#         v += 1
#     if count == 2:
#         print(i)
#     i += 1


# n = input()
# length = 0
# for i in n:
#     length += 1
# v = 0
# for i in n:
#     v += (int(i) ** length)
# n = int(n)
# if v == n:
#     print("This is an armstrong number")
# else:
#     print("This is not an armstrong number")


# n = input()
# length = len(n)
# a = int(n)
# x = 1
# sum = 0
# while x <= len(n):
#     b = a // (10**(length-1))
#     a -= b*(10**(length - 1))
#     sum += (b**len(n))
#     length -= 1
#     x += 1
# if str(sum) == n:
#     print("true")
# else:
#     print("false")

# n = input()
# length = len(n)
# a = int(n)
# sum = 0
# sum += (a % 10)**(length)
# a = a // 10
# sum += (a % 10)**(length)
# a = a // 10
# sum += (a % 10)**length
# if str(sum) == n:
#     print("true")
# else:
#     print("false")


# num = int(input())
# sum = 0
# temp1 = num
# temp2 = num
# length = 0
# while temp2 > 0:
#     length += 1
#     temp2 //= 10
# while temp1 > 0:
#     digit = temp1 % 10
#     sum += digit ** length
#     temp1 //= 10
# if num == sum:
#     print("true")
# else:
#     print("false")


# def fib(num):
#     fiblist = [1]
#     a = 0
#     b = 1
#     while fiblist[-1] < num:
#         c = a + b
#         fiblist.append(c)
#         a = b
#         b = c
#     fiblist.pop()
#     return fiblist
#
#
# N = int(input())
# print(fib(N))


# def fib(num):
#     fiblist = [1]
#     a = 0
#     b = 1
#     while (num-1) > 0:
#         c = a + b
#         fiblist.append(c)
#         a = b
#         b = c
#         num -= 1
#     return fiblist
#
#
# N = int(input())
# print(fib(N))


# n = int(input())
# i = 0
# j = 0
# while i < n:
#     while j < n:
#         print("*", end="")
#         j += 1
#     j = 0
#     i += 1
#     print()

# n = int(input())
# for i in range(n-1):
#     print("*"*(n-i-1), end="")
#     for j in range(1,i+2):
#         print(" ", end="")
#     for k in range(i,0,-1):
#         print(" ", end="")
#     print("*" * (n - i - 1), end="")
#     print()
# for i in range(n-3,-1,-1):
#     print("*" * (n - i - 1), end="")
#     for j in range(1, i + 2):
#         print(" ", end="")
#     for k in range(i, 0, -1):
#         print(" ", end="")
#     print("*" * (n - i - 1), end="")
#     print()

# a = [1,1,1,2,2,1,1,3,5,5,4]
# a.sort()
# c = a[0]
# for i in a[1:]:
#     if i == c:
#         a.pop(i)
#     c = i
# print(a)

# n = int(input())
# i = 2
# while i <= n:
#     a = 2
#     count = 0
#     while a <= i:
#         if i % a == 0:
#             count += 1
#         a += 1
#     if count == 1:
#         print(i)
#     i += 1

# i = int(input())
# a = 2
# count = 0
# while a <= i:
#     if i % a == 0:
#         count += 1
#     a += 1
# if count == 1:
#     print("prime")
# else:
#     print("composite")

# li = []
# el = int(input())
# for i in range(el):
#     dat = int(input())
#     li.append(dat)
# for i in range(el):
#     if i % 2 == 0:
#         print(li[i])


# li = input().split()
# for i in range(len(li)):
#     if i % 2 == 0:
#         print(li[i])

# li = input().split()
# a = li[::-1]
# print(a)


# li = input().split()
# min = int(li[0])
# for i in li:
#     if int(i) < min:
#         min = int(i)
# print(min)

# li = input().split()
# upd = [int(li[-1])]
# for i in li[:-1]:
#     upd.append(int(i))
# print(upd)

# str = input()
# l = str.split()
# rem = input()
# l.remove(rem)
# print(*l)


# a = [10,20,30,40]
# b = [5,10, 10,25,20]
# c = [0]
# for i in a:
#     for j in b:
#         if i == j:
#             if c[-1] != i:
#                 c.append(i)
# c.remove(0)
# print(c)

# str = input()
# l = str.split("a")
# rem = input()
# l.remove(rem)
# for i in l:
#     print(i, end=" ")


# str = input()
# map = ["Jan","Feb","Mar","Apr","May","June","July","Aug","Sept","Oct","Nov","Dec"]
# temp = str.split("/")
# a = int(temp[0])
# print(map[a-1], temp[1], ",", temp[2])


# sentence = input()
# temp = sentence.split()
# for i in range(len(temp)):
#     temp[i] = temp[i].capitalize()
# print(*temp)

# study from interviewbit.com

# from turtle import *
# while True:
#     color("red")
#     begin_fill()
#     pensize(3)
#     left(50)
#     forward(133)
#     circle(50, 200)
#     right(140)
#     circle(50, 200)
#     forward(133)
#     end_fill()


# h = int(input())
# n,a,c = h,0,True
# b = h*h
# forward,backward = [],[]
# while n<=b:
#     if c == True:
#         l1 = []
#         for i in range(a+1, n + 1):
#             l1.append(i)
#         forward.append(l1)
#         n,a,c = n+h,a+h,False
#     else:
#         l2 = []
#         for i in range(a+1, n + 1):
#             l2.append(i)
#         backward.append(l2)
#         n,a,c = n+h,a+h,True
# for i in forward:
#     print(*i)
# for j in backward[::-1]:
#     print(*j)


# n = int(input())
# l1 = []
# for i in range(n):
#     l1.append(int(input()))
# b = tuple(l1)
# c = l1
# a = c[0]
# c.sort()
# for i in c[1:]:
#     if i == a:
#         c.remove(i)
#     else:
#         a = i
# for i in c:
#     print(i, end=" ")
#     print(b.count(i))

# n = int(input())
# a = 2
# b = 1
# for i in range(1,n+3,2):
#     for k in range(2 * n, 0, -3):
#         print(" ", end="")
#     for j in range(i):
#         print(a+b, end=" ")
#         a = a+b
#         b += 2
#     print()
#
# a = [[(i,j) for j in range(5)] for i in range(4)]
# print(a)
#
# rows = int(input("enter the rows - "))
# cols = int(input("enter the column - "))
# print("enter the first matrix - ")
# mat1 = [[(int(input("Enter the element " + str(i) + " " + str(j) + " - "))) for j in range(cols)] for i in range(rows)]
# print("enter the second matrix - ")
# mat2 = [[(int(input("Enter the element " + str(i) + " " + str(j) + " - "))) for j in range(cols)] for i in range(rows)]
#
# out = []
# for i in range(rows):
#     l1 = []
#     for j in range(cols):
#         l1.append(mat1[i][j] + mat2[i][j])
#     out.append(l1)
# print(out)
#
# *******************************************MATRIX MULTIPLICATION*****************************************************
# rows = int(input("enter the rows - "))
# cols = int(input("enter the column - "))
# print("enter the first matrix - ")
# mat1 = [[(int(input("Enter the element " + str(i) + " " + str(j) + " - "))) for j in range(cols)] for i in range(rows)]
# print(mat1)
# print("enter the second matrix - ")
# mat2 = [[(int(input("Enter the element " + str(i) + " " + str(j) + " - "))) for j in range(cols)] for i in range(rows)]
# print(mat2)
# out = []
# for i in range(rows):
#     l1 = []
#     for j in range(cols):
#         sum = 0
#         for k in range(cols):
#             sum += mat1[i][k]*mat2[k][j]
#         l1.append(sum)
#     out.append(l1)
# for i in out:
#     print(*i)



# **************************************************SUM OF ROWS*********************************************************

# rows = int(input("enter the rows - "))
# cols = int(input("enter the column - "))
# print("enter the matrix - ")
# mat1 = [[(int(input("Enter the element " + str(i) + " " + str(j) + " - "))) for j in range(cols)] for i in range(rows)]
# print(mat1)
# out = []
# for i in range(rows):
#     sum = 0
#     for j in range(cols):
#         sum += mat1[i][j]
#     out.append(sum)
# print(out)

# **************************************************SUM OF COLUMNS******************************************************

# rows = int(input("enter the rows - "))
# cols = int(input("enter the column - "))
# print("enter the matrix - ")
# mat1 = [[(int(input("Enter the element " + str(i) + " " + str(j) + " - "))) for j in range(cols)] for i in range(rows)]
# print(mat1)
# out = []
# for i in range(rows):
#     sum = 0
#     for j in range(cols):
#         sum += mat1[j][i]
#     out.append(sum)
# print(out)

# ***********************************************PRODUCT OF ROWS********************************************************

# rows = int(input("enter the rows - "))
# cols = int(input("enter the column - "))
# print("enter the matrix - ")
# mat1 = [[(int(input("Enter the element " + str(i) + " " + str(j) + " - "))) for j in range(cols)] for i in range(rows)]
# print(mat1)
# out = []
# for i in range(rows):
#     product = 1
#     for j in range(cols):
#         product *= mat1[i][j]
#     out.append(product)
# print(out)

# ********************************************PRODUCT OF COLUMNS********************************************************

# rows = int(input("enter the rows - "))
# cols = int(input("enter the column - "))
# print("enter the matrix - ")
# mat1 = [[(int(input("Enter the element " + str(i) + " " + str(j) + " - "))) for j in range(cols)] for i in range(rows)]
# print(mat1)
# out = []
# for i in range(rows):
#     product = 1
#     for j in range(cols):
#         product *= mat1[j][i]
#     out.append(product)
# print(out)

# *******************************************TRANSPOSE OF A MATRIX******************************************************

# rows = int(input("enter the rows - "))
# cols = int(input("enter the column - "))
# print("enter the matrix - ")
# mat1 = [[(int(input("Enter the element " + str(i) + " " + str(j) + " - "))) for j in range(cols)] for i in range(rows)]
# print(mat1)
# mat2 = [[ 0 for j in range(cols)] for i in range(rows)]
# for i in range(rows):
#     for j in range(cols):
#         mat2[j][i] = mat1[i][j]
# print(mat2)

# import numpy as np
# rows = int(input("enter the rows - "))
# cols = int(input("enter the column - "))
# a = np.array([[(int(input("Enter the element " + str(i) + " " + str(j) + " - "))) for j in range(cols)] for i in range(rows)])
# b = np.array([[(int(input("Enter the element " + str(i) + " " + str(j) + " - "))) for j in range(cols)] for i in range(rows)])
# c = a + b
# print(c)

# n = int(input())
# mat1 = [[0 for j in range(n)] for i in range(n)]
#
# for i in range(n):
#     for j in range(n):
#         if i < j:
#             mat1[i][j] = 0
#         elif i == j:
#             mat1[i][j] = 1
#         elif i > j:
#             mat1[i][j] = 2
# print(mat1)

# n = int(input())
# mat1 = [[0 for j in range(n)] for i in range(n)]
#
# for i in range(n):
#     for j in range(n):
#         if i + j < n-1:
#             mat1[i][j] = 0
#         elif i + j == n-1:
#             mat1[i][j] = 1
#         else:
#             mat1[i][j] = 2
# print(mat1)


# rows = int(input())
# cols = int(input())
# mat1 = [[(int(input("Enter the element " + str(i) + " " + str(j) + " - "))) for j in range(cols)] for i in range(rows)]
# col1 = int(input())
# col2 = int(input())
# for i in range(rows):
#     for j in range(cols):
#         if j == col2:
#             temp = mat1[i][j]
#             mat1[i][j] = mat1[i][col1]
#             mat1[i][col1] = temp
# print(mat1)


# x = input()
# c = x[-1] + x[1:-1] + x[0]
# print(c)


# x = input()
# c = x[1:] + x[0]
# print(c)

# x = input()
# c = x[::-1]
# print(c)


# word = input()
# for i in range(len(word)+1):
#     x =""
#     for j in range(i,len(word)):
#         x += word[j]
#     for z in range(0,i):
#         x+=word[z]
#     print(x)


# x = input()
# c = x[::-1]
# if x == c:
#     print("The word is a palindrome")
# else:
#     print("The word is not a palindrome")



# x = int(input())
# y = int(input())
# l1 = []
# l2 = []
# i = 1
# while i <= x:
#     if x % i == 0:
#         l1.append(i)
#     i += 1
# i = 1
# while i <= y:
#     if y % i == 0:
#         l2.append(i)
#     i += 1
# a = 0
# common = []
# while a < len(l1):
#     b = 0
#     while b < len(l2):
#         if l1[a] == l2[b]:
#             common.append(l1[a])
#         b += 1
#     a += 1
# print(max(common))


# s = "how are you"
# s = s[::-1]
# s = s.split(" ",1)
# for i in range(len(s)):
#     s[i]= s[i][::-1]
# s.reverse()
# print(s)


# word = input()
# for i in range(len(word)+1):
#     x =""
#     for j in range(i,len(word)):
#         x += word[j]
#     for z in range(0,i):
#         x+=word[z]
#     print(x)


# a = [(10,20,40),(40,50,60),(70,80,90)]
# for i in range(len(a)):
#     a[i] = list(a[i])
# for i in a:
#     i[-1] = 100
# for i in range(len(a)):
#     a[i] = tuple(a[i])
# print(a)

# a = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# i = 0
# while len(a[i]) == 0:
#     i += 1
#     for j in a:
#         if len(j) == 0:
#             a.remove(j)
#             i = 0
# print(a)


# a = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
# userinput = input()
# out = False
# for i in a:
#     for j in i:
#         if j == userinput:
#             out = True
#             print(out)
#             exit()
#         else:
#             out = False
# print(out)


# n = int(input())
# for i in range(n):
#     for j in range(i):
#         print(1**j,end= " ")
#     print(2 ** i, end=" ")
#     if i != n-1:
#         print()
#     if i != n-1:
#         print()

# rows = int(input())
# columns = int(input())
# n = [[int(input()) for j in range(columns)] for i in range(rows)]
# print(n)



# n = int(input())
# list1 = []
# for i in range(n):
#     list1.append(int(input()))
# list1 = set(list1)
#
# list2 = []
# for i in range(1,n+1):
#     list2.append(i)
# list2 = set(list2)
#
# out = list2-list1
# out = list(out)
# print(out)


# n = int(input())
# init = input().split()
# fin = []
# for i in range(n):
#     temp = []
#     for j in init[i::n]:
#         temp.append(j)
#     fin.append(temp)
# print(fin)

# n = int(input())
# a = 0
# b = 1
# for i in range(n):
#     if i == 1:
#         print(i)
#     else:
#         x = a+b
#         a = b
#         b = x
#         print(x)


# arr = input().split()
# for i in range(len(arr)):
#     arr[i] = int(arr[i])
# n = len(arr)
# for i in range(n):
#     min = i
#     for j in range(i + 1, n):
#         if arr[j] < arr[min]:
#             min = j
#     arr[i], arr[min] = arr[min], arr[i]
# print(arr)


# def sayhello(username):
#     greet = "Hello "
#     global users
#     users = ["Ram", "Mahesh", "Vasudha", "Uma",  "Sekhar", "John"]
#     for i in username:
#         z = greet + i
#         print(z)
# users = ["Ram", "Mahesh", "Vasudha", "Uma",  "Sekhar", "John"]
# sayhello(users)





# def intput(a):
#     try:
#         b = int(a)
#         return b
#     except:
#         print("Enter integer value only.")
# a = input()
# print(intput(a))
#
#


# PRIME PALINDROME NUMBER:
# n = int(input("n: "))
#
#
# def prime(n):
#     i = 1
#     count = 0
#     while(i <= n):
#         if n % i == 0:
#             count = count + 1
#         i = i + 1
#     if count == 2:
#         return 1
#     else:
#         return 0
#
#
# def palindrome(n):
#     rev = 0
#     orig = n
#     while(n > 0):
#         rev = rev * 10 + (n % 10)
#         n = n // 10
#     if orig == rev:
#         return 1
#     else:
#         return 0
#
#
# if prime(n) and palindrome(n):
#     print("True!")
# else:
#     print("False!")


# def fib(a,b):
#     c = a + b
#     fiblist.append(c)
#     a = b
#     b = c
#     if fiblist[-1] < n:
#         return fib(a,b)
#     else:
#         fiblist.pop()
#         return fiblist
#
#
# n = int(input())
# fiblist = [1]
# a = 0
# b = 1
# print(fib(a,b))


# def printrange(a,b):
#     if a != b:
#         print(a)
#         return printrange(a+1,b)
#
#
# a = int(input("Enter starting number-"))
# b = int(input("Enter Ending number - "))
# printrange(a,b)


# number = int(input("Enter dob in format DD/MM/YYYY - "))
# year = number % 10000
# number //= 10000
# month = number % 100
# number //= 100
# date = number
#
# print(f"{date}-{month}-{year}")


# def calculate_factorial(n,ans):
#     if n==1 or n==0:
#         return ans
#     else:
#         return calculate_factorial(n-1, ans*n)
#
# print(calculate_factorial(5,1))

