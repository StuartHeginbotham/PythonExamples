#! python3
#  original date: 2016/01/13
# listBuckets.py

#aws configure with you credentials

import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

    
