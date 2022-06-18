pip3 install -r requirement.txt

python3 test.py --runner=DataFlowRunner --project=named-inn-349004 --temp_location=gs://named-inn-349004/temp --region=us-central1 --job_name test

f=$(gcloud dataflow jobs list --filter="name=test" --region="us-central1" --status="active" | grep "STATE" | sed 's:.*/::')
echo $f


if [[ "$f" = 'STATE: Running' ]]
then
    echo "Dataflow Job created and Running" 
fi
