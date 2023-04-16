# mannuall-search

Sosyal medya hesaplarında kullanıcı aramaya yarayan bir araçtır.

## Gereksinimler

mannuall-search aşağıdaki kütüphaneleri kullanır.

* Colorama
* Requests

## Kurulumu

Projeyi klonlamak için;

```python
git clone https://github.com/thealper2/mannuall-search.git
```
Gerekli kütüphaneleri kurmak için;

```python
python -m pip install -r requirements.txt
```

## Kullanımı

```bash
usage: mannuall-search.py [-h] [--username USERNAME] [--site SITE] [--all] [--out OUT] [--list]

options:
  -h, --help           show this help message and exit
  --username USERNAME
  --site SITE
  --all
  --out OUT
  --list
```

## Örnekler

```python
python3 mannuall-search.py --username alperkaraca --out alper.txt
python3 mannuall-search.py --username alperkaraca --site github --out alper.txt
python3 mannuall-search.py --list
```
