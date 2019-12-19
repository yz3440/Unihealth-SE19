
from unihealth_back.tests.test_base import *

#Register user (patient/doctor) with POST request
def test_register_patient(client):
    data = {
        'firstName': 'Zhiye',
        'lastName': 'Xie',
        'gender': 'male',
        'birthday': '2121-12-12',
        'phone': '123456',
        'password': 'mypwd',
        'role': 'patient'
    }
    rep = client.post(
        '/resources/user',
        data = json.dumps(data),
        content_type='application/json'
    )
    assert rep != None

def test_register_psuedo_patient(client):
    data = {
        'firstName': 'ZZhiye',
        'lastName': 'XXie',
        'gender': 'male',
        'birthday': '2121-12-12',
        'phone': '1123456',
        'password': 'mypwd',
        'role': 'patient'
    }
    rep = client.post(
        '/resources/user',
        data = json.dumps(data),
        content_type='application/json'
    )
    assert rep != None

def test_register_doctor(client):
    data = {
        'firstName': 'Yufeng',
        'lastName': 'Zhao',
        'gender': 'male',
        'birthday': '1212-12-12',
        'phone': '654321',
        'password': 'mypwd',
        'role': 'doctor'
    }
    rep = client.post(
        '/resources/user',
        data = json.dumps(data),
        content_type='application/json'
    )
    assert rep != None

def test_register_admin(client):
    data = {
        'firstName': 'Admin',
        'lastName': 'Admin',
        'gender': 'male',
        'birthday': '2019-12-12',
        'phone': 'admin',
        'password': 'mypwd',
        'role': 'admin'
    }
    rep = client.post(
        '/resources/user',
        data = json.dumps(data),
        content_type='application/json'
    )
    assert rep != None


# #Get user info with GET request
# def test_get_info_by_patient(client):
#     #this returns the patient's own profile
#     data = None
#     rep = client.get(
#         '/resources/user',
#         data = json.dumps(data),
#         content_type='application/json'
#     )

#     print(rep)
#     assert 0