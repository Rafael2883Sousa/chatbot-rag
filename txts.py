import os

# Criar amostras simuladas de textos sobre phishing
textos = {
    "phishing_definicao.txt": """
Phishing é uma técnica de engenharia social utilizada por cibercriminosos para enganar usuários e induzi-los a revelar informações sensíveis, como senhas, números de cartão de crédito ou credenciais de acesso.
O ataque normalmente ocorre através de e-mails ou sites falsos que se disfarçam como entidades confiáveis.
""",

    "tipos_de_phishing.txt": """
Existem diversos tipos de phishing:
- Spear phishing: ataque direcionado a indivíduos específicos;
- Whaling: ataques voltados a executivos de alto escalão;
- Vishing: phishing por meio de chamadas telefônicas;
- Smishing: phishing via mensagens SMS.
""",

    "exemplos_reais.txt": """
Em 2021, uma campanha de phishing simulava mensagens da Microsoft pedindo atualização de senha. Milhares de usuários clicaram em links falsos, resultando em roubo de credenciais.
Outro exemplo ocorreu em 2020, durante a pandemia, com e-mails falsos sobre vacinas da COVID-19.
""",

    "como_identificar_phishing.txt": """
Algumas formas de identificar e-mails de phishing incluem:
- Verificar o domínio do remetente;
- Desconfiar de erros gramaticais;
- Evitar clicar em links encurtados ou anexos inesperados;
- Verificar se o site possui certificado HTTPS.
""",

    "como_prevenir.txt": """
Para se proteger contra phishing:
- Ative a autenticação de dois fatores;
- Nunca forneça informações sensíveis por e-mail;
- Use filtros antispam atualizados;
- Realize treinamentos de conscientização com funcionários.
""",

    "spf_dkim_dmarc.txt": """
SPF, DKIM e DMARC são mecanismos de autenticação de e-mails que ajudam a prevenir spoofing e phishing.
- SPF: verifica se o IP do remetente tem permissão para enviar e-mails em nome do domínio.
- DKIM: autentica a integridade da mensagem.
- DMARC: política de aplicação dos dois anteriores.
""",

    "ataques_em_portugal.txt": """
Em Portugal, ataques de phishing têm aumentado nos últimos anos. Em 2022, houve um pico de campanhas falsas simulando bancos portugueses, como a CGD e o BPI.
Os ataques visavam principalmente obter dados bancários através de sites falsos.
""",

    "phishing_redes_sociais.txt": """
Redes sociais também são alvo de phishing. Ataques comuns incluem links encurtados enviados por contas comprometidas e solicitações de login falsas em páginas que imitam redes populares como Instagram e Facebook.
""",

    "phishing_bancos.txt": """
Bancos são alvos recorrentes de phishing. Os atacantes criam sites que simulam o ambiente bancário real para capturar senhas e números de conta.
Mensagens SMS com links fraudulentos são uma das táticas mais utilizadas.
""",

    "boas_praticas_empresas.txt": """
Empresas devem implementar políticas robustas contra phishing:
- Realizar simulações periódicas;
- Monitorar logs de e-mail;
- Sensibilizar todos os departamentos;
- Estabelecer canais de denúncia seguros e acessíveis.
"""
}

base_path = "phishing_texts"
os.makedirs(base_path, exist_ok=True)

for nome_arquivo, conteudo in textos.items():
    with open(os.path.join(base_path, nome_arquivo), "w", encoding="utf-8") as f:
        f.write(conteudo)

base_path
