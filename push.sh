set -e
sourcename=$1

git add . $1
git commit -m $1
git push origin

echo "Successfully pushed $1 to github.."
