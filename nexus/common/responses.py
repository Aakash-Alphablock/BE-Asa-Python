from rest_framework.response import Response

class BaseResponseMixin:
    """
    Base response class for API responses with common success and error handling.
    """

    def create_success_response(self, data=None,  message=None, status=200, **kwargs):
        """
        Create a success response with an optional message.

        Args:
            data (dict, optional): Data to be included in the response. Defaults to None.
            message (str, optional): Message to be included in the response. Defaults to None.
            status (int, optional): HTTP status code. Defaults to 200.
            **kwargs: Additional keyword arguments to be passed to the Response constructor.

        Returns:
            Response: A success response object.
        """
        custom_data = {
            'success': True,
            'data': data,
            'status': status,
            'message': message
        }
        custom_data.update(kwargs)
        return Response(data=custom_data,  status=status)

    def create_error_response(self, message=None, status=400, **kwargs):
        """
        Create an error response with an optional message and status code.

        Args:
            message (str, optional): Message to be included in the response. Defaults to "An error occurred.".
            status (int, optional): HTTP status code. Defaults to 400.
            **kwargs: Additional keyword arguments to be passed to the Response constructor.

        Returns:
            Response: An error response object.
        """
        # you can pass the request object here and add custom data to the response
        # Eg: based on the request you can select the content type and serialize teh data accordingly before sending the response
        custom_data = {
            'success': False,
            'data': None,
            'status': status,
            'message': message
        }
        custom_data.update(kwargs)
        return Response(data=custom_data,  status=status)