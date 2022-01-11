import json

print('Loading function')

def lambda_handler(event, context):
	#1. Parse out query string params
	transactionId = event['queryStringParameters']['transactionid']
	transactionType = event['queryStringParameters']['type']
	transactionAmount = event['queryStringParameters']['amount']

	print('transactionId=' + transactionId)
	print('transactionType=' + transactionType)
	print('transactionAmount=' + transactionAmount)

	#2. Construct the body of the response object
	transactionResponse = {}
	transactionResponse['transactionid'] = transactionId
	transactionResponse['type'] = transactionType
	transactionResponse['amount'] = transactionAmount
	transactionResponse['message'] = 'Hello from Lambda land'

	#3. Construct http response object
	responseObject = {}
	responseObject['statusCode'] = 200
	responseObject['headers'] = {}
	responseObject['headers']['Content-Type'] = 'application/json'
	responseObject['headers']['Access-Control-Allow-Origin'] = 'https://heyitslogan.com'
	responseObject['body'] = json.dumps(transactionResponse)

	#4. Return the response object
	return responseObject