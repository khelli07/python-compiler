for file in testcase/*
do
	echo "====="
	echo "testing $file..."
	echo "====="
	python3 run.py $file
	printf "\n"
done