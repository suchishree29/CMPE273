import psutil

myArray = []
pidArray = []
myFrequency = []

#print the header and extract required fields from net_connections function
print('"pid","laddr","raddr","status"')
for n in psutil.net_connections(kind='tcp'):
    pid = n.pid
    laddr = "%s@%s" % n.laddr
    #If raddr and pid are not empty, then proceed
    if n.raddr and pid :
        raddr = "%s@%s" % (n.raddr)
        myArray.append([pid,laddr,raddr,n.status])
        pidArray.append(pid)

#Sort the  final list with all required fields
mySortedarray = sorted(myArray)

#Count no. of times pid occurs in myFrequency list and add it to myset list.
myset = set()
for s in pidArray:
    if s not in myset:
        myFrequency.append([pidArray.count(s),s])
        myset.add(s)

#sort the list as per no. of processses in descending order
myCounts = sorted(myFrequency, reverse = True)

#match the pids in both the list and print the output
for m in myCounts:
    for s in mySortedarray:
        if m[1] == s[0]:
            #format the string with double quotes
            print '"%s","%s","%s","%s"' % (s[0], s[1],s[2],s[3])
