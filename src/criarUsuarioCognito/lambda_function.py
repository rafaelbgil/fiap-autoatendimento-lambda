import boto3
from botocore.config import Config



def lambda_handler(event, context):
    config = Config(region_name='us-east-1')
    client = boto3.client('cognito-idp', config=config)
    attributos = [
        {
            'Name': 'name',
            'Value': event['nome']
        },
        {
            'Name': 'email',
            'Value': event['email']
        }
        ,
        {
            'Name': 'email_verified',
            'Value': 'true'
        }
    ]

    try:
        response = client.admin_create_user(
            UserPoolId='us-east-1_EHvshsyoV',
            Username=event['cpf'],
            UserAttributes=attributos,
            ForceAliasCreation=False,
            MessageAction='SUPPRESS',
        )


        response = client.admin_set_user_password(
            UserPoolId='us-east-1_EHvshsyoV',
            Username=event['cpf'],
            Password=event['senha'],
            Permanent=True
        )


    except:
        return {
            'statusCode': 400,
            'body': 'error nao foi possivel criar o usuario'
        }
    client.close()
    return {
        'statusCode': 201,
        'body': response.__str__()
    }
