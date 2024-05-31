import argparse
import src.encode as encode
import src.decode as decode

def main():
    parser = argparse.ArgumentParser(description='Steganography tool for encoding and decoding messages in images.')
    subparsers = parser.add_subparsers(dest='command', help='sub-command help')

    # Encode subcommand
    encode_parser = subparsers.add_parser('encode', help='Encode a message into an image')
    encode_parser.add_argument('image_path', type=str, help='Path to the input image')
    encode_parser.add_argument('message', type=str, help='Message to be encoded')
    encode_parser.add_argument('--debug', action='store_true', help='Enable debug mode')

    # Decode subcommand
    decode_parser = subparsers.add_parser('decode', help='Decode a message from an image')
    decode_parser.add_argument('image_path', type=str, help='Path to the encoded image')
    decode_parser.add_argument('--debug', action='store_true', help='Enable debug mode')

    args = parser.parse_args()

    if args.command == 'encode':
        encode.insert_msg(args.image_path, args.message, args.debug)
    elif args.command == 'decode':
        secret_message = decode.decode(args.image_path, args.debug)
        print(f"Secret message: {secret_message}")
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
