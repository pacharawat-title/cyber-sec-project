def login(username, password):
    """Basic login function"""
    print("Login attempt detected")
    if username == "admin":
        return "Login Successsss"
    return "Login Failed"