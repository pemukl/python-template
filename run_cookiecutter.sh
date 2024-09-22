template_path=$(pwd)
cd ../
rm -rf ./generated_projects
mkdir -p ./generated_projects
cd ./generated_projects
cookiecutter "${template_path}"