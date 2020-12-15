import os

import telnyx

if __name__ == '__main__':
    profile_name = 'fill-me'

    telnyx.api_key = os.environ.get("TELNYX_SECRET_KEY")
    res = telnyx.VerifyProfile.create(
        name=profile_name,
        messaging_enabled=True,
        default_timeout_secs=600,
    )
    print(res)
    profiles = telnyx.VerifyProfile.list()
    print(len(profiles))