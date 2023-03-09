
from email import message
from django.db.models.signals import post_save, post_delete

from django.dispatch import receiver


from django.contrib.auth.models import User

from users.views import profile
from .models import Profile

from django.core.mail import send_mail
from django.conf import settings


# @receiver(post_save, sender=Profile)
def creatprofil(sender, instance, created, **kwargs):
    print('profile trigged on')
    if created:
        user = instance
        profile = Profile.objects.create(

            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,


        )

        subject = 'welcome to our website '
        message = 'thank you for you registration ,'

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,

        )


def deleteuser(sender, instance, **kwargs):

    user = instance.user
    user.delete()


def updateuser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()


post_save.connect(updateuser, sender=Profile)
post_save.connect(creatprofil, sender=User)
post_delete.connect(deleteuser, sender=Profile)
