from tests.test_lambda_task01 import LambdaTask01LambdaTestCase


class TestSuccess(LambdaTask01LambdaTestCase):

    def test_success(self):
        expected_value = {
            "statusCode": 200,
            "message": "Hello from Lambda"
        }

        self.assertEqual(self.HANDLER.handle_request(dict(), dict()), expected_value)

