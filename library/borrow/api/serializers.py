from rest_framework import serializers
from ..models import Borrow


class BorrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrow
        fields = ["id", "user", "book", "borrow_date", "return_date"]
