from django.shortcuts import render
from django.core.cache import cache

# def user_account(request):
    # return render(request, 'app_users/account.html')

def user_account(request):
    username = request.user.username
    balance = get_balance()

    promotions_cache_key = 'promotions:{}'.format(username)
    offers_cache_key = 'offers:{}'.format(username)
    promotions = get_promotions()
    offers = get_offers()

    user_account_cache_data = {
        promotions_cache_key: promotions,
        offers_cache_key: offers
    }

    cache.set_many(user_account_cache_data)
    payment_history = get_payment_history

    # cache.get_or_set(promotions_cache_key, promotions, 30*60)
    # if promotions_cache_key not in cache:
    #     promotions = get_promotions()
    #     cache.set(promotions_cache_key, promotions, 30*60)

    return render(request, 'users/account.html', context={
        'balance': balance,
        'promotion': promotion,
        'offers': offers,
        'payment_history': payment_history
    })



