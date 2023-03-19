import pandas as pd
from django.http import JsonResponse
from rest_framework.decorators import APIView
from .models import Project
from . import globalparameters
from .serializers import ProjectSerializers
from django.db.models import Sum

class ReadExcelCreateApiView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self,request):
        try:
            objects = []
            df = pd.read_excel('file.xlsx', sheet_name='Sheet1')
            df = df.astype(object).where(df.notna(), None) 
            datas = df.to_dict('records')
            for data in datas:
                province = data.get('Province')
                district= data.get('District')
                municipality= data.get('Municipality')
                project_title = data.get('Project Title')
                project_status = data.get('Project Status')
                donor = data.get('Donor')
                executing_agency = data.get('Executing Agency')
                implementing_partner = data.get('Implementing Partner')
                counterpart_ministry = data.get('Counterpart Ministry')
                type_of_assistance = data.get('Type of Assistance')
                budget_type = data.get('Budget Type')
                humanitarian = False
                sector = data.get('Sector')
                agreement_date = str(data.get('Agreement Date'))
                commitments = data.get('Commitments')
                disbursement = data.get('Disbursement')
                if commitments is None:
                    commitments = 0.00
                if disbursement is None:
                    disbursement = 0.00

                objects.append(Project(province = province, district=district, municipality=municipality, project_title=project_title,
                    project_status=project_status, donor=donor, executing_agency=executing_agency,implementing_partner=implementing_partner,
                    counterpart_ministry=counterpart_ministry,type_of_assistance=type_of_assistance,budget_type=budget_type,
                    humanitarian=humanitarian, sector=sector, agreement_date=agreement_date, commitments=commitments,
                    disbursement=disbursement))
                
            Project.objects.bulk_create(objects)
            msg = {
                'responseCode': globalparameters.SUCCESS_RESPONSE_CODE,
                'response': globalparameters.SUCCESS_RESPONSE
            }
            return JsonResponse(msg, status = 200)

        except Exception as e:
            print(e)
            print(e.__class__)
            msg = {
                'responseCode': globalparameters.UNSUCCESS_RESPONSE_CODE,
                'response': globalparameters.UNSUCCESS_RESPONSE
            }
            return JsonResponse(msg, status = 500)


class ReadExcelListApiView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self,request):
        try:
            data_list = []
            datas = Project.objects.values('sector', 'counterpart_ministry', 'project_status', 'agreement_date')
            for data in datas:
                data_list.append({
                    "sector": data.get('sector'),
                    "counterpartMinistry": data.get('counterpart_ministry'),
                    "projectStatus": data.get('project_status'),
                    "agreementDate": data.get('agreement_date')
                })

            # serializers = ProjectSerializers(datas, many=True)
            msg = {
                'responseCode': globalparameters.SUCCESS_RESPONSE_CODE,
                'response': globalparameters.LIST_SUCCESS_RESPONSE,
                'data':data_list
            }
            return JsonResponse(msg, status = 200)

        except Exception as e:
            print(e)
            print(e.__class__)
            msg = {
                'responseCode': globalparameters.UNSUCCESS_RESPONSE_CODE,
                'response': globalparameters.UNSUCCESS_RESPONSE
            }
            return JsonResponse(msg, status = 500)
        


class ReadExcelFilterApiView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self,request):
        try:
            data_list = []
            sector_list = []
            sectors = Project.objects.values('sector').distinct()
            for sector in sectors:
                sector = sector.get('sector')
                sector_count =  Project.objects.filter(sector=sector).count()
                sector_budget = Project.objects.filter(sector=sector).aggregate(Sum('commitments'))
                sector = Project.objects.filter(sector=sector).first()
                sector_budget = sector_budget.get('commitments__sum')
                sector_list.append({
                    "id": sector.id,
                    'name': sector.sector,
                    'project_count': sector_count,
                    'budget':sector_budget
                })
            project_count = Project.objects.values('project_title').distinct().count()
            total_budget = Project.objects.aggregate(Sum('commitments'))
            total_budget = total_budget.get('commitments__sum')
            
            data_list.append({
                "project_count": project_count,
                "total_budget": total_budget,
                "sector": sector_list
            })
                
            msg = {
                'responseCode': globalparameters.SUCCESS_RESPONSE_CODE,
                'response': globalparameters.LIST_SUCCESS_RESPONSE,
                'data':data_list
            }
            return JsonResponse(msg, status = 200)

        except Exception as e:
            print(e)
            print(e.__class__)
            msg = {
                'responseCode': globalparameters.UNSUCCESS_RESPONSE_CODE,
                'response': globalparameters.UNSUCCESS_RESPONSE
            }
            return JsonResponse(msg, status = 500)
        



class ReadExcelMunicipalityApiView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self,request):
        try:
            municipality_list = []
            municipalitys = Project.objects.values('municipality').distinct()
            for municipality in municipalitys:
                municipality = municipality.get('municipality')
                municipality_count =  Project.objects.filter(municipality=municipality).count()
                municipality_budget = Project.objects.filter(municipality=municipality).aggregate(Sum('commitments'))
                municipality = Project.objects.filter(municipality=municipality).first()
                municipality_budget = municipality_budget.get('commitments__sum')
                municipality_list.append({
                    "id": municipality.id,
                    'municipality': municipality.municipality,
                    'project_count': municipality_count,
                    'budget':municipality_budget
                })
                
            msg = {
                'responseCode': globalparameters.SUCCESS_RESPONSE_CODE,
                'response': globalparameters.LIST_SUCCESS_RESPONSE,
                'data':municipality_list
            }
            return JsonResponse(msg, status = 200)

        except Exception as e:
            print(e)
            print(e.__class__)
            msg = {
                'responseCode': globalparameters.UNSUCCESS_RESPONSE_CODE,
                'response': globalparameters.UNSUCCESS_RESPONSE
            }
            return JsonResponse(msg, status = 500)