import streamlit as st
import pandas as pd

st.title("So sánh HTTP/2 vs HTTP/3 trên mạng Việt Nam")
st.write("Dashboard đo lường tự động, cập nhật theo giờ qua GitHub Actions.")

df = pd.read_csv("measurements.csv")
st.write(f"Tổng số lần đo: {len(df)}")

DOMAIN_CATEGORY = {
    "https://www.google.com/": "Big Tech",
    "https://www.cloudflare.com/": "Big Tech",
    "https://www.facebook.com/": "Big Tech",
    "https://www.youtube.com/": "Big Tech",
    "https://mbbank.com.vn/": "Banking",
    "https://www.vietcombank.com.vn/": "Banking",
    "https://shopee.vn/": "E-commerce",
    "https://tiki.vn/": "E-commerce",
    "https://vnu.edu.vn/": "Education",
    "https://phenikaa-uni.edu.vn/vi": "Education",
    "https://qldtbeta.phenikaa-uni.edu.vn/conggiangvien/login.aspx": "Education",
    "https://www.wikipedia.org/": "Reference",
}

df["category"] = df["url"].map(DOMAIN_CATEGORY)
df_http3 = df[df["protocol"] == "http3"]
support_rate = df_http3.groupby("category")["status"].apply(
    lambda x: (x == "success").mean() * 100
)

st.subheader("Tỷ lệ hỗ trợ HTTP/3 theo nhóm domain (%)")
st.bar_chart(support_rate)

st.subheader("Thời gian phản hồi trung bình theo domain (giây)")
st.caption("Lưu ý: Giá trị HTTP/3 bao gồm overhead khởi động tiến trình con, "
           "không phản ánh thuần túy tốc độ giao thức QUIC. Chỉ nên dùng "
           "để so sánh domain nào timeout/failed, không dùng để kết luận "
           "'giao thức nào nhanh hơn' theo giá trị tuyệt đối.")

df_success = df[df["status"] == "success"]
avg_table = df_success.groupby(["url", "protocol"])["elapsed_time"].mean().unstack()
st.dataframe(avg_table)