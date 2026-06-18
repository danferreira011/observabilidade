# 📊 Curso Prometheus - Instrumentação Básica

## Visão Geral

Este repositório contém um **projeto prático completo** para aprender instrumentação de métricas Prometheus através de uma aplicação e-commerce.

> 🎓 **Este projeto faz parte da [Formação DevOps Pro](https://devopspro.com.br)**.

## 🎯 Objetivos do Curso

- **Instrumentar aplicações** com os 4 tipos de métricas Prometheus
- **Configurar Postgres Exporter** para métricas de infraestrutura
- **Validar coleta** de métricas via endpoints `/metrics`
- **Deployar em Docker e Kubernetes** com monitoramento

## 📁 Estrutura do Projeto

### **01-projeto-inicial/**
Aplicação e-commerce **original** sem instrumentação Prometheus - ponto de partida da aula.

### **00-documentacao/**
Material didático completo:
- **[METRICAS_PROMETHEUS.md](./00-documentacao/METRICAS_PROMETHEUS.md)**: Objetivos e conceitos da aula
- **[DESAFIO_INSTRUMENTACAO.md](./00-documentacao/DESAFIO_INSTRUMENTACAO.md)**: Desafio prático step-by-step

## 📚 Projeto: E-commerce Fake Shop

### 📖 **Instrumentação Completa**
- **Aplicação**: Flask + PostgreSQL
- **Métricas**: Counter, Gauge, Histogram, Summary
- **Exporter**: Postgres Exporter para métricas de banco
- **Ambientes**: Docker Compose e Kubernetes

## 🚀 Como Começar

### Pré-requisitos
- **Docker** e **Docker Compose**
- **Kubernetes** (minikube, kind, ou cluster)
- **Git**
- **Python 3.8+** (para módulos específicos)

### Quick Start

#### 📖 **Começar pelos Fundamentos**
```bash
# Ler objetivos e conceitos
cat 00-documentacao/METRICAS_PROMETHEUS.md

# Entender o desafio
cat 00-documentacao/DESAFIO_INSTRUMENTACAO.md
```

#### 🚀 **Executar Projeto Original**
```bash
# Navegar para aplicação base
cd 01-projeto-inicial

# Executar com Docker Compose
docker-compose up -d

# Acessar: http://localhost:5000
```

#### ⚡ **Implementar Instrumentação**
```bash
# Trabalhar na versão instrumentada
cd src

# Seguir instruções no CLAUDE.md
```

## 🛠️ Tecnologias Utilizadas

### **Core Stack**
- **Prometheus**: Coleta e armazenamento de métricas
- **prometheus_client**: Biblioteca Python para instrumentação
- **Postgres Exporter**: Métricas de banco PostgreSQL

### **Aplicação**
- **Flask** (Python): Aplicação web e-commerce
- **PostgreSQL**: Banco de dados para monitoramento

### **Infraestrutura**
- **Docker**: Containerização
- **Kubernetes**: Orquestração
- **Docker Compose**: Ambiente local

## 📚 Documentação

- **[Objetivos da Aula](./00-documentacao/METRICAS_PROMETHEUS.md)**: Fundamentos e conceitos
- **[Desafio Prático](./00-documentacao/DESAFIO_INSTRUMENTACAO.md)**: Implementação step-by-step
- **[Instruções Detalhadas](./CLAUDE.md)**: Comandos e configurações específicas
