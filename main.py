import os
import subprocess
import datetime

def check_network_connection(ip_address):
    # Pingコマンドを実行して応答を確認
    result = subprocess.run(['ping', '-c', '1', ip_address], capture_output=True)
    
    # 応答がある場合は成功、ない場合は失敗と判定
    if result.returncode == 0:
        # print(f"{ip_address} is reachable.")
        return True
    else:
        # print(f"{ip_address} is unreachable.")
        return False

# 例として8.8.8.8に対して実行
isInternetConnected = check_network_connection('8.8.8.8')

file_path = "/Users/keta/Python/NetDownTimeTracker/downtime.txt"

# Check if the file exists
now = datetime.datetime.now()
if os.path.exists(file_path):
    with open(file_path, "r") as file:
        # Read all lines and retrieve the last line
        lines = file.readlines()
        last_line = lines[-1].strip() if lines else ""

    with open(file_path, "a") as file:
        # 前回ダウンしていて今はアップの場合
        if "down" in last_line and isInternetConnected:
            file.write(f"{now}, up\n")

        # 前回アップしていて今はダウンの場合
        elif "up" in last_line and not isInternetConnected:
            file.write(f"{now}, down\n")
else:
    with open(file_path, "w") as file:
        if isInternetConnected:
            file.write(f"{now}, up\n")
        else:
            file.write(f"{now}, down\n")
