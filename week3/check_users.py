def check_users(current_users, new_users):
    pass

    new_list = []
    for current_user in current_users:
        new_list.append(current_user.lower())

    for new_user in new_users:
        if new_user.lower() not in new_list:
            print(f"The username {new_user} is available!")
        else:
            print(f"The username {new_user} is already taken. Please select a new username.")

if __name__ == "__main__":
 current_us = ['JOSH','haritha', 'sally', 'darnell', 'supErman']
 new_us = ['george', 'ringo', 'SuPerMan', 'hannibal', 'joSh']
 check_users(current_us, new_us)
