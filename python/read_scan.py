from pathlib import Path 

file_path=Path("../nmap/localhost_scan.txt")

if file_path.exists():
	content = file_path.read_text()
	print(content)
else:
	print("Scan file not found")

