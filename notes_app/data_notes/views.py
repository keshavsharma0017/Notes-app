from .serializers import NotesSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Notes_Attributes

# Create your views here.
@api_view(['Get'])
def notes(request):
    Notes = Notes_Attributes.objects.all()
    return Response(Notes.values())

@api_view(['POST'])
def postnotes(request):
    try:
        data = request.data
        title = data.get('title', None)
        description = data.get('description', None)

        if title is not None and description is not None:
            new_note = Notes_Attributes(title=title, description=description)
        elif title is not None:
            new_note = Notes_Attributes(title=title)
        elif description is not None:
            new_note = Notes_Attributes(description=description)
        else:
            return JsonResponse({'error': 'Invalid data format'}, status=status.HTTP_400_BAD_REQUEST)

        new_note.save()
        return JsonResponse({'message': 'Note created successfully'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
def updatenotes(request, pk):
    try:
        ress = Notes_Attributes.objects.get(id=pk)
        data = request.data

        if 'title' in data:
            ress.title = data['title']
        
        if 'description' in data:
            ress.description = data['description']

        ress.save()
        return JsonResponse(ress)
    except Notes_Attributes.DoesNotExist:
        return JsonResponse({'error': 'Note not found'}, status=status.HTTP_404_NOT_FOUND)
    except KeyError:
        return JsonResponse({'error': 'Invalid data format'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def deleteNotes(request, pk):
    try:
        ress = Notes_Attributes.objects.get(id=pk)
        ress.delete()
        return JsonResponse({'message': 'Note was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    except Notes_Attributes.DoesNotExist:
        return JsonResponse({'error': 'Note not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def home(request):
    routes=[
        {
            'method':'GET' ,
            'Endpoint':'/notes/'
        },
        {
            'method':'Post',
            'Endpoint':'/notes/create/'
        },
        {
            'method':'Update' ,
            'Endpoint':'notes/id/update/'
        },
        {
            'method':'Delete' ,
            'Endpoint':'/notes/id/delete/'
        },

    ]
    return Response(routes)