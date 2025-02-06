from google.cloud import storage
import os, sys

from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

client = storage.Client()

buckets = list(client.list_buckets())
print([bucket.name for bucket in buckets])
