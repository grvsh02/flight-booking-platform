# quickstart.schema.py

import strawberry
from gqlauth.user import arg_mutations


@strawberry.type
class UserMutations:
    register = arg_mutations.Register.field
    verify_account = arg_mutations.VerifyAccount.field
    resend_activation_email = arg_mutations.ResendActivationEmail.field
    send_password_reset_email = arg_mutations.SendPasswordResetEmail.field
    password_reset = arg_mutations.PasswordReset.field
    password_set = arg_mutations.PasswordSet.field
    password_change = arg_mutations.PasswordChange.field
    archive_account = arg_mutations.ArchiveAccount.field
    delete_account = arg_mutations.DeleteAccount.field
    update_account = arg_mutations.UpdateAccount.field
    send_secondary_email_activation = arg_mutations.SendSecondaryEmailActivation.field
    verify_secondary_email = arg_mutations.VerifySecondaryEmail.field
    swap_emails = arg_mutations.SwapEmails.field

    token_auth = arg_mutations.ObtainJSONWebToken.field
    verify_token = arg_mutations.VerifyToken.field
    refresh_token = arg_mutations.RefreshToken.field
    revoke_token = arg_mutations.RevokeToken.field
