from django_codemod.constants import DJANGO_2_0, DJANGO_3_0
from django_codemod.visitors.base import BaseSimpleFuncRenameTransformer


class LRUCacheTransformer(BaseSimpleFuncRenameTransformer):
    """Resolve deprecation of ``django.utils.lru_cache.lru_cache``."""

    deprecated_in = DJANGO_2_0
    removed_in = DJANGO_3_0
    rename_from = "django.utils.lru_cache.lru_cache"
    rename_to = "functools.lru_cache"
