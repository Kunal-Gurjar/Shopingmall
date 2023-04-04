from rest_framework import status
from rest_framework.response import Response


def responsedata(status, message, data=None):
    return {"status": status, "message": message, "data": data}

def validate_url_vale(price):
    try:
        if price <= 0:
            return Response(responsedata(False, "price can't less zero"), status=status.HTTP_400_BAD_REQUEST)

    except:
        pass