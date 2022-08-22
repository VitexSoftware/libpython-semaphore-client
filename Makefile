deffile = ansible-semaphore-openapi3.yaml

get-def:
	curl "https://converter.swagger.io/api/convert?url=https://ansible-semaphore.com/api/api-docs.yml" -H "Accept: application/yaml" -o ${deffile}

generate:
		openapi-generator-cli generate -i ${deffile} -g python --git-user-id VitexSoftware --git-repo-id libpython-semaphore-client -c .openapi-generator/config.yaml 
		

