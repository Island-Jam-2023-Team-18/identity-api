#!/bin/sh

echo "Setting up environment"
docker-compose up --force-recreate --build -d
echo "Waiting 3 seconds for the services to be started..."
sleep 3
echo "Runing API tests"
python3 test_api.py
TEST_RESULT=$?
echo "Testing finished, tearing down services"
docker-compose down

if [ $TEST_RESULT -eq 0 ]
then
  echo "=============================================="
  echo " API tests PASSED!"
  echo "=============================================="
else
  echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
  echo " API tests FAILED!!!"
  echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
  exit $TEST_RESULT
fi