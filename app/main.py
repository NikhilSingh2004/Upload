from fastapi import FastAPI, File, UploadFile, HTTPException
from pathlib import Path
import os
from cryptography.fernet import Fernet

app = FastAPI()

# Directory to store uploaded files
UPLOAD_DIR = Path(r".\uploaded_files")

# Create the upload directory if it doesn't exist
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

# Load encryption key from environment variable or generate a new one if not available
ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY")

# If no encryption key is provided, generate a new one and store it in an environment variable
if ENCRYPTION_KEY is None:
    ENCRYPTION_KEY = Fernet.generate_key()
    os.environ["ENCRYPTION_KEY"] = ENCRYPTION_KEY.decode()

# Initialize Fernet cipher with the encryption key
cipher = Fernet(ENCRYPTION_KEY)

# Function to encrypt file
def encrypt_file(input_file_path, output_file_path):
    with open(input_file_path, "rb") as f_in:
        data = f_in.read()
        encrypted_data = cipher.encrypt(data)
        with open(output_file_path, "wb") as f_out:
            f_out.write(encrypted_data)

# Function to decrypt file
def decrypt_file(input_file_path, output_file_path):
    print(input_file_path)
    print(output_file_path)
    with open(input_file_path, "rb") as f_in:
        encrypted_data = f_in.read()
        decrypted_data = cipher.decrypt(encrypted_data)
        with open(output_file_path, "wb") as f_out:
            f_out.write(decrypted_data)


@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        # Save the uploaded file

        file_path = UPLOAD_DIR / file.filename
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())

        # Encrypt the file
        encrypted_file_path = file_path.with_suffix(".enc")
        encrypt_file(file_path, encrypted_file_path)

        # Delete the original file after encryption
        os.remove(file_path)

        # Return the public path to the encrypted file
        public_path = f"/files/{file.filename}.enc"
        return {"file_path": public_path}
    except Exception as e:
        print(e.__str__())
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
