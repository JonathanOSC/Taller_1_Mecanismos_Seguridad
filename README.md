# WAAP_BASE_ATTACK_LAB_v1.0

Laboratorio académico de Web Application and API Protection (WAAP)
para pruebas controladas de seguridad.

## Arquitectura

Cliente
   |
   v
WAAP - ModSecurity + OWASP CRS
Puerto 8080
   |
   v
Juice Shop
Puerto 3000 interno
   |
   v
Red Docker lab-net

## Componentes

- Ubuntu Server
- Docker
- Docker Compose
- OWASP Juice Shop
- Nginx
- ModSecurity
- OWASP Core Rule Set (CRS)

## Puertos

### WAAP

Puerto externo:

    8080

Acceso:

    http://IP_DE_LA_VM:8080

### Juice Shop

Puerto:

    3000

El servicio está expuesto únicamente dentro de la red Docker.

No se debe acceder directamente desde el equipo anfitrión.

## Obtener la IP de la VM

Ejecutar:

    ip addr

Buscar la dirección IPv4 de la interfaz de red.

Ejemplo:

    192.168.x.x

Desde el equipo anfitrión:

    http://IP_DE_LA_VM:8080

No asumir que la IP será siempre la misma.

## Iniciar el laboratorio

    cd ~/taller-waap
    docker compose up -d

Verificar:

    docker compose ps

## Verificar WAAP

    docker exec waap nginx -t

Debe aparecer:

    syntax is ok
    test is successful

Probar acceso:

    curl -I http://localhost:8080

## Ver logs

Logs generales:

    docker logs waap

Últimos eventos:

    docker logs --since 5m waap

Seguimiento en tiempo real:

    docker logs -f waap

## Validación de ModSecurity

Consultar reglas cargadas:

    docker exec waap nginx -t

La configuración base utiliza ModSecurity con OWASP CRS.

El laboratorio debe permitir identificar:

- solicitudes permitidas
- solicitudes bloqueadas
- reglas CRS activadas
- puntuación de anomalía
- código HTTP generado
- URI atacada
- información de la transacción

## Prueba controlada de SQL Injection

Ejemplo académico:

    curl -i -G "http://localhost:8080/rest/products/search" --data-urlencode "q=' OR '1'='1"

Una solicitud detectada por CRS puede devolver:

    HTTP/1.1 403 Forbidden

Consultar evidencia:

    docker logs --since 5m waap 2>&1 | tail -n 100

## Alcance

Este laboratorio está destinado exclusivamente a:

- pruebas académicas
- análisis de tráfico
- pruebas de reglas WAF
- validación de OWASP CRS
- pruebas controladas de vulnerabilidades
- experimentación con técnicas de evasión
- análisis de logs
- desarrollo posterior de ML, RASP y DevSecOps

Las pruebas deben ejecutarse únicamente contra las máquinas y aplicaciones desplegadas dentro del laboratorio.

No utilizar esta infraestructura para atacar sistemas de terceros.

## Libertad de experimentación

Los participantes pueden modificar:

- reglas ModSecurity
- configuración del CRS
- configuración Nginx
- configuración Docker
- aplicación Juice Shop
- scripts de pruebas
- mecanismos de logging
- futuras capas ML/RASP/DevSecOps

La VM entregada debe considerarse una copia experimental.

Cada participante debe trabajar sobre su propia copia de la máquina virtual.

## Restauración

Si una modificación rompe el laboratorio, se puede restaurar la configuración utilizando los respaldos disponibles en:

    ~/taller-waap/

Respaldos actuales:

    docker-compose.fase0-backup.yml
    docker-compose.antes-tuning.yml
    docker-compose.antes-template.yml

## Estado de esta versión

WAAP_BASE_ATTACK_LAB_v1.0

Incluye:

- Juice Shop
- ModSecurity
- OWASP CRS
- Nginx
- Docker Compose
- regla personalizada para tráfico Socket.IO
- logging
- validación básica del WAAP
- prueba controlada de detección/bloqueo SQLi

Pendiente para versiones posteriores:

- detección ML
- orquestador de decisiones
- RASP
- DevSecOps
- SAST
- SCA
- escaneo de contenedores
- DAST/ZAP
- observabilidad avanzada
- métricas
- evaluación de evasiones
# Taller_1_Mecanismos_Seguridad
# Taller_1_Mecanismos_Seguridad
