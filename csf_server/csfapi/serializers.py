from rest_framework import serializers
from csfapi.models import Issues, Users, Clients, ClientGroups


class IssuesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Issues
        fields = ('issueId', 'checkId', 'checkDesc', 'severity', 'issueClientId', 'fixStatus', 'creationDate', 'checkComment')


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ('userId', 'userName', 'userPassword', 'fullName', 'accessLevel', 'creationDate', 'userPref')


class ClientsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clients
        fields = ('clientId', 'clientIP', 'clientName', 'clientPrefs', 'clientGroupID')


class ClientGroupsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientGroups
        fields = ('groupID', 'groupName', 'groupPrefs')
