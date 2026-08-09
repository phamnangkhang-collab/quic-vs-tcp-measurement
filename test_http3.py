import subprocess
import time

def measure_http3(url: str ,timeout_seconds: int = 15):
    """
    Đo thời gian phản hồi HTTP/3 bằng cách gọi http3_client.py qua subprocess.
    
    LƯU Ý: elapsed_time bao gồm cả thời gian khởi động tiến trình Python con
    (~0.3-0.8s), không phải thời gian thuần của giao thức QUIC. Vì vậy KHÔNG
    nên so sánh trực tiếp giá trị tuyệt đối với measure_http2() để kết luận
    "giao thức nào nhanh hơn" - chỉ dùng để so sánh TƯƠNG ĐỐI giữa các domain
    trong cùng phương pháp đo này (domain nào chậm/nhanh hơn domain khác khi
    đo bằng cùng cách).
    """
    start = time.time()
    try:  
        result = subprocess.run(
            ["python3", "http3_client.py", url],
            capture_output= True,
            text= True,
            timeout= timeout_seconds
        )
        end = time.time()
        elapsed = end - start

        print(f"URL: {url}")
        print(f"Total time: {elapsed:.4f} seconds")

        if result.returncode == 0:
            return {
            "url": url,
            "protocol": "http3",
            "elapsed_time": elapsed,
            "status": "success"
            }
        else:
            return {
            "url": url,
            "protocol": "http3",
            "elapsed_time": elapsed,
            "status": "failed",
            "error_message": result.stderr
            }

    except subprocess.TimeoutExpired:
        end = time.time()
        elapsed = end - start
        return {
            "url": url,
            "protocol": "http3",
            "elapsed_time": elapsed,
            "status": "timeout"
            }

if __name__ == "__main__":
    result = measure_http3("https://example.com/")
    print(result)
