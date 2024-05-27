class Message:
    def __init__(self, content, emisor, receptor, state, visible) -> None:
        self.content = content
        self.emisor = emisor
        self.receptor = receptor
        self.state = state
        self.visible = visible

    def ShowMessage(self):
        message = str()

        if(self.visible):
            if(self.state == "Recibido"):
                message = f"De {self.emisor} para {self.receptor}: {self.content}"
            else:
                message = "Usted no tiene nuevos mensajes"
        else:
            message = "No se puede mostrar mensaje"
        
        return message

    def UpdateMessageState(self, newState):
        self.state = newState

Message2 = Message("Hola como estas bebe", "Andy", "Señor Boza", "Enviado", True)

print(Message2.ShowMessage())

print("5 minutos despues . . . ")

Message2.UpdateMessageState("Recibido")

print(Message2.ShowMessage())

Message2.UpdateMessageState("Visto")