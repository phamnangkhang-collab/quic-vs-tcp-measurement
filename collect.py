import csv
import time
from datetime import datetime
from test_http2 import measure_http2
from test_http3 import measure_http3

DOMAINS = [
    "https://www.google.com/",
    "https://www.cloudflare.com/",
    "https://www.facebook.com/",
    "https://www.youtube.com/",
    "https://www.wikipedia.org/",
]