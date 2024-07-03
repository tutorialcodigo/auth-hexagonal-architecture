from infra.cloud.conn import CloudServices
from infra.cloud.nosql import NoSql

service =  CloudServices("dynamodb")
print(service.conn())
db_nosql = NoSql(conn=service.conn())
