### main.py
import streamlit as st
from pages import SignUp, SignIn, Home

def main():
    st.set_page_config(page_title="Hotel Management System", layout="wide")
    menu = ["Sign In", "Sign Up"]
    choice = st.sidebar.selectbox("Navigation", menu)

    if choice == "Sign Up":
        SignUp.render()
    elif choice == "Sign In":
        SignIn.render()
        if "user" in st.session_state:
            Home.render()

if __name__ == "__main__":
    main()


### database/mongodb.py
from pymongo import MongoClient

MONGO_URI = "mongodb+srv://bingChillingROOMS:bingChillingROOMS@cluster0.eeijvuh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_URI)
db = client['hotel_management']
users_collection = db['users']


### auth/auth_service.py
from database.mongodb import users_collection
from auth.user_factory import UserFactory
from users.user_type import UserType

class AuthService:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def register_user(self, username, password, role):
        if users_collection.find_one({"username": username}):
            return "User already exists!"
        users_collection.insert_one({"username": username, "password": password, "role": role})
        return f"User {username} registered successfully as {role}."

    def login_user(self, username, password):
        user_data = users_collection.find_one({"username": username, "password": password})
        if user_data:
            return UserFactory.create_user(user_data["role"], username)
        return "Invalid credentials!"


### auth/user_factory.py
from users.Admin import Admin
from users.Host import Host
from users.Guest import Guest
from users.user_type import UserType

class UserFactory:
    @staticmethod
    def create_user(role, username):
        if role == UserType.ADMIN.value:
            return Admin(username)
        elif role == UserType.HOST.value:
            return Host(username)
        elif role == UserType.GUEST.value:
            return Guest(username)
        else:
            raise ValueError("Invalid role")


### users/User.py
class User:
    def __init__(self, username):
        self.__username = username

    @property
    def username(self):
        return self.__username

    def browse_listings(self):
        return f"{self.__username} is browsing available listings."


### users/Admin.py
from users.User import User

class Admin(User):
    def manage_users(self):
        return f"{self.username} is managing user accounts."

    def view_reports(self):
        return f"{self.username} is viewing business reports."

    def delete_account(self, user):
        return f"{self.username} deleted {user}'s account."


### users/Host.py
from users.User import User

class Host(User):
    def create_listing(self):
        return f"{self.username} created a new listing."

    def manage_bookings(self):
        return f"{self.username} is managing bookings."

    def view_earnings(self):
        return f"{self.username} is viewing earnings."


### users/Guest.py
from users.User import User

class Guest(User):
    def book_accommodation(self):
        return f"{self.username} booked an accommodation."


### users/user_type.py
from enum import Enum

class UserType(Enum):
    ADMIN = "admin"
    HOST = "host"
    GUEST = "guest"


### proxy/user_proxy.py
class UserProxy:
    def __init__(self, user):
        self.user = user
        self.permissions = self.get_role_permissions()

    def get_role_permissions(self):
        role_permissions = {
            "admin": ["browse_listings", "manage_users", "view_reports", "delete_account"],
            "host": ["browse_listings", "create_listing", "manage_bookings", "view_earnings"],
            "guest": ["browse_listings", "book_accommodation"],
        }
        return role_permissions.get(self.user.__class__.__name__.lower(), [])

    def execute(self, action, *args):
        if action in self.permissions and hasattr(self.user, action):
            return getattr(self.user, action)(*args)
        return f"Access Denied! {self.user.username} cannot perform {action}."


### pages/SignUp.py
import streamlit as st
from auth.auth_service import AuthService
from users.user_type import UserType

def render():
    st.subheader("Create Account")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    role = st.selectbox("Select Role", [role.value for role in UserType])
    if st.button("Register"):
        result = AuthService.get_instance().register_user(username, password, role)
        st.success(result)


### pages/SignIn.py
import streamlit as st
from auth.auth_service import AuthService

def render():
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        user = AuthService.get_instance().login_user(username, password)
        if isinstance(user, str):
            st.error(user)
        else:
            st.success(f"Welcome {user.username}!")
            st.session_state["user"] = user


### pages/Home.py
import streamlit as st
from proxy.user_proxy import UserProxy

def render():
    st.subheader("Home Dashboard")
    user = st.session_state.get("user")
    proxy = UserProxy(user)

    st.write(f"Welcome back, **{user.username}**!")

    if st.button("Sign Out"):
        st.session_state.pop("user", None)
        st.success("You have been signed out.")
        st.experimental_rerun()
        return

    if st.button("Browse Listings"):
        st.info(proxy.execute("browse_listings"))

    if user.__class__.__name__.lower() == "admin":
        if st.button("Manage Users"):
            st.info(proxy.execute("manage_users"))
        if st.button("View Reports"):
            st.info(proxy.execute("view_reports"))

    elif user.__class__.__name__.lower() == "host":
        if st.button("Create Listing"):
            st.info(proxy.execute("create_listing"))
        if st.button("Manage Bookings"):
            st.info(proxy.execute("manage_bookings"))
        if st.button("View Earnings"):
            st.info(proxy.execute("view_earnings"))

    elif user.__class__.__name__.lower() == "guest":
        if st.button("Book Accommodation"):
            st.info(proxy.execute("book_accommodation"))
