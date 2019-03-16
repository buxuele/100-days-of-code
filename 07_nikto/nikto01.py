"""
1. 解压 log.tar.gz
# tar -zxvf log.tar.gz

2. 网站渗透工具
# sudo apt-get install nikto
nikto -h http://some-site.com

3. 查看具体是那个进程在占用网速。
# sudo apt install nethogs
# sudo nethogs -a

4. install apt-fast

5. 这个报错
# subprocess.call(['sudo', 'ls', '-a'], shell=True)
改用这个:
# os.system(f'sudo ifconfig {interface} down')

6.


"""