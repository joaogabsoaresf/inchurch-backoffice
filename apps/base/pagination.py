from ninja.pagination import PaginationBase
from ninja import Schema
from typing import List, Any, Optional
import math
from urllib.parse import urlencode

class CustomPagination(PaginationBase):
    items_attribute = "results"

    class Input(Schema):
        page: int = 1
        page_size: Optional[int] = 15

    class Output(Schema):
        results: List[Any]
        total: int
        page: int
        page_size: int
        total_pages: int
        next: Optional[str]
        previous: Optional[str]
        
    def paginate_queryset(self, queryset, pagination: Input, request, **params):
        page = pagination.page
        page_size = pagination.page_size or 15

        total = queryset.count()
        total_pages = math.ceil(total / page_size)
        start = (page - 1) * page_size
        end = start + page_size

        base_url = request.path
        query_params = request.GET.dict()

        def build_url(page_number):
            query_params.update({"page": page_number, "page_size": page_size})
            relative_url = f"{base_url}?{urlencode(query_params)}"
            return request.build_absolute_uri(relative_url)

        next_url = build_url(page + 1) if page < total_pages else None
        previous_url = build_url(page - 1) if page > 1 else None

        return {
            "results": queryset[start:end],
            "total": total,
            "page": page,
            "page_size": page_size,
            "total_pages": total_pages,
            "next": next_url,
            "previous": previous_url,
        }