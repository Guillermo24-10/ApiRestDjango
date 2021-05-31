from usuario.viewset import UsuarioViewSet
from mascota.viewset import MascotaViewSet
from juguete.viewset import JugueteViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('usuario',UsuarioViewSet)
router.register('mascota',MascotaViewSet)
router.register('juguete',JugueteViewSet)
