from django.template.loader import render_to_string
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework import viewsets

from app.models import *
from app.serializers import *
from app.constants import *

from django.db.utils import IntegrityError

import json
import django_filters

class AddressView(ModelViewSet):

    """
    Address API.
    """
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['street', 'city', 'state', 'country', 'pincode']

    def get_serializer_class(self):
        if self.action == 'list':
            return AddressReadSerializer
        if self.action == 'retrieve':
            return AddressReadSerializer
        return AddressSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            return Address.objects.none()

        return Address.objects.filter(user = user).order_by('-created')

    def create(self, request, *args, **kwargs):
        user = request.user
        data = request.data.copy()

        serializer = AddressSerializer(data=data, context = {'request': request})
        if serializer.is_valid():
            try:

                address = serializer.save()
                address.user = user
                address.save()
                return JsonResponse({}, status=200)
            except IntegrityError as e:
                return JsonResponse({"error" : "Duplicate address found. Please add a new unique address"}, status=403)
            except Exception as e:
                return JsonResponse({"error" : e}, status=403)
        else:
            return JsonResponse(serializer.errors, status=403)

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = AddressSerializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save(id=instance.id, **serializer.validated_data)
            return JsonResponse({}, status=200)
        except IntegrityError as e:
            return JsonResponse({"error" : "Duplicate address found. Please add a new unique address"}, status=403)
        except Exception as e:
            return JsonResponse({"error" : e}, status=403)


    @action(detail=False, methods=['POST'], name='Delete multiple objects')
    def delete_multiple(self, request):
        ids = request.data.get('ids', [])
        ids = ids.split(",")
        if len(ids) <= 1:
            return JsonResponse({"error" : "use this for deleting more than one address"}, status=403)

        is_int = False
        input = []
        for i in ids:
            if i.isnumeric() == False:
                is_int = True
                break
            else:
                input.append( int(i))
                
            
        if is_int:
            return JsonResponse({"error" : "Invalid inputs. Check your inputs"}, status=403)

        #Ignoring objects that are not yours to delete. Deleting rest.
        #Might be a better idea to throw error.
        Address.objects.filter(user=request.user, id__in=input).delete()
        return JsonResponse({}, status=200)
    
