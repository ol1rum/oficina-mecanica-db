import questionary as quest
import os, subprocess
import datetime
from decimal import Decimal
from typing import Literal

from ..models import Cliente, Veiculo, OrdemServico, ServicoRealizado, Mecanico, Servico, OSDetalhada
from ..database import DatabaseManager
from ..services import (
    ServicoService, ClienteService, VeiculoService, OrdemServicoService, MecanicoService
)
from ..repositories import (
    ServicoRepository, ClienteRepository, VeiculoRepository, OSRepository, MecanicoRepository,
    ServicoRealizadoRepository
)

from .validadores import NovoCPFValidator, NovoValorStr
from .titulos import *
from .utils_cli import loop_menu, limpar_cpf
from .quest_base import (
    menu, buscar_na_lista, confirmar, texto, pausar, data, numero, opcoes_com_paginacao
)


class OficinaCLI:

    def __init__(self, db_manager: DatabaseManager) -> None:
        # iniciar repositorios
        # Os repositórios agora recebem o db_manager compartilhado
        __servico_repo = ServicoRepository(db_manager)
        __veiculo_repo = VeiculoRepository(db_manager)
        __cliente_repo = ClienteRepository(db_manager)
        __mecanico_repo = MecanicoRepository(db_manager)
        __os_repo = OSRepository(db_manager)
        __sr_repo = ServicoRealizadoRepository(db_manager)

        # iniciar services
        self.servico_serv = ServicoService(__servico_repo)
        self.veiculo_serv = VeiculoService(__veiculo_repo)
        self.cliente_serv = ClienteService(__cliente_repo, self.veiculo_serv)
        self.mecanico_serv = MecanicoService(__mecanico_repo)
        self.os_serv = OrdemServicoService(__os_repo, __sr_repo)

    @loop_menu
    def iniciar(self):
        self.__limpar_tela()
        print(t_nome)

        escolha = menu(
            "Selecione uma categoria para gerenciar:",
            {
                "clientes": "Clientes",
                "veiculos": "Veículos",
                "servicos": "Serviços",
                "mecanicos": "Equipe de Mecânicos",
                "os": "Ordens de Serviço (OS)",
                "sair": "Sair do Sistema"
            }
        )

        match escolha:
            case "clientes":
                self.menu_clientes()

            case "veiculos":
                self.menu_veiculos()
            
            case "servicos":
                self.menu_servicos()
            
            case "mecanicos":
                self.menu_mecanicos()
            
            case "os":
                self.menu_os()
                
            case "sair":
                self.__limpar_tela()
                return "sair"
    
    # =============== Submenu de clientes ===============
    @loop_menu
    def menu_clientes(self):
        self.__limpar_tela()
        print(t_clientes)

        escolha = menu(
            "Selecione uma ação para gerenciar clientes:",
            {
                "adicionar": "Adicionar Novo Cliente",
                "vincular veiculo": "Vincular Novo Veiuculo",
                "listar": "Listar Todos os Clientes",
                "voltar": "Voltar ao Menu Principal"
            }
        )

        print()
        match escolha:
            case "adicionar":
                self.fluxo_adicionar_cliente()
                pass

            case "vincular veiculo":
                self.fluxo_vincular_veiculo()
            
            case "listar":
                self.fluxo_listar_clientes()
            
            case "voltar":
                return "voltar"

    # -------- vincular novo veiculo ---------
    def fluxo_vincular_veiculo(self) -> None:
        print('\033[33;1m', "Pressione Ctrl+C para voltar", '\033[m', end="\n\n")

        lista_busca = self.cliente_serv.lista_busca()

        cliente_busca = buscar_na_lista("Nome/CPF do cliente:", lista_busca)
        
        marca = texto("Marca do Veículo:")
        modelo = texto("Modelo do Veículo:")
        ano = numero("Ano do Veículo:")
        placa = texto("Placa do Veículo:")
        cor = texto("Cor do Veículo:")

        veiculo = Veiculo(
            marca=marca,
            modelo=modelo,
            ano=int(ano),
            placa=placa,
            cor=cor
        )

        cpf = limpar_cpf(cliente_busca.split()[-1])
        cliente = self.cliente_serv.buscar_por_cpf(cpf)

        confirm = confirmar(f"Vincular {veiculo.marca} {veiculo.modelo} {veiculo.ano} ao cliente {cliente.nome}?")
        
        if confirm:
            self.cliente_serv.vincular_veiculo(cliente, veiculo)
        else:
            return
        
    # -------- lista de clietnes ---------
    def fluxo_listar_clientes(self) -> None:
        print('\033[33;1m', "Pressione Ctrl+C para voltar", '\033[m', end="\n\n")
        lista_clientes = self.cliente_serv.lista_formatada()
        print(*lista_clientes, sep="\n")
        print()
        pausar()

    # -------- adicionar cliente ---------
    def fluxo_adicionar_cliente(self) -> None:
        print('\033[33;1m', "Pressione Ctrl+C para voltar", '\033[m', end="\n\n")

        # -------- cliente ---------
        print(f"{' Cliente ':═^50}")
        cpf = texto("CPF do Cliente (apenas números):", validate=NovoCPFValidator(self.cliente_serv.existe_cliente))
        nome = texto("Nome do Cliente:")
        data_nasc = data("Data de Nascimento do Cliente:")
        endereco = texto("Endereço do Cliente:")

        # -------- veiculo ---------
        print()
        print(f"{' Veiculo ':═^50}")
        marca = texto("Marca do Veículo:")
        modelo = texto("Modelo do Veículo:")
        ano = numero("Ano do Veículo:")
        placa = texto("Placa do Veículo:")
        cor = texto("Cor do Veículo:")

        cliente = Cliente(
            cpf=cpf,
            nome=nome,
            data_nasc=datetime.date.strptime(data_nasc, "%d/%m/%Y"),
            endereco=endereco
        )
        veiculo = Veiculo(
            marca=marca,
            modelo=modelo,
            ano=int(ano),
            placa=placa,
            cor=cor
        )

        self.cliente_serv.adicionar_cliente(cliente_model=cliente, veiculo_model=veiculo)

    # =============== Submenu de veiculos ===============
    @loop_menu
    def menu_veiculos(self):
        self.__limpar_tela()
        print(t_veiculos)

        escolha = menu(
            "Selecione uma ação para gerenciar veículos:",
            {
                "Trocar": "Trocar Proprietário",
                "buscar placa": "Buscar Veículo por Placa",
                "listar": "Listar Todos os Veículos",
                "voltar": "Voltar ao Menu Principal"
            }
        )

        match escolha:

            case "Trocar":
                self.fluxo_trocar_proprietario()

            case "buscar placa":
                self.fluxo_buscar_por_placa()

            case "listar":
                self.fluxo_listar_veiculos()

            case "voltar":
                return "voltar"
    
    # ------- listar veiculos ---------
    def fluxo_listar_veiculos(self) -> None:
        print('\033[33;1m', "Pressione Ctrl+C para voltar", '\033[m', end="\n\n")
        lista_veiculos = self.veiculo_serv.lista_formatada()
        
        print(*lista_veiculos, sep="\n")
        print()
        pausar()

    # -------- buscar por placa ---------
    def fluxo_buscar_por_placa(self) -> None:
        print('\033[33;1m', "Pressione Ctrl+C para voltar", '\033[m', end="\n\n")
        lista_placas = self.veiculo_serv.listar_todas_placas()

        placa = buscar_na_lista("Placa do veículo:", lista_placas)

        veiculo = self.veiculo_serv.buscar_por_placa(placa)
        prop = self.cliente_serv.buscar_por_id(veiculo.cliente_id) if veiculo.cliente_id else None
        
        if prop:
            print(f"{' Veiculo ':═^20}╦{' Proprietário ':═^45}")
            print(f"{f'Placa: {veiculo.placa}':<20}║ {f'Nome: {prop.nome}':<45}")
            print(f"{f'Marca: {veiculo.marca}':<20}║ {f'CPF: {prop.cpf}':<45}")
            print(f"{f'Modelo: {veiculo.modelo}':<20}║ {f'Endereço: {prop.endereco}':<45}")
            print(f"{f'Ano: {veiculo.ano}':<20}║ {f'Data de Nascimento: {prop.data_nasc}':<45}")
            print(f"{f'Cor: {veiculo.cor}':<20}║ {f'ID: {prop.id}':<45}")
            print()
            pausar()
        
    # -------- trocar proprietario ---------
    def fluxo_trocar_proprietario(self) -> None:
        print('\033[33;1m', "Pressione Ctrl+C para voltar", '\033[m', end="\n\n")
        lista_placas = self.veiculo_serv.listar_todas_placas()
        lista_busca = self.cliente_serv.lista_busca()

        placa = buscar_na_lista("Placa do veículo:", lista_placas)
        cliente_busca = buscar_na_lista("Nome/CPF do cliente:", lista_busca)
        cpf = limpar_cpf(cliente_busca.split()[-1])

        cliente = self.cliente_serv.buscar_por_cpf(cpf)

        if cliente.id:
            self.veiculo_serv.transferir_proprietario(cliente_id=cliente.id, placa=placa)

    
    # =============== Submenu de servicos ===============
    @loop_menu
    def menu_servicos(self):
        self.__limpar_tela()
        print(t_servicos)

        escolha = menu(
            "Selecione uma ação para gerenciar serviços:",
            {
                "cadastrar": "Cadastrar Novo Serviço",
                "listar ativos": "Listar Serviços Ativos",
                "desativar": "Desativar Serviço",
                "editar": "Editar Serviço",
                "voltar": "Voltar ao Menu Principal"
            }
        )

        match escolha:

            case "cadastrar":
                self.fluxo_cadastrar_servico()
            
            case "listar ativos":
                self.fluxo_listar_servicos()
            
            case "desativar":
                self.fluxo_desativar_servico()
            
            case "editar":
                self.fluxo_editar_servico()
            
            case "voltar":
                return "voltar"

    # -------- cadastar serviço ---------
    def fluxo_cadastrar_servico(self):
        print('\033[33;1m', "Pressione Ctrl+C para voltar", '\033[m', end="\n\n")
        servicos_ativos = self.servico_serv.listar_ativos()
        desc_servicos_ativos = self.servico_serv.listar_descricao(servicos_ativos)

        nome = texto("Nome do Serviço:", validate=NovoValorStr(desc_servicos_ativos, "Já existe um serviço cadastrado com esse nome."))
        preco = numero("Preço do Serviço:", decimal=True)

        servico = Servico(
            descricao=nome,
            preco=Decimal(preco)
        )

        self.servico_serv.adicionar(servico_model=servico)

    # -------- listar serviços ativos ---------
    def fluxo_listar_servicos(self):
        print('\033[33;1m', "Pressione Ctrl+C para voltar", '\033[m', end="\n\n")
        serv_ativos = self.servico_serv.listar_ativos()
        lista_serv = self.servico_serv.lista_formatada(serv_ativos)
        
        print(*lista_serv, sep="\n")
        print()
        pausar()

    # -------- desativar serviço ---------
    def fluxo_desativar_servico(self):
        print('\033[33;1m', "Pressione Ctrl+C para voltar", '\033[m', end="\n\n")
        lista_serv_ativo = self.servico_serv.listar_ativos()
        lista_serv_format = self.servico_serv.lista_formatada(lista_serv_ativo)
        
        dict_menu = {str(n):serv for n, serv in enumerate(lista_serv_format)}
        serv_esc = menu("Selecione o serviço a ser desativado:", dict_menu)

        servico = lista_serv_ativo[int(serv_esc)]
        if servico.id:
            self.servico_serv.desativar(servico.id)

    # -------- editar serviço ---------
    def fluxo_editar_servico(self):
        print('\033[33;1m', "Pressione Ctrl+C para voltar", '\033[m', end="\n\n")
        lista_serv_ativo = self.servico_serv.listar_ativos()
        lista_serv_format = self.servico_serv.lista_formatada(lista_serv_ativo)
        
        dict_menu = {str(n):serv for n, serv in enumerate(lista_serv_format)}
        serv_esc = menu("Selecione o serviço a ser desativado:", dict_menu)

        servico = lista_serv_ativo[int(serv_esc)]

        while True:
            if servico.id:
                edit_esc = menu(
                    "Selecione o que deseja editar:",
                    {
                        "nome": f"Nome: {servico.descricao}",
                        "preco": f"Preço: {servico.preco}",
                        "voltar": "Voltar ao menu"
                    }
                )
                match edit_esc:
                    case "nome":
                        nome = texto("Novo nome do serviço:", default=servico.descricao)
                        servico.descricao = nome
                        self.servico_serv.alterar_preco_descricao(servico.id, servico)


                    case "preco":
                        preco = numero("Novo preço do serviço:", decimal=True, default=str(servico.preco))
                        servico.preco = Decimal(preco)
                        self.servico_serv.alterar_preco_descricao(servico.id, servico)

                    case "voltar":
                        return

    # =============== Submenu de mecanicos ===============
    @loop_menu
    def menu_mecanicos(self):
        self.__limpar_tela()
        print(t_mecanicos)

        escolha = menu(
            "Selecione uma ação para gerenciar mecanicos:",
            {
                "contratar": "Contratar Novo Mecânico",
                "demitir": "Demitir Mecânico",
                "listar ativos": "Listar Mecânicos Ativos",
                "voltar": "Voltar ao Menu Principal"
            }
        )

        match escolha:

            case "contratar":
                self.fluxo_contratar_mecanico()
            
            case "demitir":
                self.fluxo_demitir_mecanico()

            case "listar ativos":
                self.fluxo_listar_mecanicos()
            
            case "voltar":
                return "voltar"

    # -------- contratar mecanico ---------
    def fluxo_contratar_mecanico(self):
        print('\033[33;1m', "Pressione Ctrl+C para voltar", '\033[m', end="\n\n")

        mecanico = texto("CPF do Mecânico (apenas números):", validate=NovoCPFValidator(self.mecanico_serv.mecanico_ativo))
        nome = texto("Nome do Mecânico:")
        data_contratacao = data("Data de Contratação do Mecânico:")
        salario = numero("Salário do Mecânico:")

        mecanico = Mecanico(
            cpf=mecanico,
            nome=nome,
            data_contratacao=datetime.date.strptime(data_contratacao, "%d/%m/%Y"),
            salario=Decimal(salario)
        )

        self.mecanico_serv.adicionar(mecanico)

    # -------- demitir mecanico ---------
    def fluxo_demitir_mecanico(self):
        print('\033[33;1m', "Pressione Ctrl+C para voltar", '\033[m', end="\n\n")
        lista_mecanico_busca = self.mecanico_serv.lista_busca()

        mecanico = buscar_na_lista("CPF do Mecânico:", lista_mecanico_busca)
        # limpar cpf
        cpf = limpar_cpf(mecanico.split()[-1])

        mecanico = self.mecanico_serv.buscar_por_cpf(cpf)

        if mecanico.id:
            self.mecanico_serv.demitir(mecanico.id)
    
    # =============== Submenu de ordens de servico ===============

    # -------- lista de mecânicos ativos ---------
    def fluxo_listar_mecanicos(self):
        print('\033[33;1m', "Pressione Ctrl+C para voltar", '\033[m', end="\n\n")

        lista_formatada = self.mecanico_serv.lista_formatada()
        print(*lista_formatada, sep="\n")
        print()
        pausar()


    @loop_menu
    def menu_os(self):
        self.__limpar_tela()
        print(t_os)

        escolha = menu(
            "Selecione uma ação para gerenciar ordens de serviço:",
            {
                "Abrir": "Abrir OS",
                "historico": "Ver Histórico de OSs",
                "gerenciar": "Gerenciar OSs ativa",
                "voltar": "Voltar ao Menu Principal"
            }
        )

        match escolha:
            case "Abrir":
                self.fluxo_abrir_os()
            
            case "historico":
                self.menu_historico_os()
            
            case "gerenciar":
                self.fluxo_gerenciar_os()
            
            case "voltar":
                return "voltar"
    
    # -------- abrir nova ordem de serviço ---------
    def fluxo_abrir_os(self):
        print('\033[33;1m', "Pressione Ctrl+C para voltar", '\033[m', end="\n\n")
        
        busca_cliente = self.cliente_serv.lista_busca()

        # Pegar cliente da OS
        cliente_esc = buscar_na_lista("Nome/CPF do Cliente:", busca_cliente)
        cpf = limpar_cpf(cliente_esc.split()[-1])
        cliente = self.cliente_serv.buscar_por_cpf(cpf)

        # Pegar veiculo da OS
        lista_veiculos_cliente = self.veiculo_serv.buscar_por_cliente(cliente)
        busca_veiculo = self.veiculo_serv.listar_placas(lista_veiculos_cliente)

        veiculo_esc = buscar_na_lista("Placa do Veículo:", busca_veiculo)
        veiculo = self.veiculo_serv.buscar_por_placa(veiculo_esc)

        km_atual = numero("Quilometragem Atual do Veículo:")
        obs = texto("Observações da OS:")

        if cliente.id and veiculo.id:
            os = OrdemServico(
                cliente_id=cliente.id,
                veiculo_id=veiculo.id,
                quilometragem_abertura=int(km_atual),
                observacoes=obs
            )
            self.os_serv.abrir_os(os)
            print("\nOrdem de Serviço aberta com sucesso!")
            pausar()

    def selecionar_os(self, lista_os: list[OrdemServico], mensagem: str) -> int | Literal["voltar"]:
        if not lista_os:
            print("\nNenhuma Ordem de Serviço encontrada.")
            pausar()
            return "voltar"

        dict_formatado = {
            os.id: f"{os.numero_os} - {os.status} | Aberta em: {os.data_hora_abertura.strftime('%d/%m/%Y %H:%M') if os.data_hora_abertura else 'N/A'}"
            for os in lista_os if os.id is not None
        }

        return opcoes_com_paginacao(mensagem, dict_formatado)

    # -------- historico de ordens de serviços ---------
    @loop_menu
    def menu_historico_os(self):
        print('\033[33;1m', "Pressione Ctrl+C para voltar", '\033[m', end="\n\n")

        lista_finalizadas = self.os_serv.listar_finalizadas()
        lista_canceladas = self.os_serv.listar_canceladas()
        
        os_id = self.selecionar_os(
            lista_finalizadas + lista_canceladas, 
            "Selecione uma OS do histórico para visualizar:"
        )

        if os_id == "voltar":
            return "voltar"
        
        det_os = self.os_serv.detalhes_os(os_id)
        self.mostrar_detalhes_os(det_os)


    def mostrar_detalhes_os(self, det_os: OSDetalhada):
        print(f"{f' OS-{det_os.numero_os} ':═^50}")
        print(f"Cliente: {det_os.cliente_nome}")
        print(f"CPF: {det_os.cliente_cpf}")
        print(f"Placa: {det_os.veiculo_placa}")
        print(f"Data de Abertura: {det_os.data_hora_abertura.strftime('%d/%m/%Y %H:%M')}")
        if det_os.data_hora_fechamento:
            print(f"Data de Fechamento: {det_os.data_hora_fechamento.strftime('%d/%m/%Y %H:%M')}")
        print(f"Status: {det_os.status}")
        print(f"Quilometragem: {det_os.quilometragem_abertura}")
        print(f"Observações: {det_os.observacoes or 'Nenhuma'}")
        print()
        pausar()


    # -------- gerenciar ordens de serviços ---------
    @loop_menu
    def fluxo_gerenciar_os(self):
        print('\033[33;1m', "Pressione Ctrl+C para voltar", '\033[m', end="\n\n")
        
        lista_abertas = self.os_serv.listar_abertas()
        os_id = self.selecionar_os(lista_abertas, "Selecione uma OS aberta para gerenciar:")

        if os_id == "voltar":
            return "voltar"

        self.menu_acoes_os(os_id)

    @loop_menu
    def menu_acoes_os(self, os_id: int):
        self.__limpar_tela()
        det_os = self.os_serv.detalhes_os(os_id)
        print(f"Gerenciando OS: {det_os.numero_os} - {det_os.cliente_nome}")
        
        escolha = menu(
            "Selecione uma ação:",
            {
                "detalhes": "Ver Detalhes Completos",
                "add_servico": "Adicionar Serviço Realizado",
                "mudar_obs": "Alterar Observações",
                "finalizar": "Finalizar OS",
                "cancelar": "Cancelar OS",
                "voltar": "Voltar"
            }
        )

        match escolha:
            
            case "detalhes":
                self.mostrar_detalhes_os(det_os)

            case "add_servico":
                self.fluxo_add_servico_os(os_id)

            case "mudar_obs":
                nova_obs = texto("Nova observação:", default=det_os.observacoes or "")
                self.os_serv.alterar_observacoes(os_id, nova_obs)

            case "finalizar":
                if confirmar(f"Deseja realmente FINALIZAR a OS {det_os.numero_os}?"):
                    self.os_serv.finalizar_os(os_id)
                    return "voltar"
                
            case "cancelar":
                if confirmar(f"Deseja realmente CANCELAR a OS {det_os.numero_os}?"):
                    self.os_serv.cancelar_os(os_id)
                    return "voltar"
                
            case "voltar":
                return "voltar"

    def fluxo_add_servico_os(self, os_id: int):
        servicos = self.servico_serv.listar_ativos()
        mecanicos = self.mecanico_serv.lista_busca() # Precisamos de uma lista de mecanicos

        # Selecionar Serviço
        dict_servicos = {s.id: f"{s.descricao} (R$ {s.preco})" for s in servicos if s.id is not None}
        servico_id = opcoes_com_paginacao("Selecione o serviço:", dict_servicos)
        if servico_id == "voltar": return

        # Selecionar Mecânico
        mecanico_esc = buscar_na_lista("Selecione o mecânico:", mecanicos)
        m_cpf = limpar_cpf(mecanico_esc.split()[-1])
        mecanico = self.mecanico_serv.buscar_por_cpf(m_cpf)

        # Valor (pode sugerir o padrão)
        serv_obj = next(s for s in servicos if s.id == servico_id)
        valor = numero(f"Valor cobrado (Padrão: {serv_obj.preco}):", decimal=True, default=str(serv_obj.preco))

        sr = ServicoRealizado(
            os_id=os_id,
            servico_id=servico_id,
            mecanico_id=mecanico.id, # type: ignore
            valor_cobrado=Decimal(valor)
        )
        
        self.os_serv.add_servico_realizado(sr)
        print("\nServiço adicionado com sucesso!")
        pausar()

    def __limpar_tela(self) -> None:
        subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
