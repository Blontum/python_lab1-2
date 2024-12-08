import boto3

def create_text_file():
    # Creating and writing to a text file
    file_name = "python-on-aws.txt"
    with open(file_name, "w") as file:
        file.write("programming is fun, but you got to practice")
    print(f"{file_name} has been created with the specified text.")

def upload_file_to_s3(bucket_name, file_name="python-on-aws.txt"):
    # Initialize S3 client
    s3_client = boto3.client("s3")

    try: 
        # Upload the file
        s3_client.upload_file(file_name, bucket_name, file_name)
        print(f"File '{file_name}' has been uploaded to bucket '{bucket_name}' successfully.")
    except Exception as e:
        print(f"Error uploading file: {e}")

# Usage
create_text_file()
upload_file_to_s3("lontum-sql-files")  
