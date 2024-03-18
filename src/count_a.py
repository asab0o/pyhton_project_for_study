from datetime import datetime
import time

def count_a(s):
    """与えられた文字列sに含まれる'a'または'A'の個数を返す。含まれない場合は'nothing.'を返す。"""
    now = datetime.now()
    formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
    print("time is:", formatted_now)
    time.sleep(5)
    count = s.lower().count('a')
    return count if count > 0 else "nothing."
