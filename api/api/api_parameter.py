from drf_yasg import openapi

authorization = openapi.Parameter('Authorization', openapi.IN_HEADER,
                                  description="Bearer <access_token>", type=openapi.TYPE_STRING)

csrf_authorization = openapi.Parameter('X-CSRFToken', openapi.IN_HEADER,
                                       description="<csrf_token>", type=openapi.TYPE_STRING)
page = openapi.Parameter('page', openapi.IN_QUERY,
                         description="page number", type=openapi.TYPE_INTEGER)
page_size = openapi.Parameter(
    'page_size', openapi.IN_QUERY, description="page size", type=openapi.TYPE_INTEGER)
start = openapi.Parameter('start', openapi.IN_QUERY,
                          description="start UNIX UTC Timestamp", type=openapi.TYPE_INTEGER)
end = openapi.Parameter('end', openapi.IN_QUERY,
                        description="end UNIX UTC Timestamp", type=openapi.TYPE_INTEGER)

server_error_dict = {'message': "Server error."}
