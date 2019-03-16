"""
1. unzip 解压到指定目录, 使用 -d 参数:
# unzip some.zip -d newFolder/

2. 安装 hashcat:
	下载(binaries)https://hashcat.net/hashcat/
	sudo apt-get install p7zip
	sudo p7zip -d hashcat-xx.7z
	cd hashcat-5.1.0/
	sudo cp hashcat64.bin /usr/bin/
 	sudo ln -s /usr/bin/hashcat64.bin /usr/bin/hashcat
	sudo cp -Rv OpenCL /usr/bin/
	sudo cp hashcat.hcstat2	/usr/bin/
	sudo cp hashcat.hctune /usr/bin/
	reboot

	test if ok:
	# sudo hashcat --benchmark

3. 安装　wireshark
# https://askubuntu.com/questions/700712/how-to-install-wireshark

4. witete 常用命令：
	wifite -h  (查看帮助信息，这个是入口。)
	sudo wifite -e Tenda --kill
	sudo wifite -e Tenda --pmkid --kill
	sudo wifite -e Tenda -c 10 --pmkid --kill
	sudo wifite --wep --kill

	sudo wifite --wpa --mac --wpadt 15 --aircrack

	下次再继续吧

5. gist被墙，修改 /etc/hosts,加入(下面的失败了):
	204.232.175.78 documentcloud.github.com
	207.97.227.239 github.com
	204.232.175.94 gist.github.com
	107.21.116.220 help.github.com
	207.97.227.252 nodeload.github.com
	199.27.76.130 raw.github.com
	107.22.3.110 status.github.com
	204.232.175.78 training.github.com
	207.97.227.243 www.github.com
	192.30.253.118 gist.github.com
	192.30.253.119 gist.github.com
更新生效:
	# sudo /etc/init.d/dns-clean start
	# sudo /etc/init.d/networking restart



"""