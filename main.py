from contactList import writeContactList
from sendMessage import sendSingleMessage, sendMultipleMessages
from chatLog import getLogOfContact
from utils import connectToBrowser
import time

def main():
    contato = '+55 32 8845-7769'
    browser = connectToBrowser("https://web.whatsapp.com/", contato)

    #writeContactList('contactList.whats')
    #sendMessageForWhatsappContact('+55 32 9943-9078', 'oi, eu sou o bot do Lucas')
    #sendMessageForWhatsappContact('Painel COVID-19', 'oi pessoal, essa mensagem foi enviada por mim usando um script em python. só pra dizer que o código funcionou rsrsrs')

    '''
    contacts = ['Bibi', '+55 32 9943-9078', 'Mariza', '+55 32 8845-6990', 'Mateus Lattari', 'Humanos do Tobi']
    messages = ['teste do bot 1 =)', 'teste do bot 2 =)', 'teste', 'oi noslin', 'oi chateus', 'ignorem mensagens estranhas pq estou testando um código que eu fiz q manda mensagem sozinho pro whatsapp. vou fazer meu gabinete do ódio']
    sendMultipleMessages(browser, contacts, messages)
    '''
    '''sendSingleMessage(browser, '+55 32 9943-9078', 'e aí meu bem? na verdade quem mandou essa mensagem nem foi eu, mas meu bot. oq é meio estranho se for pensar o.o')'''

    getLogOfContact(browser, contato)
    browser.close()

if __name__ == "__main__":
    main()
