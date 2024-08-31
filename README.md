# python-generic-script-executor-api
Send script as parameter and get results.

#### Example Request
```
curl -X 'POST' \
  'http://localhost:9595/executors/exec' \
  -H 'accept: application/json' \
  -H 'Authorization: Basic dXNlcjE6' \
  -H 'Content-Type: application/json' \
  -d '{
  "command_text": "return_me=x+y",
  "input_args_as_key_value": {"x": 5, "y":6},
  "output_args_keys": ["return_me"]
}'
```

#### Build and publish
##### Build
```shell
docker build -f Dockerfile -t satac/python-script-executor .
```

##### Tag
```shell
docker image tag satac/python-script-executor satac/python-script-executor:v1
```

##### Publish
```shell
docker push satac/python-script-executor:v1
```

#### Docker Image
```shell
docker pull satac/python-script-executor:v1
```

#### References
- https://stackoverflow.com/questions/9672791/how-to-safely-use-exec-in-python