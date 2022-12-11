from rest_framework import serializers

from app.models import Teacher, Exercise, Student, Group


class TeacherModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'name', 'last_name', 'email']
        read_only_fields = ['id']

    def validate_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError(
                'Name should contains only letters!'
            )
        return value

    def validate_last_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError(
                'Last name should contains only letters!'
            )
        return value


class ExerciseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True)
    description = serializers.CharField(required=True)

    def create(self, validated_data):
        return Exercise.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'last_name', 'email', 'school', 'edu_level', 'phone']
        read_only_fields = ['id']

    def validate_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError(
                'Name should contains only letters!'
            )
        return value

    def validate_last_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError(
                'Last name should contains only letters!'
            )
        return value


class GroupSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    def create(self, validated_data):
        return Group.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
