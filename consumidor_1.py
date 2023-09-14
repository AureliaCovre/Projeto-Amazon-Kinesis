import boto3

# Criando o cliente
cliente = boto3.client('kinesis',aws_access_key_id='AKIAWLILQOJGY23U6CXY', aws_secret_access_key='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', region_name='us-east-2' )

# Criando um Shard
shard = cliente.get_shard_iterator(
    StreamName="fluxo_stream",
    ShardId = 'shardId-000000000002',
    ShardIteratorType = 'LATEST'
)["ShardIterator"]

#Monitorando o objeto
while shard is not None:
    resultado = cliente.get_records(ShardIterator=shard)
    registros = resultado['Records']
    shard = resultado["NextShardIterator"]
    for registro in registros:
        print(registro["SequenceNumber"])
        print(registro["ApproximateArrivalTimestamp"])
        print(registro["PartitionKey"])
        print(registro["Data"])
        
