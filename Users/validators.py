from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class SimpleCharacterTypeValidator:
    def validate(self, password, user=None):
        if not any(char.isdigit() for char in password):
            raise ValidationError(_("Le mot de passe doit contenir au moins un chiffre."), code='password_no_digit')
        if not any(char.islower() for char in password):
            raise ValidationError(_("Le mot de passe doit contenir au moins une lettre minuscule."),
                                  code='password_no_lower')
        if not any(char.isupper() for char in password):
            raise ValidationError(_("Le mot de passe doit contenir au moins une lettre majuscule."),
                                  code='password_no_upper')
        if not any(char in "!@#$%^&*()_-+=<>?/,.:;{}[]|\"'~" for char in password):
            raise ValidationError(_("Le mot de passe doit contenir au moins un caractère spécial."),
                                  code='password_no_special')

    @staticmethod
    def get_help_text():
        return _(
            "Your password must contain at least one digit, one lowercase letter, "
            "one uppercase letter, and one special character."
        )
