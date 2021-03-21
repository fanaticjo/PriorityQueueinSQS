import boto3

client = boto3.client('dynamodb')


class dynamodbReader:
    def __init__(self, tablename=None):
        self.tablename = tablename

    def selectquery(self, message):
        message = message.replace("tablename", self.tablename)
        print(message)
        response = client.execute_statement(Statement=message)
        result=response.get('Items',[])
        return {
                'result':result,
                 'count':len(result)
        }

    def insertquery(self,message):
        message=message.replace('tablename',self.tablename)
        response=client.execute_statement(Statement=message)
        return response

    def updatequery(self,message):
        message = message.replace('tablename', self.tablename)
        response = client.execute_statement(Statement=message)
        return response




if __name__ == "__main__":
    db = dynamodbReader("priority")
    print(db.selectquery(
        """select * from {tablename} where begins_with("pk",'high') and begins_with("sk",'scheduled_started')"""))
