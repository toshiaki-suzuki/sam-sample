
def lambda_handler(event, context):
    # 0~9の値をランダムで生成して、それを文字列に変換して返す
    import random
    return {
        'statusCode': 200,
        'body': str(random.randint(0, 9))
    }
