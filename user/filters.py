from django_filters import rest_framework as filters


class UserFilter(filters.FilterSet):
    email = filters.CharFilter(lookup_expr="exact")


class TalentFilter(filters.FilterSet):
    first_name = filters.CharFilter(lookup_expr="icontains")
    email = filters.CharFilter(lookup_expr="icontains")
    profession = filters.CharFilter(lookup_expr="icontains")
    address = filters.CharFilter(lookup_expr="icontains")
