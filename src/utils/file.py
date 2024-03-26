import boto3

s3_client = boto3.client("s3")


def get_file_from_event(event):
    bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
    key_name = event["Records"][0]["s3"]["object"]["key"]
    print(bucket_name)
    print(key_name)

    response = s3_client.get_object(Bucket=bucket_name, Key=key_name)
    data = response["Body"].read().decode("utf-8")

    return data
