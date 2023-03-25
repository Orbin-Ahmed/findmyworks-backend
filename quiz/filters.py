from django_filters import rest_framework as filters


class SkillQuizResultFilter(filters.FilterSet):
    skill = filters.NumberFilter(lookup_expr="exact")
