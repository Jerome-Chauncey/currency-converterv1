from lib.helpers import(
    convert_currency,
    list_currencies,
    find_currency_by_code,
    create_currency,
    update_currency,
    delete_currency,
    exit_program
)

def main():
    while True:
        menu()
        choice = input("> ").strip()

        if choice == "0":
            exit_program()
        elif choice == "1":
            convert_currency()
        elif choice == "2":
            list_currencies()
        elif choice == "3":
            find_currency_by_code()
        elif choice == "4":
            create_currency()
        elif choice == "5":
            update_currency()
        elif choice == "6":
            delete_currency()
        else:
            print("Invalid choice. Please try again.")

def menu():
    
    print("\n💱 Welcome to the Currency Converter CLI")
    print("Please choose an option:")
    print("0. Exit")
    print("1. Convert currency")
    print("2. List all currencies")
    print("3. Find currency by code")
    print("4. Create a new currency")
    print("5. Update a currency")
    print("6. Delete a currency")


if __name__ == "__main__":
    main()
















































# import click
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import create_engine
# from lib.db.models import Currency, ExchangeRate

# engine = create_engine("sqlite:///converter.db")
# Session = sessionmaker(bind=engine)
# session = Session()

# @click.group(invoke_without_command=True)
# @click.pass_context
# def cli(ctx):
#     """💱 Welcome to the Currency Converter CLI!"""
#     click.secho("\n🌍 Welcome to the Currency Converter CLI!", fg="green", bold=True)

#     if ctx.invoked_subcommand is None:
#         click.echo("\nWhat would you like to do?")
#         click.echo("1. 💱 Convert currency")
#         click.echo("2. 🛠 Manage currencies")

#         choice = click.prompt("Enter your choice (1 or 2)", type=int)

#         if choice == 1:
#             ctx.invoke(convert)
#         elif choice == 2:
#             click.echo("\nTry one of these commands:\n")
#             click.secho("• currency create", fg="cyan")
#             click.secho("• currency list", fg="cyan")
#             click.secho("• currency update", fg="cyan")
#             click.secho("• currency delete", fg="cyan")
#         else:
#             click.secho("Invalid choice. Please restart.", fg="red")




# @cli.command()
# def convert():
#     """💱 Convert from one currency to another"""
    
#     click.secho("Lets convert your money. 🪙")

#     try:
#         amount = click.prompt("How much money do you want to convert?", type=float)


#         currencies = session.query(Currency).all()
#         if not currencies:
#             click.secho("No currencies found in the database.", fg= "red")
#             return
        
#         click.echo("\nChoose the currency to convert **to**:")
#         for idx, currency in enumerate(currencies, start= 1):
#             click.echo(f"{idx}, {currency.code} ({currency.name})")

#         base_choice = click.prompt("Choose the currency you are converting FROM (enter number)", type=int)

#         if base_choice < 1 or base_choice > len(currencies):
#             click.secho("Invalid choice. Please run the converter again.", fg="red")
#             return
#         base_currency = currencies[base_choice -1]


#         click.echo()
#         for idx, currency in enumerate(currencies, start=1):
#             click.echo(f"{idx}. {currency.code} ({currency.name})")

#         target_choice = click.prompt("\nChoose the currency you are converting To (enter number)", type=int)
#         if target_choice < 1 or target_choice > len(currencies):
#             click.secho(f"Invalid choice. Please run the converter again.", fg="red")
#             return
#         target_currency = currencies[target_choice -1]

#         if base_currency.id == target_currency.id:
#             click.secho("You selected the same currency for both. Nothing to convert.", fg="red")

#         rate_obj = session.query(ExchangeRate).filter_by(
#             base_currency_id=base_currency.id,
#             target_currency_id=target_currency.id
#         ).order_by(ExchangeRate.timestamp.desc()).first()

#         if not rate_obj:
#             click.secho("No exchange rate found for this currency pair.", fg="red")
#             return

#         converted = float(rate_obj.rate) * amount
#         click.secho(f"\nConverted amount in {target_currency.code}: {target_currency.symbol}{converted:,.2f}", fg="cyan", bold=True)
#     except Exception as e:
#         click.secho(f"Something went wrong: {str(e)}", fg="red")
    



# if __name__ == "__main__":
#     cli()




