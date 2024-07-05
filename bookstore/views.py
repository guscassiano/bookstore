from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import logging
import git

# Configuração básica do logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  # Definir o nível de log conforme necessário
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# Definir um manipulador de log para arquivo ou console
file_handler = logging.FileHandler('update_log.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

@csrf_exempt
def update(request):
    if request.method == "POST":
        logger.info('Recebido pedido de atualização')

        try:
            repo = git.Repo('/home/guscassiano/bookstore')
            origin = repo.remotes.origin
            origin.pull()
            logger.info('Código atualizado com sucesso no PythonAnywhere')
            return HttpResponse("Updated code on PythonAnywhere")
        except git.GitCommandError as e:
            logger.error(f'Erro ao atualizar o código: {e}')
            return HttpResponse("Couldn't update the code on PythonAnywhere. Check logs for details.", status=500)
        except Exception as e:
            logger.error(f'Erro inesperado: {e}')
            return HttpResponse("An unexpected error occurred. Check logs for details.", status=500)
    else:
        return HttpResponse("Couldn't update the code on PythonAnywhere. Invalid request method.", status=400)



def hello_world(request):
  template = loader.get_template('hello_world.html')
  return HttpResponse(template.render())