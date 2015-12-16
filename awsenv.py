import sys
from botocore.session import Session
from botocore.exceptions import ProfileNotFound


def main():
    if len(sys.argv) != 2:
        print("A profile argument is required.")
        sys.exit(3)

    try:
        creds = Session(profile=sys.argv[1]).get_credentials()
    except ProfileNotFound:
        sys.exit(4)

    exports = (
        "export AWS_ACCESS_KEY_ID={} && export AWS_SECRET_ACCESS_KEY={}"
    ).format(
        creds.access_key,
        creds.secret_key
    )

    print(exports)
