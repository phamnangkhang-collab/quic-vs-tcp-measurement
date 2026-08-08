import httpx
import time 

def measure_http2(url: str):
    start = time.time()
    try:
        with httpx.Client(http2 = True) as client:
            response = client.get(url)
        end = time.time()
        elapsed = end - start

        return {
            "url": url,
            "protocol": "http2",
            "http_version": response.http_version,
            "elapsed_time": elapsed,
            "status": "success"
        }

    except Exception as e:
        end = time.time()
        elapsed = end - start
        return {
            "url": url,
            "protocol": "http2",
            "elapsed_time": elapsed,
            "status": "failed"
        }

if __name__ == "__main__":
    result = measure_http2("https://www.google.com")
    print(result)