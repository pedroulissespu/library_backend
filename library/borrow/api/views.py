from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions

from .serializers import BorrowSerializer
from ..models import Borrow


class BorrowViewSet(viewsets.ModelViewSet):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'book', 'borrow_date']
