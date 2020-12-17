import os

import telnyx

if __name__ == "__main__":
    telnyx.api_key = os.environ.get("TELNYX_SECRET_KEY")
    phone_number = "fill-me"
    type = "sms"

    verify_profiles = telnyx.VerifyProfile.list()
    print(verify_profiles)
    verification = telnyx.Verification.create(
        phone_number=phone_number,
        type=type,
        verify_profile_id=verify_profiles.data[0].id,
    )
    print(verification)
