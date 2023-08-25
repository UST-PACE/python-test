__AUTHOR__ = "Anjali Anil"
__MAINTAINER__ = "Nitin Vishwakarma"


try:
    import json
    import boto3
    from botocore.client import Config
    import pandas as pd
    import io
    import os
    import sys
    import hashlib
    import logging
    import pymysql
    import argparse
    from datetime import datetime
    from urllib.parse import unquote_plus
    from pyqldb.driver.qldb_driver import QldbDriver
    print("All Modules Loaded")

except Exception as e:
    print("Error : {} ".format(e))


def file_reader(inputBucket, fileName):
    print(inputBucket, fileName)

    # Do any further processing

def main():

    # Defining a global variable for number of records to be processed in one batch
    global MAX_DOCUMENT_PER_TRANSACTION

    inputBucket = "someBucketName"
    fileName = "someFileNameKey"
    region = "us-east-2"

    try:
        if inputBucket == "" and fileName == "":
            parser = argparse.ArgumentParser()
            parser.add_argument("--bucketName", "-js", type=str, required=True)
            parser.add_argument("--fileName", "-js", type=str, required=True)
            parser.add_argument("--region", "-js", type=str, required=True)
            parser.add_argument("--documentSize", "-js", type=str, required=True)
            args = parser.parse_args()
            inputBucket = args.bucketName
            fileName = args.fileName
            region = args.region
            logger.error('received ' + inputBucket + "  " +
                         fileName + "  " + "from params")

    except Exception as ex:
        logger.error(fileName + "Unexpected error:" + str(ex))

    if(not documentSize):
        documentSize = '40'
    MAX_DOCUMENT_PER_TRANSACTION = int(documentSize)

    file_reader(inputBucket, fileName)


print("Python file invoked")
if __name__ == '__main__':
    main()