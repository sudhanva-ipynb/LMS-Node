# LMS SERVER

The server for the grpc enabled system. 
ce4483a2-b7f4-4809-9ad9-446dc61dedc9 192.168.91.30        50050      2024-11-15 19:21:48
5255f3d0-c8c7-463d-aaee-8d20a170ca6b 192.168.91.17        50050      2024-11-15 19:22:09
## Functions :
    1. Store Resources (Materials /Assignments)
    2. Provide Authentication/Authorization
    3. Manage (create/fetch) resorces

## Steps to run :
### Step 1: Create a virtual environment
```shell
python -m venv venv
```
### Step 2: Activate the virtual environment
```shell
venv/Scripts/activate
```

### Step 3: Install all requirements
```shell
pip install -r requirements.txt
```
    
### Step 4: Generate grpc python code
```shell

python -m grpc_tools.protoc -I.  --python_out=. --pyi_out=. --grpc_python_out=. ./protos/Lms.proto
```

### Step 5: Download the model and save it under Models Directory
```
GDrive Link : https://drive.google.com/file/d/1ilCP4urzzLl5g0vHGtNcfT3KKJYhmF0P/view?usp=sharing
```
    
### Step 5: Run the source file
```shell
python main.py
```
    
