import matplotlib.pyplot as plt
l = [98, 183, 41, 122, 14, 124, 65, 67]     # points
h = 53                                      # header
rang = [0, 199]                             # range 


l.insert(0, h)
print(l)        # printing the list with header

n =len(l)
ff = [h]
ss = [h]
sc = [h]
csc  = [h]
lo = [h]
clo = [h]

def fcfs():
    global l, n, ff
    seek_time = 0
    print('\nFCFS:')
    for i in range(1, n):
        print('(', l[i], '-', l[i-1], ')', end = ' + ')
        seek_time += abs(l[i] - l[i-1])
        ff.append(l[i])
    print('\nSeek Time: ', seek_time)

def sstf():
    global l, n, ss
    li = [a for a in l]
    seek_time = 0
    print('\nSSTF:')
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
        ss.append(ele)
        if now in li:
            li.remove(now)
        now = ele
        
                
    print('\nSeek Time: ', seek_time, '\n')

def scan():
    global l, n, h, rang, sc
    li = [a for a in l]
    li.append(rang[1])
    li.sort()
    seek_time = 0
    print('\nSCAN:')
    ind = li.index(h)
    li = li[ind: ] + li[:ind][::-1]
    for i in range(0, n):
        print('(', li[i], '-', li[i+1], ')', end = ' + ')
        seek_time += abs(li[i] - li[i+1])
        sc.append(li[i+1])
    print('\nSeek Time: ', seek_time, '\n')

def cscan():
    global l, n, h, rang, csc
    li = [a for a in l]
    li.append(rang[0])
    li.append(rang[1])
    li.sort()
    seek_time = 0
    print('\nC-SCAN:')
    ind = li.index(h)
    li = li[ind: ] + li[:ind]
    for i in range(0, n+1):
        print('(', li[i], '-', li[i+1], ')', end = ' + ')
        seek_time += abs(li[i] - li[i+1])
        csc.append(li[i+1])
    print('\nSeek Time: ', seek_time, '\n')

def look():
    global l, n, h, rang, lo
    li = [a for a in l]
    li.sort()
    seek_time = 0
    print('\nLOOK:')
    ind = li.index(h)
    li = li[ind: ] + li[:ind][::-1]
    for i in range(0, n-1):
        print('(', li[i], '-', li[i+1], ')', end = ' + ')
        seek_time += abs(li[i] - li[i+1])
        lo.append(li[i+1])
    print('\nSeek Time: ', seek_time, '\n')

def clook():
    global l, n, h, rang, clo
    li = [a for a in l]
    li.sort()
    seek_time = 0
    print('C-LOOK:')
    ind = li.index(h)
    li = li[ind: ] + li[:ind]
    for i in range(0, n-1):
        print('(', li[i], '-', li[i+1], ')', end = ' + ')
        seek_time += abs(li[i] - li[i+1])
        clo.append(li[i+1])
    print('\nSeek Time: ', seek_time, '\n')

def plot():
    global n, ff, ss, sc, csc, lo, clo
    figure, axis = plt.subplots(3, 2)
    y = [-i for i in range(1, n+1)]
    y1 = [-i for i in range(1, n+2)]
    y2 = [-i for i in range(1, n+3)]
    
    # FCFS
    axis[0, 0].plot(ff, y)
    axis[0, 0].set_title("FCFS")
      
    # SSTF
    axis[0, 1].plot(ss, y)
    axis[0, 1].set_title("SSTF")
      
    # SCAN
    axis[1, 0].plot(sc, y1)
    axis[1, 0].set_title("SCAN")
      
    # C-SCAN
    axis[1, 1].plot(csc, y2) 
    axis[1, 1].set_title("C-SCAN")

    # LOOK
    axis[2, 0].plot(lo, y)
    axis[2, 0].set_title("LOOK")
      
    # C-LOOK
    axis[2, 1].plot(clo, y)
    axis[2, 1].set_title("C-LOOK")
    
    # Combine all the operations and display
    plt.show()

    
fcfs()
sstf()
scan()
cscan()
look()
clook()
plot()
