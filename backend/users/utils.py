import uuid as uid
from functools import wraps 
from rest_framework.response import Response
from rest_framework import status 

def validate_uuid_param(view):
  @wraps(view) 
  def wrapper(self, request, uuid, *args, **kwargs):
    try:
      uuid_obj = uid.UUID(str(uuid))
    except ValueError:
      return Response({"error": "Invalid UUID format"}, status=status.HTTP_400_BAD_REQUEST)
    return view(self, request, uuid_obj, *args, **kwargs)
  return wrapper 