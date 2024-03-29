from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# The following code was written based on the Code Institute Boutique Ado
# walkthrough and customised to fit this application
class UserProfile(models.Model):
    """ A user profile model for default info and order history """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_street_address_1 = models.CharField(max_length=80,
                                                null=True, blank=True)
    default_street_address_2 = models.CharField(max_length=80,
                                                null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40,
                                            null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """ Create or update the user profile """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: Just save the profile
    instance.userprofile.save()
