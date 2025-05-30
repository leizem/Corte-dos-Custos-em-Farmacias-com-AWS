# Corte-dos-Custos-em-Farmacias-com-AWS
Projeto Redução dos Custos em Farmácias com AWS na DIO | https://web.dio.me/

# Projeto de Otimização de Custos com Serviços AWS

**Data:** 30/05/2025  
**Empresa:** Abstergo Industries  
**Responsável:** Tiago Monteiro  
**Departamento:** Tecnologia da Informação  
**Período de Execução:** Janeiro - Maio 2025  

---

## 1. Introdução

### 1.1 Contexto e Justificativa

Este relatório técnico tem como finalidade apresentar o processo de planejamento, execução e resultados obtidos com a implementação de soluções na nuvem utilizando serviços da Amazon Web Services (AWS), realizados na empresa Abstergo Industries sob a responsabilidade do profissional Tiago Monteiro.

A Abstergo Industries, empresa líder no setor de tecnologia e inovação, enfrentava desafios significativos relacionados ao crescimento exponencial dos custos operacionais em sua infraestrutura de nuvem. Com o aumento da demanda por serviços digitais e a expansão das operações globais, os gastos mensais com AWS haviam crescido 340% nos últimos 18 meses, impactando diretamente a margem operacional da empresa.

### 1.2 Problemática Identificada

A análise preliminar da infraestrutura revelou diversos pontos críticos que contribuíam para o desperdício de recursos:

- **Sobre-provisionamento de recursos:** Instâncias EC2 configuradas com capacidade superior à demanda real
- **Falta de visibilidade:** Ausência de monitoramento detalhado sobre uso e custos por departamento
- **Recursos ociosos:** Aproximadamente 35% dos recursos permaneciam inativos durante horários de baixa demanda
- **Arquitetura legada:** Aplicações ainda utilizando modelo tradicional de servidores dedicados
- **Ausência de automação:** Processos manuais de escalabilidade resultando em ineficiências

### 1.3 Objetivos do Projeto

#### Objetivo Principal
Identificar e aplicar três ferramentas oferecidas pela AWS que permitissem reduzir, de forma imediata e eficaz, os custos operacionais relacionados ao uso da infraestrutura em nuvem da empresa, sem comprometer a performance, a escalabilidade ou a segurança das aplicações e serviços da organização.

#### Objetivos Específicos
- Implementar sistema de monitoramento e análise de custos em tempo real
- Reduzir em pelo menos 30% os custos mensais com infraestrutura
- Aumentar a eficiência operacional através da automação
- Estabelecer governança de custos para sustentabilidade a longo prazo
- Migrar aplicações críticas para arquitetura serverless quando aplicável
- Criar cultura de consciência de custos entre as equipes de desenvolvimento

---

## 2. Metodologia e Abordagem

### 2.1 Framework de Implementação

O projeto foi estruturado seguindo a metodologia PDCA (Plan-Do-Check-Act) adaptada para ambientes de nuvem, garantindo uma abordagem sistemática e mensurável para cada etapa da implementação.

### 2.2 Cronograma de Execução

**Fase 1 - Planejamento e Análise (Janeiro 2025):**
- Levantamento completo da infraestrutura atual
- Análise de padrões de uso e identificação de gargalos
- Definição de KPIs e métricas de sucesso

**Fase 2 - Implementação Piloto (Fevereiro-Março 2025):**
- Deploy das ferramentas em ambiente de teste
- Configuração inicial e ajustes finos
- Treinamento das equipes envolvidas

**Fase 3 - Implementação Produção (Abril 2025):**
- Rollout gradual em ambiente de produção
- Monitoramento intensivo e correções
- Documentação de processos

**Fase 4 - Otimização e Governança (Maio 2025):**
- Análise de resultados e refinamentos
- Estabelecimento de políticas de governança
- Planejamento de melhorias futuras

---

## 3. Descrição Detalhada do Projeto

