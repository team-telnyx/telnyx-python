# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .comment_type import CommentType as CommentType
from .comment_list_params import CommentListParams as CommentListParams
from .comment_create_params import CommentCreateParams as CommentCreateParams
from .reference_input_param import ReferenceInputParam as ReferenceInputParam
from .dir_phone_number_status import DirPhoneNumberStatus as DirPhoneNumberStatus
from .phone_number_add_params import PhoneNumberAddParams as PhoneNumberAddParams
from .reference_create_params import ReferenceCreateParams as ReferenceCreateParams
from .reference_update_params import ReferenceUpdateParams as ReferenceUpdateParams
from .phone_number_list_params import PhoneNumberListParams as PhoneNumberListParams
from .phone_number_remove_params import PhoneNumberRemoveParams as PhoneNumberRemoveParams
from .verify_email_confirm_params import VerifyEmailConfirmParams as VerifyEmailConfirmParams
from .phone_number_batch_list_params import PhoneNumberBatchListParams as PhoneNumberBatchListParams

if TYPE_CHECKING:
    from .dir import Dir as Dir
    from .reference import Reference as Reference
    from .dir_comment import DirComment as DirComment
    from .reference_list import ReferenceList as ReferenceList
    from .dir_phone_number import DirPhoneNumber as DirPhoneNumber
    from .rejection_reason import RejectionReason as RejectionReason
    from .phone_number_batch import PhoneNumberBatch as PhoneNumberBatch
    from .comment_create_response import CommentCreateResponse as CommentCreateResponse
    from .phone_number_add_response import PhoneNumberAddResponse as PhoneNumberAddResponse
    from .reference_update_response import ReferenceUpdateResponse as ReferenceUpdateResponse
    from .phone_number_remove_response import PhoneNumberRemoveResponse as PhoneNumberRemoveResponse
    from .email_verification_status_wrapped import EmailVerificationStatusWrapped as EmailVerificationStatusWrapped
    from .phone_number_batch_retrieve_response import (
        PhoneNumberBatchRetrieveResponse as PhoneNumberBatchRetrieveResponse,
    )


def __getattr__(name: str) -> Any:
    if name == "Dir":
        from .dir import Dir

        return Dir
    if name == "DirComment":
        from .dir_comment import DirComment

        return DirComment
    if name == "CommentCreateResponse":
        from .comment_create_response import CommentCreateResponse

        return CommentCreateResponse
    if name == "PhoneNumberBatch":
        from .phone_number_batch import PhoneNumberBatch

        return PhoneNumberBatch
    if name == "PhoneNumberBatchRetrieveResponse":
        from .phone_number_batch_retrieve_response import PhoneNumberBatchRetrieveResponse

        return PhoneNumberBatchRetrieveResponse
    if name == "DirPhoneNumber":
        from .dir_phone_number import DirPhoneNumber

        return DirPhoneNumber
    if name == "RejectionReason":
        from .rejection_reason import RejectionReason

        return RejectionReason
    if name == "PhoneNumberAddResponse":
        from .phone_number_add_response import PhoneNumberAddResponse

        return PhoneNumberAddResponse
    if name == "PhoneNumberRemoveResponse":
        from .phone_number_remove_response import PhoneNumberRemoveResponse

        return PhoneNumberRemoveResponse
    if name == "Reference":
        from .reference import Reference

        return Reference
    if name == "ReferenceList":
        from .reference_list import ReferenceList

        return ReferenceList
    if name == "ReferenceUpdateResponse":
        from .reference_update_response import ReferenceUpdateResponse

        return ReferenceUpdateResponse
    if name == "EmailVerificationStatusWrapped":
        from .email_verification_status_wrapped import EmailVerificationStatusWrapped

        return EmailVerificationStatusWrapped
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
