for file in testcase/*
do
	echo "====="
	echo "testing $file..."
	echo "====="
	python3 parserprogram.py $file
	printf "\n"
done