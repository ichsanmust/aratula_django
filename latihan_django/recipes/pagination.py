from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'pageSize'
    page_query_param = 'pageNumber'

    def get_paginated_response(self, data):
        return Response({
            # 'my_custom_field': ....,
            'total': self.page.paginator.count,
            'data': data,
            'message': 'Success',
            'statusCode': 200,
            'status': 'OK',
            'next': self.get_next_link(),
            'previous': self.get_previous_link()
        })