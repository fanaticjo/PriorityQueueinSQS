from Lambda.Processor import processEvents

def lambda_handler(event,context):
    processEvents(event,context).makeAudit().checkPriority().run()




if __name__=="__main__":
    event = {
            "Records": [
                {
                    "messageId": "6fd7392e-ebf6-4977-8e8b-09f25edf8d11213123819",
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
    lambda_handler(event, '1')