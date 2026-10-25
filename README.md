💈 Barbearia Matheus do Corte — Sistema de Agendamento e Gestão Financeira
Um sistema web completo, moderno e responsivo desenvolvido para otimizar o fluxo de atendimento, agendamentos via WhatsApp e controle financeiro da Barbearia Matheus do Corte.

O projeto foi planejado para oferecer uma experiência ágil aos clientes através de uma página pública intuitiva e, ao mesmo tempo, fornecer um Painel Administrativo protegido por autenticação para o controlo total do negócio pelo barbeiro responsável.

🚀 Principais Funcionalidades
🌐 1. Site Público e Agendamento Inteligente (index.html)
Interface Moderna: Desenvolvida com Tailwind CSS num layout escuro e elegante com detalhes em dourado (barber style), totalmente responsivo para telemóveis e computadores.

Tabela de Serviços: Apresenta os serviços disponíveis (Corte Degradê/Social, Barba Completa e Combo) com valores e durações estimadas.

Agendamento com WhatsApp: O cliente preenche os seus dados, escolhe o serviço, a data e o horário, e ao confirmar, o sistema:

Guarda o registo automaticamente no sistema do painel administrativo.

Redireciona o utilizador instantaneamente para o WhatsApp com a mensagem de agendamento formatada e pronta a enviar.

🔒 2. Painel Administrativo Exclusivo (admin.html)
Acesso Restrito: Painel protegido por credenciais de administrador (matheus / 12345) com persistência de sessão para maior comodidade.

Gestão de Caixa e Ganhos:

Valor A Receber: Lista dinâmica com os clientes agendados e pendentes.

Saldo Realizado (Pago): Registo de atendimentos concluídos com valores confirmados.

Faturamento Automático: Cálculo em tempo real do faturamento do mês atual e do acumulado anual.

Controlo de Status: Botões interativos para alternar o atendimento entre "Pendente" e "Concluído / Pago" com atualização instantânea de caixa.

Ferramenta de Limpeza: Opção rápida para limpar dados de testes e redefinir o painel.

📊 3. Central de Relatórios e Exportação (relatorios.html)
Pré-visualização em Tempo Real: Tabela interativa com filtros rápidos para visualizar dados de "Todos", "Deste Mês", "Pagos" ou "Pendentes".

Exportação Profissional:

Excel (CSV): Opção para descarregar relatórios segmentados compatíveis com Microsoft Excel e Google Sheets.

PDF: Geração automática de relatórios em PDF diretamente no navegador utilizando a biblioteca jsPDF, organizados com o cabeçalho e tema da barbearia.

💻 Tecnologias Utilizadas
Frontend: HTML5, Tailwind CSS (via CDN) e JavaScript Moderno (ES6+).

Ícones e Estilização: Font Awesome.

Armazenamento de Dados: localStorage do navegador para sincronização imediata e persistência local entre sessões.

Geração de Documentos: jsPDF e jsPDF-AutoTable para exportação de relatórios em PDF.

Integração Backend (Opcional): Compatibilidade estruturada para comunicação com API em FastAPI (Python).