from requests import get, exceptions, post

"""try:
    print(get('http://localhost:8080/api/jobs').json())
except exceptions.ConnectionError:
    print("Connection 1 refused")
try:
    print(get('http://localhost:8080/api/jobs/1').json())
except exceptions.ConnectionError:
    print("Connection 2 refused")
try:
    print(get('http://localhost:8080/api/jobs/999').json())
except exceptions.ConnectionError:
    print("Connection 3 refused")
try:
    print(get('http://localhost:8080/api/jobs/s').json())
except exceptions.ConnectionError:
    print("Connection 4 refused")"""

try:
    print(post('http://localhost:8080/api/jobs').json())

    print(post('http://localhost:8080/api/jobs',
               json={'job': 'Заголовок'}).json())

    print(post('http://localhost:8080/api/jobs',
               json={"id": 1, "team_leader": "test-run@mars.org", "job": "test-run",
                     "work_size": 16, "hazard_level": 2, "collaborators": None, "start_date": None, "end_date": None,
                     "is_finished": False}).json())
except exceptions.ConnectionError:
    print("Connections 5-8 refused")
