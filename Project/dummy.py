# Singleton: Authentication Service
class AuthService:
    _instance = None  # Singleton instance

    @classmethod
    def get_instance(cls):
        """Ensures only one instance of AuthService exists"""
        if cls._instance is None:
            cls._instance = cls()
            cls._instance.users = {}  # Dictionary to store registered users
        return cls._instance

    def register_user(self, username, password, role):
        """Registers a new user"""
        if username in self.users:
            return "User already exists!"
        self.users[username] = {"password": password, "role": role}
        return f"User {username} registered successfully as {role}."

    def login_user(self, username, password):
        """Logs in a user and returns the corresponding User object"""
        if username in self.users and self.users[username]["password"] == password:
            return UserFactory.create_user(self.users[username]["role"], username)
        return "Invalid credentials!"


# User Roles with Specific Functions
class User:
    def __init__(self, username):
        self.username = username

    def browse_listings(self):
        return f"{self.username} is browsing available listings."

class Admin(User):
    def manage_users(self):
        return f"{self.username} is managing user accounts."

    def view_reports(self):
        return f"{self.username} is viewing business reports."

    def delete_account(self, user):
        return f"{self.username} deleted {user}'s account."

class Host(User):
    def create_listing(self):
        return f"{self.username} created a new listing."

    def manage_bookings(self):
        return f"{self.username} is managing bookings."

    def view_earnings(self):
        return f"{self.username} is viewing earnings."

class Guest(User):
    def book_accommodation(self):
        return f"{self.username} booked an accommodation."


# Factory Method: Creates User Objects Based on Role
class UserFactory:
    @staticmethod
    def create_user(role, username):
        """Creates user objects based on role"""
        if role == "admin":
            return Admin(username)
        elif role == "host":
            return Host(username)
        elif role == "guest":
            return Guest(username)
        else:
            raise ValueError("Invalid role")


# Proxy: Controls Access to Actions and Allows Post-Execution Functions
class UserProxy:
    def __init__(self, user):
        self.user = user
        self.permissions = self.get_role_permissions()

    def get_role_permissions(self):
        """Defines valid functions for each role"""
        role_permissions = {
            "admin": ["browse_listings", "manage_users", "view_reports", "delete_account"],
            "host": ["browse_listings", "create_listing", "manage_bookings", "view_earnings"],
            "guest": ["browse_listings", "book_accommodation"],
        }
        return role_permissions.get(self.user.__class__.__name__.lower(), [])

    def execute(self, action, post_action=None, *args):
        """Checks if the user has permission before executing an action"""
        if action in self.permissions and hasattr(self.user, action):
            result = getattr(self.user, action)(*args)  # Execute main action
            
            if post_action and hasattr(self.user, post_action):
                post_result = getattr(self.user, post_action)()
                return f"{result} | {post_result}"  # Execute post-action after main function
            
            return result  # Return main function result if no post-action
        return f"Access Denied! {self.user.username} cannot perform {action}."


# Example Usage
auth_service = AuthService.get_instance()

# Registering Users
print(auth_service.register_user("alice", "pass123", "admin"))
print(auth_service.register_user("bob", "pass123", "host"))
print(auth_service.register_user("eve", "pass123", "guest"))

# Logging In
admin = auth_service.login_user("alice", "pass123")
host = auth_service.login_user("bob", "pass123")
guest = auth_service.login_user("eve", "pass123")

# Using Proxy to control access
admin_proxy = UserProxy(admin)
host_proxy = UserProxy(host)
guest_proxy = UserProxy(guest)

# Testing Functionality
print(admin_proxy.execute("manage_users"))  # Allowed, calls manage_users then view_reports
print(admin_proxy.execute("delete_account", None, "bob"))  # Allowed, deletes bob's account
print(host_proxy.execute("create_listing", "view_earnings"))  # Allowed, calls create_listing then view_earnings
print(host_proxy.execute("manage_bookings", None))  # Allowed
print(guest_proxy.execute("book_accommodation", "browse_listings"))  # Allowed, calls book then browse
print(guest_proxy.execute("create_listing", "browse_listings"))  # Denied
