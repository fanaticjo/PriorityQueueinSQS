import json
from Utils.uniquegen import generator
from Utils.ResultParser import resultparser
from Utils.DynamoDbReader import dynamodbReader
from datetime import datetime
import time
from random import choice

MAX_RESOURCE = 4


class processEvents(resultparser):
    def __init__(self, event, context):
        super().__init__(event)
        self.process = None
        self.uuid = None
        self.run_time = datetime.now().strftime("%Y%m%d_%H%M%s")
        self.run_date = datetime.now().strftime("%Y-%m-%d")
        self.id = None

    def makeAudit(self):
        record = {
            'pk': f'{self.messageid}',
            'sk': f'{self.priority}#{self.run_date}',
            'executiondate': self.run_date,
            'run_message': self.body,
            'priority': self.priority,
            'messageid': self.messageid,
            'attributes': self.attributes,
            'execution_time': self.run_time,
            'schedulor': 'scheduled'
        }
        dynamodbReader("priority").insertquery(f"""insert into tablename 
                                                value {record}""")
        return self

    @property
    def checkResource(self):
        if self.priority == 'high':
            response = dynamodbReader("priority.search_process").selectquery(f"""select sk from tablename
             where schedulor='running'""")
            if response.get('count') < MAX_RESOURCE:
                self.process = True
            else:
                raise Exception('Resource Not aviliable waiting for resource')
        else:
            response = dynamodbReader("priority.search_process").selectquery(
                f"""select pk from tablename where schedulor='scheduled' or schedulor='running'""")
            if response.get('count') < MAX_RESOURCE:
                self.process = True
            else:
                raise Exception('Resource Not aviliable for lower priority waiting for resource')

    def checkPriority(self):
        self.checkResource
        return self

    def pick_resource(self):
        self.id = choice(['i-jk'])

    def update_process(self):
        self.pick_resource()
        dynamodbReader("priority").updatequery(f"""update tablename set id='{self.id}' 
                                                  set schedulor='running'
                                                  where pk='{self.messageid}' and sk='{self.priority}#{self.run_date}'""")

    def complete_process(self):
        dynamodbReader("priority").updatequery(f"""update tablename  
                                                          set schedulor='processed'
                                                          where pk='{self.messageid}' and sk='{self.priority}#{self.run_date}'""")

    def startProcess(self):
        time.sleep(10)
        #self.complete_process()


    def run(self):
        if self.process:
            self.update_process()
            self.startProcess()
            return 0
        else:
            return 1


if __name__ == "__main__":
    event = {
        "Records": [
            {
                "messageId": "6fd7392e-ebf6-4977-8e8b-09f25edf8d44",
                "receiptHandle": "AQEBwcEG447BqnfBD7+KEF2z+m+1VeLumrbZsR9rHgSAkFKpLARHaKrhyDioqhKdXYKWh/U4PPPCc51paUzdl9IDPCj9miHjiNhX8m2+R2QUYlwcOpFU4L7xvcc8PencTCNnwgKeKu6UrdXyTN1g6nOfmkUheMZx5YvZkh13CpWDoN7uFM06e7Xb76rF6ISBP6aaMh2pbTr8pOaflXri3usIi0R1qHmQKKTUdQw8Kxq8WiLFNq1plH+DDEiae9foxWHHi0/13cYmoBeYBF8JscEGlPGzuFI904MAKrmSnyIpPhc=",
                "body": "{\n  \"hello\":\"123\"\n}",
                "attributes": {
                    "ApproximateReceiveCount": "1",
                    "SentTimestamp": "1616243614969",
                    "SequenceNumber": "37307246512851167488",
                    "MessageGroupId": "1k;jf;a",
                    "SenderId": "AIDARXSIOE6S5JRGNYIQ6",
                    "MessageDeduplicationId": "ajd;aj;d",
                    "ApproximateFirstReceiveTimestamp": "1616243614969"
                },
                "messageAttributes": {
                    "priority": {
                        "stringValue": "high",
                        "stringListValues": [

                        ],
                        "binaryListValues": [

                        ],
                        "dataType": "String"
                    }
                },
                "md5OfMessageAttributes": "929d0e72e13b38d32202d64b5b07023c",
                "md5OfBody": "e981b99ea38f201157eb683b8356dc09",
                "eventSource": "aws:sqs",
                "eventSourceARN": "arn:aws:sqs:ap-south-1:944556464382:HighThrouputConsumer.fifo",
                "awsRegion": "ap-south-1"
            }
        ]
    }
    processEvents(event, 1)
