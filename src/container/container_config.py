import socket

COUCHDB_URL = 'http://openwhisk:openwhisk@host.docker.internal:5984/'
KAFKA_URL = 'broker:29092'
KAFKA_CHUNK_SIZE = 256 * 1024
KAFKA_NUM_PARTITIONS = 8
KAFKA_NUM_TOPICS = 1
REDIS_HOST = f'{socket.gethostbyname("host.docker.internal")}'
REDIS_PORT = 6379
REDIS_DB = 0
REMOTE_DB = 'KAFKA'

SOCKET_CHUNK_SIZE = 1024 * 1024