A implementação foi estruturada em três etapas distintas, cada uma focada em um serviço específico da AWS com propósitos complementares. A seguir, são detalhadas as ferramentas escolhidas, os objetivos de cada uma e os respectivos cenários de uso aplicados à realidade da Abstergo Industries.

### 3.1 Etapa 1 – AWS Cost Explorer

#### 3.1.1 Objetivo da Ferramenta
Monitoramento, análise e gestão dos custos e uso dos serviços AWS com capacidade de forecasting e identificação de anomalias de gastos.

#### 3.1.2 Análise Técnica Prévia

Antes da implementação do AWS Cost Explorer, foi realizada uma auditoria completa da infraestrutura existente que revelou:

- **Distribuição de Custos por Serviço:**
  - EC2: 45% do total de gastos mensais
  - RDS: 20% do total de gastos mensais
  - S3: 15% do total de gastos mensais
  - CloudFront: 10% do total de gastos mensais
  - Outros serviços: 10% do total de gastos mensais

- **Padrões de Uso Identificados:**
  - Picos de utilização entre 9h-18h nos dias úteis
  - Redução de 70% na demanda durante finais de semana
  - Variações sazonais relacionadas ao ciclo comercial da empresa

#### 3.1.3 Implementação Detalhada

**Configuração de Dashboards Personalizados:**
Foram criados dashboards específicos para diferentes níveis organizacionais:

- **Dashboard Executivo:** Visão consolidada de custos com comparativos mensais e projeções trimestrais
- **Dashboard Técnico:** Detalhamento por serviço, região e tag de projeto
- **Dashboard Departamental:** Custos segregados por centro de custo e responsável

**Sistema de Alertas e Notificações:**
Implementação de sistema automatizado de alertas para:
- Desvios superiores a 15% em relação ao orçamento mensal
- Identificação de recursos não utilizados por mais de 72 horas
- Anomalias de gastos baseadas em machine learning

**Políticas de Tagging:**
Estabelecimento de política obrigatória de tagging para todos os recursos:
- Environment (Production, Staging, Development)
- Project (nome do projeto ou aplicação)
- Owner (responsável técnico)
- CostCenter (centro de custo departamental)
- Schedule (horário de funcionamento esperado)

#### 3.1.4 Descrição do Caso de Uso

Nesta etapa inicial, foi adotado o AWS Cost Explorer como ferramenta estratégica para aumentar a visibilidade sobre o consumo dos recursos em nuvem da empresa. Com ele, foi possível realizar uma análise detalhada dos gastos por serviço, região, período e até mesmo por usuário.

Através dos dashboards personalizados, a equipe de TI conseguiu identificar diversos pontos de ineficiência críticos:

**Instâncias EC2 Ociosas:**
- 23 instâncias m5.large executando 24/7 com utilização média de CPU inferior a 5%
- 8 instâncias c5.xlarge em ambiente de desenvolvimento sem uso há mais de 30 dias
- 15 instâncias dedicadas a processos batch executando apenas 2 horas por dia

**Volumes EBS Não Utilizados:**
- 45 volumes EBS desconectados totalizando 2.3 TB de armazenamento
- 12 snapshots antigas sem política de retenção definida
- Volumes com IOPS provisionados muito acima da utilização real

**Serviços com Baixa Utilização:**
- Load Balancers configurados mas sem tráfego significativo
- Bancos RDS dimensionados para picos que ocorrem apenas 10% do tempo
- Instâncias reservadas subutilizadas devido a mudanças arquiteturais

#### 3.1.5 Ações Corretivas Implementadas

Com base nas informações coletadas, foram implementadas ações imediatas de correção:

**Otimização de Instâncias EC2:**
- Desativação de 31 instâncias ociosas
- Redimensionamento de 47 instâncias para tipos mais adequados
- Implementação de scheduler automatizado para instâncias de desenvolvimento

