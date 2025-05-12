import requests

def test_upload_file():
    url = "https://api.example.com/upload"
    files = {'file': open('my_file.txt', 'rb')}
    response = requests.post(url, files=files)

    assert response.status_code == 200
    print("File upload response:", response.json())
