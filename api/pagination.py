from rest_framework.pagination import PageNumberPagination

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_query_param = '_page'
    page_size_query_param = '_page_size'
    max_page_size = 1000
