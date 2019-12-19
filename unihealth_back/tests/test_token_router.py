from unihealth_back.tests.test_base import *
import base64
#Login user and get the JWT with POST request
def test_patient_login_and_refresh(client):
    #Zhiye Xie is a patient in the db, his phone is 123456
    data = {
        'phone': '123456',
        'password': 'mypwd',
    }
    rep = client.post(
        '/auth/token',
        data = json.dumps(data),
        content_type='application/json'
    )
    assert rep.status_code == 200

    #Refresh Zhiye Xie and get the jwt with PUT request
    refresh_token = rep.get_json()['refresh_token']

    data2 = {
        'refresh_token': refresh_token
    }
    rep2 = client.put(
        '/auth/token',
        data = json.dumps(data2),
        content_type='application/json'
    )
    assert rep2.status_code == 200


def test_doctor_login(client):
    #Yufeng Zhao is a doctor in the db, his phone is 654321
    data = {
        'phone': '654321',
        'password': 'mypwd',
    }
    rep = client.post(
        '/auth/token',
        data = json.dumps(data),
        content_type='application/json'
    )
    assert rep.status_code == 200

def test_admin_login(client):
    #Admin is an admin in the db, his phone is Admin
    data = {
        'phone': 'admin',
        'password': 'mypwd',
    }
    rep = client.post(
        '/auth/token',
        data = json.dumps(data),
        content_type='application/json'
    )
    assert rep.status_code == 200

# #Logout user and delete the jwt with DELETE request
# def test_logout_psuedo_patient(client):
#     #ZZhiye XXie is a psuedo patient in the db, his phone is 1123456
#     data = {
#         'phone': '1123456',
#         'password': 'mypwd',
#     }
#     rep = client.post(
#         '/auth/token',
#         data = json.dumps(data),
#         content_type='application/json'
#     )
#     assert rep.status_code == 200

#     refresh_token = rep.get_json()['refresh_token']

#     data2 = {
#         'refresh_token': refresh_token
#     }
#     rep2 = client.delete(
#         '/auth/token',
#         data = json.dumps(data2),
#         headers ={
#             'Authorization': "Basic {}".format(refresh_token)
#         }
#     )
#     assert rep2.status_code == 200
