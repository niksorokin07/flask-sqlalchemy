from requests import get

print(get('http://localhost:8080/api/jobs').json())

print(get('http://localhost:5000/api/jobs/1').json())

print(get('http://localhost:5000/api/jobs/999').json())

print(get('http://localhost:5000/api/jobs/s').json())
