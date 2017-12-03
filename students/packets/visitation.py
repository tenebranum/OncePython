# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

def visitation_list(request):
	visitation = (
		{'id':1,
		 'name': u'Ваниш Изи',
		 'visit': {'1':1,'2':0,'3':1,'4':1,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'11':0,'12':0,'13':0,'14':0,'15':0,'16':0,'17':0,'18':0,'19':0,'20':0,'21':0,'22':0,'23':0,'24':0,'25':0,'26':0,'27':0,'28':0,'29':0,'30':0,'31':0}
		},
		{'id':2,
		  'name': u'Хата зе-Биг',
		 'visit': {'1':0,'2':1,'3':1,'4':0,'5':1,'6':1,'7':0,'8':0,'9':0,'10':0,'11':0,'12':0,'13':0,'14':0,'15':0,'16':0,'17':0,'18':0,'19':0,'20':0,'21':0,'22':0,'23':0,'24':0,'25':0,'26':0,'27':0,'28':0,'29':0,'30':0,'31':0}

		},
		{'id':3,
		 'name': u'Богдан Иванов',
		 'visit': {'1':1,'2':1,'3':0,'4':0,'5':0,'6':1,'7':1,'8':0,'9':0,'10':0,'11':0,'12':0,'13':0,'14':0,'15':0,'16':0,'17':0,'18':0,'19':0,'20':0,'21':0,'22':0,'23':0,'24':0,'25':0,'26':0,'27':0,'28':0,'29':0,'30':0,'31':0}
		}
		)
	return render(request, 'students/visitation_list.html', {'visitation' : visitation})




# Views for groups

def visitation_edit(request,vid):
	return HttpResponse('<h1>Visitation Edit %s</h1>' %vid)
