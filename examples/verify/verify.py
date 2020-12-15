import os

import telnyx

if __name__ == "__main__":
    telnyx.api_key = os.environ.get("TELNYX_SECRET_KEY")
    verification_id = "fill-me"
    code = "fill-me"
    phone_number = "fill-me"

    verification = telnyx.Verification.retrieve(verification_id)
    print("Verification status: {}".format(verification))
    verify_resp = verification.verify_by_phone_number(
        code=code, phone_number=phone_number
    )
    if verify_resp["data"]["response_code"] == "accepted":
        print("Verify successful!")
    else:
        print("There was an issue verifying: {}".format(verify_resp["data"]))