**Limpeza de Armazenamento:**
- Remoção de 45 volumes EBS desconectados
- Criação de política de lifecycle para snapshots
- Otimização de IOPS baseada em padrões reais de uso

**Reorganização de Instâncias Reservadas:**
- Modificação de 25 Reserved Instances para melhor aproveitamento
- Implementação de estratégia de Savings Plans
- Criação de processo de revisão trimestral de capacidade

Essas ações resultaram em uma redução imediata de 42% nos custos mensais, superando a meta inicial estabelecida.

### 3.2 Etapa 2 – Amazon EC2 Auto Scaling

#### 3.2.1 Objetivo da Ferramenta
Prover escalabilidade automática da infraestrutura de servidores, de forma elástica e sob demanda, garantindo performance otimizada e custos reduzidos através do dimensionamento dinâmico baseado em métricas de utilização.

#### 3.2.2 Análise de Padrões de Carga

Antes da implementação do Auto Scaling, foi conduzido um estudo detalhado dos padrões de carga das aplicações críticas:

**Aplicação Web Principal:**
- Pico de tráfego: 1.500 usuários simultâneos (horário comercial)
- Vale de tráfego: 150 usuários simultâneos (madrugada)
- Crescimento sazonal: +200% durante campanhas promocionais

**Sistema de Processamento de Dados:**
- Processamento batch: 4 horas diárias de alta demanda
- Processamento em tempo real: variável conforme volume de transações
- Picos imprevisíveis durante fechamentos mensais

**Aplicações Microserviços:**
- 12 serviços com padrões de carga independentes
- Dependências cruzadas requerendo coordenação de scaling
- SLA de resposta: 95% das requisições em menos de 200ms

#### 3.2.3 Configuração Técnica Detalhada

**Auto Scaling Groups (ASGs) Configurados:**

*ASG Web Frontend:*
- Instâncias: t3.medium (baseline) / c5.large (scale-out)
- Capacidade mínima: 2 instâncias
- Capacidade desejada: 4 instâncias
- Capacidade máxima: 20 instâncias
- Políticas de scaling baseadas em CPU, memória e latência

*ASG Processamento Backend:*
- Instâncias: m5.large (baseline) / m5.xlarge (scale-out)
- Capacidade mínima: 1 instância
- Capacidade desejada: 3 instâncias
- Capacidade máxima: 15 instâncias
- Políticas customizadas baseadas em tamanho de fila SQS

*ASG Microserviços:*
- Configuração individual para cada serviço
- Políticas de scaling baseadas em métricas customizadas
- Integração com Application Load Balancer para distribuição inteligente

**Métricas e Thresholds Configurados:**

- **CPU Utilization:** Scale-out quando >70% por 3 minutos consecutivos
- **Memory Utilization:** Scale-out quando >80% por 2 minutos consecutivos
- **Request Count:** Scale-out quando >1000 req/min por instância
- **Response Time:** Scale-out quando latência >300ms por 5 minutos
- **Queue Depth:** Scale-out quando >100 mensagens na fila SQS

**Políticas de Cool-down:**
- Scale-out cool-down: 300 segundos
- Scale-in cool-down: 600 segundos
- Proteção contra oscilações com warm-up period de 120 segundos

#### 3.2.4 Descrição do Caso de Uso

Para atender às demandas variáveis de uso dos sistemas corporativos, especialmente durante horários de pico ou em períodos de alta sazonalidade, foi configurado o serviço Amazon EC2 Auto Scaling de forma abrangente e inteligente.

A implementação considerou não apenas as métricas básicas de CPU e memória, mas também métricas customizadas específicas do negócio, como:

**Métricas de Negócio:**
- Volume de transações financeiras processadas
- Número de usuários simultâneos autenticados
- Tamanho das filas de processamento
- Latência de resposta das APIs críticas

**Integração com CloudWatch:**
Foram criados dashboards específicos para monitoramento do Auto Scaling com alertas proativos:
- Notificações quando scaling events são disparados
- Alertas de capacidade máxima atingida
- Métricas de eficiência de scaling (tempo de resposta dos novos instances)

