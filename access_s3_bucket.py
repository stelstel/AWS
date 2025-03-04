import boto3

from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def list_bucket_objects(bucket_name):
    """List objects in an S3 bucket"""
    s3 = boto3.client('s3')

    try:
        response = s3.list_objects_v2(Bucket=bucket_name)

        if 'Contents' in response:
            for obj in response['Contents']:
                print(f' - {obj["Key"]}')
        else:
            print(f'Bucket {bucket_name} is empty.')
    except NoCredentialsError:
        print('Credentials not available.')
    except PartialCredentialsError:
        print('Incomplete credentials provided.')


if __name__ == '__main__':
    bucket_name = 'stelstelbucket' ### Change this to your bucket name ###
    print("")
    list_bucket_objects(bucket_name)