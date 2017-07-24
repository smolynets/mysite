from .util import basket_list

def buy_processor(request):
	return {'buy_status': basket_list(request)}