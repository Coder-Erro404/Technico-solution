from technico_app.models import blog
from django.contrib.auth.models import User
import django_filters
 
class UserFilter(django_filters.FilterSet):
    class Meta:
        model = blog
        fields = ['cat', ]
       