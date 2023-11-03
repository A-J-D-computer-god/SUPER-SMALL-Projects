import random

p ="ROCK", 1
m ="PAPER", 2
k = "SISER", 3

asc = 0
bsc = 0

a = input("Enter your name")
b = input("enter your name")

for x in range(int(input("Times to play"))):
    Q = input("ROCK PAPER SISER!!!")
    W = str(random.randrange(1,4))

if W == p == Q or W==m==Q or W==k==Q:
    print("Draw")

if Q == "ROCK" and W==k:
      asc=asc+1

if Q == "PAPER" and W==k:
      bsc = bsc+1

if Q == "SISER" and W==p:
      bsc = bsc+1

if Q == "PAPER" and W==p:
      asc = asc+1

if Q ==" ROCK" and W==m:
    bsc=bsc+1

if Q == "SISER" and W==m:
    asc = asc+1

if asc == bsc:
    print("draw with: ", a, asc, "and :", b, bsc)
elif asc > bsc:
    print(a+" is WINNER WITH ", asc, " SCORE")
elif asc < bsc:
    print(b+" is WINNER WITH ", bsc, " SCORE")
