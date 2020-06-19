from rest_framework.authentication import get_authorization_header, BaseAuthentication
from rest_framework import exceptions
from django.http import HttpResponse
from .models import User
import jwt, json
from jwt import InvalidTokenError, DecodeError, InvalidSignatureError
from django.utils.translation import ugettext_lazy as _

from rest_framework import HTTP_HEADER_ENCODING, exceptions
import base64
import binascii

JWT_SECRET = "SECRET_KEY"


class TokenAuthentication(BaseAuthentication):
    keyword = "Token"
    model = None

    def get_model(self):
        return User

    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None

        if len(auth) == 1:
            msg = _("Encabezado de token no válido No se proporcionan credenciales.")
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _("Encabezado de token no válido La cadena de token no debe contener espacios.")
            raise exceptions.AuthenticationFailed(msg)

        try:
            token = auth[1].decode()
        except UnicodeError:
            msg = _(
                "Encabezado de token no válido La cadena de token no debe contener caracteres no válidos."
            )
            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(token)

    def authenticate(self, request):
        auth = get_authorization_header(request).split()
        if not auth or auth[0].lower() != b"token":
          return None

        if len(auth) == 1:
            msg = "Encabezado de token no válido No se proporcionan credenciales."
            raise exceptions.AuthenticationFailed(msg)
            elif len(auth) > 2:
            msg = "Encabezado de token no válido"
            raise exceptions.AuthenticationFailed(msg)

        try:
           token = auth[1]
            if token == "null":
                msg = "Token nulo no permitido"
                raise exceptions.AuthenticationFailed(msg)
        except UnicodeError:
            msg = "Encabezado de token no válido La cadena de token no debe contener caracteres no válidos."
            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(token)

    def authenticate_credentials(self, token):
        model = self.get_model()
        try:
            payload = jwt.decode(token, JWT_SECRET)
            email = payload["email"]
            userid = payload["id"]
            msg = {"Error": "falta de coincidencia de token", "estado": "401"}

            user = model.objects.get(email=email, id=userid)
            print(user)

            if not user.token["token"] == token:
               raise exceptions.AuthenticationFailed(msg)

        except InvalidSignatureError:
            return HttpResponse({"Error": "El token no es válido"}, status="403")
        except DecodeError:
            return HttpResponse({"Error": "El token no es válido"}, status="403")
        except InvalidTokenError:
            return HttpResponse({"Error": "El token no es válido"}, status="403")
        except User.DoesNotExist:
            return HttpResponse({"Error": "Internal server error"}, status="500")

        return (user, token)

    def authenticate_header(self, request):
        return "Token"
