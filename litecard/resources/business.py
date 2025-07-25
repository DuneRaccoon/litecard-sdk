"""
Business resource for the Litecard API.
"""

from typing import Dict, Any
from .base import LitecardResource
from ..models import Business as BusinessModel


class Business(LitecardResource):
    """
    Business resource for managing business information.
    """
    
    endpoint = "business"
    model_class = BusinessModel
