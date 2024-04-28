
def lambda_handler(event, context):
    html_content = """
    <html>
        <head>
            <title>Canary Test</title>
        </head>
        <body>
            <h1>CanaryTest</h1>
        </body>
    </html>
    """

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/html',
        },
        'body': html_content
    }
