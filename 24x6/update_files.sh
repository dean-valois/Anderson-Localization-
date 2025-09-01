echo "Copying eigenvalue files from Bielefeld cluster"

rsync -r --ignore-existing --include="eigL*" --include="*/" --exclude="*" -v influx:/work/DATA/dvalois/database/anderson_transition/24x6/* ./
