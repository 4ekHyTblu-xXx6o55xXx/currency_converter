import click
from .converter import convert
from .api import get_currencies
from .exceptions import CurrencyError

@click.group()
def cli():
    pass

@cli.command()
@click.argument("amount", type=float)
@click.argument("from_currency")
@click.argument("to_currency")
@click.option("--date", help="Дата в формате ГГГГ-ММ-ДД")
def convert_cmd(amount, from_currency, to_currency, date):
    from_cur = from_currency.upper()
    to_cur = to_currency.upper()
    try:
        result = convert(amount, from_cur, to_cur, date)
        if date:
            click.echo(f"{amount} {from_cur} = {result:.2f} {to_cur} (курс на {date})")
        else:
            click.echo(f"{amount} {from_cur} = {result:.2f} {to_cur}")
    except CurrencyError as e:
        click.echo(f"❌ Ошибка: {e}", err=True)

@cli.command()
def list_currencies():
    try:
        currencies = get_currencies()
        for code, name in sorted(currencies.items()):
            click.echo(f"{code}: {name}")
    except CurrencyError as e:
        click.echo(f"❌ Ошибка: {e}", err=True)

if __name__ == "__main__":
    cli()