import subprocess
import time

def measure_http3(url: str ,timeout_seconds: int = 15):
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
