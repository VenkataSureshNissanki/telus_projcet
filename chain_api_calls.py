import requests

def test_chain_api_calls():
    # First call - login and get token
    res1 = requests.post("https://api.example.com/auth", json={"user": "abc", "pass": "123"})
    token = res1.json().get("token")

    assert token is not None, "Failed to retrieve token"

    # Use token in second call
    headers = {"Authorization": f"Bearer {token}"}
    res2 = requests.get("https://api.example.com/profile", headers=headers)

    assert res2.status_code == 200
    print("Profile Data:", res2.json())
