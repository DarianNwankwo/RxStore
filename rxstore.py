from app import apps, db
from app.models import Prescription, Patient, Doctor, Pharmacist
from threading import Thread


for app, node in apps:
    Thread(target=app.run, kwargs={"port": node.port}).start()
    
@app.shell_context_processor
def make_shell_context():
    return {"db": db, "Patient": Patient, "Prescription": Prescription, "Doctor": Doctor, "Pharmacist": Pharmacist}
