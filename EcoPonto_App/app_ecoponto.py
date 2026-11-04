import streamlit as st
import pandas as pd
from datetime import datetime

# Configuração da página móvel
st.set_page_config(
    page_title="EcoPonto JF",
    page_icon="♻️",
    layout="centered"
)

# Dados oficiais dos Ecopontos de Juiz de Fora (DEMLURB)
ECOPONTOS_DADOS = [
    {
        "nome": "Ecoponto Aeroporto",
        "tipo": "Tradicional",
        "endereco": "Rua José Apolônio dos Reis, 100",
        "referencia": "Em frente ao Ginásio Municipal",
        "bairro": "Aeroporto",
        "horario": "Seg a Sex: 7h às 17h | Sáb: 8h às 12h",
        "residuos": ["Construção Civil / Entulho", "Móveis Velhos / Volumosos", "Eletrodomésticos e Eletrônicos", "Podas de Jardim", "Recicláveis Comuns"]
    },
    {
        "nome": "Ecoponto Barbosa Lage",
        "tipo": "Tradicional",
        "endereco": "Rua Antônio Weitzel, s/nº",
        "referencia": "Em frente ao nº 710",
        "bairro": "Barbosa Lage",
        "horario": "Seg a Sex: 7h às 17h | Sáb: 8h às 12h",
        "residuos": ["Construção Civil / Entulho", "Móveis Velhos / Volumosos", "Eletrodomésticos e Eletrônicos", "Podas de Jardim", "Recicláveis Comuns"]
    },
    {
        "nome": "Ecoponto Nova Benfica",
        "tipo": "Tradicional",
        "endereco": "Rua Francisco Pinheiro, s/nº",
        "referencia": "Próximo à praça do bairro",
        "bairro": "Benfica",
        "horario": "Seg a Sex: 7h às 17h | Sáb: 8h às 12h",
        "residuos": ["Construção Civil / Entulho", "Móveis Velhos / Volumosos", "Eletrodomésticos e Eletrônicos", "Podas de Jardim", "Recicláveis Comuns"]
    },
    {
        "nome": "Ecoponto Parque das Águas",
        "tipo": "Tradicional",
        "endereco": "Rua José Meirelles, s/nº",
        "referencia": "Região Norte",
        "bairro": "Parque das Águas",
        "horario": "Seg a Sex: 7h às 17h | Sáb: 8h às 12h",
        "residuos": ["Construção Civil / Entulho", "Móveis Velhos / Volumosos", "Eletrodomésticos e Eletrônicos", "Podas de Jardim", "Recicláveis Comuns"]
    },
    {
        "nome": "Ecoponto do Retiro",
        "tipo": "Tradicional",
        "endereco": "Rua Carlos Tavares de Pinho, s/nº",
        "referencia": "Região Sudeste",
        "bairro": "Retiro",
        "horario": "Seg a Sex: 7h às 17h | Sáb: 8h às 12h",
        "residuos": ["Construção Civil / Entulho", "Móveis Velhos / Volumosos", "Eletrodomésticos e Eletrônicos", "Podas de Jardim", "Recicláveis Comuns"]
    },
    {
        "nome": "Ecoponto de Pneus",
        "tipo": "Especializado",
        "endereco": "Rua Bartolomeu dos Santos, s/nº",
        "referencia": "Divisa Benfica e São Damião",
        "bairro": "Benfica / São Damião",
        "horario": "Seg a Sex: 7h às 16h30",
        "residuos": ["Pneus"]
    },
    {
        "nome": "Coleta Seletiva Móvel - Estação",
        "tipo": "Ponto Móvel",
        "endereco": "Praça Dr. João Penido",
        "referencia": "Praça da Estação (Centro)",
        "bairro": "Centro",
        "horario": "Quintas-feiras: 8h às 13h",
        "residuos": ["Recicláveis Comuns", "Eletrodomésticos e Eletrônicos", "Óleo de Cozinha Usado"]
    }
]

# Inicializa o histórico com o descarte de teste da Patrícia Pereira
if "historico_descartes" not in st.session_state:
    st.session_state["historico_descartes"] = [
        {
            "Cidadão": "Patrícia Pereira",
            "Bairro": "Barbosa Lage",
            "Ecoponto": "Ecoponto Barbosa Lage",
            "Resíduo": "Construção Civil / Entulho",
            "Volume (m³)": 0.50,
            "Observações": "Restos de piso cerâmico e argamassa ensacados.",
            "Data": datetime.now().strftime("%d/%m/%Y %H:%M")
        }
    ]

# Cabeçalho Principal do App
st.title("♻️ EcoPonto JF")
st.caption("Juiz de Fora Sustentável | Alinhado ao ODS 11 - Meta 11.6")

# Menu de Navegação Superior
menu = st.radio(
    "Navegue pelo Aplicativo:",
    ["🏠 Painel Informativo", "📍 Localizar Ecopontos", "🔍 Onde Descartar?", "📝 Registrar Descarte"],
    horizontal=True
)

st.divider()

