import click

@click.command()
@click.argument('filepath')
def process_data(filepath):
    processor = DataProcessor()
    processor.process_csv(filepath)

if __name__ == '__main__':
    process_data()