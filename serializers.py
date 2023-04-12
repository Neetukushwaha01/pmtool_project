from rest_framework import serializers
from .models import *


class ProjectAttachmentSerializer( serializers.ModelSerializer ):
    class Meta:
        model = ProjectAttachment
        fields = ['attachment']


class ProjectDetailsSerializer( serializers.ModelSerializer ):
    product_attachment = ProjectAttachmentSerializer( many=True, read_only=True )

    class Meta:
        model = ProjectDetails
        fields = '__all__'


# this code for viedo aad  start
class ViedoProjectSerializer( serializers.ModelSerializer ):
    class Meta:
        model = ViedoProject
        fields = '__all__'


class Loom_linkAddsSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Loom_linkAdd
        fields = '__all__'


class Attachment_viedoAddSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Attachment_viedoAdd
        fields = '__all__'
# this code for viedo aad  end

# def to_representation(self, instance):
#     # Call the parent to_representation method
#     data = super().to_representation(instance)
#     # Add the new field to the serialized data
#     data['product_attachment'] = ''
#     return data
