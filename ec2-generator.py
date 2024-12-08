import boto3
import csv
import logging
# Setup loggers
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# global var
REPORT_NAME = 'ec2_report.csv'

def list_all_ec2_instances():
    """
    Gather all ec2 instance
    :param
    :return
    """

    # create an empty list
    list_ec2_instances =[]

    # initialize client
    ec2_client = boto3.client('ec2')
    response = ec2_client.describe_instances()

    # retrieve a list of instance

    reservations = response['Reservations']

    #looping through reservations
    for reservation in reservations:
        # we need to loop to retrieve instances

        for instance in reservation["Instances"]:
            instance_name = "Unnamed Instance"
            if 'Tags' in instance:
                instance_name = next(
                    (tag['Value'] for tag in instance['Tags'] if tag['Key'] == 'Name'),
                    "Unnamed Instance"
                )
            instance_type  = instance["InstanceType"]
            image_id       = instance["ImageId"]
            state          = instance["State"]["Name"]

            # add all elements to the list
            list_ec2_instances.append([instance_name, instance_type, image_id, state])


    return list_ec2_instances    

def generate_csv_report(instances):
    """
        This function will generate a csv report 
        :param list of instances
        :return returns true if valid
    """
    try:

        with open(REPORT_NAME, 'w', newline='') as csvfile:
            fieldnames = ['Instance_name', 'Instance_type', 'Image_id', 'State']
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(fieldnames)
            csvwriter.writerows(instances)
    
    except OSError as error:
        logging.error(f"Error writinf to file file:!{error}")
        return False
    return True #optional

def upload_report_to_s3():
    """
        This function will upload csv report to s3 bucket
        :param
        :return
    """
    try:
        s3_client = boto3.client('s3')
        bucket_name = 'complex-chalenging-bucket-001'

        # Use REPORT_NAME as the key in s3
        s3_client.upload_file(REPORT_NAME, bucket_name, REPORT_NAME)
        logger.info(f"Report Succesfully uploaded to s3 bucket:{bucket_name}/{REPORT_NAME}")

    except boto3.exceptions.Boto3Error as e:
        logger.error(f"Error uploading file to s3: {e}")

# main
if __name__ =='__main__':

    # call function
    instances = list_all_ec2_instances()
    # generate report
    generate_csv_report(instances)
    # upload report
    upload_report_to_s3() 

   # print(instances) 