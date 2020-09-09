def check_users(current_users, new_users):
    pass

current_users = ['chris','haritha', 'sally', 'darnell', 'supErman']
new_users =['george', 'ringo', 'SuPerMan', 'hannibal', 'josh']

new_list = []
for current_user in current_users:
    new_list.append(current_user.lower())

for new_user in new_users:
    if new_user.lower() not in new_list:
        print(f"The username {new_user} is available!")
else:
    print("This username is already taken.")

if __name__ == "__main__":
 current_us = ['chris','haritha', 'sally', 'darnell', 'superman']
 new_us = ['george', 'ringo', 'superman', 'hannibal', 'josh']
 check_users(current_us, new_us)
