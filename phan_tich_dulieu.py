import pandas as pd

df = pd.read_csv("measurements.csv")

print(df.head())
print(df.shape)

df_success = df[df["status"] == "success"]
# tính trung bình giao thuc http2 va http 3
avg_by_protocol = df_success.groupby("protocol")["elapsed_time"].mean()
print(avg_by_protocol)

avg_by_domain_protocol = df_success.groupby(["url", "protocol"])["elapsed_time"].mean()
print(avg_by_domain_protocol)

status_counts = df.groupby(["url", "protocol"])["status"].value_counts()
print(status_counts)


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
print(df[["url", "category"]].drop_duplicates())

# loai bo cac dong do http2 chi giu http3
df_http3 = df[df["protocol"] == "http3"]

#tinh trung binh ti le true/false
support_rate = df_http3.groupby("category")["status"].apply(
    lambda x: (x == "success").mean() * 100
)
print(support_rate)

