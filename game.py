f=input().split()
s=input().split()
t=input().split()
if (f[0]==f[1]==f[2]=='O' or s[0]==s[1]==s[2]=='O' or f[2]==s[2]==t[2]=='O' or t[0]==t[1]==t[2]=='O' or f[0]==s[0]==t[0]=='O' or f[1]==s[1]==t[1]=='O' or f[0]==s[1]==t[2]=='O' or f[2]==s[1]==t[0]=='O'):
     print('Abhinav Wins')
elif (f[0]==f[1]==f[2]=='X' or f[1]==s[1]==t[1]=='X' or t[0]==t[1]==t[2]=='X' or f[2]==s[2]==t[2]=='X' or f[0]==s[0]==t[0]=='X' or s[0]==s[1]==s[2]=='X' or f[0]==s[1]==t[2]=='X' or f[2]==s[1]==t[0]=='X'):
     print('Anjali Wins')
else:
    print("Tie") 
# input can be any random 3x3 pattern of 'O' and 'X'
