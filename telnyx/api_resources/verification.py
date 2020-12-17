from telnyx.api_resources.abstract import CreateableAPIResource, ListableAPIResource


class Verification(CreateableAPIResource, ListableAPIResource):
    OBJECT_NAME = "verification"

    def verify_by_phone_number(self, code, phone_number):
        return self.request(
            method="post",
            url="/v2/verifications/by_phone_number/{}/actions/verify".format(
                phone_number
            ),
            params={"code": code},
        )
