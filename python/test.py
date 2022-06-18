import apache_beam as beam
from apache_beam.options.pipeline_options import GoogleCloudOptions
from apache_beam.options.pipeline_options import SetupOptions
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import StandardOptions

options =PipelineOptions()
options.view_as(StandardOptions).streaming=True
p=beam.Pipeline(options=options)
input_sub='projects/named-inn-349004/subscriptions/test-sub'

(
    p
    |beam.io.ReadFromPubSub(subscription=input_sub)
    |beam.Map(print)

)
result=p.run()
result.wait_until_finish()
