# pip install matplotlib pandas

import pandas as pd
import matplotlib.pyplot as plt

# ファイルパス
file_path = 'downtime.txt'

# データを読み込む
df = pd.read_csv(file_path, names=['Timestamp', 'Status'], sep=', ', parse_dates=['Timestamp'], engine='python')

# 状態を数値に変換
df['Status'] = df['Status'].map({'up': 1, 'down': 0})



# 日付ごとのダウン回数を計算
df['Date'] = df['Timestamp'].dt.date
down_count = df[df['Status'].diff() == -1].groupby('Date').size()

# 日付ごとのダウン時間を計算（分単位、整数）
df['Duration'] = df.groupby((df['Status'].diff() == -1).cumsum())['Timestamp'].transform(lambda x: x.max() - x.min())
down_duration = df[df['Status'] == 0].groupby('Date')['Duration'].sum().apply(lambda x: int(x.total_seconds() / 60))

# 結果を出力
print("日付ごとのダウン回数:")
print(down_count)
print("日付ごとのダウン時間（分、整数）:")
print(down_duration)





# グラフを描画
plt.figure(figsize=(10, 4))
plt.plot(df['Timestamp'], df['Status'], drawstyle='steps-post', marker='o')
plt.ylim(-0.2, 1.2)
plt.yticks([0, 1], ['Down', 'Up'])
plt.xlabel('Timestamp')
plt.ylabel('Network Status')
plt.title('Network Downtime Visualization')
plt.grid(True)
plt.show()




















