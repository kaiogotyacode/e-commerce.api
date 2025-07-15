from pydantic import BaseModel

class BaseDTO(BaseModel):
    """
    Base Data Transfer Object (DTO) class that provides a common structure for all DTOs.
    It includes a method to convert the DTO to a dictionary format.
    """

    def to_dict(self) -> dict:
        """
        Converts the DTO instance to a dictionary.

        Returns:
            dict: A dictionary representation of the DTO instance.
        """
        return self.model_dump(by_alias=True, exclude_none=True)
    
    def to_json(self) -> str:
        """
        Converts the DTO instance to a JSON string.

        Returns:
            str: A JSON string representation of the DTO instance.
        """
        return self.model_dump_json(by_alias=True, exclude_none=True)
    
    @classmethod
    def from_dict(cls, data: dict):
        """
        Creates a DTO instance from a dictionary.

        Args:
            data (dict): Dictionary with the data to create the DTO

        Returns:
            BaseDTO: DTO instance created from the dictionary
        """
        return cls.model_validate(data)
    
    @classmethod
    def from_json(cls, json_str: str):
        """
        Creates a DTO instance from a JSON string.

        Args:
            json_str (str): JSON string with the data to create the DTO

        Returns:
            BaseDTO: DTO instance created from the JSON string
        """
        return cls.model_validate_json(json_str)