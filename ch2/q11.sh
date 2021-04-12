# sed -e "s/\t/ /g" ../data/popular_names.txt

cat ../data/popular_names.txt | tr '\t' ' ' 
