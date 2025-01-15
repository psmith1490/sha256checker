import argparse
import hashlib 
import sys

def sha256(filename: str) -> str:
        result = ''
        with open(filename, "rb") as f:
                file_contents = f.read()
                hash_obj = hashlib.sha256()
                hash_obj.update(file_contents)
                result = hash_obj.hexdigest()
        f.close() 
        return result

def readHashFile(hashfile:str) -> str:
        result = ""
        with open(hashfile, 'r') as f:
                result = f.read()
        f.close()
        return(result)

def main():
        parser = argparse.ArgumentParser(prog='sha256 checker generator',
                description='Comparison tool for sha256 checksums', usage='%(prog)s [options]')
        parser.add_argument('file_path', help='Path to the file to checksum')
        parser.add_argument('-s', '--string', help="check hash of a file with a string of the expected hash")
        parser.add_argument('-f', '--expected_file', help="check hash of file with hash string stored in expected_file")
        args = parser.parse_args()

        try:
                file_digest = sha256(args.file_path)
        except FileNotFoundError:
                print("Error: '" + str(args.file_path) +"', file not found.")
                sys.exit()
        verdict = "Equal"
        comp_hash = ""

        if (args.expected_file is not None) and  (args.string is not None):
                print("Too many arguments.\n")
                parser.print_help()
                sys.exit()
        elif args.expected_file is not None:
                try:
                        comp_hash = readHashFile(str(args.expected_file))
                except FileNotFoundError:
                        print("Error: '" + str(args.expected_file) +"', file not found.")
                        sys.exit()
                print("file: " + args.file_path + ", \nsha256: " + file_digest + "\n\nchecked against: " + str(args.expected_file) + ",\nsha256: " + comp_hash)               
        elif args.string is not None:
                comp_hash = args.string
        else:
                print(file_digest)


        if comp_hash != file_digest:
                verdict = "Not " + verdict
        
        print("\n" + verdict)

if __name__ == "__main__":
        main()
