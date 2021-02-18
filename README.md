# controle

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/regomes33/controle.git
cd controle
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements/dev.txt # ou
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
```

### Variáveis de ambiente

Defina suas variáveis de ambiente em `.env`

```
