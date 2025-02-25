# middleware.py
import uuid
from django.utils.deprecation import MiddlewareMixin
from .models import DeviceVisit

class DeviceCountMiddleware(MiddlewareMixin):
    
    def process_request(self, request):
        # Look for a device ID in cookies
        device_id = request.COOKIES.get('device_id')
        if not device_id:
            # Mark that we need to set a cookie later
            request.new_device = True
            # Generate a new unique identifier for this device
            device_id = str(uuid.uuid4())
        else:
            request.new_device = False
        request.device_id = device_id
        
        # Log or update the device entry
        obj, created = DeviceVisit.objects.get_or_create(device_id=device_id)
        if not created:
            # Optionally, update last_visit (auto-handled by save if modified)
            obj.save()  # This will update the timestamp if you have signals or overrides

    def process_response(self, request, response):
        # If this is a new device, set the cookie so subsequent visits are recognized
        if getattr(request, 'new_device', False):
            # Set cookie for one year (adjust max_age as needed)
            response.set_cookie('device_id', request.device_id, max_age=60*60*24*365)
        return response
