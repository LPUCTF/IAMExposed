import boto3

# Replace these with your actual AWS access and secret keys
aws_access_key_id = 'AKIAUDWBSUEY4FOYPVRS'
aws_secret_access_key = 'Yo3V4KzIZNvuo2wCYs2MFFXGEmiLKjb09EO/X2zQ'

# Create a session using the provided credentials
session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

# Create an IAM client
iam = session.client('iam')

# Function to list all users and their associated permissions
def list_users_and_permissions():
    try:
        # List all users
        users = iam.list_users()
        
        for user in users['Users']:
            user_name = user['UserName']
            print(f"User: {user_name}")
            
            # List user policies
            user_policies = iam.list_user_policies(UserName=user_name)
            for policy_name in user_policies['PolicyNames']:
                print(f"  User Policy: {policy_name}")
                policy_document = iam.get_user_policy(UserName=user_name, PolicyName=policy_name)
                print(f"    Policy Document: {policy_document['PolicyDocument']}")
            
            # List managed policies attached to the user
            attached_user_policies = iam.list_attached_user_policies(UserName=user_name)
            for policy in attached_user_policies['AttachedPolicies']:
                print(f"  Attached User Policy: {policy['PolicyName']}")
            
            # List groups the user belongs to
            groups = iam.list_groups_for_user(UserName=user_name)
            for group in groups['Groups']:
                group_name = group['GroupName']
                print(f"  Group: {group_name}")
                
                # List group policies
                group_policies = iam.list_group_policies(GroupName=group_name)
                for policy_name in group_policies['PolicyNames']:
                    print(f"    Group Policy: {policy_name}")
                    policy_document = iam.get_group_policy(GroupName=group_name, PolicyName=policy_name)
                    print(f"      Policy Document: {policy_document['PolicyDocument']}")
                
                # List managed policies attached to the group
                attached_group_policies = iam.list_attached_group_policies(GroupName=group_name)
                for policy in attached_group_policies['AttachedPolicies']:
                    print(f"    Attached Group Policy: {policy['PolicyName']}")
    
    except Exception as e:
        print(f"Error: {e}")

# Execute the function
list_users_and_permissions()
