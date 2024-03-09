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

    if 'cpf' in event:
        attributos.append(
            {'Name': 'custom:cpf',
             'Value': event['cpf']
             }
        )
    try:
        client.admin_create_user(
            UserPoolId='us-east-1_aEdl4I2z8',
            Username=event['email'],
            UserAttributes=attributos,

            ForceAliasCreation=False,
            MessageAction='SUPPRESS',

            ClientMetadata={
                'string': 'string'
            }
        )

        response = client.admin_set_user_password(
            UserPoolId='us-east-1_aEdl4I2z8',
            Username=event['email'],
            Password=event['senha'],
            Permanent=True
        )
    except:
        return {
            'statusCode': 400,
            'body': 'error'
        }
    client.close()
    return {
        'statusCode': 201,
        'body': response.__str__()
    }
