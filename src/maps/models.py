from django.db.models.signals import post_save
from django.dispatch import receiver  
from django.db import models
from django.contrib.auth.models import User

ORGANIZATION = (
  ('', '--Select Organization--'),
  ('KH', 'Cambodia'),
  ('EC', 'Ecuador'),
  ('HN', 'Honduras'),
  ('KE', 'Kenya'),
  ('MM', 'Myanmar'),
  ('PH', 'Philippines'),
  ('LK', 'Sri Lanka'),
  ('TZ', 'Tanzania'),
  ('UG', 'Ugnada'),
  ('ZM', 'Zambia'),
  ('VFI', 'VisionFund International'),
  ('AFR', 'Africa Regional'),
  ('ASR', 'Asia Regional'),
  ('LAR', 'Latin America Regional'),
)

class Map(models.Model):
    class Meta:
        permissions = (
          ("KE", "Kenya Permission"),
        )
    
    linkto_map = models.TextField()
  
    def __str__(self):
      return self.linkto_map
  
class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    organization = models.CharField(max_length=3, choices=ORGANIZATION, default='None')
    
    def __str__(self):
      return self.user.first_name
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
      Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
