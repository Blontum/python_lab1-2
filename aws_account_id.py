# Writing a program that will display account id from an arn below
# "arn:aws:iam::123456789012:user/Development/product_1234/*"

# cake3: aws-account-id.py

# Defining the ARN string
arn = "arn:aws:iam::123456789012:user/Development/product_1234/*"

# spliting the ARN string using ':' as the separator

arn_parts = arn.split(':')

# the account ID will be the 5th element(index4) in the resulting list:

account_id = arn_parts[4]
# Deplay result:
print(f" the arn splitting is {arn_parts} \n")
print(f"The aws account id is {account_id}")