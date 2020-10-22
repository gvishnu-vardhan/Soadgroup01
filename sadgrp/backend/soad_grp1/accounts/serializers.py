from rest_framework import serializers
from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken,TokenError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

def aadharNumVerify(adharNum: str) -> bool:
    """
    Takes a N digit aadhar number and
    returns a boolean value whether that is Correct or Not
    """
    verhoeff_table_d = (
        (0, 1, 2, 3, 4, 5, 6, 7, 8, 9),
        (1, 2, 3, 4, 0, 6, 7, 8, 9, 5),
        (2, 3, 4, 0, 1, 7, 8, 9, 5, 6),
        (3, 4, 0, 1, 2, 8, 9, 5, 6, 7),
        (4, 0, 1, 2, 3, 9, 5, 6, 7, 8),
        (5, 9, 8, 7, 6, 0, 4, 3, 2, 1),
        (6, 5, 9, 8, 7, 1, 0, 4, 3, 2),
        (7, 6, 5, 9, 8, 2, 1, 0, 4, 3),
        (8, 7, 6, 5, 9, 3, 2, 1, 0, 4),
        (9, 8, 7, 6, 5, 4, 3, 2, 1, 0))

    verhoeff_table_p = (
        (0, 1, 2, 3, 4, 5, 6, 7, 8, 9),
        (1, 5, 7, 6, 2, 8, 3, 0, 9, 4),
        (5, 8, 0, 3, 7, 9, 6, 1, 4, 2),
        (8, 9, 1, 6, 0, 4, 3, 5, 2, 7),
        (9, 4, 5, 3, 1, 2, 6, 8, 7, 0),
        (4, 2, 8, 6, 5, 7, 3, 9, 0, 1),
        (2, 7, 9, 3, 8, 0, 6, 4, 1, 5),
        (7, 0, 4, 6, 9, 1, 3, 2, 5, 8))

    # verhoeff_table_inv = (0, 4, 3, 2, 1, 5, 6, 7, 8, 9)

    def checksum(s: str) -> int:
        """For a given number generates a Verhoeff digit and
        returns number + digit"""
        c = 0
        for i, item in enumerate(reversed(s)):
            c = verhoeff_table_d[c][verhoeff_table_p[i % 8][int(item)]]
        return c

    # Validate Verhoeff checksum
    return checksum(adharNum) == 0 and len(adharNum) == 12






        

class RegisterSerializer(serializers.ModelSerializer):
    aadharnumber = serializers.CharField(max_length=12)
    password = serializers.CharField(max_length=30, min_length=6, write_only=True)
    slugname=serializers.SlugRelatedField(read_only=True,slug_field='name')
    def validate(self, attrs):
        aadharnumber= attrs.get('aadharnumber', '')
        

        if not aadharNumVerify(aadharnumber):
            raise serializers.ValidationError(
                "Please enter valid AadharNumber")
        return attrs

    

    class Meta:
        model = User
        fields = ['email','name','aadharnumber','person', 'password','slugname']


    

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)




class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)
    
    name=serializers.CharField()
    
    def validate(self, attrs):
        email=attrs.get('email','')
        name=attrs.get('name',''),
        password=attrs.get('password','')
        
        user=auth.authenticate(email=email,name=name,password=password)
        if not user:
            raise AuthenticationFailed('Invalid Credentials try again')
        
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')
     

        
        

        return {
            'email': user.email,
             'name':user.name,
            'tokens': user.tokens
        }

        return super().validate(attrs)
    
    class Meta:
        model = User
        fields = ['email','name','password',  'tokens']


class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)

    #redirect_url = serializers.CharField(max_length=500, required=False)

    class Meta:
        fields = ['email']


    
class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        min_length=6, max_length=68, write_only=True)
    confirmpassword = serializers.CharField(
        min_length=6, max_length=68, write_only=True)   
    token = serializers.CharField(
        min_length=1, write_only=True)
    uidb64 = serializers.CharField(
        min_length=1, write_only=True)

    class Meta:
        fields = ['password','confirmpassword', 'token', 'uidb64']

    def validate(self, attrs):
        password=''
        confirmpassword=''
        token=''
        uidb64=''
        user=''
        try:
            password = attrs.get('password')
            confirmpassword=attrs.get('confirmpassword','')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')
            if not password==confirmpassword:
                raise AuthenticationFailed('Passwords do not match')
            else:

                id = force_str(urlsafe_base64_decode(uidb64))
                user = User.objects.get(id=id)

                if not PasswordResetTokenGenerator().check_token(user, token):
                    raise AuthenticationFailed('The reset link is invalid', 401)

           


                user.set_password(password)
                user.save()

                return (user)
        except Exception as e:
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed('The reset link is invalid', 401)
            
        return super().validate(attrs)


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_message = {
        'bad_token': ('Token is expired or invalid')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):

        try:
            RefreshToken(self.token).blacklist()

        except TokenError:
            self.fail('bad_token')            
               
       

        