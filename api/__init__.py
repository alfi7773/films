# class UpdateFilmSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Film
#         fields = '__all__'  # Исправлено с field на fields
#
#     def update(self, instance, validated_data):
#         # Удаляем данные атрибутов и изображений из validated_data
#         attributes = validated_data.pop('attributes', None)
#         images = validated_data.pop('image', None)
#
#         # Обновляем оставшиеся поля объекта instance
#         for attr, value in validated_data.items():
#             setattr(instance, attr, value)
#         instance.save()
#
#         # Обновляем или пересоздаём связанные атрибуты
#         if attributes:
#             FilmAttribute.objects.filter(film=instance).delete()
#             for attribute in attributes:
#                 FilmAttribute.objects.create(film=instance, **attribute)
#
#         # Обновляем или пересоздаём изображения
#         if images:
#             FilmImage.objects.filter(film=instance).delete()
#             file_images = []
#             for image in images:
#                 try:
#                     file = base64_to_image_file(image, uuid.uuid4())
#                     file_images.append(file)
#                 except Exception as e:
#                     raise serializers.ValidationError({'images': ['Загрузите корректное изображение']})
#
#             for file in file_images:
#                 film_image = FilmImage.objects.create(film=instance)
#                 film_image.image.save(file.name, file)
#
#         return instance
