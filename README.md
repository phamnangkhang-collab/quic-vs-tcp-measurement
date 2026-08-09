# quic-vs-tcp-measurement
Đo và so sánh hiệu năng QUIC/HTTP3 vs TCP/HTTP2 trên mạng Việt Nam

## Hạn chế của phương pháp đo lường

Do công cụ `curl` có sẵn không hỗ trợ HTTP/3, dự án đo HTTP/2 và HTTP/3 
bằng hai cơ chế khác nhau:
- HTTP/2: gọi trực tiếp qua thư viện `httpx` trong cùng tiến trình Python.
- HTTP/3: gọi `http3_client.py` (dựa trên `aioquic`) như một tiến trình con riêng.

Vì HTTP/3 phải khởi động một tiến trình Python mới cho mỗi lần đo, giá trị 
`elapsed_time` của HTTP/3 bao gồm thêm chi phí khởi động tiến trình (ước 
tính 0.3-0.8 giây), không phản ánh thuần túy tốc độ giao thức QUIC. Do đó:

- **Không nên** dùng dữ liệu này để kết luận "QUIC nhanh/chậm hơn TCP bao 
  nhiêu %" theo giá trị tuyệt đối.
- **Có thể tin cậy**: dữ liệu về domain nào hỗ trợ/không hỗ trợ HTTP/3 
  (cột `status`), vì đây là phép đo nhị phân không bị ảnh hưởng bởi overhead 
  thời gian.
- Hướng cải thiện trong tương lai: đo và trừ overhead khởi động tiến trình, 
  hoặc tự viết QUIC client tối giản không qua subprocess.
