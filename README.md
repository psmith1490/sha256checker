# sha256checker
## sha256 Checker
Computes the sha256 digest of a specified file and compares with another sha256 digest. 
## Usage
- `python3 sha256checker.py [file path]` outputs sha256 digest of file
- `python3 sha256checker.py [file path] -s [digest string]` computes digest of file and compares with digest string
- `python3 sha256checker.py [file path] -f [a file containing a digest string]` computes digest of file and compares with digest string stored in digest string file


## Example:
`python3 sha256checker ../files/pic.webp -f pic.hash`

## Expected output: 
