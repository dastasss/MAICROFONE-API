from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.db import connection

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10  # Número de elementos por página
    page_size_query_param = 'page_size'
    max_page_size = 1000  # Tamaño máximo permitido para una página

class NeumannViewSet(viewsets.ViewSet):

    pagination_class = StandardResultsSetPagination  # Configurar la paginación

    def list(self, request):
        paginator = self.pagination_class()
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM neumann")
            rows = cursor.fetchall()
            columns = [col[0] for col in cursor.description]
            result = [dict(zip(columns, row)) for row in rows]
        page = paginator.paginate_queryset(result, request)
        return paginator.get_paginated_response(page)

    def retrieve(self, request, pk=None):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM neumann WHERE id = %s", [pk])
            row = cursor.fetchone()
            if row:
                columns = [col[0] for col in cursor.description]
                result = dict(zip(columns, row))
                return Response(result)
            return Response(status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        data = request.data
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO neumann (title, title_url, image) VALUES (%s, %s, %s)",
                [data['title'], data['title_url'], data['image']]
            )
        return Response(status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        data = request.data
        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE neumann SET title = %s, title_url = %s, image = %s WHERE id = %s",
                [data['title'], data['title_url'], data['image'], pk]
            )
        return Response(status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM neumann WHERE id = %s", [pk])
        return Response(status=status.HTTP_204_NO_CONTENT)


class SennheiserViewSet(viewsets.ViewSet):

    pagination_class = StandardResultsSetPagination  # Configurar la paginación

    def list(self, request):
        paginator = self.pagination_class()
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM sennheiser")
            rows = cursor.fetchall()
            columns = [col[0] for col in cursor.description]
            result = [dict(zip(columns, row)) for row in rows]
        page = paginator.paginate_queryset(result, request)
        return paginator.get_paginated_response(page)

    def retrieve(self, request, pk=None):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM sennheiser WHERE id = %s", [pk])
            row = cursor.fetchone()
            if row:
                columns = [col[0] for col in cursor.description]
                result = dict(zip(columns, row))
                return Response(result)
            return Response(status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        data = request.data
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO sennheiser (title, title_url, image) VALUES (%s, %s, %s)",
                [data['title'], data['title_url'], data['image']]
            )
        return Response(status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        data = request.data
        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE sennheiser SET title = %s, title_url = %s, image = %s WHERE id = %s",
                [data['title'], data['title_url'], data['image'], pk]
            )
        return Response(status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM sennheiser WHERE id = %s", [pk])
        return Response(status=status.HTTP_204_NO_CONTENT)
