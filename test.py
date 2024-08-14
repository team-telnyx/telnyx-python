from telnyx.api_resources.verification import Verification

def example_verification_by_id():
    verification_id = "your_verification_id"
    code = "123456"
    verify_profile_id = "your_verify_profile_id"

    try:
        response = Verification.verification_by_id(
            id=verification_id,
            code=code,
            verify_profile_id=verify_profile_id
        )
        print("Verification successful:", response)
    except Exception as e:
        print("Error during verification:", e)

if __name__ == "__main__":
    example_verification_by_id()
