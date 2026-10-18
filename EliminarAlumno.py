import boto3

def lambda_handler(event, context):
    # Entrada (json)
    print(event)
    tenant_id = event['body']['tenant_id']
    alumno_id = event['body']['alumno_id']
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')
    response = table.delete_item(
        Key={
            'tenant_id': tenant_id,
            'alumno_id': alumno_id
        },
        ReturnValues='ALL_OLD'
    )
    print(response)
    # Salida (json)
    if 'Attributes' not in response:
        return {
            'statusCode': 404,
            'mensaje': 'Alumno no encontrado'
        }
    return {
        'statusCode': 200,
        'mensaje': 'Alumno eliminado',
        'alumno': response['Attributes']
    }
