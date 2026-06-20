from prometheus_client import Counter,Gauge, Histogram
import psutil
import threading

cart_additionn_total = Counter(
    'ecommerce_cart_additions_total',
    'Total de adições ao carrinho por produto',
    ['product_id']
)

errors_total = Counter(
    'ecommerce_errors_total',
    'Total de erros',
    ['error_type', 'endpoint', 'status_code']
)

active_sessions_gauge = Gauge(
    'ecommerce_active_sessions',
    'Número de sessões ativas'
)

cpu_usage_gauge = Gauge(
    'ecommerce_cpu_usage_percent',
    'Uso da CPU'
)

def update_cpu_usage():
    try:
        cpu_percent = psutil.cpu_percent()
        cpu_usage_gauge.set(cpu_percent)
        printf(f" CPU Usage: {cpu_percent}%")
    except Exception as e:
        print(f"Erro ao obter uso da CPU: {e}")

def update_active_sessions():
    try:
        from models.order import Order
        active_count = Order.query.filter_by(is_open=True).count()
        active_sessions_gauge.set(active_count)
        print(f"Número de sessões ativas: {active_count}")  
    except Exception as e:
        print(f"Erro ao obter número de sessões ativas: {e}")

request_duration_histogram = Histogram(
    'ecommerce_request_duration_seconds',
    'Duração das requisições em segundos',
    ['method', 'endpoint', 'status_code'],
    buckets=[0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1, 2.5, 5, 10]
)