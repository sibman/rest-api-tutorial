# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.product import Product
from openapi_server import util

from openapi_server.models.product import Product  # noqa: E501

class GetAllProducts200ResponseAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data=None):  # noqa: E501
        """GetAllProducts200ResponseAllOf - a model defined in OpenAPI

        :param data: The data of this GetAllProducts200ResponseAllOf.  # noqa: E501
        :type data: List[Product]
        """
        self.openapi_types = {
            'data': List[Product]
        }

        self.attribute_map = {
            'data': 'data'
        }

        self._data = data

    @classmethod
    def from_dict(cls, dikt) -> 'GetAllProducts200ResponseAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The getAllProducts_200_response_allOf of this GetAllProducts200ResponseAllOf.  # noqa: E501
        :rtype: GetAllProducts200ResponseAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this GetAllProducts200ResponseAllOf.


        :return: The data of this GetAllProducts200ResponseAllOf.
        :rtype: List[Product]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this GetAllProducts200ResponseAllOf.


        :param data: The data of this GetAllProducts200ResponseAllOf.
        :type data: List[Product]
        """

        self._data = data