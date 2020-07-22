from django.shortcuts import render
from django.core.paginator import Paginator
# Create your views here.
import csv


def index(request):
    eleList=list(range(50))
    if request.GET.get('noOfElements') == None:
        noOfElements=10
    else:
        noOfElements=request.GET.get('noOfElements')
    if request.GET.get('pageNo') == None:
        pageNO=1
    else:
        pageNO=request.GET.get('pageNo')
    
    pagC=Paginator(eleList,noOfElements)
    data=pagC.page(pageNO)
    context={'data':data.object_list,'noOfPages':list(pagC.page_range)}
    return render(request,'index.html',context)


def csvPagination(request):

    arrayRows=[]
    with open('irisDataset.csv','r') as f:
        fileObj=csv.reader(f,delimiter=',')
        linCount=0
        for row in fileObj:
            if linCount==0:
                headerInfo=row
                linCount +=1
            else:
                arrayRows.append(row)
    
    if request.GET.get('pageNo') == None:
        pageNO=1
    else:
        pageNO=request.GET.get('pageNo')
    if request.GET.get('noOfElements') == None:
        noOfElements=10
    else:
        noOfElements=request.GET.get('noOfElements')
    pagC=Paginator(arrayRows,noOfElements)
    pacgObj=pagC.page(pageNO)
    data=pacgObj.object_list
    context={'data':data,'headerInfo':headerInfo,'noOfPages':list(pagC.page_range)}
    return render(request,'csvPagination.html',context)