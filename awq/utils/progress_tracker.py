import requests
import os

# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────── #
#                           specifies all modules that shall be loaded and imported into the                           #
#                                current namespace when we use 'from package import *'                                 #
# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────── #

__all__ = ["progress_tracker"]


class ProgressTracker:
    def __init__(self):
        self.job_id = os.getenv("JOB_ID")
        self.api_url = os.getenv("JOB_LISTENER_URL")
        if not self.job_id or not self.api_url:
            print("Not running using a job scheduler. Progress tracking will not work.")
            return
        self.api_endpoint = f"{self.api_url}/api/jobs/{self.job_id}"

        print(f"Progress tracking enabled for job {self.job_id}")
        print(f"API URL: {self.api_url}")
        print(f"API Endpoint: {self.api_endpoint}")
        self.update_job_status("started")

    def update_job_status(self, status):
        if not self.job_id or not self.api_url:
            return

        payload = {
            "status": status,
        }
        try:
            response = requests.post(self.api_endpoint, json=payload)
            if response.status_code != 200:
                print(f"Failed to update job status: {response.text}")
        except Exception as e:
            print(f"Failed to update job status: {e}")


# ─────────────────────────────────────────────── ConfManager Instance ─────────────────────────────────────────────── #

progress_tracker = ProgressTracker()
