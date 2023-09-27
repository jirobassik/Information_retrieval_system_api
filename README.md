# Information_retrieval_system_api
## Run
```python manage.py runserver localhost:8001```
## Has the following functionality:
- Add, delete files (localhost:8001/api/v1/uploadfiles)
- Search data in all files (localhost:8001/api/v1/search/)
- Calculate metric (localhost:8001/api/v1/metric/)
- Download file (localhost:8001/api/v1/download/<int:id>)
- Classificate file (localhost:8001/api/v1/classification/<int:id>)

## Works in conjunction with https://github.com/jirobassik/Information_retrieval_system_client
