from fastapi import FastAPI, UploadFile, File
import subprocess, os, tempfile, uvicorn

app = FastAPI()


@app.get("/healthz")
def healthz():
    return {"ok": True}


@app.post("/segment")
async def segment(nifti: UploadFile = File(...)):
    with tempfile.TemporaryDirectory() as td:
        in_path = os.path.join(td, "input.nii.gz")
        out_dir = os.path.join(td, "out")
        with open(in_path, "wb") as f:
            f.write(await nifti.read())
        env = os.environ.copy()
        env["TOTALSEG_CACHE_DIR"] = "/root/.totalsegmentator"
        subprocess.check_call([
            "TotalSegmentator", "-i", in_path, "-o", out_dir, "--fast"
        ], env=env)
        return {"outputs": os.listdir(out_dir)}

# allow local run
if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000)