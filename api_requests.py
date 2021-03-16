import requests

def get_branches():
    r = requests.get("https://api.github.com/repos/dward2/BME547/branches")
    print(r)
    print(type(r))
    print(r.status_code)
    print(r.text)
    branches = r.json()
    print(branches)
    for branch in branches:
        print(branch["name"])


def countries():
    server = "http://vcm-7631.vm.duke.edu:5000"
    r = requests.get(server+"/countries")
    print(r.status_code)
    print(r.text)

    my_countries = {"one": "Austria", "two": "Argentina"}
    r = requests.post(server+"/compare", json=my_countries)
    print(r.status_code)
    print(r.text)
    data = r.json()
    print(data)


def student_data():
    server = "http://vcm-6764.vm.duke.edu:5000/student"
    my_data = {"name": "Alana Gonzales", "net_id": "agg24", "e-mail": "alana.gonzales@duke.edu"}
    r = requests.post(server, json=my_data)
    print(r.status_code)
    print(r.text)
    data = r.json()
    print(data)


if __name__ == '__main__':
    student_data()
