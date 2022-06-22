#!/bin/python3
#Python Program for deleting an S3 bucket
import boto3
import sys

#connecting to S3

s3 = boto3.resource('s3')
bucket_name = 'jyothypython123bucket'
bucket = s3.Bucket(bucket_name)
response = bucket.delete(ExpectedBucketOwner='408474111132')
