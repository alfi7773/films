from rest_framework.generics import GenericAPIView

class SerializerByMethodMixin:
    serializer_classes = {}
    
    def get_serializer_class(self):
        serializer = self.serializer_classes.get(self.request.method)
        
        if serializer is None:
            serializer = super().get_serializer_class()
        
        return serializer
    
    
class ResponseSerializerMixin:
    response_serializer = None

    def get_response_serializer(self, *args, **kwargs):
        assert self.response_serializer is not None, (
                "'%s' should either include a `response_serializer` attribute"
                % self.__class__.__name__
        )

        serializer_class = self.response_serializer
        kwargs.setdefault('context', self.get_serializer_context())
        return serializer_class(*args, **kwargs)


class SuperGenericAPIView(SerializerByMethodMixin, ResponseSerializerMixin, GenericAPIView): ...




# from rest_framework.generics import GenericAPIView


# class SerializerByMethodMixin:
#     serializer_classes = {}

#     def get_serializer_class(self):
#         serializer = self.serializer_classes.get(self.request.method)

#         if serializer is None:
#             serializer = super().get_serializer_class()

#         return serializer


# class ResponseSerializerMixin:
#     response_serializer = None

#     def get_response_serializer(self, *args, **kwargs):
#         assert self.response_serializer is not None, (
#                 "'%s' should either include a `response_serializer` attribute"
#                 % self.__class__.__name__
#         )

#         serializer_class = self.response_serializer
#         kwargs.setdefault('context', self.get_serializer_context())
#         return serializer_class(*args, **kwargs)


# class SuperGenericAPIView(SerializerByMethodMixin, ResponseSerializerMixin, GenericAPIView): ...
