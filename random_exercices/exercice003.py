#!/usr/bin/env python3
name = input ("Enter Your Name : ").strip().capitalize()
email = input ("Enter your email : ").strip()

username = email[:email.index("@")]
domain = email[email.index("@")+1:]

print(f"Hello {name} Welcome to our community ,your email is {email}")
print(f"Your username is {username} \nYour domain is {domain}")
