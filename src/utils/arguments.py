import argparse

# Constants
OPERATION_IMAGE = "img"
OPERATION_TEXT = "txt"
ALLOWED_OPERATIONS = [OPERATION_IMAGE, OPERATION_TEXT]

SIZE_BG = "1024"
SIZE_MD = "512"
SIZE_SM = "256"
ALLOWED_SIZE = [SIZE_BG, SIZE_MD, SIZE_SM]


def validate_arguments(args):
    if args.operation not in ALLOWED_OPERATIONS:
        exit(f"Operation argument --operation must be one of {ALLOWED_OPERATIONS}.")

    if args.operation == OPERATION_IMAGE and args.img_size not in ALLOWED_SIZE:
        exit(f"Image size argument --size must be one of {ALLOWED_SIZE}")


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--operation', dest='operation', required=False, default=OPERATION_TEXT, type=str,
                        help='Type of operation')
    parser.add_argument('-s', '--size', dest='img_size', required=False, default="512", type=str, help='Image size')
    parser.add_argument('-c', '--continuous', required=False, action='store_true',
                        help='Indicates if continuous mode is enabled')

    args = parser.parse_args()
    validate_arguments(args)

    return args.operation, args.img_size, args.continuous
