from django_filters import rest_framework as filters


class ProjectFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr="icontains")
    category = filters.CharFilter(lookup_expr="icontains")
    min_price = filters.CharFilter(field_name="price", lookup_expr="gte")
    max_price = filters.CharFilter(field_name="price", lookup_expr="lte")
    date = filters.DateFilter(field_name="sponsors_due_date", lookup_expr="exact")


class ProjectActivityFilter(filters.FilterSet):
    project = filters.NumberFilter(lookup_expr="exact")


class AllProjectFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr="icontains")
    start_date = filters.DateFilter(field_name="sponsors_due_date", lookup_expr="gte")
    end_date = filters.DateFilter(field_name="sponsors_due_date", lookup_expr="lte")
    category = filters.CharFilter(lookup_expr="icontains")
    min_price = filters.CharFilter(field_name="price", lookup_expr="gte")
    max_price = filters.CharFilter(field_name="price", lookup_expr="lte")
    project_user = filters.NumberFilter(field_name="user", lookup_expr="exact")
