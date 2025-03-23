import socket
import psutil

print("Name of the computer: ", socket.gethostname())
hostname = socket.gethostname()
print()
print("IP-address: ",socket.gethostbyname_ex(hostname)[2][1])
print()
def get_ram_info():
    ram = psutil.virtual_memory()
    total_ram = ram.total #Total RAM installed
    available_ram = ram.available #Available RAM for prosesses
    used_ram = ram.used #Used RAM
    free_ram = ram.free 
    percent_used = ram.percent

    return total_ram, available_ram, used_ram, free_ram, percent_used

if __name__== "__main__":
    total, available, used, free, percent = get_ram_info()
    print(f"Total RAM: {total} bytes")
    print(f"Available RAM: {available} bytes")
    print(f"Used RAM: {used} bytes")
    print(f"Free RAM: {free} bytes")
    print(f"Percent of RAM used: {percent}%")
print()
cputimes = psutil.cpu_times()
print(cputimes)
print()
cpucount = psutil.cpu_count()
print(f"You have {cpucount} cpus in the system.")
print()
for x in range(3):
    print("CPU percent:")
    cpupercent = psutil.cpu_percent(interval=1, percpu=True)
    print(cpupercent)
print()

cpufreq = psutil.cpu_freq()
print("CPUs frequenzy is:")
print(cpufreq)
print()
#hdusage = psutil.disk_usage('/')
#print("Disk usage is:")
#print(hdusage)
#print()
