from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Declaration
from main.serializers import DeclarationModelSerializer
from main.service.declaration.selectors import get_all_declarations
from main.service.declaration.use_cases import insert_declaration_to_table
from main.service.google_sheets.google_sheets_service import get_data_from_googlesheets


def index(request):
    rows = Declaration.objects.all()
    return render(request, 'main/index.html', {'rows': rows})


class DeclarationApiView(APIView):
    serializer_class = DeclarationModelSerializer

    def get(self, request):
        table_from_google = get_data_from_googlesheets()
        insert_declaration_to_table(table_from_google)
        return Response(self.serializer_class(get_all_declarations(), many=True).data, status=status.HTTP_200_OK)


def update_table(request):
    table_from_google = get_data_from_googlesheets()
    insert_declaration_to_table(table_from_google)
    return redirect('index')
