import datetime
from aueb_api.settings import LOGFILE_PATH


class RequestLogMiddleware:
    """ Middleware for logging all incoming requests. """
    def __init__(self, get_response) -> None:
        self.get_response  = get_response


    def __call__(self, request):
        # Create the logfile entry
        entry = 'DATETIME: {} URL: {} IP ADDRESS: {} STATUS: '.format(
            datetime.datetime.now().strftime(r'%d/%m/%Y - %H:%M:%S:%f %Z'),
            request.get_full_path(),
            self.__get_ip_address(request)
        )

        # Move on to the next middleware or call view
        response = self.get_response(request)

        # Add the response status code to the entry
        entry += str(response.status_code) + '\n'

        # Open the logfile
        with open(LOGFILE_PATH, 'a') as logfile:
            # Write entry to logfile
            logfile.write(entry)

        return response


    def __get_ip_address(self, request):
        """ Get the IP address of a request. """
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        return ip
