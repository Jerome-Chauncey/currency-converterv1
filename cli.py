import click
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from lib.db.models import Currency, ExchangeRate

@click.group()
def cli():
    """💱 Welcome to the currency Converter CLI!!"""
    click.secho("🌍 Currency Converter CLI ", fg= "green", bold=True)



def get_session():
    engine = create_engine("sqlite:///converter.db")
    Session = sessionmaker(bind=engine)
    return Session()

@cli.command()
def convert():
    """💱 Convert from one currency to another"""
    session = get_session()
    click.secho("Lets convert your money. 🪙")



    session.close()


    
if __name__ == "__main__":
    cli()




# import click 
# from lib.db.seed import Session 

# @click.command()

# def convert():
#     click.echo("💱 Welcome to the currency converter!!!")
#     amount = click.prompt("Enter the amount you want to convert", type = float)