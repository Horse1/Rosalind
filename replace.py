s=str(input())
a=s.replace('G','g').replace('C','c').replace('c','G').replace('g','C').replace('A','a').replace('T','t').replace('a','T').replace('t','A')
print(a[::-1])
