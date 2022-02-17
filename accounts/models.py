from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    def short_email(self):
        if len(self.email) <= 20:
            return self.email
        return self.email[:21] + "..."
