import hashlib

MERCHANT_ID = "M353109"
USERNAME = "M353109"
PASSWORD = "Myairpay@1234"
SECRET_KEY = "YOUR_SECRET_KEY"

RETURN_URL = "http://localhost:5000/payment-success"
FAIL_URL = "http://localhost:5000/payment-failure"


def generate_checksum(data):

    raw = (
        MERCHANT_ID
        + data["orderid"]
        + str(data["amount"])
        + data["email"]
        + SECRET_KEY
    )

    checksum = hashlib.sha256(raw.encode()).hexdigest()

    return checksum


def verify_checksum(post_data):

    received = post_data.get("checksum")

    raw = (
        MERCHANT_ID
        + post_data.get("TRANSACTIONID","")
        + post_data.get("AMOUNT","")
        + SECRET_KEY
    )

    calc = hashlib.sha256(raw.encode()).hexdigest()

    return received == calc