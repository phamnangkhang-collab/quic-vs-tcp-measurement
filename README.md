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
  
## Kết quả sau khi phân tích
Kết quả đo lường 12 domain qua 23 lần lặp lại cho thấy sự phân hóa rõ rệt trong việc áp dụng HTTP/3 tại Việt Nam: các nền tảng Big Tech quốc tế và một số sàn thương mại điện tử lớn (Shopee, Tiki) đã hỗ trợ HTTP/3 hoàn toàn, trong khi lĩnh vực ngân hàng và giáo dục — vốn ưu tiên tính ổn định hơn tốc độ — chưa triển khai giao thức này. Đáng chú ý, Wikipedia là ngoại lệ khi không hỗ trợ HTTP/3 dù là nền tảng công nghệ lớn