**Estratégias de Scaling Diferenciadas:**

*Predictive Scaling:*
- Implementado para cargas previsíveis (horário comercial)
- Baseado em dados históricos de 6 meses
- Redução de 40% no tempo de resposta durante scale-out

*Dynamic Scaling:*
- Configurado para cargas imprevisíveis
- Resposta em tempo real a mudanças de demanda
- Múltiplas políticas com diferentes sensibilidades

*Scheduled Scaling:*
- Aplicado para eventos conhecidos (campanhas, fechamentos)
- Pre-scaling para evitar latência durante picos
- Integração com calendário corporativo

#### 3.2.5 Resultados Técnicos Obtidos

Essa solução permitiu à empresa ajustar automaticamente a quantidade de instâncias EC2 ativas conforme a carga de trabalho, garantindo performance adequada durante picos e economia de recursos durante períodos de baixa atividade.

**Métricas de Performance:**
- Redução de 67% no tempo médio de resposta durante picos
- Aumento de 99.8% na disponibilidade dos serviços críticos
- Eliminação completa de timeouts relacionados a sobrecarga

**Métricas de Eficiência:**
- Utilização média de CPU otimizada para 65-75%
- Redução de 58% no número de instâncias ociosas
- Melhoria de 45% na relação custo-benefício por transação processada

**Impacto nos Custos:**
Com isso, a empresa evitou a necessidade de manter servidores constantemente ativos sem utilização, otimizando o uso dos recursos computacionais e reduzindo significativamente os custos fixos com infraestrutura. A economia mensal atingiu 34% em comparação ao modelo anterior de capacidade fixa.

### 3.3 Etapa 3 – AWS Lambda

#### 3.3.1 Objetivo da Ferramenta
Executar trechos de código sob demanda, sem a necessidade de provisionar ou gerenciar servidores, utilizando o modelo serverless com cobrança baseada no uso real, proporcionando máxima eficiência de custos e escalabilidade infinita.

#### 3.3.2 Análise de Candidatos para Migração

Foi conduzida uma análise detalhada para identificar as aplicações e processos mais adequados para migração para o modelo serverless:

**Critérios de Seleção:**
- Execução esporádica ou baseada em eventos
- Baixo acoplamento com outros sistemas
- Tempo de execução inferior a 15 minutos
- Requisitos computacionais moderados
- Padrão de acesso imprevisível

**Aplicações Selecionadas para Migração:**

*Sistema de Processamento de Imagens:*
- Função: Redimensionamento e otimização de imagens
- Trigger: Upload de arquivos no S3
- Volume: 2.000-8.000 processamentos/dia
- Economia estimada: 78% em relação a instância dedicada

*API de Notificações:*
- Função: Envio de emails, SMS e push notifications
- Trigger: Eventos de negócio via SQS
- Volume: 15.000-50.000 notificações/dia
- Economia estimada: 65% em relação a instância dedicada

*Processamento de Logs:*
- Função: Análise e agregação de logs de aplicação
- Trigger: CloudWatch Logs
- Volume: Processamento contínuo com picos
- Economia estimada: 72% em relação a solução tradicional

*APIs de Integração:*
- Função: Conectores com sistemas third-party
- Trigger: Requisições HTTP via API Gateway
- Volume: 5.000-20.000 chamadas/dia
- Economia estimada: 69% em relação a microserviços tradicionais

#### 3.3.3 Arquitetura e Implementação Técnica

**Padrões Arquiteturais Adotados:**

*Event-Driven Architecture:*
- Utilização de SNS/SQS para desacoplamento
- Dead Letter Queues para tratamento de falhas
- Retry logic com backoff exponencial

*API Gateway Integration:*
- Rate limiting e throttling configurados
- Caching de respostas para otimização
- Autorização via Cognito User Pools

