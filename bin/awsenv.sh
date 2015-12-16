#!/usr/bin/env bash

EXPORTS="$(awsenvp $1)"
EXIT_CODE=$?

if [ $EXIT_CODE -eq 0 ]; then
  echo $EXPORTS
elif [ $EXIT_CODE -eq 3 ]; then
  echo "echo \"Profile argument required.\""
elif [ $EXIT_CODE -eq 4 ]; then
  echo "echo \"Profile $1 not found.\""
else
  echo "echo \"An unknown error occurred.\""
fi
