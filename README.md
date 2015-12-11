# thumbor_s3_loader
Thumbor S3 File Loader

Uses boto to retrieve images from S3 to use with thumbor - https://github.com/thumbor/thumbor

**This loader in beta BETA status. Use at your own risk**

Example config:

```python
LOADER = 'thumbor_s3_loader.s3_loader'
AWS_S3_ACCESS_KEY=''
AWS_S3_SECRET_KEY=''
AWS_S3_BUCKET = ''
AWS_HOST='s3.eu-central-1.amazonaws.com'
HTTP_LOADER_CA_CERTS="/etc/ssl/certs/ca-certificates.crt"
```
