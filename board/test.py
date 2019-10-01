import os


# difference with os.getenv is os.environ.get returns none when there's no valid system variable
ID = os.environ.get('GOOGLE_ID')

DB = os.environ.get('DB_USER')
print(ID)
print(DB)

AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')

print(AWS_ACCESS_KEY)
print(AWS_SECRET_ACCESS_KEY)
print(AWS_STORAGE_BUCKET_NAME)