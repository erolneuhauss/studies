#/bin/bash
#
# what this script is for: delete given number of files in given directory
# use cases: extracted enron_mail_20150507.tgz and wanted to able to produce
# more realistic datasets with sets of 1000, 5000, 10000, 50000 ... files
# in directories and run performance tests with puppet in order to find out
# if puppet is able to handle thousands of files effectivly

# usage: ./delete_given_no_of_files.sh ~/enron_mail_20150507/dataset_5000_files 294
# deletes 294 files in ~/enron_mail_20150507/dataset_5000_files

DIRECTORY=$1
COUNTTO=$2

COUNTER=0

while [ $COUNTER -lt "$COUNTTO" ]; do
  find "$DIRECTORY" -type f \
    | head -n1 | xargs rm
  let COUNTER=COUNTER+1
done
