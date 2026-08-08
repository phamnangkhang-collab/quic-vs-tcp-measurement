import csv
import time
from datetime import datetime
from test_http2 import measure_http2
from test_http3 import measure_http3
import os

DOMAINS = [
    #big tech
    "https://www.google.com/",
    "https://www.cloudflare.com/",
    "https://www.facebook.com/",
    "https://www.youtube.com/",
    "https://www.wikipedia.org/",
    # ngân hàng Vn
    "https://mbbank.com.vn/",
    "https://www.vietcombank.com.vn/",
    # sàn thương mại
    "https://shopee.vn/",
    "https://tiki.vn/",
    # đại học 
    "https://vnu.edu.vn/",
    "https://phenikaa-uni.edu.vn/vi",
    "https://qldtbeta.phenikaa-uni.edu.vn/conggiangvien/login.aspx",
]

def collect_all():
    results = []
    for domain in DOMAINS:
        print(f"Đang đo: {domain}")
        result_http2 = measure_http2(domain)
        results.append(result_http2)
        result_http3 = measure_http3(domain)
        results.append(result_http3)
    return results

if __name__ == "__main__":
    data = collect_all()
    print(f"Tổng số kết quả thu được: {len(data)}")

#Lưu dữ liệu 

def save_to_csv(results, filename="measurements.csv"):
    fieldnames = ["url", "protocol", "http_version", "elapsed_time", "status", "error_message"]
    file_exists = os.path.exists(filename)
    
    with open(filename, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerows(results)

if __name__ == "__main__":
    data = collect_all()
    print(f"Tổng số kết quả thu được: {len(data)}")
    save_to_csv(data)
    print("Đã lưu vào measurements.csv")