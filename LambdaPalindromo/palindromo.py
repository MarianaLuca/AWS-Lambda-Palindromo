import json

def lambda_handler(event, context):
    body = json.loads(event['body'])
    frase = body.get('frase')
    count = 0
    left = frase[0]
    right = frase[len(frase) - 1]
    
    while count < len(frase):
        if left != right:
            return {
                'statusCode': 200,
                'body': json.dumps('Não  um palindromo!')
            }

        left = frase[count]
        right = frase[len(frase) - 1 - count]
        count += 1
    
    return {
        'statusCode': 200,
        'body': json.dumps('É um palindromo!')
    }
