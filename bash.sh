args=("$@")
python astrophlocal/main.py ${args[0]}
cp html/main.html /users/PCON0003/chto/chto.github.io/_pages/arxiv.md
export today=`date`
sed -i "1s/^/---\npermalink: \/Arxiv\/\ntitle: \"Arxiv ($today) \"\nclasses: wide\n---\n/" /users/PCON0003/chto/chto.github.io/_pages/arxiv.md
cd /users/PCON0003/chto/chto.github.io/_pages
git pull
git add arxiv.md
git commit -m "change arxiv"
git push
cd /users/PCON0003/chto/astrophlocal
