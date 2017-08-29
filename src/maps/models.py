import re, itertools
from collections import defaultdict
from functools import partial 


from django.db.models.signals import post_save
from django.dispatch import receiver  
from django.db import models
from django.contrib.auth.models import User
import boto3 
from boto3 import client
from django.conf import settings



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
  ('UG', 'Uganda'),
  ('ZM', 'Zambia'),
  ('VFI', 'VisionFund International'),
  ('AFR', 'Africa Regional'),
  ('ASR', 'Asia Regional'),
  ('LAR', 'Latin America Regional'),
)

class Map(models.Model):
#    class Meta:
#        permissions = (
#          ("KE", "Kenya Permission"),
#        )
    
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
    
class s3resource():
    def __init__(self):
        self.conn = boto3.client(
            's3',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        )
        self.all_list = []    
    
    def return_maps(self, country):
        mapmatrix = self.conn.list_objects(Bucket='wmicopy', Prefix= 'maps/' + country + '/')['Contents']
        path_id = []
        for file in mapmatrix:
            key_string = file['Key']
            if not key_string.endswith('/'):
                path_id.append(key_string)

        url_list = []
        for file in mapmatrix:
            key_string = file['Key']
            if not key_string.endswith('/'):
                url_string = 'https://s3-us-west-2.amazonaws.com/wmicopy/' + key_string
                url_list.append( url_string)

        country_list = []
        for file in mapmatrix:
            key_string = file['Key']
            if not key_string.endswith('/'):
                country_list.append(re.findall(r'(\w+)', key_string)[1])

        theme_list = []
        for file in mapmatrix:
            key_string = file['Key']
            if not key_string.endswith('/'):
                theme_list.append(re.findall(r'(\w+)', key_string)[2])

        name_list = []
        for file in mapmatrix:
            key_string = file['Key']
            if not key_string.endswith('/'):
#                match = re.search(r'([A-Z])\w+([-\s+])?\w+', key_string) **Old regex**
                match = re.search(r'[A-Z][\w\s:-]+', key_string)
                if match:
                    name_list.append(match.group(0))
  
        
        all_list = [] #combine all the lists
        all_list.append(path_id)
        all_list.append(country_list)
        all_list.append(theme_list)
        all_list.append(url_list)
        all_list.append(name_list)
        
        link_list = []
        for i in range(len(all_list[0])):
            url_dict = {all_list[3][i]:all_list[4][i]}
            theme_dict = {all_list[2][i]:url_dict}
            link_list.append({all_list[1][i]:theme_dict})
        return(link_list)
		

    def country_filter(self, country):
        output = []
        link_list = self.return_maps(country)
        for i in link_list:    
          for key, value in i.items():
            if key == country:
              output.append(value)
        return output
