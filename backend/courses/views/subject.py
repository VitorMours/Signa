from rest_framework.views import APIView 
from courses.services.subject_service import SubjectService 
from courses.serializers.subject_serializer import SubjectSerializer
from rest_framework.request import Request 
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status 
from uuid import UUID

class SubjectView(APIView):
  permission_classes = [IsAuthenticated]
  authentication_classes = [JWTAuthentication]
  
  def get_permissions(self) -> None:
    if self.request.method == "POST":
      return [AllowAny()]
    return [IsAuthenticated()]

  @swagger_auto_schema(responses = {200: SubjectSerializer})
  def get(self, request: Request) -> Response:
    subjects = SubjectService.get_all_subjects()
    serializer = SubjectSerializer(subjects, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


  @swagger_auto_schema(request_body = SubjectSerializer, responses = {201: SubjectSerializer})
  def post(self, request: Request) -> Response:
    serializer = SubjectSerializer(data=request.data)

    if not serializer.is_valid():
      return Response(serializer.errors, stauts=status.HTTP_400_BAD_REQUEST)

    try:
      subject = SubjectService.create_subject(serializer.validated_data)
      response_json = SubjectSerializer(subject)
      return Response(response_json.data, status=status.HTTP_201_CREATED)
    except Exception as e:
      return Response({"error": str(e)}, status = status.HTTP_400_BAD_REQUEST)

class SubjectSingleView(APIView):
  permissions_classes = [IsAuthenticated]
  authentication_classes = [JWTAuthentication]

  @swagger_auto_schema(responses = {200: SubjectSerializer})
  def get(self, request: Request, uuid: str) -> Response:
    subject = SubjectService.get_subject_by_id(uuid)
    
    if not subject:
      return Response(
        {"detail":"Subject not found"}, 
        status=status.HTTP_404_NOT_FOUND
      )
    
    serializer = SubjectSerializer(subject)
    return Response(serializer.data, status = status.HTTP_200_OK)

  @swagger_auto_schema(responses = {201: SubjectSerializer})
  def patch(self, request: Request, uuid: str) -> Response:
    subject = SubjectService.get_subject_by_id(uuid)
    
    if not subject:
      return Response(
        {"detail":"Subject from id not found"}, 
        status=status.HTTP_404_NOT_FOUND
      )
      
    serializer = SubjectSerializer(subject, data=request.data, partial=True)
    if not serializer.is_valid():
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    updated_serializer = SubjectService.update_subject(subject, serializer.validated_data)
    output = SubjectSerializer(updated_serializer)
    return Response(output.data, status=status.HTTP_200_OK)
    
  @swagger_auto_schema(responses = {204: SubjectSerializer})
  def delete(self, request: Request, uuid: str) -> Response:
    subject = SubjectService.get_subject_by_id(uuid)
    if not subject:
      return Response(
        {"detail":"Subject from id not found"},
        status=status.HTTP_404_NOT_FOUND
      )
    SubjectService.deactivate_subject(uuid)
    return Response(status=status.HTTP_204_NO_CONTENT)



