import click

@click.command()
@click.argument('file')
def main(file):
    process_data(file)
    click.echo('Done!')