import boto3

# Define the username and password
username = 'exposed_iam_user_lab'
password = '@MyUniqP@$$11'
account_id = '282800070961'

# Create an IAM client using the default AWS CLI profile
iam = boto3.client('iam')
sts = boto3.client('sts')

# Function to check the account ID
def check_account_id(expected_account_id):
    try:
        current_account_id = sts.get_caller_identity()["Account"]
        if current_account_id != expected_account_id:
            raise Exception(f"Account ID mismatch: expected {expected_account_id}, but got {current_account_id}")
        print(f"Verified account ID: {current_account_id}")
    except Exception as e:
        print(f"Error verifying account ID: {e}")
        exit(1)

# Function to create the IAM user and set the password for web console access
def create_iam_user_with_console_access():
    try:
        # Create IAM user
        iam.create_user(UserName=username)
        print(f"User '{username}' created successfully.")
        
        # Create login profile (console access) with the specified password
        iam.create_login_profile(
            UserName=username,
            Password=password,
            PasswordResetRequired=False
        )
        print(f"Login profile created successfully for user '{username}' with the specified password.")
        
    except iam.exceptions.EntityAlreadyExistsException:
        print(f"User '{username}' already exists.")
    except iam.exceptions.LimitExceededException:
        print("Cannot create more IAM users, account limit exceeded.")
    except iam.exceptions.PasswordPolicyViolationException as e:
        print(f"Password policy violation: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Check the account ID
check_account_id(account_id)

# Execute the function
create_iam_user_with_console_access()
