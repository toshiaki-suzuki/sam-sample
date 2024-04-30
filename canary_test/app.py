import requests
import os


def lambda_handler(event, context):
    # 環境変数からAPIのエンドポイントURLを取得
    api_url = os.environ['API_ENDPOINT']

    try:
        # APIにGETリクエストを送信
        response = requests.get(api_url)

        # レスポンスのステータスコードをチェック
        if response.status_code == 200:
            # レスポンスのJSONデータを取得
            data = response.json()

            # 取得したデータを文字列に変換
            api_data = str(data)
        else:
            # APIリクエストが失敗した場合のエラーメッセージ
            api_data = "API request failed with status code: " + \
                str(response.status_code)
    except Exception as e:
        # APIリクエストが例外を発生させた場合のエラーメッセージ
        api_data = "API request failed with an exception: " + str(e)

    html_content = """
    <html>
        <head>
            <title>Canary Test</title>
        </head>
        <body>
            <h1>CanaryTest: {}</h1>
        </body>
    </html>
    """.format(api_data)

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/html',
        },
        'body': html_content
    }
