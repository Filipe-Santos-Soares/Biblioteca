"""
URL configuration for projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin # painel administrativo do Django
from django.urls import path, include # path para rotas, include para incluir outras URLs
from rest_framework.routers import DefaultRouter # router que gera rotas para ViewSets
from livros.views import AutorViewSet, LivroViewSet # ViewSets registrados no router
from rest_framework.authtoken.views import obtain_auth_token # view para obter token de autenticação
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView # Adicionado para o drf-spectacular

router = DefaultRouter()
router.register(r'autores', AutorViewSet)
router.register(r'livros', LivroViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', obtain_auth_token),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'), # Adicionado para o drf-spectacular
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'), # Adicionado para o drfspectacular
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'), # Adicionado para o drf-spectacular
]
