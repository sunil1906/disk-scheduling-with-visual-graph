l = [98, 183, 41, 122, 14, 124, 65, 67]
h = 53
rang = [0, 199]


l.insert(0, h)
print(l)
n =len(l)

def fcfs():
    global l, n
    seek_time = 0
    print('FCFS:')
    for i in range(1, n):
        print('(', l[i], '-', l[i-1], ')', end = ' + ')
        seek_time += abs(l[i] - l[i-1])
    print('\nSeek Time: ', seek_time)

def sstf():
    global l, n
    li = [a for a in l]
    seek_time = 0
    print('SSTF:')
    now = li[0]
    li.remove(li[0])
    for i in range(n-1):
        small = 10000000
        ele = -1
        for j in li:
            if (abs(now - j) < small and now - j):
                small = abs(now - j)
                ele = j

        print('(', now, '-', ele, ')', end = ' + ')
        seek_time += abs(now - ele)
        if now in li:
            li.remove(now)
        now = ele
        
                
    print('\nSeek Time: ', seek_time, '\n')

def scan():
    global l, n, h, rang
    li = [a for a in l]
    li.append(rang[1])
    li.sort()
    seek_time = 0
    print('SCAN:')
    ind = li.index(h)
    li = li[ind: ] + li[:ind][::-1]
    for i in range(0, n):
        print('(', li[i], '-', li[i+1], ')', end = ' + ')
        seek_time += abs(li[i] - li[i+1])
    print('\nSeek Time: ', seek_time, '\n')

def cscan():
    global l, n, h, rang
    li = [a for a in l]
    li.append(rang[0])
    li.append(rang[1])
    li.sort()
    seek_time = 0
    print('C-SCAN:')
    ind = li.index(h)
    li = li[ind: ] + li[:ind]
    for i in range(0, n+1):
        print('(', li[i], '-', li[i+1], ')', end = ' + ')
        seek_time += abs(li[i] - li[i+1])
    print('\nSeek Time: ', seek_time, '\n')

def look():
    global l, n, h, rang
    li = [a for a in l]
    li.sort()
    seek_time = 0
    print('LOOK:')
    ind = li.index(h)
    li = li[ind: ] + li[:ind][::-1]
    for i in range(0, n-1):
        print('(', li[i], '-', li[i+1], ')', end = ' + ')
        seek_time += abs(li[i] - li[i+1])
    print('\nSeek Time: ', seek_time, '\n')

def clook():
    global l, n, h, rang
    li = [a for a in l]
    li.sort()
    seek_time = 0
    print('C-LOOK:')
    ind = li.index(h)
    li = li[ind: ] + li[:ind]
    for i in range(0, n-1):
        print('(', li[i], '-', li[i+1], ')', end = ' + ')
        seek_time += abs(li[i] - li[i+1])
    print('\nSeek Time: ', seek_time, '\n')


fcfs()
sstf()
scan()
cscan()
look()
clook()
