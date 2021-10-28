# psutil, process and system utilities

# read https://www.liaoxuefeng.com/wiki/1016959663602400/1183565811281984

import psutil

print (psutil.cpu_count()) # 8 # CPU逻辑数量

print (psutil.cpu_count(logical=False), '\n') # 4 # CPU物理核心

# 4说明是4核超线程, 8则是8核非超线程



# 统计CPU的用户／系统／空闲时间：
print (psutil.cpu_times(), '\n') 
# scputimes(user=3949.734375, system=2222.1406249998836, idle=674339.875, interrupt=156.625, dpc=102.53125)

"""
for x in range(10):
    # 再实现类似top命令的CPU使用率，每秒刷新一次，累计10次：
    print (psutil.cpu_percent(interval=1, percpu=True))
"""


# 使用psutil获取物理内存和交换内存信息，分别使用：

# 物理内存
print (psutil.virtual_memory())
# svmem(total=17092849664, available=8118059008, percent=52.5, used=8974790656, free=8118059008)

# 交换内存
print (psutil.swap_memory(), '\n')
# sswap(total=18367918080, used=11191181312, free=7176736768, percent=60.9, sin=0, sout=0)

# 交换区大小是1073741824 = 1 GB。





# 获取磁盘信息

# 可以通过psutil获取磁盘分区、磁盘使用率和磁盘IO信息：
print (psutil.disk_partitions()) # 磁盘分区信息

print (psutil.disk_usage('/')) # 磁盘使用情况

print (psutil.disk_io_counters(), '\n') # 磁盘IO






# 获取网络信息

# psutil可以获取网络接口和网络连接信息：

"""
print (psutil.net_io_counters()) # 获取网络读写字节／包的个数

print (psutil.net_if_addrs()) # 获取网络接口信息

print (psutil.net_if_stats()) # 获取网络接口状态

# 要获取当前网络连接信息，使用net_connections()：
print (psutil.net_connections())

# 你可能会得到一个AccessDenied错误，原因是psutil获取信息也是要走系统接口，
# 而获取网络连接信息需要root权限，
# 这种情况下，可以退出Python交互环境，用sudo重新启动：
"""


"""
$ sudo python3
Password: ******
Python 3.8 ... on darwin
Type "help", ... for more information.
>>> import psutil
>>> psutil.net_connections()
"""




# 通过psutil可以获取到所有进程的详细信息：

print  (psutil.pids()) # 所有进程ID

p = psutil.Process(16684) # 获取指定进程ID=16684, task manager-details

print (p.name)

print (
p.name(), # 进程名称
p.exe(), # 进程exe路径
p.cwd(), # 进程工作目录
p.cmdline(), # 进程启动的命令行
p.ppid(), # 父进程ID
p.parent(), # 父进程
p.children(), # 子进程列表
p.status(), # 进程状态
p.username(), # 进程用户名
p.create_time(), # 进程创建时间
#p.terminal(), # 进程终端, for Mac
p.cpu_times(), # 进程使用的CPU时间
p.memory_info(), # 进程使用的内存
p.open_files(), # 进程打开的文件
p.connections(), # 进程相关网络连接
p.num_threads(), # 进程的线程数量
p.threads(), # 所有线程信息
p.environ(),)# 进程环境变量
# p.terminate() # 结束进程