*Database Connectivity:*
- RDS Proxy para otimização de conexões
- Connection pooling para Lambda functions
- Implementação de circuit breaker pattern

**Configurações de Performance:**

*Memory Allocation:*
- Função de imagens: 1024MB (otimizada para processamento)
- APIs de notificação: 256MB (I/O intensivo)
- Processamento de logs: 512MB (balanceado)
- APIs de integração: 128MB (lightweight)

*Timeout Settings:*
- Processamento de imagens: 5 minutos
- Notificações: 30 segundos
- Logs: 2 minutos
- APIs de integração: 15 segundos

*Concurrent Executions:*
- Limite global: 1000 execuções simultâneas
- Reserved concurrency para funções críticas
- Monitoring de throttling events

#### 3.3.4 Otimizações de Performance e Custos

**Cold Start Mitigation:**
- Implementação de provisioned concurrency para APIs críticas
- Otimização do código para reduzir initialization time
- Utilização de layers para compartilhamento de dependências

**Memory e Runtime Optimization:**
- Profiling detalhado para right-sizing de memória
- Escolha de runtime otimizado (Node.js 18.x para melhor performance)
- Implementação de connection reuse para databases

**Monitoring e Observabilidade:**
- CloudWatch Logs estruturados para todas as funções
- X-Ray tracing para análise de performance
- Custom metrics para KPIs de negócio
- Alertas automáticos para error rates elevadas

#### 3.3.5 Descrição do Caso de Uso

Nesta fase, parte das aplicações backend da Abstergo Industries foi redesenhada e migrada para o modelo serverless, utilizando funções AWS Lambda de forma estratégica e otimizada.

O processo de migração seguiu uma abordagem gradual e baseada em dados:

**Fase 1 - Prova de Conceito:**
Migração inicial do sistema de processamento de imagens como piloto, validando:
- Padrões de arquitetura serverless
- Ferramentas de deployment e monitoring
- Processos de troubleshooting e debugging

**Fase 2 - Migração de APIs:**
Conversão das APIs de integração e notificações:
- Refatoração para arquitetura event-driven
- Implementação de rate limiting e caching
- Integração com API Gateway para exposição

**Fase 3 - Processamento Batch:**
Migração dos processos de análise de logs:
- Implementação de processamento paralelo
- Otimização para grandes volumes de dados
- Integração com Data Lake para armazenamento

#### 3.3.6 Benefícios Quantificados

Com isso, a empresa passou a executar código sob demanda, pagando exclusivamente pelo tempo de execução e pela quantidade de requisições, eliminando os custos associados à manutenção de servidores dedicados em funcionamento contínuo.

**Métricas de Custo:**
- Redução de 71% nos custos operacionais das aplicações migradas
- Eliminação de R$4.200/mês em custos de instâncias dedicadas
- ROI de 340% no primeiro ano após migração

**Métricas de Performance:**
- Redução de 89% no tempo de provisioning de novos recursos
- Aumento de 15x na velocidade de deployment
- Redução de 67% no tempo de troubleshooting

Além da economia gerada, a adoção do AWS Lambda trouxe benefícios como maior escalabilidade (automaticamente até 1000 execuções simultâneas), facilidade de manutenção (sem gerenciamento de SO ou runtime) e menor complexidade operacional (monitoramento integrado com CloudWatch).

---

## 4. Análise de Resultados e Métricas

### 4.1 Indicadores de Performance (KPIs)

**Redução de Custos:**
- **Custo Total de Propriedade (TCO):** Redução de 43% em 4 meses
- **Custos Mensais Recorrentes:** De R$28.400 para R$16.200 mensais
- **Custo por Transação:** Redução de 38% no custo unitário
- **ROI do Projeto:** 285% em 12 meses projetados

**Eficiência Operacional:**
- **Utilização de Recursos:** Aumento de 45% para 78% de utilização média
- **Tempo de Provisioning:** Redução de 4 horas para 15 minutos
- **Incidents Relacionados a Capacity:** Redução de 87%
- **Mean Time to Recovery (MTTR):** Redução de 45 minutos para 12 minutos

