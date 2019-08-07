from rest_framework import status
import json
import base64
from django.http import HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from csfapi.models import Issues, Users, Clients, ClientGroups
from csfapi.serializers import IssuesSerializer, UsersSerializer, ClientsSerializer, ClientGroupsSerializer


@api_view(['GET', 'POST'])
def issues_view(request):
    # Functionality 1: To view all issues
    # Functionality 2: To add new issue
    if request.method == 'GET':
        issues = Issues.objects.all()
        serializer = IssuesSerializer(issues, many=True)
        return Response(serializer.data)

    if request.method == 'POST':

        decoded_data = base64.b64decode(request.POST.get('data'))
        decoded_obj = json.loads(decoded_data)

        with open('static/checks.json') as checks_json:
            checks_data = json.load(checks_json)

        #Save Client IP in Clients model if not already exists
        try:
            issue_client = Clients.objects.get(clientIP=request.META.get('REMOTE_ADDR'))
        except:
            print("DEBUG LOG: Client not exists: %s" % request.META.get('REMOTE_ADDR'), flush=True)
            client_data = {
                    "clientIP": request.META.get('REMOTE_ADDR')
                }
            cl_serializer = ClientsSerializer(data=client_data)
            if cl_serializer.is_valid():
                cl_serializer.save()
            issue_client = Clients.objects.get(clientIP=request.META.get('REMOTE_ADDR'))

        for i in range(0, len(decoded_obj["tests"])):
            for j in range(0, len(decoded_obj["tests"][i]["results"])):
                issue_obj = decoded_obj["tests"][i]["results"][j]

                #if issue_obj['result'] == "INFO" or issue_obj['result'] == "NOTE":
                    #issue_fix_status = "I"
                if issue_obj['result'] == 'WARN':
                    issue_fix_status = 'N'
                elif issue_obj['result'] == 'PASS':
                    issue_fix_status = 'F'

                # If the client has already reported issues to CSF Server
                try:
                    found_obj = Issues.objects.get(checkId=issue_obj['id'],issueClientId=issue_client.clientId)
                    print("DEBUG LOG: Issue is previously created! ID: %s" % issue_obj['id'], flush=True)
                    found_obj.fixStatus = issue_fix_status
                    found_obj.save()
                    serializer = IssuesSerializer()
                # If the client has NOT already reported issues
                except:
                    print("DEBUG LOG: New Issue for this client! Check: %s, Client Id: %s" % (issue_obj['id'], issue_client.clientId) , flush=True)
                    issue_data = {
                        "checkId": issue_obj['id'],
                        "checkDesc": issue_obj['desc'],
                        "severity": checks_data[issue_obj['id']]['severity'],
                        "issueClientId": issue_client.clientId,
                        "fixStatus": issue_fix_status
                    }
                    serializer = IssuesSerializer(data=issue_data)
                    if serializer.is_valid():
                        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def issues_view_details(request, pk):
    # Functionality 1: To view specific issues
    # Functionality 2: To edit specific issues
    # Functionality 3: To delete specific issues
    try:
        issue = Issues.objects.get(pk=pk)
    except Issues.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = IssuesSerializer(issue)
        return Response(serializer.data)
    if request.method == 'PUT':
        if request.POST.get('severity'):
            issue.severity = request.POST.get('severity')
        if request.POST.get('fixStatus'):
            issue.fixStatus = request.POST.get('fixStatus')
        if request.POST.get('checkComment'):
            issue.checkComment = request.POST.get('checkComment')
        issue.save()
        serializer = IssuesSerializer(issue)
        return Response(serializer.data)
    if request.method == 'DELETE':
        issue.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def clients_view(request):
    if request.method == 'GET':
        clients = Clients.objects.all()
        serializer = ClientsSerializer(clients, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def clients_view_details(request, pk):
    try:
        client = Clients.objects.get(pk=pk)
    except Clients.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClientsSerializer(client)
        return Response(serializer.data)
    if request.method == 'PUT':
        if request.POST.get('clientName'):
            client.clientName = request.POST.get('clientName')
        if request.POST.get('clientPrefs'):
            client.clientPrefs = request.POST.get('clientPrefs')
        if request.POST.get('clientGroupID'):
            client.clientGroupID = request.POST.get('clientGroupID')

        client.save()
        serializer = ClientsSerializer(client)
        return Response(serializer.data)
    if request.method == 'DELETE':
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def clientgroups_view(request):
    if request.method == 'GET':
        clientgroups = ClientGroups.objects.all()
        serializer = ClientGroupsSerializer(clientgroups, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        clientgroup_data = {
            "groupName": request.POST.get('groupName') if request.POST.get('groupName') else "",
            "groupPrefs": request.POST.get('groupPrefs') if request.POST.get('groupPrefs') else "",
        }
        clg_serializer = ClientGroupsSerializer(data=clientgroup_data)
        if clg_serializer.is_valid():
            clg_serializer.save()
        return Response(clg_serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def clientgroups_view_details(request, pk):
    try:
        clientgroup = ClientGroups.objects.get(pk=pk)
    except ClientGroups.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClientGroupsSerializer(clientgroup)
        return Response(serializer.data)
    if request.method == 'PUT':
        if request.POST.get('groupName'):
            clientgroup.groupName = request.POST.get('groupName')
        if request.POST.get('groupPrefs'):
            clientgroup.groupPrefs = request.POST.get('groupPrefs')
        clientgroup.save()
        serializer = ClientGroupsSerializer(clientgroup)
        return Response(serializer.data)
    if request.method == 'DELETE':
        clientgroup.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# TBD. Future Functionality.
@api_view(['GET', 'PUT', 'POST', 'DELETE'])
def users_view(request):
    if request.method == 'GET':
        users = Users.objects.all()
        serializer = IssuesSerializer(users, many=True)
        return Response(serializer.data)


# TBD. Future Functionality.
@api_view(['POST'])
def userlogin_view(request):
    if request.method == 'POST':
        issues = Users.objects.all()
        serializer = UsersSerializer(issues, many=True)
        return Response(serializer.data)
