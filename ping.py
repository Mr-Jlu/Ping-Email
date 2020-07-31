from io import StringIO
from ping3 import ping, verbose_ping
import os
import csv
import sys
up_down = ['𝗨𝗣','𝗗𝗢𝗪𝗡']
ISP_names = ['IP Address 01','IP Address 02','Test-Down IP Address']
result = []
greeting = "Hello Sir/Madam, \n"
temp_rest = []


def ping(hostname):
    
    old_stdout = sys.stdout
    result = StringIO()
    sys.stdout = result
    verbose_ping(dest_addr=hostname, count=2)
    sys.stdout = old_stdout
    result_string = result.getvalue()
    pingStatus = 'ok';
    
    if (result_string.find('Timeout') != -1):
        pingStatus = 'timed_out'
    print(pingStatus)
    return pingStatus
#endDef    


def printPingResult(hostname):
    statusOfPing = ping(hostname)
    if (statusOfPing == 'ok') :
        status_output = ISP+' ( '+hostname+' ) is '+up_down[0]
    else:
        status_output = ISP+' ( '+hostname+' ) is '+up_down[1]
    return status_output
    
def writeToFile(filename, data) :
    with open(filename, 'w') as output:
        output.write(data + '\n')

def appendToFile(filename, data) :
    with open(filename, 'a') as output:
        output.write(data + '\n')


file = open('/storage/emulated/0/Ping&Email/hosts.txt')
writeToFile('/storage/emulated/0/Ping&Email/result.txt', greeting)

try:
    reader = csv.reader(file)
    for ISP in ISP_names:
        for item in reader:
            result = printPingResult(item[0].strip())
            appendToFile('/storage/emulated/0/Ping&Email/result.txt', result)
            break
        #endFor
    
finally:
    file.close()
    #qpy:qpyapp  
#endTry