**Performance das Aplicações:**
- **Latência Média:** Redução de 340ms para 180ms
- **Availability:** Aumento de 99.2% para 99.8%
- **Throughput:** Aumento de 35% na capacidade de processamento
- **Error Rate:** Redução de 0.8% para 0.2%

### 4.2 Análise Comparativa: Antes vs. Depois

**Período de Referência: Janeiro 2025 (Antes) vs. Maio 2025 (Depois)**

| Métrica | Antes | Depois | Melhoria |
|---------|--------|---------|----------|
| Custo Mensal AWS | R$28.400 | R$16.200 | -43% |
| Instâncias EC2 Ativas | 78 | 45 | -42% |
| Utilização Média CPU | 45% | 78% | +73% |
| Downtime Mensal | 4.2 horas | 0.8 horas | -81% |
| Deployment Time | 3.5 horas | 25 minutos | -88% |
| Manual Tasks/Month | 124 | 31 | -75% |

### 4.3 Impacto nos Diferentes Ambientes

**Ambiente de Produção:**
- Redução de 41% nos custos
- Aumento de 67% na confiabilidade
- Zero incidentes relacionados a capacidade

**Ambiente de Staging:**
- Redução de 78% nos custos (maior impacto devido ao uso intermitente)
- Implementação de shutdown automático fora do horário comercial
- Economia de R$2.100/mês

**Ambiente de Desenvolvimento:**
- Redução de 85% nos custos
- Implementação de scheduler para instâncias (ligadas apenas durante horário de trabalho)
- Economia de R$3.400/mês

---

## 5. Governança e Sustentabilidade

### 5.1 Políticas de Governança Implementadas

**Policy de Cost Management:**
- Budget alerts configurados para todos os projetos
- Revisão mensal obrigatória de custos por equipe
- Aprovação obrigatória para recursos acima de R$500/mês

**Tagging Strategy:**
- Tags obrigatórias para todos os recursos
- Automation para aplicação de tags padrão
- Relatórios automáticos de recursos sem tags adequadas

**Resource Lifecycle Management:**
- Políticas automáticas de cleanup para recursos temporários
- Revisão trimestral de Reserved Instances
- Processo formal para decommissioning de recursos

### 5.2 Processo de Monitoramento Contínuo

**Dashboards Operacionais:**
- Dashboard executivo com métricas de alto nível
- Dashboard técnico com detalhes de utilização
- Dashboard de forecast com projeções de custos

**Alertas e Notificações:**
- Slack integration para alertas críticos
- Email reports semanais para managers
- SMS alerts para incidents de alta severidade

**Revisões Regulares:**
- Weekly: Revisão técnica de alertas e anomalias
- Monthly: Análise de custos e otimizações
- Quarterly: Revisão estratégica e planejamento

### 5.3 Roadmap de Melhorias Futuras

**Curto Prazo (6 meses):**
- Implementação de AWS Savings Plans
- Migração adicional de workloads para Lambda
- Implementação de Spot Instances para cargas não-críticas

**Médio Prazo (12 meses):**
- Adoção de containers com ECS/Fargate
- Implementação de data archiving para S3
- Otimização de databases com Aurora Serverless

**Longo Prazo (18 meses):**
- Machine Learning para predictive scaling
- Multi-region optimization
- Carbon footprint reduction initiatives

---

## 6. Lições Aprendidas e Boas Práticas

### 6.1 Principais Desafios Enfrentados

**Desafios Técnicos:**
- **Cold Starts em Lambda:** Resolvido com provisioned concurrency para funções críticas
- **Complexidade de Monitoring:** Implementação de observabilidade distribuída
- **Database Connection Pooling:** Utilização de RDS Proxy para otimização

