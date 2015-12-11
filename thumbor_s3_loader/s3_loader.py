#-*- coding: utf8 -*-
import boto
import boto.s3.connection
from tornado.concurrent import return_future
from thumbor.loaders import LoaderResult

if not boto.config.get('s3', 'use-sigv4'):
    boto.config.add_section('s3')
    boto.config.set('s3', 'use-sigv4', 'True')


@return_future
def load(context, path, callback):
  result = LoaderResult()
  conn = boto.connect_s3(
    aws_access_key_id = context.config.AWS_S3_ACCESS_KEY,
    aws_secret_access_key = context.config.AWS_S3_SECRET_KEY,
    host=context.config.AWS_HOST,
    calling_format = boto.s3.connection.OrdinaryCallingFormat(),
    )
  bucket =  conn.get_bucket(context.config.AWS_S3_BUCKET,validate=False)
  data = bucket.get_key(path)
  if data is None:
      result.successful = False
      result.error = LoaderResult.ERROR_NOT_FOUND
  else:
    result.buffer = data.get_contents_as_string()
    result.successful = True

  callback(result)
