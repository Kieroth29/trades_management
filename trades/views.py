import random
from .models import Trade
from django.http import HttpResponse
from django.shortcuts import redirect, render
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup

def stock_form(request):
    return render(request, 'stock_form.html', locals())

def stock_search(request):
    stock_codes = request.POST.get('stock_codes').split(',')
    
    options = Options()
    options.add_argument('--headless') # Rodar sem uso de interface gráfica
    options.add_argument("--log-level=3") # Exibir somente erros do console do webdriver no console da aplicação
    driver = webdriver.Remote(f"http://selenium:4444/wd/hub", options=options)
    
    driver.get('https://valorinveste.globo.com/cotacoes/')

    def get_elementText(element):
        elementContent = element.get_attribute('outerHTML')
        elementContent = BeautifulSoup(elementContent, 'html.parser')
        return elementContent.get_text()

    tables = driver.find_elements(By.XPATH, '//table')
    
    rows = []
    for table in tables:
        for element in table.find_elements(By.XPATH, './/tbody//tr'):
            rows.append(element)
    
    for stock_code in stock_codes:
        for element in rows:
            if get_elementText(element.find_element(By.XPATH, './/td[2]')).strip() == stock_code:
                trade = Trade()
                trade.code = get_elementText(element.find_element(By.XPATH, './/td[2]')).strip()
                trade.execution_price = random.uniform(0, 100)
                trade.save()
        
    driver.quit()
    return redirect('trades:stored_stock_data')

def stored_stock_data(request):
    query = request.GET.get('query')
    value = request.GET.get('value')
    
    all_trades = Trade.objects.all()
    
    if query is None:
        trades = Trade.objects.all()
    elif query == "price_gt":
        trades = Trade.objects.filter(execution_price__gt=float(value))
    elif query == "price_lt":
        trades = Trade.objects.filter(execution_price__lt=float(value))
    elif query == "price_mod_gt":
        code = value.split(',')[0]
        price = float(value.split(',')[1])
        trades = Trade.objects.filter(code=code, execution_price__gt=price)
    elif query == "price_mod_lt":
        code = value.split(',')[0]
        price = float(value.split(',')[1])
        trades = Trade.objects.filter(code=code, execution_price__lt=price)
    elif query == "stock":
        trades = Trade.objects.filter(code=value)
        
    return render(request, 'stored_stock_data.html', locals())