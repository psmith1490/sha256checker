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
```
file: ../files/pic.webp,
sha256: 16c810ac2614c7e663bbd23a2fc19c035d4b10cbdebd90a487aeff0dd1f52b9b

checked against: ../files/pic.hash,
sha256: 16c810ac2614c7e663bbd23a2fc19c035d4b10cbdebd90a487aeff0dd1f52b9b

Equal
```
