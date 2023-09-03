import requests
import json

# Authorization and resource urls
auth_url = "http://localhost:9001"
resource_url = "http://localhost:9002"
# Create a user with username and password
data = json.dumps({"username": "temp", "password": "one"})


def register_login() -> str:
    """
    Register and login the user by returning a token
    :return: token on success
    :rtype: string
    :raises HTTPError: If the register or login fails
    :raises Timeout: If the register or login takes too much time
    :raises Exception: For every other error
    """
    try:
        # Register
        response = requests.post(f"{auth_url}/register", data=data,
                                 headers={"Content-Type": "application/json"})
        response.raise_for_status()
        # Login. In this case login is redundunt since register also returns a token
        response = requests.post(f"{auth_url}/login", data=data,
                                 headers={"Content-Type": "application/json"})
        response.raise_for_status()
        token = response.json()
        return token.get('auth_token')
    except requests.HTTPError as e:
        # possibly check response for a message
        print(f"Error: {str(e)}, {response.json()}")
        raise e
    except requests.Timeout:
        print("Timeout, request took too long")
    except Exception as e:
        print(f"Something went wrong: {str(e)}")


def print_resource(token: str) -> None:
    """
    Example of using the token to access the resource server
    :rtype: None
    :raises HTTPError: If the register or login fails
    :raises Timeout: If the register or login takes too much time
    :raises Exception: For every other error
    """
    try:
        response = requests.get(f"{resource_url}/user",
                                headers={"Authorization": f"Bearer {token}"})
        response.raise_for_status()
        print(response.text)
    except requests.HTTPError as e:
        # possibly check response for a message
        print(f"Error: {str(e)}")
        raise e
    except requests.Timeout:
        print("Timeout, request took too long")
    except Exception as e:
        print(f"Something went wrong: {str(e)}")


if __name__ == "__main__":
    token = register_login()
    print_resource(token)
