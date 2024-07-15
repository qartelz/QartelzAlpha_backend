from django.shortcuts import render
from django.views import View
# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from api.models import User,Opstmt,Assets,Oca, Ratio, Wctl, Ff, Kfi
from rest_framework import viewsets
from rest_framework.views import APIView
from api.serializer import MyTokenObtainPairSerializer, RegisterSerializer, OpstmtSerializer, AssetsSerializer, OcaSerializer, RatioSerializer,WctlSerializer,FfSerializer,KfiSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


# Get All Routes

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token/',
        '/api/register/',
        '/api/token/refresh/'
    ]
    return Response(routes)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def testEndPoint(request):
# def dashboard(request):
    if request.method == 'GET':
        # response = f"Hey {request.user},You are seeing a Get response"
        data = f"Congratulation {request.user}, your API just responded to GET request"
        return Response({'response': data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = "Hello buddy"
        data = f'Congratulation your API just responded to POST request with text: {text}'
        # text = request.POST.get("text")
        # response = f"Hey{request.user},your text is {text}"
        return Response({'response': data}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)  

class SaveOpstmtView(generics.CreateAPIView):
    queryset = Opstmt.objects.all()
    serializer_class = OpstmtSerializer

    def create(self, request, *args, **kwargs):
        print(request)
        cell_id = request.data.get('cell_id')
        cell_value = request.data.get('cell_value')
        user_id = request.data.get('user_id')

        # Check if the cell_id already exists in the database
        opstmt_instance = Opstmt.objects.filter(cell_id=cell_id, user_id=user_id).first()

        if opstmt_instance:
            # If cell_id exists, update the existing object
            serializer = self.get_serializer(opstmt_instance, data=request.data)
        else:
            # If cell_id doesn't exist, create a new object
            serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class SaveAssetsView(generics.CreateAPIView):
    queryset = Assets.objects.all()
    serializer_class = AssetsSerializer  # Use AssetsSerializer here

    def create(self, request, *args, **kwargs):
        print(request)
        cell_id = request.data.get('cell_id')
        cell_value = request.data.get('cell_value')
        user_id = request.data.get('user_id')

        # Check if the cell_id already exists in the database
        assets_instance = Assets.objects.filter(cell_id=cell_id, user_id=user_id).first()

        if assets_instance:
            # If cell_id exists, update the existing object
            serializer = self.get_serializer(assets_instance, data=request.data)
        else:
            # If cell_id doesn't exist, create a new object
            serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class SaveOcaView(generics.CreateAPIView):
    queryset = Oca.objects.all()
    serializer_class = OcaSerializer  # Use AssetsSerializer here

    def create(self, request, *args, **kwargs):
        print(request)
        cell_id = request.data.get('cell_id')
        cell_value = request.data.get('cell_value')
        user_id = request.data.get('user_id')

        # Check if the cell_id already exists in the database
        oca_instance = Oca.objects.filter(cell_id=cell_id, user_id=user_id).first()

        if oca_instance:
            # If cell_id exists, update the existing object
            serializer = self.get_serializer(oca_instance, data=request.data)
        else:
            # If cell_id doesn't exist, create a new object
            serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class SaveRatioView(generics.CreateAPIView):
    queryset = Ratio.objects.all()
    serializer_class = RatioSerializer  # Use AssetsSerializer here

    def create(self, request, *args, **kwargs):
        print(request)
        cell_id = request.data.get('cell_id')
        cell_value = request.data.get('cell_value')
        user_id = request.data.get('user_id')

        # Check if the cell_id already exists in the database
        ratio_instance = Ratio.objects.filter(cell_id=cell_id, user_id=user_id).first()

        if ratio_instance:
            # If cell_id exists, update the existing object
            serializer = self.get_serializer(ratio_instance, data=request.data)
        else:
            # If cell_id doesn't exist, create a new object
            serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class SaveWctlView(generics.CreateAPIView):
    queryset = Wctl.objects.all()
    serializer_class = WctlSerializer  # Use AssetsSerializer here

    def create(self, request, *args, **kwargs):
        print(request)
        cell_id = request.data.get('cell_id')
        cell_value = request.data.get('cell_value')
        user_id = request.data.get('user_id')

        # Check if the cell_id already exists in the database
        wctl_instance = Wctl.objects.filter(cell_id=cell_id, user_id=user_id).first()

        if wctl_instance:
            # If cell_id exists, update the existing object
            serializer = self.get_serializer(wctl_instance, data=request.data)
        else:
            # If cell_id doesn't exist, create a new object
            serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class SaveFfView(generics.CreateAPIView):
    queryset = Ff.objects.all()
    serializer_class = FfSerializer  # Use AssetsSerializer here

    def create(self, request, *args, **kwargs):
        print(request)
        cell_id = request.data.get('cell_id')
        cell_value = request.data.get('cell_value')
        user_id = request.data.get('user_id')

        # Check if the cell_id already exists in the database
        ff_instance = Ff.objects.filter(cell_id=cell_id, user_id=user_id).first()

        if ff_instance:
            # If cell_id exists, update the existing object
            serializer = self.get_serializer(ff_instance, data=request.data)
        else:
            # If cell_id doesn't exist, create a new object
            serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class SaveKfiView(generics.CreateAPIView):
    queryset = Kfi.objects.all()
    serializer_class = KfiSerializer  # Use AssetsSerializer here

    def create(self, request, *args, **kwargs):
        print(request)
        cell_id = request.data.get('cell_id')
        cell_value = request.data.get('cell_value')
        user_id = request.data.get('user_id')

        # Check if the cell_id already exists in the database
        kfi_instance = Kfi.objects.filter(cell_id=cell_id, user_id=user_id).first()

        if kfi_instance:
            # If cell_id exists, update the existing object
            serializer = self.get_serializer(kfi_instance, data=request.data)
        else:
            # If cell_id doesn't exist, create a new object
            serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
 
class HomeView(APIView):
    # permission_classes = [IsAuthenticated]
# user_id=request.user.id,
    def get(self, request):
         
       
                
        specific_cell_ids = ['B7_11', 'C7_11', 'D7_11', 'E7_11', 'F7_11', 'G7_11', 'H7_11', 'I7_11']
        data = Kfi.objects.filter( cell_id__in=specific_cell_ids)
        serializer = KfiSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
class DashView(APIView):
    def get(self, request):
        # data = Kfi.objects.all()  # Get all objects
        # data = Kfi.objects.order_by('-id')[:10] 
        data = Opstmt.objects.all()
        serializer = OpstmtSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
class DashassetView(APIView):
    def get(self, request):
        # data = Kfi.objects.all()  # Get all objects
        # data = Kfi.objects.order_by('-id')[:10] 
        data = Assets.objects.all()
        serializer = AssetsSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
class DashocaView(APIView):
    def get(self, request):
        # data = Kfi.objects.all()  # Get all objects
        # data = Kfi.objects.order_by('-id')[:10] 
        data = Oca.objects.all()
        serializer =OcaSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
class DashratioView(APIView):
    def get(self, request):
        # data = Kfi.objects.all()  # Get all objects
        # data = Kfi.objects.order_by('-id')[:10] 
        data = Ratio.objects.all()
        serializer = RatioSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
class DashWctlView(APIView):
    def get(self, request):
        # data = Kfi.objects.all()  # Get all objects
        # data = Kfi.objects.order_by('-id')[:10] 
        data = Wctl.objects.all()
        serializer = WctlSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
class DashffView(APIView):
    def get(self, request):
        # data = Kfi.objects.all()  # Get all objects
        # data = Kfi.objects.order_by('-id')[:10] 
        data = Ff.objects.all()
        serializer =FfSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DatavisualView(APIView):
    queryset = Opstmt.objects.all()
    serializer_class = OpstmtSerializer
    def get(self, request,*args, **kwargs):
        
        specific_cell_ids = ['C1_10', 'D1_10', 'E1_10', 'F1_10']

        data = Opstmt.objects.filter( cell_id__in=specific_cell_ids,user_id='abin@abin.com')
        serializer = OpstmtSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
class DatavisualView1(APIView):
    def get(self, request):
        specific_cell_ids = ['C1_35', 'D1_35', 'E1_35', 'F1_35']
        data = Opstmt.objects.filter( cell_id__in=specific_cell_ids,user_id='abin@abin.com')
        serializer = OpstmtSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
class DatavisualView2(APIView):
    def get(self, request):
        specific_cell_ids = ['C1_37', 'D1_37', 'E1_37', 'F1_37']
        data = Opstmt.objects.filter( cell_id__in=specific_cell_ids,user_id='abin@abin.com')
        serializer = OpstmtSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
class DatavisualView3(APIView):
    def get(self, request):
        specific_cell_ids = ['C1_38', 'D1_38', 'E1_38', 'F1_38']
        data = Opstmt.objects.filter( cell_id__in=specific_cell_ids,user_id='abin@abin.com')
        serializer = OpstmtSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
class DatavisualView4(APIView):
    def get(self, request):
        specific_cell_ids = ['C1_42', 'D1_42', 'E1_42', 'F1_42']
        data = Opstmt.objects.filter( cell_id__in=specific_cell_ids,user_id='abin@abin.com')
        serializer = OpstmtSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
class DatavisualView5(APIView):
    def get(self, request):
        specific_cell_ids = ['C4_37', 'D4_37', 'E4_37', 'F4_37']
        data = Ratio.objects.filter( cell_id__in=specific_cell_ids,user_id='abin@abin.com')
        serializer = RatioSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class DatavisualView6(APIView):
    def get(self, request):
        specific_cell_ids = ['C7_10', 'D7_10', 'E7_10', 'F7_10']
        data = Kfi.objects.filter( cell_id__in=specific_cell_ids,user_id='abin@abin.com')
        serializer = KfiSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

