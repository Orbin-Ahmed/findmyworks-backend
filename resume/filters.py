from django_filters import rest_framework as filters


class SkillFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr="icontains")


class InstituteFilter(filters.FilterSet):
    institute_type = filters.CharFilter(lookup_expr="exact")
    name = filters.CharFilter(lookup_expr="exact")
