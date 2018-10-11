# bmc
通过BMC/ILO控制hp dl2000服务器开关机

1、Openwrt上安装python（2.7完整包）

2、修改config.py填写对应参数

3、通过cron定时任务来自动开机关

#crontab -e

0 9 * * * python /root/bmc/relayon.py # 9:00 先开继电器，给服务器通电
1 9 * * * python /root/bmc/poweron.py # 9:01 软开机
50 20 * * * python /root/bmc/poweroff.py 
51 20 * * * python /root/bmc/poweroff.py # 20:51 软关机调两次
0 21 * * * python /root/bmc/relayoff.py  #21:00 关闭继电器，彻底断电，静音

