from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    stripe_id = models.CharField(max_length=40, default='', blank=True)
    free_trial = models.BooleanField(default=True, blank=True)
    paying_subscription = models.BooleanField(default=False, blank=True)
    progress = models.IntegerField(default=0)

    @property
    def subscription_active(self):
        return self.subscription_end > timezone.now()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
