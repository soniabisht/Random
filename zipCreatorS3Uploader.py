import shutil
import threading
import boto3


def zipFile():
    threading.Timer(5.0, zipFile).start()
    target_path = r'C:\\Users\\e5583205\\projects\\practice\\data\\'
    file_to_zip = 'countries.json'            # file to zip
    file_list = file_to_zip.split('.')
    zipped_file_name = file_list[0]
    print("i came here")
    final_file_with_path = target_path + zipped_file_name
    try:
        shutil.make_archive(final_file_with_path, 'zip', target_path, file_to_zip)
        return zipped_file_name +'zip'
    except OSError:
        print("error")
# Code to upload zipped file to s3 bucket

def uploadZipToS3(filename):
    # Create an S3 client, 
    # Add your own aws_access_key_id , aws_secret_access_key values
    s3 = boto3.client('s3',aws_access_key_id="jsdajsdahsdka",
        aws_secret_access_key="dssdfsdfsdfsdfsdfsdfsd")
    bucket_name = 'audiofilebucket2'
    # uploading file to s3 bucket
    s3.upload_file(filename, bucket_name, filename)

if __name__ == '__main__':  
    final_file_name = zipFile()  
    uploadZipToS3(final_file_name)
