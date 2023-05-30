"""Replaces the PII text entity with a unique new string.
"""
from typing import Dict

from presidio_anonymizer.operators import Operator, OperatorType
from presidio_anonymizer.services.validators import validate_type


class ConsistentReplace(Operator):
    """Receives new text to replace old PII text entity with a new unique string."""

    NEW_VALUE = "lookup_table"

    def operate(self, text: str = None, params: Dict = None) -> str:
        """:return: new_value."""
        lookup_table = params.get(self.NEW_VALUE)
        new_val = lookup_table.get(text)
        return new_val

    def validate(self, params: Dict = None) -> None:
        """Validate the new value is string."""
        #validate_type(params.get(self.NEW_VALUE), self.NEW_VALUE, str)
        pass

    def operator_name(self) -> str:
        """Return operator name."""
        return "consistent_replace"

    def operator_type(self) -> OperatorType:
        """Return operator type."""
        return OperatorType.Anonymize


class ConsistentReplaceReverse(Operator):
    """Receives new text to replace old PII text entity with a new unique string."""

    NEW_VALUE = "lookup_table"

    def operate(self, text: str = None, params: Dict = None) -> str:
        """:return: new_value."""
        lookup_table = params.get(self.NEW_VALUE)
        new_val = lookup_table.reverse_lookup(text)
        return new_val

    def validate(self, params: Dict = None) -> None:
        """Validate the new value is string."""
        #validate_type(params.get(self.NEW_VALUE), self.NEW_VALUE, str)
        pass

    def operator_name(self) -> str:
        """Return operator name."""
        return "consistent_replace_reverse"

    def operator_type(self) -> OperatorType:
        """Return operator type."""
        return OperatorType.Deanonymize
