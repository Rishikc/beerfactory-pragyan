from django.shortcuts import redirect
import beerf_15
from django.http import JsonResponse
class UserAuth(object):
	def process_request(self, request):
		if 'user_id' not in request.session:
			return redirect(beerf_15.views.login)
		return None

class SessionPIDAuth(object):
	def process_request(self, request):
		if 'user_id' not in request.session:
			id = request.session.get("user_id")
			return JsonResponse({"status":"101", "data":{"description":"Failed! Session not set"}})
		if(int(request.session.get('user_id')) != int(request.POST.get("user_id"))):
		 	return JsonResponse({"status":"102", "data":{"description":"Failed! Session mismatch"}})
		return None