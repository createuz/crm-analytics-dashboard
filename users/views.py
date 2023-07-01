from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .serializers import UserSerializer
from django.core.mail import send_mail
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=201)

    @action(detail=False, methods=['post'])
    def reset_password(self, request):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'success': False, 'error': 'User not found'}, status=404)

        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        subject = 'Reset Password'
        message = f'''
            User: {user.email}\n
            token: {token}\n
            uid: {uid}
        '''
        send_mail(subject, message, 'no-reply@gmail.com', [user.email])

        return Response({'success': True, 'message': 'Email sent'})

    @action(detail=False, methods=['post'])
    def reset_password_confirm(self, request, token, uid):
        try:
            user_id = force_str(urlsafe_base64_decode(uid))
            user = User.objects.get(pk=user_id)
        except (User.DoesNotExist, ValueError):
            return Response({'success': False, 'error': '❌ Invalid user or token'}, status=400)
        if not default_token_generator.check_token(user, token):
            return Response({'success': False, 'error': '❌ Invalid token'}, status=400)
        new_password = request.data.get('password')
        user.set_password(new_password)
        user.save()
        return Response({'success': True, 'message': '✅ Password changed'})


class LogoutViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def create(self, request):
        token = RefreshToken(request.user)
        token.blacklist()
        return Response(status=200)