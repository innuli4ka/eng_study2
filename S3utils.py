import boto3

#functions that download and upload files 

BUCKET_NAME = "eng.study"  

def download_file_from_s3(s3_key: str, local_path: str):
    s3 = boto3.client('s3')
    try:
        s3.download_file(BUCKET_NAME, s3_key, local_path)
        print(f"Downloaded '{s3_key}' from S3 to '{local_path}'.")
    except Exception as e:
        print(f"Error downloading '{s3_key}' from S3: {e}")

def upload_file_to_s3(local_path: str, s3_key: str):
    s3 = boto3.client('s3')
    try:
        s3.upload_file(local_path, BUCKET_NAME, s3_key)
        print(f"Uploaded '{local_path}' to S3 as '{s3_key}'.")
    except Exception as e:
        print(f"Error uploading '{local_path}' to S3: {e}")

