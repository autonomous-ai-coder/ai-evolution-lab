if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Data Processor CLI')
    parser.add_argument('input', help='Input data file')
    args = parser.parse_args()
    
    # Call DataProcessor with args.input
    # Assuming DataProcessor is defined elsewhere
    # DataProcessor(args.input)