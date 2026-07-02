#LocalHost Nmap scan Report
target: 127.0.01
tool: namp
command used : nmap 127.0.0.1 -sV

findings:
-open ports:none all in ignored state
-Service : as all port are in ignored stateno servise are shown
-Notes :simply aren't running any network services (like a web server, SSH, or database)
	 on your local machine 


target:192.168.0.1[router]
tool: nmap
cmd : same

findings: 
-open port service : 22/ssh remote admin access
	   53/dns 80,443 tplink setting sebsite 1900/upnp network discovary
-note :


target:192.168.0.167[pc]
tool: nmap
cmd: same
findings: 
-open port $ service: 445/tcp (microsoft-ds) file share and printer sharing across the 
			network

WHAt i learned :
-when nmap used one router ip it give info on the router port and service running
 for host device need host ip address 
