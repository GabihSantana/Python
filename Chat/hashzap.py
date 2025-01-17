# Tela inicial
    # Título: Hashzap
    # Botão: Iniciar chat
        # Ao clicar no botão:
            # abrir um popup/modal
        # Título: Bem-vindo ao Hashzap
        # Caixa de Texto: Escreva o nome no chat
        # Botão entrar no chat
            # ao clicar no botão:
                # fechar o popup
                # sumir com o título     
                # sumir com o botão iniciar chat
                    # carregar o chat
                    # carregar o campo de enviar mensagem: DIgite sua mensagem
                    # carregar botão enviar
                        # ao clicar em enviar, a mensagem será enviada e a caixa de mensagem será limpa

# Flet
# websocket

# Importar o Flet
import flet as ft

# Criar uma função principal para rodar o app
def main(pagina):
    # título
    titulo = ft.Text("Hashzap")
    pagina.add(titulo)

    def enviar_mensagem_tunel(mensagem):
        # executar tudo oq eu quero q aconteça para todos os usuários que receberem a msgm
        texto = ft.Text(mensagem)
        chat.controls.append(texto)
        pagina.update()
    
    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        nome_usuario = caixa_nome.value
        texto = campo_enviar_msgm.value
        mensagem = f"{nome_usuario}: {texto}"
        pagina.pubsub.send_all(mensagem)

        campo_enviar_msgm.value=""
        pagina.update()

    campo_enviar_msgm = ft.TextField(label="Digite aqui sua mensagem", on_submit=enviar_mensagem)
    botao_enviar_msgm = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    linha_enviar = ft.Row([campo_enviar_msgm, botao_enviar_msgm])
    chat = ft.Column()

    def entrar_chat(evento):
        popup.open = False
        pagina.remove(titulo)
        pagina.remove(botao_inicial)

        pagina.add(chat)
        pagina.add(linha_enviar)

        usuario = caixa_nome.value
        usuarios_chat = f"{usuario} entrou no chat"
        pagina.pubsub.send_all(usuarios_chat)
        pagina.update()

    # criar o popup
    titulo_popup = ft.Text("Bem-vindo ao Hashzap")
    caixa_nome = ft.TextField(label="Digite o seu nome")
    botao_popup = ft.ElevatedButton("Entrar no Chat", on_click=entrar_chat)

    popup = ft.AlertDialog(title=titulo_popup, content=caixa_nome, actions=[botao_popup])

    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    # botão inicial
    botao_inicial = ft.ElevatedButton("Iniciar chat", on_click=abrir_popup)
    pagina.add(botao_inicial)


# executar essa função com o flet
# ft.app(main)
ft.app(main, view=ft.WEB_BROWSER)