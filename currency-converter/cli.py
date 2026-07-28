import click
from .converter import convert
from .api import get_currencies
from .exceptions import CurrencyError
from .utils import normalize_currency_code, format_amount

@cli.command()
@click.argument("amount", type=float)
@click.argument("from_currency")
@click.argument("to_currency")
@click.option("--date")

@click.group()
def cli():
    pass
    
def convert_cmd(amount, from_currency, to_currency, date):
    try:
        from_cur = normalize_currency_code(from_currency)
        to_cur = normalize_currency_code(to_currency)
        result = convert(amount, from_cur, to_cur, date)
        formatted_result = format_amount(result)
        click.echo(f"{format_amount(amount)} {from_cur} = {formatted_result} {to_cur}")
    except ValueError as e:
        click.echo(f"❌ Ошибка ввода: {e}", err=True)
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
