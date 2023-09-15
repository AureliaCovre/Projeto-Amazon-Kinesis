import boto3
import json

# Criando o cliente
cliente = boto3.client('kinesis',aws_access_key_id='XXXXXXXXXXXXXX', aws_secret_access_key='XVXVXVXVXVXVVX', region_name='us-east-2' )

# Criando objeto dicionario:
registro = {'idvendedor' : '999', 'name' : 'Nelson'}

resposta = cliente.put_record(
    StreamName='fluxo_stream',
    Data=json.dumps(registro),
    PartitionKey='02'
)
print(resposta)