# ----------------- TELA 1: PAINEL INFORMATIVO -----------------
if menu == "🏠 Painel Informativo":
    st.subheader("Regras de Segurança e Utilização (DEMLURB)")
    
    st.error("⚠️ **ATENÇÃO ÀS NORMAS OBRIGATÓRIAS DE SEGURANÇA:**\n"
             "- Proibida terminantemente a entrada de chinelos ou calçados abertos.\n"
             "- Proibida a entrada de bermudas ou shorts.\n"
             "- Proibida a entrada sem camisa.\n"
             "- Uso obrigatório de calça comprida e sapato/tênis fechado.")
    
    st.info("📦 **Limite Regulamentar Gratuito:**\n"
            "Cada cidadão pode descartar até **1 m³ (um metro cúbico)** de resíduos por dia, o equivalente a cerca de 1.000 litros ou entulho ensacado.")



    st.markdown("### Por que usar os Ecopontos?")
    st.write("O descarte irregular em encostas e calçadas entope bueiros, causa enchentes e gera riscos à saúde pública em Juiz de Fora. Utilize sempre as unidades gratuitas do DEMLURB.")

# ----------------- TELA 2: LOCALIZAR ECOPONTOS -----------------
elif menu == "📍 Localizar Ecopontos":
    st.subheader("Unidades Oficiais de Juiz de Fora")
    
    bairros = ["Todos os Bairros"] + sorted(list(set(e["bairro"] for e in ECOPONTOS_DADOS)))
    filtro_bairro = st.selectbox("Filtrar por Região/Bairro:", bairros)
    
    for eco in ECOPONTOS_DADOS:
        if filtro_bairro == "Todos os Bairros" or eco["bairro"] == filtro_bairro:
            with st.expander(f"📍 {eco['nome']} ({eco['tipo']})", expanded=True):
                st.write(f"**Endereço:** {eco['endereco']} - {eco['referencia']}")
                st.write(f"**Bairro:** {eco['bairro']}")
                st.write(f"**Horário:** {eco['horario']}")
                st.write(f"**Materiais aceitos:** {', '.join(eco['residuos'])}")

# ----------------- TELA 3: ONDE DESCARTAR? -----------------
elif menu == "🔍 Onde Descartar?":
    st.subheader("Consulta Inteligente de Resíduos")
    st.write("Selecione o que você precisa descartar para encontrar os locais autorizados:")
    
    tipos = [
    
        "Construção Civil / Entulho",
        "Móveis Velhos / Volumosos",
        "Eletrodomésticos e Eletrônicos",
        "Podas de Jardim",
        "Pneus",
        "Recicláveis Comuns",
        "Óleo de Cozinha Usado"
    ]
    escolha_residuo = st.selectbox("Qual material você quer descartar?", tipos)
    
    encontrados = [e for e in ECOPONTOS_DADOS if escolha_residuo in e["residuos"]]
    st.success(f"Encontramos **{len(encontrados)}** unidade(s) que recebem **{escolha_residuo}**:")
    
    for item in encontrados:
        st.markdown(f"- **{item['nome']}**: {item['endereco']} ({item['bairro']}) | *Horário:* {item['horario']}")

# ----------------- TELA 4: REGISTRAR DESCARTE -----------------
elif menu == "📝 Registrar Descarte":
    st.subheader("Registro Comunitário de Descarte Voluntário")
    st.write("Cadastre sua intenção de descarte para controle comunitário:")
    
    with st.form("form_descarte", clear_on_submit=True):
        nome = st.text_input("Nome Completo do Cidadão:", placeholder="Ex: Patrícia Pereira")
        bairro_cidadao = st.text_input("Bairro de Origem:", placeholder="Ex: Barbosa Lage")
        
        ecoponto_dest = st.selectbox(
            "Ecoponto de Destino:",
            [e["nome"] for e in ECOPONTOS_DADOS]
        )
        
        tipo_mat = st.selectbox(
            "Tipo de Resíduo:",
            [
                "Construção Civil / Entulho",
                "Móveis Velhos / Volumosos",
                "Eletrodomésticos e Eletrônicos",
                "Podas de Jardim",
                "Pneus",
                "Recicláveis Comuns",
                "Óleo de Cozinha Usado"
            ]
        )
        
        volume = st.number_input("Volume Estimado em m³ (Máximo permitido: 1.0 m³):", min_value=0.1, max_value=1.0, value=0.5, step=0.1)
        obs = st.text_area("Observações (opcional):", placeholder="Ex: Entulho em sacos de ráfia.")
        
        enviado = st.form_submit_button("Confirmar e Registrar Descarte")
        
        if enviado:
            if not nome:
                st.error("Por favor, preencha o seu nome.")
            else:
                novo_registro = {
                    "Cidadão": nome,
                    "Bairro": bairro_cidadao,
                    "Ecoponto": ecoponto_dest,
                    "Resíduo": tipo_mat,
                    "Volume (m³)": float(volume),
                    "Observações": obs,
                    "Data": datetime.now().strftime("%d/%m/%Y %H:%M")
                }
                st.session_state["historico_descartes"].append(novo_registro)
                st.success("✅ Registro de descarte cadastrado com sucesso!")

    st.divider()
    st.subheader("📊 Histórico Operacional de Descartes Registrados")
    df_historico = pd.DataFrame(st.session_state["historico_descartes"])
    st.dataframe(df_historico, use_container_width=True)