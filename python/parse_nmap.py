from pathlib import Path 

scan_file =Path("../nmap/router_scan.txt")

if not scan_file.exists():
	print("Nmap scan file not found.")
	exit()
lines=scan_file.read_text().splitlines()

print("Possible open port/service:")
print("-"*30)

for line in lines:
	if "/tcp" in line and "open" in line:
		print(line)
