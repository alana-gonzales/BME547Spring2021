import requests

patient = {"name": "Evan", "id": 1, "blood_type": "O+"}

r = requests.post("http://127.0.0.1:5000/new_patient", json=patient)
print(r.status_code)
print(r.text)


test_data = {"id": 103, "test_name": "HDL", "test_result": 60}

r = requests.post("http://127.0.0.1:5000/add_test", json=test_data)
print(r.status_code)
print(r.text)


r = requests.get("http://127.0.0.1:5000/get_results/5")
print(r.status_code)
print(r.text)
