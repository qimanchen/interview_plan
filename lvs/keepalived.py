# 若是有一天 Load Balancer 不堪重负，那岂不是我们再大的集群也无用，
# 所以我们引入了 keepalived 工具来解决我们的单点故障问题

# 简介
"""
是一个用 C 语言写的一个路由软件，这个项目的主要目标是能为 Linux 系统和基于 Linux 的基础设施平台提供在负载均衡与高可用上稳定，简单的软件

keepalived 实现了一套通过对服务器池（也就是Real Server 池，Server pool）健康状态来动态地、
自动维护的管理被负载均衡的服务器池的 checker。

keepalived 高可用（High-available）是通过 VRRP 协议来实现的，
VRRP 在路由器的故障转移中是非常基础、常用的，
而 keepalived 实现了一套 hooks 为 VRRP finite state machine 提供底层，高速的协议互动
"""

# 提供的功能
"""
在 LVS 框架上扩展，二者具备良好的兼容性。
通过对服务器池的健康检查，对失效机器的故障隔离与通知。
通过 VRRP 实现的负载均衡器之间的切换，达到高可用
"""

# keepalived框架
"""
keepalived 分为两层结构：
用户空间
内核空间


keepalived 涉及到内核空间的两个网络功能，分别是：
IPVS：LVS 的 IP 负载均衡技术的使用
NETLINK：提供高级路由及其他相关的网络功能

在用户空间主要分为4个部分，分别是Scheduler I/O Multiplexer、Memory Mangement、Control Plane 和Core components。
Scheduler I/O Multiplexer：一个I/O复用分发调度器，它负责安排keepalived 所有内部的任务请求。
Memory Management：一个内存管理机制，这个框架提供的访问内存的一些通用方法。
Control Plane 是 keepalived 的控制面板，可以实现对配置文件进行编译和解析，keepalived的配置文件解析比较特殊，它只有在用到某模块时才解析相应的配置。
Core components 是 keepalived 要核心组件，包含了一系列的功能模块


其中就会有这样的一些模块：
WatchDog：监控checkers和VRRP进程的状况；
Checkers：真实服务器的健康检查 health checking，是 keepalived 最主要的功能；
VRRP Stack：负载均衡器之间的切换；
IPVS wrapper:设定规则到内核 ipvs 的接口；
Netlink Reflector：设定 vrrp 的vip地址等路由相关的功能。
"""
#  keepalived 主要功能实现还是依赖于 LVS 与 VRRP

# VRRP
"""
提出的解决局域网中配置静态网关出现单点失效现象的路由协议，使得在发生故障而进行设备功能切换时可以不影响内外数据通信

VRRP 协议需要具有IP地址备份，优先路由选择，减少不必要的路由器间通信等功能
"""
# 功能
"""
VRRP 协议的功能实现是将两台或多台路由器设备虚拟成一个设备，对外提供虚拟路由器IP


通过算法多角度的选举此时的 MASTER 机器作为这个对外 IP 的拥有者，也就是 ARP 的解析，
MASTER 的 MAC 地址与 IP 相互对应，其他设备不拥有该 IP，状态是 BACKUP，
而 BACKUP 除了接收 MASTER 的 VRRP 状态通告信息外，不执行对外的网络功能。
当主机失效时，BACKUP 将立即接管原先 MASTER 的网络功能。
从而达到了无缝的切换，而用户并不会知道网络设备出现了故障。
"""
# VRRP设置备胎
"""
主路由会每隔 1 秒（这个值可以修改配置）发送 vrrp 包通知 Backup 路由自己还是健康的存活着，
而 Backup 路由若是3秒（这个值可以修改）没有收到主路由的 vrrp 包，便会将自己切换成主路由来接替工作。

"""

# VRRP与LVS区别
"""
LVS 在后面的Server Pool 中每台都可以同时工作，而 VRRP 同时工作的机器只有一台，只有当一台出问题之后才会启用另外一台。
"""