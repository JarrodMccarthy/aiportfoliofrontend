import os
import json
import boto3
import base64
import io
import csv
import pandas as pd
import codecs
        

class S3:
    def __init__(self):
        self.client = boto3.client(
            's3',
            aws_access_key_id=settings['awsaccesskeyid'],
            aws_secret_access_key=settings['awssecretkey'],
        )

    
    def list_buckets(self):
        resp = self.client.list_buckets()
        return resp 

    def upload_csv(self, img_location, bucketname, objectname):
        resp = self.client.upload_file(img_location, bucketname, object_name)
        return resp

    def download_csv_as_dataframe(self, bucketname, objectname, datatypes=None):
        try:
            obj = self.client.get_object(Bucket=bucketname, Key=objectname)
            reader = csv.DictReader(codecs.getreader("utf-8-sig")(obj["Body"]))
            df = pd.DataFrame(reader)
            if datatypes:
                df = df.astype(datatypes)
            return df
        except Exception as e:
            return pd.Dataframe()

    def upload_dataframe_as_csv(self, df, bucketname, objectname):
        try:
            csv_buffer = io.StringIO()
            df.to_csv(csv_buffer, index=False)
            response = self.client.put_object(Bucket=bucketname, Key=objectname, Body=csv_buffer.getvalue())
            return response
        except Exception as e:
            return pd.Dataframe()
    


