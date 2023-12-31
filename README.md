### Overview
This project consists of a simple Python application to monitor network connectivity and log downtime periods. It's primarily designed to be run periodically using `cron`, but can also be executed in a loop for continuous monitoring.

### Files
- `main.py`: The core script that checks the network connection to a specified IP address (default is 8.8.8.8, Google's DNS server) and logs the connectivity status.
- `launch.py`: An auxiliary script for continuous monitoring by running `main.py` every 60 seconds.

### How to Use
1. **Setup**: Clone the repository and navigate to the project directory.
2. **Run with `cron`**: Set up a cron job to execute `main.py` at your desired frequency.
3. **Run Continuously**: Alternatively, execute `launch.py` to continuously check the connection every 60 seconds.

### Dependencies
- Python 3
- Access to `ping` command

### Note
The script logs the connection status in `downtime.txt`. Ensure you have the necessary permissions to write to this file or modify the path as needed.

---

### 概要
このプロジェクトは、ネットワーク接続の監視とダウンタイム期間のログ記録を行う簡単なPythonアプリケーションです。主に`cron`を使用して定期的に実行することを想定していますが、ループ内で継続的に実行することもできます。

### ファイル
- `main.py`: 指定したIPアドレス（デフォルトは8.8.8.8、GoogleのDNSサーバー）へのネットワーク接続を確認し、接続状態をログに記録するメインスクリプトです。
- `launch.py`: `main.py`を60秒ごとに実行することで継続的な監視を行う補助スクリプトです。

### 使用方法
1. **セットアップ**: リポジトリをクローンし、プロジェクトディレクトリに移動します。
2. **`cron`で実行**: お好みの頻度で`main.py`を実行するためのcronジョブを設定します。
3. **継続的に実行**: 代わりに`launch.py`を実行し、60秒ごとに接続を確認します。

### 依存関係
- Python 3
- `ping`コマンドへのアクセス

### 注意
スクリプトは接続状態を`downtime.txt`に記録します。このファイルへの書き込み権限が必要ですので、必要に応じてパスを変更してください。