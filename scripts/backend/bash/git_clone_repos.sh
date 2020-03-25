#! /bin/bash

export json=$(curl -u ymmmtym: -ks "https://api.github.com/users/ymmmtym/repos")
export count=$(($(echo "${json}" | jq '. | length') - 1))

echo -e "Following repos are found.\n"
echo "${json}" | jq '.[].name' | nl
read -p "clone repository number : " nums
if [ -z "${nums}" ]; then
  echo "Please input nums!!"
  exit 1
fi
for i in ${nums}; do
  number=$((i - 1))
  git clone $(echo "${json}" | jq -r ".[${number}].ssh_url")
done
echo "Done!"
exit 0