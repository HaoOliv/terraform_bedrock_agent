def get_named_parameter(event, name):
    return next(item for item in event['parameters'] if item['name'] == name)['value']


def gather_evidence(event):
    claim_id = get_named_parameter(event, 'claimId')

    return {
        "response": {
            "claimStatus": "APPROVED",
        }
    }


def lambda_handler(event, context):
    response_code = 200
    action_group = event['actionGroup']
    api_path = event['apiPath']

    # API path routing
    if api_path == '/claims/{claimId}/gather-evidence':
        body = gather_evidence(event)
    else:
        response_code = 400
        body = {"{}::{} is not a valid api, try another one.".format(action_group, api_path)}

    response_body = {
        'application/json': {
            'body': str(body)
        }
    }

    # Bedrock action group response format
    action_response = {
        "messageVersion": "1.0",
        "response": {
            'actionGroup': action_group,
            'apiPath': api_path,
            'httpMethod': event['httpMethod'],
            'httpStatusCode': response_code,
            'responseBody': response_body
        }
    }

    return action_response
