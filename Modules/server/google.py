from google.cloud import storage


def create_folder(bucket_name, folder_name):
    """ 가상의 폴더를 GCS 버킷에 추가하는 함수 """
    client = storage.Client()
    bucket = client.bucket(bucket_name)

    # 빈 파일을 업로드하여 폴더처럼 보이게 함
    blob = bucket.blob(f"{folder_name}/")
    blob.upload_from_string("")  # 빈 파일 업로드


def upload_bytes_to_gcs(bucket_name, folder_name, file_name, file_bytes, content_type):
    """ 바이트 객체를 GCS 버킷에 추가하는 함수 """
    client = storage.Client()
    bucket = client.bucket(bucket_name)

    # 폴더 포함한 객체 경로 지정
    blob = bucket.blob(f"{folder_name}/{file_name}")

    # 바이트 객체를 GCS에 업로드
    blob.upload_from_string(file_bytes, content_type=content_type)

    # 업로드된 파일의 공개 URL 반환
    return blob.public_url  # https://storage.googleapis.com/{bucket_name}/{folder_name}/{file_name}