**Desafios Organizacionais:**
- **Resistência à Mudança:** Programa de treinamento e workshops técnicos
- **Mudança de Mindset:** De "sempre ligado" para "on-demand"
- **Skillset Development:** Investimento em certificações AWS para a equipe

### 6.2 Boas Práticas Estabelecidas

**Design Principles:**
- Well-Architected Framework como padrão para novos projetos
- Cost optimization como critério obrigatório em architectural reviews
- Security by design em todas as implementações

**Operational Excellence:**
- Infrastructure as Code para todos os recursos
- Automated testing para Lambda functions
- Comprehensive logging e monitoring

**Reliability:**
- Multi-AZ deployment para recursos críticos
- Disaster recovery procedures testadas
- Chaos engineering practices implementadas

---

## 7. Conclusão

### 7.1 Síntese dos Resultados

A implementação das três ferramentas da AWS trouxe resultados excepcionais e superou as expectativas iniciais do projeto. Entre os principais benefícios alcançados pela Abstergo Industries, destacam-se:

**Impacto Financeiro:**
- **Redução expressiva de 43% nos custos mensais** com infraestrutura em nuvem, equivalente a uma economia de R$12.200 mensais
- **ROI de 285%** considerando o investimento em tempo e recursos do projeto
- **Payback period de 4.2 meses** para o investimento total realizado

**Visibilidade e Controle:**
- **Maior visibilidade e controle sobre o consumo** de serviços, possibilitando um planejamento mais eficaz e estratégico
- **Implementação de cultura de cost awareness** em todas as equipes de desenvolvimento
- **Processo automatizado de alertas e correções** para desvios de orçamento

**Eficiência Operacional:**
- **Otimização da eficiência operacional**, com automação de escalabilidade e execução de código sem necessidade de servidores permanentes
- **Redução de 75% nas tarefas manuais** relacionadas ao gerenciamento de infraestrutura
- **Aumento de 67% na confiabilidade** dos serviços críticos

**Capacitação da Equipe:**
- **Diminuição do esforço necessário para gerenciamento** da infraestrutura, liberando a equipe de TI para focar em iniciativas de maior valor agregado
- **Upskilling da equipe** em tecnologias cloud-native e serverless
- **Estabelecimento de center of excellence** para cloud optimization

### 7.2 Impacto Estratégico

O projeto demonstrou que a otimização de custos em nuvem não é apenas uma questão operacional, mas uma vantagem competitiva estratégica. A empresa conseguiu:

- **Reinvestir a economia** em iniciativas de inovação e novos produtos
- **Estabelecer benchmark** para outras unidades de negócio
- **Melhorar a posição competitiva** através de custos operacionais otimizados

### 7.3 Recomendações Futuras

Diante dos resultados obtidos, recomenda-se enfaticamente:

**Continuidade e Expansão:**
- **A continuidade da utilização das ferramentas implementadas**, com monitoramento constante e ajustes incrementais
- **Expansão da estratégia** para outras workloads e departamentos
- **Implementação de advanced optimization techniques** como Spot Instances e Savings Plans

**Evolução Tecnológica:**
- **A realização de estudos contínuos** para avaliar novas soluções oferecidas pela AWS que possam complementar ou substituir serviços atuais com ainda mais eficiência e economia
- **Adoção de containers e Kubernetes** para workloads não adequadas ao serverless
- **Implementação de ML/AI** para predictive optimization

**Governança e Cultura:**
- **Estabelecimento de políticas de governança** mais rigorosas e automatizadas
- **Programa de certificação AWS** para toda a equipe técnica
- **Criação de comunidade de prática** para compartilhamento de conhecimento

### 7.4 Próximos Passos

O sucesso deste projeto estabelece a fundação para uma jornada contínua de otimização e inovação. Os próximos passos incluem:

1. **Implementação das melhorias identificadas** durante o roadmap de 18 meses
2. **Expansão da metodologia** para outros projetos e departamentos
3. **Estabelecimento de partnership estratégico** com a AWS para advanced support
4. **Desenvolvimento de competências
