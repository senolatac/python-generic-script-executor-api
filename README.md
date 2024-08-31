# python-generic-script-executor-api
Send script as parameter and get results.

#### Access Swagger
- http://localhost:9595/docs

#### Example Request
- Execute Example
```
curl -X 'POST' \
  'http://localhost:9595/python-scripts/exec' \
  -H 'accept: application/json' \
  -H 'Authorization: Basic dXNlcjpwYXNz' \
  -H 'Content-Type: application/json' \
  -d '{
  "command_text": "return_me=x+y",
  "input_args_as_key_value": {"x": 5, "y":6},
  "output_args_keys": ["return_me"]
}'
```
- Evaluate Example
```
curl -X 'POST' \
  'http://localhost:9595/python-scripts/eval' \
  -H 'accept: application/json' \
  -H 'Authorization: Basic dXNlcjpwYXNz' \
  -H 'Content-Type: application/json' \
  -d '{
  "command_text": "x+y",
  "input_args_as_key_value": {"x": 3, "y": 5}
}'
```
- Json Example
```
curl -X 'POST' \
  'http://localhost:9595/python-scripts/exec' \
  -H 'accept: application/json' \
  -H 'Authorization: Basic dXNlcjpwYXNz' \
  -H 'Content-Type: application/json' \
  -d '{
  "command_text": "x =  '\''{ \"name\":\"John\", \"age\":30, \"city\":\"New York\"}'\''\ny = json.loads(x)\nage=y[\"age\"]",
  "input_args_as_key_value": {"x": 5, "y": 4},
  "output_args_keys": ["age"]
}'
```
- Request Example
```
curl -X 'POST' \
  'http://localhost:9595/python-scripts/eval' \
  -H 'accept: application/json' \
  -H 'Authorization: Basic dXNlcjpwYXNz' \
  -H 'Content-Type: application/json' \
  -d '{
  "command_text": "requests.get('\''https://w3schools.com/python/demopage.htm'\'').text",
  "input_args_as_key_value": {}
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
- https://realpython.com/python-eval-function/