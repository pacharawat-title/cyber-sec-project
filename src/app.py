def login(username, password):
    """Basic login function"""
    print("Login attempt detected")
    if username == "admin":
        return "Login Successsss"
    return "Login Failed"
    if username == "admin" and \
    password == "1234":
        return "Login Success"
    return "Login Failed"
    """Basic login function"""
    if username == "admin" and password == "secure_pw":
        return True
    return False

def logout():
    """Basic logout function"""
    # In a real app, this would clear the session
    print("User logged out successfully")
    return True
